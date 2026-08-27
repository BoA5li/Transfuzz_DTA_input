import importlib.util
import sys
import types
import unittest
from pathlib import Path


def _load_analyzer_module():
    """Load graph helpers without requiring Triton/pyelftools in the test host."""
    elftools = types.ModuleType('elftools')
    elftools_elf = types.ModuleType('elftools.elf')
    elftools_elffile = types.ModuleType('elftools.elf.elffile')
    elftools_elffile.ELFFile = object

    triton = types.ModuleType('triton')
    triton.TritonContext = object
    triton.ARCH = types.SimpleNamespace(X86_64=object())
    triton.Instruction = object
    triton.MemoryAccess = object
    triton.OPERAND = types.SimpleNamespace(REG=1, MEM=2, IMM=3)

    fake_modules = {
        'elftools': elftools,
        'elftools.elf': elftools_elf,
        'elftools.elf.elffile': elftools_elffile,
        'triton': triton,
    }
    saved = {name: sys.modules.get(name) for name in fake_modules}
    sys.modules.update(fake_modules)

    try:
        module_path = Path(__file__).resolve().parents[1] / 'taint_dep_analyzer_optimized.py'
        spec = importlib.util.spec_from_file_location('taint_dep_analyzer_for_test', module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        for name, previous in saved.items():
            if previous is None:
                sys.modules.pop(name, None)
            else:
                sys.modules[name] = previous


analyzer = _load_analyzer_module()


class EdgeTypeSeparationTests(unittest.TestCase):
    def test_instruction_edges_accept_only_integer_pcs(self):
        edges = {}
        analyzer.add_inst_edge_meta(edges, 0x401100, 0x401108, 'data', pc=0x401108)
        self.assertIn((0x401100, 0x401108), edges)

        with self.assertRaises(TypeError):
            analyzer.add_inst_edge_meta(edges, 'reg:rax', 0x401108, 'data')
        with self.assertRaises(TypeError):
            analyzer.add_inst_edge_meta(edges, True, 0x401108, 'data')

    def test_object_edges_accept_only_string_object_ids(self):
        edges = {}
        analyzer.add_object_edge_meta(edges, 'reg:rax', 'var:array2', 'data', pc=0x401108)
        self.assertIn(('reg:rax', 'var:array2'), edges)

        with self.assertRaises(TypeError):
            analyzer.add_object_edge_meta(edges, 0x401100, 'var:array2', 'data')

    def test_object_relations_are_stored_separately(self):
        inst_edges = {}
        object_edges = {}
        relations = {}

        analyzer.add_object_relation_meta(
            relations, 'mem:0x404000', 'var:array2', 'seed_bridge', pc=0x401108
        )

        self.assertEqual(inst_edges, {})
        self.assertEqual(object_edges, {})
        self.assertIn(('mem:0x404000', 'var:array2'), relations)
        self.assertEqual(relations[('mem:0x404000', 'var:array2')]['kinds'], {'seed_bridge'})

    def test_validation_rejects_preexisting_mixed_edges(self):
        with self.assertRaises(TypeError):
            analyzer.validate_edge_table_types(
                inst_edge_meta={('reg:rax', 0x401108): {}},
                object_edge_meta={},
                object_relation_meta={},
            )

        with self.assertRaises(TypeError):
            analyzer.validate_edge_table_types(
                inst_edge_meta={},
                object_edge_meta={(0x401100, 'var:array2'): {}},
                object_relation_meta={},
            )

    def test_relation_details_are_json_ready(self):
        relations = {}
        analyzer.add_object_relation_meta(
            relations, 'var:array2', 'mem:0x404000', 'seed_bridge', pc=0x401108
        )
        details = analyzer.build_object_relation_details(relations)
        self.assertEqual(details[0]['source_object'], 'var:array2')
        self.assertEqual(details[0]['target_object'], 'mem:0x404000')
        self.assertEqual(details[0]['relations'], ['seed_bridge'])
        self.assertEqual(details[0]['pcs'], ['0x401108'])


class SysvProcessVectorTests(unittest.TestCase):
    def test_initial_stack_contains_argc_and_argv_pointer_table(self):
        layout = analyzer.build_minimal_sysv_process_vector(
            stack_addr=0x70000000,
            stack_size=0x20000,
            argv=('prog',),
        )

        values = [
            int.from_bytes(layout['entry_stack_image'][offset:offset + 8], 'little')
            for offset in range(0, len(layout['entry_stack_image']), 8)
        ]
        argc, argv0_pointer, argv_terminator, envp_terminator, at_null, null_value = values

        self.assertEqual(argc, 1)
        self.assertEqual(layout['argc'], 1)
        self.assertEqual(argv0_pointer, layout['arg_addresses'][0])
        self.assertEqual(layout['argv_addr'], layout['initial_rsp'] + 8)
        self.assertNotEqual(layout['argv_addr'], layout['arg_addresses'][0])
        self.assertEqual(argv_terminator, 0)
        self.assertEqual(envp_terminator, 0)
        self.assertEqual((at_null, null_value), (0, 0))
        self.assertEqual(layout['envp_addr'], layout['argv_addr'] + 16)
        self.assertEqual(layout['auxv_addr'], layout['envp_addr'] + 8)
        self.assertEqual(layout['initial_rsp'] % 16, 0)
        self.assertEqual(layout['string_writes'], ((argv0_pointer, b'prog\0'),))

    def test_multiple_arguments_have_distinct_pointers_and_null_terminators(self):
        layout = analyzer.build_minimal_sysv_process_vector(
            stack_addr=0x70000000,
            stack_size=0x20000,
            argv=('prog', '--mode', 'full'),
        )

        values = [
            int.from_bytes(layout['entry_stack_image'][offset:offset + 8], 'little')
            for offset in range(0, len(layout['entry_stack_image']), 8)
        ]
        self.assertEqual(layout['argc'], 3)
        self.assertEqual(values[0], 3)
        self.assertEqual(values[1:4], list(layout['arg_addresses']))
        self.assertEqual(values[4:], [0, 0, 0, 0])
        self.assertEqual(
            [raw for _, raw in layout['string_writes']],
            [b'prog\0', b'--mode\0', b'full\0'],
        )

    def test_invalid_or_oversized_arguments_fail_closed(self):
        with self.assertRaises(ValueError):
            analyzer.build_minimal_sysv_process_vector(0x70000000, 0x20000, ('bad\0arg',))
        with self.assertRaises(ValueError):
            analyzer.build_minimal_sysv_process_vector(0x70000000, 0x110, ('prog',))

    def test_libc_arguments_are_remapped_for_main(self):
        layout = analyzer.build_minimal_sysv_process_vector(
            0x70000000, 0x20000, ('prog', '--mode')
        )
        main_args = analyzer.derive_main_process_args(
            layout['argc'], layout['argv_addr'], 0x70000000, 0x20000
        )

        self.assertEqual(
            main_args,
            (layout['argc'], layout['argv_addr'], layout['envp_addr']),
        )

    def test_invalid_libc_argv_is_rejected(self):
        with self.assertRaises(ValueError):
            analyzer.derive_main_process_args(1, 0x60000000, 0x70000000, 0x20000)
        with self.assertRaises(ValueError):
            analyzer.derive_main_process_args(4097, 0x70001000, 0x70000000, 0x20000)


class TaintInitializationTests(unittest.TestCase):
    def test_secret_region_is_tainted_without_symbolization(self):
        class RecordingContext:
            def __init__(self):
                self.tainted = []

            def taintMemory(self, memory):
                self.tainted.append(memory)

            def symbolizeMemory(self, *_args, **_kwargs):
                self.fail('symbolizeMemory must not be called')

            def fail(self, message):
                raise AssertionError(message)

        original_memory_access = analyzer.MemoryAccess
        analyzer.MemoryAccess = lambda address, size: (address, size)
        try:
            ctx = RecordingContext()
            analyzer.taint_memory_region(ctx, 0x404000, 4)
        finally:
            analyzer.MemoryAccess = original_memory_access

        self.assertEqual(
            ctx.tainted,
            [(0x404000, 1), (0x404001, 1), (0x404002, 1), (0x404003, 1)],
        )

    def test_invalid_taint_region_is_rejected(self):
        with self.assertRaises(ValueError):
            analyzer.taint_memory_region(object(), -1, 1)
        with self.assertRaises(ValueError):
            analyzer.taint_memory_region(object(), 0x404000, -1)
        with self.assertRaises(TypeError):
            analyzer.taint_memory_region(object(), 0x404000, True)


class HybridControlDependenceTests(unittest.TestCase):
    def test_diamond_cfg_uses_merge_as_immediate_postdominator(self):
        nodes = {0x100, 0x110, 0x120, 0x130, 0x140}
        successors = {
            0x100: {0x110, 0x120},
            0x110: {0x130},
            0x120: {0x130},
            0x130: {0x140},
            0x140: set(),
        }

        regions, result = analyzer.build_control_regions(nodes, successors)

        self.assertEqual(result['unresolved_nodes'], set())
        self.assertEqual(result['immediate_postdominators'][0x100], 0x130)
        self.assertEqual(regions[0x100]['successor_regions'][0x110], {0x110})
        self.assertEqual(regions[0x100]['successor_regions'][0x120], {0x120})

    def test_multi_exit_branch_has_no_false_common_merge(self):
        nodes = {0x200, 0x210, 0x220}
        successors = {
            0x200: {0x210, 0x220},
            0x210: set(),
            0x220: set(),
        }

        regions, result = analyzer.build_control_regions(nodes, successors)

        self.assertIsNone(result['immediate_postdominators'][0x200])
        self.assertEqual(regions[0x200]['successor_regions'][0x210], {0x210})
        self.assertEqual(regions[0x200]['successor_regions'][0x220], {0x220})

    def test_cfg_without_exit_is_not_claimed_as_strict_control(self):
        nodes = {0x300, 0x310}
        successors = {0x300: {0x310}, 0x310: {0x300}}

        regions, result = analyzer.build_control_regions(nodes, successors)

        self.assertEqual(regions, {})
        self.assertEqual(result['unresolved_nodes'], nodes)

    def test_dynamic_taken_edge_selects_static_region_and_expires_at_merge(self):
        static_model = {
            'branches': {
                0x400: {
                    'successor_regions': {
                        0x410: {0x410, 0x411},
                        0x420: {0x420},
                    },
                    'merge_pc': 0x430,
                }
            }
        }
        context = analyzer.make_hybrid_control_context(
            static_model, 0x400, {'reg:zf'}, 0, 0x410, 0x405, 0x420
        )
        active = [context]
        keys = {context['key']}

        self.assertEqual(context['evidence'], 'static_postdom_dynamic_edge')
        self.assertEqual(context['controlled_pcs'], frozenset({0x410, 0x411}))

        analyzer.pop_inactive_control_context(active, keys, 0x411, 0)
        self.assertEqual(len(active), 1)
        analyzer.pop_inactive_control_context(active, keys, 0x430, 0)
        self.assertEqual(active, [])
        self.assertEqual(keys, set())

    def test_incomplete_static_model_uses_labeled_dynamic_fallback(self):
        context = analyzer.make_hybrid_control_context(
            {'branches': {}}, 0x500, {'reg:zf'}, 0, 0x510, 0x505, 0x520
        )
        self.assertEqual(context['evidence'], 'dynamic_alt_fallback')
        self.assertIsNone(context['controlled_pcs'])

    def test_control_edge_records_static_evidence(self):
        context = analyzer.make_hybrid_control_context(
            {
                'branches': {
                    0x600: {
                        'successor_regions': {0x610: {0x610}},
                        'merge_pc': 0x620,
                    }
                }
            },
            0x600,
            {'reg:zf'},
            0,
            0x610,
            0x605,
            0x620,
        )
        inst_controlled_by = {}
        inst_ctrl_objects = {}
        obj_ctrl_use_pcs = {}
        evidence = {}

        from collections import defaultdict
        inst_controlled_by = defaultdict(set)
        inst_ctrl_objects = defaultdict(set)
        obj_ctrl_use_pcs = defaultdict(set)
        evidence = defaultdict(set)
        edges = {}
        analyzer.apply_online_control_to_inst(
            0x610,
            {'var:out'},
            [context],
            0,
            inst_controlled_by,
            inst_ctrl_objects,
            edges,
            obj_ctrl_use_pcs,
            evidence,
        )

        self.assertIn((0x600, 0x610), edges)
        self.assertEqual(inst_controlled_by[0x610], {0x600})
        self.assertEqual(
            evidence[(0x600, 0x610)], {'static_postdom_dynamic_edge'}
        )


if __name__ == '__main__':
    unittest.main()
