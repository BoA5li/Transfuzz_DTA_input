import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "mutation_candidate_filter.py"


def load_module():
    spec = importlib.util.spec_from_file_location("mutation_candidate_filter", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


mcf = load_module()


def object_detail(*, obj_type="register", tags=None, defined_by=None,
                  used_by=None, addr_used_by=None, ctrl_used_by=None,
                  occurrence_pc=None, operand_index=None, value_hex=None,
                  bit_size=64, parents=None, children=None,
                  parent_edges=None, child_edges=None):
    return {
        "type": obj_type,
        "label": obj_type,
        "semantic_tags": tags or [],
        "source_kind": "test",
        "occurrence_pc": occurrence_pc,
        "operand_index": operand_index,
        "value_hex": value_hex,
        "bit_size": bit_size,
        "defined_by": defined_by or [],
        "used_by": used_by or [],
        "addr_used_by": addr_used_by or [],
        "ctrl_used_by": ctrl_used_by or [],
        "direct_parents": parents or [],
        "direct_children": children or [],
        "parent_edge_details": parent_edges or {},
        "child_edge_details": child_edges or {},
    }


def instruction(disasm, *, uses=None, defs=None, addrs=None, immediates=None,
                tags=None, controlled_by=None, control_evidence=None):
    return {
        "disasm": disasm,
        "semantic_tags": tags or [],
        "use_objects": uses or [],
        "def_objects": defs or [],
        "addr_objects": addrs or [],
        "immediates": immediates or [],
        "controlled_by": controlled_by or [],
        "control_evidence": control_evidence or {},
        "uses_taint": False,
        "suppressed_repeat_records": 0,
    }


def base_summary():
    imm = "imm_occurrence:0x401020:operand_imm:1:0x10:test"
    return {
        "taint_source": {
            "seed_object_nodes": ["var:secret"],
            "seed_instruction_pcs": ["0x401100"],
        },
        "backward": {
            "objects": ["var:secret", "reg:rax", imm, "reg:rbx"],
            "leaf_objects": ["reg:rax", imm],
            "instructions": ["0x401020", "0x401100", "0x401130"],
            "leaf_instructions": ["0x401020"],
        },
        "instruction_details": {
            "0x401020": instruction(
                "add eax, 0x10",
                uses=["reg:rax"],
                defs=["reg:rax"],
                immediates=[imm],
                tags=["arithmetic"],
            ),
            "0x401100": instruction("mov byte ptr [rax], al", uses=["var:secret"]),
            "0x401130": instruction("mov ebx, eax", uses=["reg:rax"], defs=["reg:rbx"]),
        },
        "object_details": {
            "var:secret": object_detail(obj_type="var", defined_by=["0x401100"]),
            "reg:rax": object_detail(
                used_by=["0x401020"],
                defined_by=["0x401020"],
                children=["var:secret"],
                child_edges={
                    "var:secret": {
                        "kinds": ["data", "addr"],
                        "pcs": ["0x401020"],
                        "count": 2,
                        "kind_counts": {"data": 1, "addr": 1},
                    }
                },
            ),
            imm: object_detail(
                obj_type="imm_occurrence",
                occurrence_pc="0x401020",
                operand_index=1,
                value_hex="0x10",
                children=["var:secret"],
                child_edges={
                    "var:secret": {
                        "kinds": ["data"],
                        "pcs": ["0x401020"],
                        "count": 1,
                        "kind_counts": {"data": 1},
                    }
                },
            ),
            "reg:rbx": object_detail(used_by=["0x401130"]),
        },
    }


class LeafInputContractTests(unittest.TestCase):
    def test_only_object_leaves_are_filtered(self):
        summary = base_summary()
        model = mcf.DependencyModel(summary)
        filt = mcf.LeafDependencyFilter(model)
        eligible, excluded = filt.filter_leaf_objects()

        ids = {item["object_id"] for item in eligible}
        self.assertEqual(ids, {
            "reg:rax",
            "imm_occurrence:0x401020:operand_imm:1:0x10:test",
        })
        self.assertNotIn("reg:rbx", ids)
        self.assertEqual(excluded, [])

    def test_only_instruction_leaves_are_direct_instruction_candidates(self):
        summary = base_summary()
        filt = mcf.LeafDependencyFilter(mcf.DependencyModel(summary))
        eligible, _ = filt.filter_leaf_instructions()
        self.assertEqual([item["pc"] for item in eligible], ["0x401020"])

    def test_leaf_membership_is_not_recomputed_from_parents(self):
        summary = base_summary()
        summary["object_details"]["reg:rax"]["direct_parents"] = ["reg:rcx"]
        summary["object_details"]["reg:rax"]["parent_edge_details"] = {
            "reg:rcx": {"kinds": ["data"], "pcs": ["0x401010"]}
        }
        filt = mcf.LeafDependencyFilter(mcf.DependencyModel(summary))
        eligible, _ = filt.filter_leaf_objects()
        self.assertIn("reg:rax", {item["object_id"] for item in eligible})


class ObjectFilteringTests(unittest.TestCase):
    def _decision_for(self, object_id, detail, disasm="mov eax, ebx"):
        summary = base_summary()
        summary["backward"]["objects"] = [object_id]
        summary["backward"]["leaf_objects"] = [object_id]
        summary["backward"]["instructions"] = ["0x401020"]
        summary["backward"]["leaf_instructions"] = []
        summary["object_details"] = {object_id: detail}
        summary["instruction_details"] = {
            "0x401020": instruction(disasm, uses=[object_id])
        }
        filt = mcf.LeafDependencyFilter(mcf.DependencyModel(summary))
        eligible, excluded = filt.filter_leaf_objects()
        return eligible, excluded

    def assertFiltered(self, object_id, detail, expected_code, disasm="mov eax, ebx"):
        eligible, excluded = self._decision_for(object_id, detail, disasm)
        self.assertEqual(eligible, [])
        self.assertIn(expected_code, excluded[0]["reason_codes"])

    def test_filters_execution_position_flags_stack_structure_and_memory_instance(self):
        cases = [
            ("reg:rip", "leaf-object.execution-position-state"),
            ("reg:zf", "leaf-object.implicit-flag-state"),
            ("reg:rsp", "leaf-object.stack-frame-structural-register"),
            ("mem:0x700000", "leaf-object.runtime-memory-instance"),
            ("reg:tmp", "leaf-object.analysis-temporary"),
        ]
        for object_id, code in cases:
            with self.subTest(object_id=object_id):
                self.assertFiltered(
                    object_id,
                    object_detail(used_by=["0x401020"]),
                    code,
                )

    def test_keeps_plain_register_without_high_value_role(self):
        eligible, excluded = self._decision_for(
            "reg:rbx", object_detail(used_by=["0x401020"])
        )
        self.assertEqual(excluded, [])
        self.assertEqual(eligible[0]["object_id"], "reg:rbx")

    def test_filters_branch_target_but_not_ordinary_immediate(self):
        branch_imm = "imm_occurrence:0x401020:operand_imm:0:0x401100:test"
        self.assertFiltered(
            branch_imm,
            object_detail(
                obj_type="imm_occurrence", occurrence_pc="0x401020",
                operand_index=0, used_by=["0x401020"],
            ),
            "leaf-object.control-flow-target-immediate",
            "jne 0x401100",
        )

        ordinary = "imm_occurrence:0x401020:operand_imm:1:0x2:test"
        eligible, excluded = self._decision_for(
            ordinary,
            object_detail(
                obj_type="imm_occurrence", occurrence_pc="0x401020",
                operand_index=1, used_by=["0x401020"],
            ),
            "add eax, 2",
        )
        self.assertEqual(excluded, [])
        self.assertEqual(eligible[0]["object_id"], ordinary)

    def test_does_not_demote_address_component_because_var_shares_pc(self):
        disp = "imm_occurrence:0x401020:mem_disp:0:0x20:test"
        summary = base_summary()
        summary["backward"]["objects"] = ["var:array", disp]
        summary["backward"]["leaf_objects"] = ["var:array", disp]
        summary["object_details"] = {
            "var:array": object_detail(obj_type="var", addr_used_by=["0x401020"]),
            disp: object_detail(
                obj_type="imm_occurrence", occurrence_pc="0x401020",
                operand_index=0,
            ),
        }
        summary["instruction_details"]["0x401020"] = instruction(
            "mov eax, dword ptr [rax+0x20]",
            addrs=["var:array"], immediates=[disp],
        )
        filt = mcf.LeafDependencyFilter(mcf.DependencyModel(summary))
        eligible, excluded = filt.filter_leaf_objects()
        self.assertEqual(excluded, [])
        self.assertEqual(
            {item["object_id"] for item in eligible}, {"var:array", disp}
        )


class InstructionFilteringTests(unittest.TestCase):
    def _filter_instruction(self, disasm, pc="0x401020"):
        summary = base_summary()
        summary["backward"]["instructions"] = [pc]
        summary["backward"]["leaf_instructions"] = [pc]
        summary["instruction_details"] = {pc: instruction(disasm)}
        filt = mcf.LeafDependencyFilter(mcf.DependencyModel(summary))
        return filt.filter_leaf_instructions()

    def test_filters_structural_instructions(self):
        cases = [
            ("push rbp", "leaf-instruction.stack-frame-structural"),
            ("mov rbp, rsp", "leaf-instruction.stack-frame-structural"),
            ("sub rsp, 0x20", "leaf-instruction.stack-space-maintenance"),
            ("push r12", "leaf-instruction.callee-saved-maintenance"),
            ("mov qword ptr [rbp - 0x8], rdi", "leaf-instruction.argument-spill"),
            ("ret", "leaf-instruction.return-structural"),
            ("nop", "leaf-instruction.padding"),
            ("endbr64", "leaf-instruction.control-flow-protection"),
            ("ud2", "leaf-instruction.trap-or-invalid"),
        ]
        for disasm, code in cases:
            with self.subTest(disasm=disasm):
                eligible, excluded = self._filter_instruction(disasm)
                self.assertEqual(eligible, [])
                self.assertIn(code, excluded[0]["reason_codes"])

    def test_keeps_type_conversions_and_plain_moves(self):
        for disasm in ("movzx eax, al", "movsx eax, al", "cdqe", "mov eax, ebx"):
            with self.subTest(disasm=disasm):
                eligible, excluded = self._filter_instruction(disasm)
                self.assertEqual(excluded, [])
                self.assertEqual(eligible[0]["disasm"], disasm)


class AnchorMappingTests(unittest.TestCase):
    def test_merges_object_and_instruction_sources_by_pc(self):
        summary = base_summary()
        filt = mcf.LeafDependencyFilter(mcf.DependencyModel(summary))
        objects, _ = filt.filter_leaf_objects()
        instructions, _ = filt.filter_leaf_instructions()
        anchors = filt.build_anchor_instructions(objects, instructions)

        self.assertEqual([item["pc"] for item in anchors], ["0x401020", "0x401130"])
        merged = anchors[0]
        self.assertEqual(merged["anchor_sources"], [
            "eligible_leaf_instruction", "eligible_leaf_object"
        ])
        self.assertEqual(
            {item["object_id"] for item in merged["leaf_object_dependencies"]},
            {
                "reg:rax",
                "imm_occurrence:0x401020:operand_imm:1:0x10:test",
            },
        )
        self.assertIn("data", merged["dependency_semantics"])
        self.assertIn("addr", merged["dependency_semantics"])
        self.assertEqual(anchors[1]["anchor_sources"], ["eligible_leaf_object"])

    def test_terminal_mapping_uses_only_direct_groups_as_anchors(self):
        summary = base_summary()
        mapping = {
            "backward_leaf_mappings": [{
                "node_id": "reg:rax",
                "pc_relation_entries": [
                    {
                        "pc": "0x401020",
                        "relation_kinds": ["direct_use"],
                        "relation_groups": ["direct_operand"],
                    },
                    {
                        "pc": "0x401130",
                        "relation_kinds": ["path_backward_related"],
                        "relation_groups": ["derived_or_related"],
                    },
                ],
                "executed_code_reference": {},
            }]
        }
        model = mcf.DependencyModel(summary, mapping)
        relations = model.direct_object_pc_relations("reg:rax")
        relation_by_pc = {item["pc"]: item for item in relations}
        self.assertTrue(any(
            value.startswith("terminal_mapping.direct_use")
            for value in relation_by_pc["0x401020"]["relation_kinds"]
        ))
        self.assertFalse(any(
            value.startswith("terminal_mapping.path_backward_related")
            for value in relation_by_pc["0x401130"]["relation_kinds"]
        ))


class OutputContractTests(unittest.TestCase):
    FORBIDDEN_TOKENS = {
        "recommended_actions", "recommended_mutations", "anchor_tier",
        "direct_mutation_preferred", "deletion_candidate_only",
        "causal_role_class", "qualification_reasons", "root_evidence",
        "backward_distance",
    }

    def test_summary_declares_non_responsibilities(self):
        summary = base_summary()
        model = mcf.DependencyModel(summary)
        filt = mcf.LeafDependencyFilter(model)
        objects, filtered_objects = filt.filter_leaf_objects()
        instructions, filtered_instructions = filt.filter_leaf_instructions()
        anchors = filt.build_anchor_instructions(objects, instructions)
        report = mcf.build_filter_summary(
            model, objects, instructions, anchors,
            filtered_objects, filtered_instructions,
        )
        self.assertEqual(report["status"], "ok")
        self.assertIn("candidate ranking or priority", report["non_responsibilities"])
        self.assertFalse(report["capabilities"]["full_instruction_dependency_edge_kinds"])

    def test_cli_writes_new_files_without_legacy_guidance_fields(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            input_path = temp / "dependency_summary.json"
            input_path.write_text(json.dumps(base_summary()), encoding="utf-8")
            output_dir = temp / "out"
            subprocess.run([
                sys.executable,
                str(MODULE_PATH),
                "--dependency-summary", str(input_path),
                "--outdir", str(output_dir),
            ], check=True, capture_output=True, text=True)

            expected = {
                "eligible_leaf_objects.json",
                "eligible_leaf_instructions.json",
                "mutation_anchor_instructions.json",
                "filtered_leaf_items.json",
                "filter_summary.json",
            }
            self.assertEqual({path.name for path in output_dir.iterdir()}, expected)
            serialized = "\n".join(
                path.read_text(encoding="utf-8") for path in output_dir.iterdir()
            )
            for token in self.FORBIDDEN_TOKENS:
                self.assertNotIn(f'"{token}"', serialized)


if __name__ == "__main__":
    unittest.main()
