# Leaf dependency filter contract (v3)

`mutation_candidate_filter.py` consumes the authoritative backward leaf sets
exported by `taint_dep_analyzer_optimized.py`:

- `backward.leaf_objects`
- `backward.leaf_instructions`

It filters unsupported/noise/runtime/ABI-structural representations and maps
the remaining leaf items to direct user-code instruction anchors. It does not
recompute reachability, rank candidates, estimate mutation value, or recommend
mutation operators.

The filter consumes semantic facts produced by the analyzer. Disassembly text
is retained only for human-readable output and is not used to reconstruct
function boundaries, classify code ownership, or parse operands.

## Required structured instruction facts

Each `instruction_details` entry should provide:

- `mnemonic` and `mnemonic_provenance`;
- `operands`, including operand kind, access, width, register identity, and
  memory base/index/scale/displacement components;
- `implicit_reads` and `implicit_writes`;
- `instruction_role`, `instruction_role_provenance`, `function_id`, and
  `frame_operation`;
- `code_region` and `code_region_provenance`;
- `module`, `section`, `symbol`, `function`, and `is_user_code`;
- complete `instruction_parent_edges`, `instruction_child_edges`, and their
  aggregated `dependency_semantics`;
- optional `source_location` and `call_target_symbol`.

The analyzer classifies `instruction_role` with function and CFG context. Frame
operations record whether stack allocation/release and callee-saved operations
have reachable matching peers. Incomplete function CFGs do not assert
prologue/epilogue roles. An ambiguous instruction is emitted as `unknown` or
`body`; the filter does not upgrade it from textual instruction patterns.

Mnemonic extraction is centralized in one analyzer adapter. A structured
decoder mnemonic API is preferred; older Triton versions use a single labeled
disassembly compatibility fallback. No filter rule parses display text.

## Code-region evidence

The analyzer applies ownership evidence in this order:

1. repeatable user-specified target ranges (`--user-code-range START:END`);
2. executable ELF section and module identity;
3. symbol/function ranges;
4. addr2line/source mapping;
5. `unknown` when no structured evidence resolves ownership.

Known loader/runtime sections and symbols are marked `runtime`. Target-module
`.text` sections, ordinary function ranges, source mappings, and explicit
ranges provide affirmative user-code evidence. The filter accepts anchors only
when `code_region == user`; `runtime`, `unknown`, missing, and unrecognized
regions fail closed. Unknown ownership is reported as `unresolved`, not silently
guessed from disassembly.

## Outputs

- `eligible_leaf_objects.json`: eligible backward object leaves and their
  direct object-to-PC relation evidence.
- `eligible_leaf_instructions.json`: eligible backward instruction leaves.
- `mutation_anchor_instructions.json`: one record per direct anchor PC, merging
  object-leaf and instruction-leaf provenance without assigning priority.
- `filtered_leaf_items.json`: excluded object/instruction leaves with stable
  reason codes, dependency edges, relation evidence, and structured context.
- `filter_summary.json`: counts, input consistency warnings, and supported
  input capabilities.

Object-leaf anchors may include instructions that are not instruction leaves.
The output distinguishes these origins with `anchor_sources`:

- `eligible_leaf_object`
- `eligible_leaf_instruction`
- `filtered_leaf_object_context`
- `filtered_leaf_instruction_context`

The latter two are context-only sources. Every anchor explicitly exports
`eligible_for_mutation_stage`; an anchor produced only to preserve filtered-leaf
semantics has this field set to `false` and is not a mutation-stage candidate.

`terminal_node_mapping.json` is optional. Only its `direct_operand` and
`structural_role` PC relation groups can add direct anchors. Path-related and
evidence-only PCs remain context and are never promoted to anchors.

`path_report` is not an input to this contract and no corresponding CLI option,
load-status field, or compatibility cache is retained.

Anchors expose `source_locations`, deduplicated by file, line, and function,
with all contributing `provenances` preserved. `source_location` is populated
only when the mapping is unique; ambiguous mappings are never resolved by
silently choosing the first record.

## Scope boundaries

The filter preserves upstream object edge kinds (`data`, `addr`, `control`),
complete typed instruction dependency edges, instruction control evidence,
semantic tags, and use/def/address/immediate membership. It never infers
instruction data/address edges from mnemonics.

Unsupported object types, malformed PCs, and unresolved user-code ownership
are emitted with `decision: unresolved`. Explicit noise, runtime, ABI, and
unsupported stable representations use `decision: filtered`. Both decisions
are ineligible for mutation-stage delivery, but their evidence is retained.

The downstream mutation component remains responsible for operator choice,
candidate scheduling, priority, effectiveness, and feedback.
