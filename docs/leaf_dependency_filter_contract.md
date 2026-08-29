# Leaf dependency filter contract

`mutation_candidate_filter.py` consumes the authoritative backward leaf sets
exported by `taint_dep_analyzer_optimized.py`:

- `backward.leaf_objects`
- `backward.leaf_instructions`

It filters unsupported/noise/runtime/ABI-structural representations and maps
the remaining leaf items to direct user-code instruction anchors. It does not
recompute reachability, rank candidates, estimate mutation value, or recommend
mutation operators.

## Outputs

- `eligible_leaf_objects.json`: eligible backward object leaves and their
  direct object-to-PC relation evidence.
- `eligible_leaf_instructions.json`: eligible backward instruction leaves.
- `mutation_anchor_instructions.json`: one record per direct anchor PC, merging
  object-leaf and instruction-leaf provenance without assigning priority.
- `filtered_leaf_items.json`: excluded object/instruction leaves with stable
  reason codes.
- `filter_summary.json`: counts, input consistency warnings, and supported
  input capabilities.

Object-leaf anchors may include instructions that are not instruction leaves.
The output distinguishes these origins with `anchor_sources`:

- `eligible_leaf_object`
- `eligible_leaf_instruction`

`terminal_node_mapping.json` is optional. Only its `direct_operand` and
`structural_role` PC relation groups can add direct anchors. Path-related and
evidence-only PCs remain context and are never promoted to anchors.

## Scope boundaries

The filter preserves upstream object edge kinds (`data`, `addr`, `control`),
instruction control evidence, semantic tags, and use/def/address/immediate
membership. The current dependency summary does not serialize complete
instruction-edge metadata, so the filter explicitly reports that capability as
unavailable and does not infer instruction data/address edges from mnemonics.

The downstream mutation component remains responsible for operator choice,
candidate scheduling, priority, effectiveness, and feedback.
