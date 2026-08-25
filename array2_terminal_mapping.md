# Terminal Object Mapping Report

## Meta

- Taint source: `array2`
- Executed instructions: `956212`
- Backward objects: `179`
- Forward objects: `38`

## Backward Leaf Mappings

### 1. `imm_occurrence:0x150f:mem_disp:1:0x20fc6f:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0x150f:mem_disp:1:0x20fc6f/i64 [rip_relative_displacement|structural_abi_constant]`
- Mapping kind: `rip_relative_displacement`
- Confidence: `semantic`
- Object semantic tags: `['rip_relative_displacement', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0x150f', 'operand_index': None, 'raw_suffix': 'mem_disp:1:0x20fc6f/i64 [rip_relative_displacement|structural_abi_constant]'}`
- Reason: 该 immediate 带有 rip_relative_displacement 标签，更适合作为 RIP 相对寻址位移解释。
- Candidate program elements: `['imm@0x150f:mem_disp:1:0x20fc6f/i64 [rip_relative_displacement|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0x150f']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0x150f']`
- direct_operand_pcs: `['0x150f']`
- structural_role_pcs: `['0x150f']`
- anchor_pcs: `['0x150f']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0x150b', '0x150c', '0x1515', '0x1517']`
- all_mapped_pcs: `['0x150b', '0x150c', '0x150f', '0x1515', '0x1517']`
- direct_parents: `[]`
- direct_children: `['var:uops_available']`

#### PC Relation Entries

- `0x150b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x150c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x150f` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0x1515` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1517` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0x150f`: `mov eax, dword ptr [rip + 0x20fc6f]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `??:None` function=`pmu_uops_snap_before`
  - use_objects: `['reg:rip', 'var:uops_available']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0x150f:mem_disp:1:0x20fc6f:i64', 'imm_occurrence:0x150f:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0x150f:mem_disp:1:0x20fc6f:i64', 'imm_occurrence:0x150f:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0x150b`: `push rbp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x150c`: `mov rbp, rsp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1515`: `test eax, eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1517`: `je 0x1577` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0x150b`     150b:	55                   	push   %rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x150c`     150c:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x150f`     150f:	8b 05 6f fc 20 00    	mov    0x20fc6f(%rip),%eax        # 211184 <uops_available> groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0x1515`     1515:	85 c0                	test   %eax,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1517`     1517:	74 5e                	je     1577 <pmu_uops_snap_before+0x6c> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 2. `imm_occurrence:0x150f:mem_scale:1:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0x150f:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0x150f', 'operand_index': None, 'raw_suffix': 'mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0x150f:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0x150f']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0x150f']`
- direct_operand_pcs: `['0x150f']`
- structural_role_pcs: `['0x150f']`
- anchor_pcs: `['0x150f']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0x150b', '0x150c', '0x1515', '0x1517']`
- all_mapped_pcs: `['0x150b', '0x150c', '0x150f', '0x1515', '0x1517']`
- direct_parents: `[]`
- direct_children: `['var:uops_available']`

#### PC Relation Entries

- `0x150b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x150c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x150f` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0x1515` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1517` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0x150f`: `mov eax, dword ptr [rip + 0x20fc6f]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `??:None` function=`pmu_uops_snap_before`
  - use_objects: `['reg:rip', 'var:uops_available']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0x150f:mem_disp:1:0x20fc6f:i64', 'imm_occurrence:0x150f:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0x150f:mem_disp:1:0x20fc6f:i64', 'imm_occurrence:0x150f:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0x150b`: `push rbp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x150c`: `mov rbp, rsp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1515`: `test eax, eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1517`: `je 0x1577` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0x150b`     150b:	55                   	push   %rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x150c`     150c:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x150f`     150f:	8b 05 6f fc 20 00    	mov    0x20fc6f(%rip),%eax        # 211184 <uops_available> groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0x1515`     1515:	85 c0                	test   %eax,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1517`     1517:	74 5e                	je     1577 <pmu_uops_snap_before+0x6c> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 3. `imm_occurrence:0x1517:operand_imm:0:0x1577:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0x1517:operand_imm:0:0x1577/i64`
- Mapping kind: `comparison_constant`
- Confidence: `semantic`
- Object semantic tags: `['comparison_constant']`
- Anchor instruction tags: `['callee_save_restore', 'conditional_branch', 'epilogue']`
- Scaffolding tags: `['callee_save_restore', 'epilogue']`
- Occurrence: `{'occurrence_pc': '0x1517', 'operand_index': None, 'raw_suffix': 'operand_imm:0:0x1577/i64'}`
- Reason: 该 immediate 带有 comparison_constant 标签，更适合作为比较语义常量解释。 检测到 ABI/脚手架标签：callee_save_restore, epilogue，应更偏向解释为结构性对象，而非优先可变异语义对象。
- Candidate program elements: `['imm@0x1517:operand_imm:0:0x1577/i64']`
- direct_use_pcs: `['0x1517']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `['0x1577', '0x1578', '0x1579']`
- direct_imm_pcs: `['0x1517']`
- direct_operand_pcs: `['0x1517']`
- structural_role_pcs: `['0x1577', '0x1578', '0x1579']`
- anchor_pcs: `['0x1517', '0x1577', '0x1578', '0x1579']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0x150f', '0x1515', '0x1519', '0x151f', '0x156e', '0x1575']`
- all_mapped_pcs: `['0x150f', '0x1515', '0x1517', '0x1519', '0x151f', '0x156e', '0x1575', '0x1577', '0x1578', '0x1579']`
- direct_parents: `[]`
- direct_children: `['reg:rbp', 'reg:rip', 'reg:rsp']`

#### PC Relation Entries

- `0x150f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1515` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1517` kinds=`['direct_immediate_occurrence', 'direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.used_by/instruction_details.use_objects']`
- `0x1519` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x151f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x156e` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1575` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1577` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1578` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1579` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`

#### Direct Anchor Instruction Evidence

- PC `0x1517`: `je 0x1577` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
  - Source: `??:None` function=`pmu_uops_snap_before`
  - instruction_semantic_tags: `['conditional_branch']`
  - use_objects: `['imm_occurrence:0x1517:operand_imm:0:0x1577:i64', 'reg:zf']`
  - def_objects: `['reg:rip']`
  - immediates: `['imm_occurrence:0x1517:operand_imm:0:0x1577:i64']`
- PC `0x1577`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x1578`: `pop rbp` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_before`
  - instruction_semantic_tags: `['callee_save_restore', 'epilogue']`
  - use_objects: `['reg:rsp', 'stack:[rbp-0x20]']`
  - def_objects: `['reg:rbp', 'reg:rip', 'reg:rsp']`
- PC `0x1579`: `ret` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_before`
  - use_objects: `['reg:rsp', 'stack:[rbp-0x18]']`
  - def_objects: `['reg:rip', 'reg:rsp']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0x150f`: `mov eax, dword ptr [rip + 0x20fc6f]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1515`: `test eax, eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1519`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x151f`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x156e`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1575`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0x150f`     150f:	8b 05 6f fc 20 00    	mov    0x20fc6f(%rip),%eax        # 211184 <uops_available> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1515`     1515:	85 c0                	test   %eax,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1517`     1517:	74 5e                	je     1577 <pmu_uops_snap_before+0x6c> groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
- `0x1519`     1519:	8b 05 41 3c 20 00    	mov    0x203c41(%rip),%eax        # 205160 <use_rdpmc> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x151f`     151f:	85 c0                	test   %eax,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x156e`     156e:	48 89 05 03 3c 20 00 	mov    %rax,0x203c03(%rip)        # 205178 <snap_retired> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1575`     1575:	eb 01                	jmp    1578 <pmu_uops_snap_before+0x6d> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1577`     1577:	90                   	nop groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1578`     1578:	5d                   	pop    %rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1579`     1579:	c3                   	retq    groups=`['structural_role']` kinds=`['branch_condition']`

#### Source Evidence

_No source evidence found._

### 4. `imm_occurrence:0x157e:operand_imm:1:0x20:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0x157e:operand_imm:1:0x20/i64 [stack_alignment_constant|structural_abi_constant]`
- Mapping kind: `stack_alignment_constant`
- Confidence: `semantic`
- Object semantic tags: `['stack_alignment_constant', 'structural_abi_constant']`
- Anchor instruction tags: `['prologue']`
- Scaffolding tags: `['prologue']`
- Occurrence: `{'occurrence_pc': '0x157e', 'operand_index': None, 'raw_suffix': 'operand_imm:1:0x20/i64 [stack_alignment_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 stack_alignment_constant 标签，更适合作为栈对齐常量解释。 检测到 ABI/脚手架标签：prologue，应更偏向解释为结构性对象，而非优先可变异语义对象。
- Candidate program elements: `['imm@0x157e:operand_imm:1:0x20/i64 [stack_alignment_constant|structural_abi_constant]']`
- direct_use_pcs: `['0x157e']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0x157e']`
- direct_operand_pcs: `['0x157e']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0x157e']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0x157a', '0x157b', '0x1582', '0x1588']`
- all_mapped_pcs: `['0x157a', '0x157b', '0x157e', '0x1582', '0x1588']`
- direct_parents: `[]`
- direct_children: `['reg:cf', 'reg:of', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf']`

#### PC Relation Entries

- `0x157a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x157b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x157e` kinds=`['direct_immediate_occurrence', 'direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.used_by/instruction_details.use_objects']`
- `0x1582` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1588` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0x157e`: `sub rsp, 0x20` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - instruction_semantic_tags: `['prologue']`
  - use_objects: `['imm_occurrence:0x157e:operand_imm:1:0x20:i64', 'reg:rsp']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0x157e:operand_imm:1:0x20:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0x157a`: `push rbp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x157b`: `mov rbp, rsp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1582`: `mov eax, dword ptr [rip + 0x20fbfc]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1588`: `test eax, eax` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0x157a`     157a:	55                   	push   %rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x157b`     157b:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x157e`     157e:	48 83 ec 20          	sub    $0x20,%rsp groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
- `0x1582`     1582:	8b 05 fc fb 20 00    	mov    0x20fbfc(%rip),%eax        # 211184 <uops_available> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1588`     1588:	85 c0                	test   %eax,%eax groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 5. `imm_occurrence:0x1582:mem_disp:1:0x20fbfc:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0x1582:mem_disp:1:0x20fbfc/i64 [rip_relative_displacement|structural_abi_constant]`
- Mapping kind: `rip_relative_displacement`
- Confidence: `semantic`
- Object semantic tags: `['rip_relative_displacement', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0x1582', 'operand_index': None, 'raw_suffix': 'mem_disp:1:0x20fbfc/i64 [rip_relative_displacement|structural_abi_constant]'}`
- Reason: 该 immediate 带有 rip_relative_displacement 标签，更适合作为 RIP 相对寻址位移解释。
- Candidate program elements: `['imm@0x1582:mem_disp:1:0x20fbfc/i64 [rip_relative_displacement|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0x1582']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0x1582']`
- direct_operand_pcs: `['0x1582']`
- structural_role_pcs: `['0x1582']`
- anchor_pcs: `['0x1582']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0x157b', '0x157e', '0x1588', '0x158a']`
- all_mapped_pcs: `['0x157b', '0x157e', '0x1582', '0x1588', '0x158a']`
- direct_parents: `[]`
- direct_children: `['var:uops_available']`

#### PC Relation Entries

- `0x157b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x157e` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1582` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0x1588` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x158a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0x1582`: `mov eax, dword ptr [rip + 0x20fbfc]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - use_objects: `['reg:rip', 'var:uops_available']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0x1582:mem_disp:1:0x20fbfc:i64', 'imm_occurrence:0x1582:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0x1582:mem_disp:1:0x20fbfc:i64', 'imm_occurrence:0x1582:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0x157b`: `mov rbp, rsp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x157e`: `sub rsp, 0x20` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1588`: `test eax, eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x158a`: `je 0x168e` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0x157b`     157b:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x157e`     157e:	48 83 ec 20          	sub    $0x20,%rsp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1582`     1582:	8b 05 fc fb 20 00    	mov    0x20fbfc(%rip),%eax        # 211184 <uops_available> groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0x1588`     1588:	85 c0                	test   %eax,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x158a`     158a:	0f 84 fe 00 00 00    	je     168e <pmu_uops_snap_after+0x114> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 6. `imm_occurrence:0x1582:mem_scale:1:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0x1582:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0x1582', 'operand_index': None, 'raw_suffix': 'mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0x1582:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0x1582']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0x1582']`
- direct_operand_pcs: `['0x1582']`
- structural_role_pcs: `['0x1582']`
- anchor_pcs: `['0x1582']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0x157b', '0x157e', '0x1588', '0x158a']`
- all_mapped_pcs: `['0x157b', '0x157e', '0x1582', '0x1588', '0x158a']`
- direct_parents: `[]`
- direct_children: `['var:uops_available']`

#### PC Relation Entries

- `0x157b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x157e` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1582` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0x1588` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x158a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0x1582`: `mov eax, dword ptr [rip + 0x20fbfc]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - use_objects: `['reg:rip', 'var:uops_available']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0x1582:mem_disp:1:0x20fbfc:i64', 'imm_occurrence:0x1582:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0x1582:mem_disp:1:0x20fbfc:i64', 'imm_occurrence:0x1582:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0x157b`: `mov rbp, rsp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x157e`: `sub rsp, 0x20` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1588`: `test eax, eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x158a`: `je 0x168e` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0x157b`     157b:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x157e`     157e:	48 83 ec 20          	sub    $0x20,%rsp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1582`     1582:	8b 05 fc fb 20 00    	mov    0x20fbfc(%rip),%eax        # 211184 <uops_available> groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0x1588`     1588:	85 c0                	test   %eax,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x158a`     158a:	0f 84 fe 00 00 00    	je     168e <pmu_uops_snap_after+0x114> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 7. `imm_occurrence:0x158a:operand_imm:0:0x168e:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0x158a:operand_imm:0:0x168e/i64`
- Mapping kind: `comparison_constant`
- Confidence: `semantic`
- Object semantic tags: `['comparison_constant']`
- Anchor instruction tags: `['conditional_branch', 'epilogue']`
- Scaffolding tags: `['epilogue']`
- Occurrence: `{'occurrence_pc': '0x158a', 'operand_index': None, 'raw_suffix': 'operand_imm:0:0x168e/i64'}`
- Reason: 该 immediate 带有 comparison_constant 标签，更适合作为比较语义常量解释。 检测到 ABI/脚手架标签：epilogue，应更偏向解释为结构性对象，而非优先可变异语义对象。
- Candidate program elements: `['imm@0x158a:operand_imm:0:0x168e/i64']`
- direct_use_pcs: `['0x158a']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `['0x168e', '0x168f', '0x1690']`
- direct_imm_pcs: `['0x158a']`
- direct_operand_pcs: `['0x158a']`
- structural_role_pcs: `['0x168e', '0x168f', '0x1690']`
- anchor_pcs: `['0x158a', '0x168e', '0x168f', '0x1690']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0x1582', '0x1588', '0x1590', '0x1596', '0x1686', '0x168c']`
- all_mapped_pcs: `['0x1582', '0x1588', '0x158a', '0x1590', '0x1596', '0x1686', '0x168c', '0x168e', '0x168f', '0x1690']`
- direct_parents: `[]`
- direct_children: `['reg:rbp', 'reg:rip', 'reg:rsp']`

#### PC Relation Entries

- `0x1582` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1588` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x158a` kinds=`['direct_immediate_occurrence', 'direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.used_by/instruction_details.use_objects']`
- `0x1590` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1596` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1686` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x168c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x168e` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x168f` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1690` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`

#### Direct Anchor Instruction Evidence

- PC `0x158a`: `je 0x168e` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - instruction_semantic_tags: `['conditional_branch']`
  - use_objects: `['imm_occurrence:0x158a:operand_imm:0:0x168e:i64', 'reg:zf']`
  - def_objects: `['reg:rip']`
  - immediates: `['imm_occurrence:0x158a:operand_imm:0:0x168e:i64']`
- PC `0x168e`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x168f`: `leave` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - instruction_semantic_tags: `['epilogue']`
  - use_objects: `['reg:rbp', 'reg:rsp', 'stack:[rbp-0x20]']`
  - def_objects: `['reg:rbp', 'reg:rip', 'reg:rsp']`
- PC `0x1690`: `ret` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - use_objects: `['reg:rsp', 'stack:[rbp-0x18]']`
  - def_objects: `['reg:rip', 'reg:rsp']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0x1582`: `mov eax, dword ptr [rip + 0x20fbfc]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1588`: `test eax, eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1590`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1596`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1686`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x168c`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0x1582`     1582:	8b 05 fc fb 20 00    	mov    0x20fbfc(%rip),%eax        # 211184 <uops_available> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1588`     1588:	85 c0                	test   %eax,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x158a`     158a:	0f 84 fe 00 00 00    	je     168e <pmu_uops_snap_after+0x114> groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
- `0x1590`     1590:	8b 05 ca 3b 20 00    	mov    0x203bca(%rip),%eax        # 205160 <use_rdpmc> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1596`     1596:	85 c0                	test   %eax,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1686`     1686:	89 05 f4 fa 20 00    	mov    %eax,0x20faf4(%rip)        # 211180 <uops_cnt> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x168c`     168c:	eb 01                	jmp    168f <pmu_uops_snap_after+0x115> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x168e`     168e:	90                   	nop groups=`['structural_role']` kinds=`['branch_condition']`
- `0x168f`     168f:	c9                   	leaveq  groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1690`     1690:	c3                   	retq    groups=`['structural_role']` kinds=`['branch_condition']`

#### Source Evidence

_No source evidence found._

### 8. `imm_occurrence:0x1695:operand_imm:1:0x10:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0x1695:operand_imm:1:0x10/i64 [stack_alignment_constant|structural_abi_constant]`
- Mapping kind: `stack_alignment_constant`
- Confidence: `semantic`
- Object semantic tags: `['stack_alignment_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0x1695', 'operand_index': None, 'raw_suffix': 'operand_imm:1:0x10/i64 [stack_alignment_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 stack_alignment_constant 标签，更适合作为栈对齐常量解释。
- Candidate program elements: `['imm@0x1695:operand_imm:1:0x10/i64 [stack_alignment_constant|structural_abi_constant]']`
- direct_use_pcs: `['0x1695']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `['0x1695']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0x1695']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0x1691', '0x1692', '0x1699', '0x16a0']`
- all_mapped_pcs: `['0x1691', '0x1692', '0x1695', '0x1699', '0x16a0']`
- direct_parents: `[]`
- direct_children: `['reg:cf', 'reg:of', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf']`

#### PC Relation Entries

- `0x1691` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1692` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1695` kinds=`['direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['object_detail.used_by/instruction_details.use_objects']`
- `0x1699` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x16a0` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0x1695`: `None` groups=`['direct_operand']` kinds=`['direct_use']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0x1691`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1692`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1699`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x16a0`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0x1691`     1691:	55                   	push   %rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1692`     1692:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1695`     1695:	48 83 ec 10          	sub    $0x10,%rsp groups=`['direct_operand']` kinds=`['direct_use']`
- `0x1699`     1699:	c7 45 fc 00 00 00 00 	movl   $0x0,-0x4(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x16a0`     16a0:	e9 8b 00 00 00       	jmpq   1730 <pmu_uops_print_results+0x9f> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 9. `imm_occurrence:0x1699:mem_disp:0:0xfffffffffffffffc:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0x1699:mem_disp:0:0xfffffffffffffffc/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0x1699', 'operand_index': None, 'raw_suffix': 'mem_disp:0:0xfffffffffffffffc/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0x1699:mem_disp:0:0xfffffffffffffffc/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0x1699']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `[]`
- structural_role_pcs: `['0x1699']`
- anchor_pcs: `['0x1699']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0x1692', '0x1695', '0x16a0', '0x16a5']`
- all_mapped_pcs: `['0x1692', '0x1695', '0x1699', '0x16a0', '0x16a5']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x4]']`

#### PC Relation Entries

- `0x1692` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1695` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1699` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0x16a0` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x16a5` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0x1699`: `None` groups=`['structural_role']` kinds=`['address_component']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0x1692`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1695`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x16a0`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x16a5`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0x1692`     1692:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1695`     1695:	48 83 ec 10          	sub    $0x10,%rsp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1699`     1699:	c7 45 fc 00 00 00 00 	movl   $0x0,-0x4(%rbp) groups=`['structural_role']` kinds=`['address_component']`
- `0x16a0`     16a0:	e9 8b 00 00 00       	jmpq   1730 <pmu_uops_print_results+0x9f> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x16a5`     16a5:	8b 45 fc             	mov    -0x4(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 10. `imm_occurrence:0x1699:mem_scale:0:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0x1699:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0x1699', 'operand_index': None, 'raw_suffix': 'mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0x1699:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0x1699']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `[]`
- structural_role_pcs: `['0x1699']`
- anchor_pcs: `['0x1699']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0x1692', '0x1695', '0x16a0', '0x16a5']`
- all_mapped_pcs: `['0x1692', '0x1695', '0x1699', '0x16a0', '0x16a5']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x4]']`

#### PC Relation Entries

- `0x1692` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1695` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1699` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0x16a0` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x16a5` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0x1699`: `None` groups=`['structural_role']` kinds=`['address_component']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0x1692`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1695`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x16a0`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x16a5`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0x1692`     1692:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1695`     1695:	48 83 ec 10          	sub    $0x10,%rsp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1699`     1699:	c7 45 fc 00 00 00 00 	movl   $0x0,-0x4(%rbp) groups=`['structural_role']` kinds=`['address_component']`
- `0x16a0`     16a0:	e9 8b 00 00 00       	jmpq   1730 <pmu_uops_print_results+0x9f> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x16a5`     16a5:	8b 45 fc             	mov    -0x4(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 11. `imm_occurrence:0x1699:operand_imm:1:0x0:i32`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0x1699:operand_imm:1:0x0/i32 [program_semantic_constant|store_constant]`
- Mapping kind: `store_constant`
- Confidence: `semantic`
- Object semantic tags: `['program_semantic_constant', 'store_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0x1699', 'operand_index': None, 'raw_suffix': 'operand_imm:1:0x0/i32 [program_semantic_constant|store_constant]'}`
- Reason: 该 immediate 带有 store_constant 标签，更适合作为写入值常量解释。
- Candidate program elements: `['imm@0x1699:operand_imm:1:0x0/i32 [program_semantic_constant|store_constant]']`
- direct_use_pcs: `['0x1699']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `['0x1699']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0x1699']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0x1692', '0x1695', '0x16a0', '0x16a5']`
- all_mapped_pcs: `['0x1692', '0x1695', '0x1699', '0x16a0', '0x16a5']`
- direct_parents: `[]`
- direct_children: `['reg:rip', 'stack:[rbp-0x4]']`

#### PC Relation Entries

- `0x1692` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1695` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1699` kinds=`['direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['object_detail.used_by/instruction_details.use_objects']`
- `0x16a0` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x16a5` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0x1699`: `None` groups=`['direct_operand']` kinds=`['direct_use']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0x1692`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1695`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x16a0`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x16a5`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0x1692`     1692:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1695`     1695:	48 83 ec 10          	sub    $0x10,%rsp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1699`     1699:	c7 45 fc 00 00 00 00 	movl   $0x0,-0x4(%rbp) groups=`['direct_operand']` kinds=`['direct_use']`
- `0x16a0`     16a0:	e9 8b 00 00 00       	jmpq   1730 <pmu_uops_print_results+0x9f> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x16a5`     16a5:	8b 45 fc             	mov    -0x4(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 12. `imm_occurrence:0x16a0:operand_imm:0:0x1730:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0x16a0:operand_imm:0:0x1730/i64`
- Mapping kind: `constant_or_address_component`
- Confidence: `structural`
- Object semantic tags: `[]`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0x16a0', 'operand_index': None, 'raw_suffix': 'operand_imm:0:0x1730/i64'}`
- Reason: 对象类型为 imm，更适合作为常量、位移、scale、比较值或地址组成部分解释。
- Candidate program elements: `['imm@0x16a0:operand_imm:0:0x1730/i64']`
- direct_use_pcs: `['0x16a0']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `['0x16a0']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0x16a0']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0x1695', '0x1699', '0x16a5', '0x16a8']`
- all_mapped_pcs: `['0x1695', '0x1699', '0x16a0', '0x16a5', '0x16a8']`
- direct_parents: `[]`
- direct_children: `['reg:rip']`

#### PC Relation Entries

- `0x1695` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1699` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x16a0` kinds=`['direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['object_detail.used_by/instruction_details.use_objects']`
- `0x16a5` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x16a8` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0x16a0`: `None` groups=`['direct_operand']` kinds=`['direct_use']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0x1695`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1699`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x16a5`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x16a8`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0x1695`     1695:	48 83 ec 10          	sub    $0x10,%rsp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1699`     1699:	c7 45 fc 00 00 00 00 	movl   $0x0,-0x4(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x16a0`     16a0:	e9 8b 00 00 00       	jmpq   1730 <pmu_uops_print_results+0x9f> groups=`['direct_operand']` kinds=`['direct_use']`
- `0x16a5`     16a5:	8b 45 fc             	mov    -0x4(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x16a8`     16a8:	48 98                	cltq    groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 13. `imm_occurrence:0x1730:mem_disp:1:0x20fa4a:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0x1730:mem_disp:1:0x20fa4a/i64 [rip_relative_displacement|structural_abi_constant]`
- Mapping kind: `rip_relative_displacement`
- Confidence: `semantic`
- Object semantic tags: `['rip_relative_displacement', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0x1730', 'operand_index': None, 'raw_suffix': 'mem_disp:1:0x20fa4a/i64 [rip_relative_displacement|structural_abi_constant]'}`
- Reason: 该 immediate 带有 rip_relative_displacement 标签，更适合作为 RIP 相对寻址位移解释。
- Candidate program elements: `['imm@0x1730:mem_disp:1:0x20fa4a/i64 [rip_relative_displacement|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0x1730']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `[]`
- structural_role_pcs: `['0x1730']`
- anchor_pcs: `['0x1730']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0x1727', '0x172c', '0x1736', '0x1739']`
- all_mapped_pcs: `['0x1727', '0x172c', '0x1730', '0x1736', '0x1739']`
- direct_parents: `[]`
- direct_children: `['var:uops_cnt']`

#### PC Relation Entries

- `0x1727` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x172c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1730` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0x1736` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1739` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0x1730`: `None` groups=`['structural_role']` kinds=`['address_component']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0x1727`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x172c`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1736`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1739`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0x1727`     1727:	e8 74 f2 ff ff       	callq  9a0 <printf@plt> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x172c`     172c:	83 45 fc 01          	addl   $0x1,-0x4(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1730`     1730:	8b 05 4a fa 20 00    	mov    0x20fa4a(%rip),%eax        # 211180 <uops_cnt> groups=`['structural_role']` kinds=`['address_component']`
- `0x1736`     1736:	39 45 fc             	cmp    %eax,-0x4(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1739`     1739:	0f 8c 66 ff ff ff    	jl     16a5 <pmu_uops_print_results+0x14> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 14. `imm_occurrence:0x1730:mem_scale:1:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0x1730:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0x1730', 'operand_index': None, 'raw_suffix': 'mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0x1730:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0x1730']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `[]`
- structural_role_pcs: `['0x1730']`
- anchor_pcs: `['0x1730']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0x1727', '0x172c', '0x1736', '0x1739']`
- all_mapped_pcs: `['0x1727', '0x172c', '0x1730', '0x1736', '0x1739']`
- direct_parents: `[]`
- direct_children: `['var:uops_cnt']`

#### PC Relation Entries

- `0x1727` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x172c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1730` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0x1736` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1739` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0x1730`: `None` groups=`['structural_role']` kinds=`['address_component']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0x1727`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x172c`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1736`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1739`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0x1727`     1727:	e8 74 f2 ff ff       	callq  9a0 <printf@plt> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x172c`     172c:	83 45 fc 01          	addl   $0x1,-0x4(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1730`     1730:	8b 05 4a fa 20 00    	mov    0x20fa4a(%rip),%eax        # 211180 <uops_cnt> groups=`['structural_role']` kinds=`['address_component']`
- `0x1736`     1736:	39 45 fc             	cmp    %eax,-0x4(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1739`     1739:	0f 8c 66 ff ff ff    	jl     16a5 <pmu_uops_print_results+0x14> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 15. `imm_occurrence:0x1736:mem_disp:0:0xfffffffffffffffc:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0x1736:mem_disp:0:0xfffffffffffffffc/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0x1736', 'operand_index': None, 'raw_suffix': 'mem_disp:0:0xfffffffffffffffc/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0x1736:mem_disp:0:0xfffffffffffffffc/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0x1736']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `[]`
- structural_role_pcs: `['0x1736']`
- anchor_pcs: `['0x1736']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0x172c', '0x1730', '0x1739', '0x173f']`
- all_mapped_pcs: `['0x172c', '0x1730', '0x1736', '0x1739', '0x173f']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x4]']`

#### PC Relation Entries

- `0x172c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1730` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1736` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0x1739` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x173f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0x1736`: `None` groups=`['structural_role']` kinds=`['address_component']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0x172c`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1730`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1739`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x173f`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0x172c`     172c:	83 45 fc 01          	addl   $0x1,-0x4(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1730`     1730:	8b 05 4a fa 20 00    	mov    0x20fa4a(%rip),%eax        # 211180 <uops_cnt> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1736`     1736:	39 45 fc             	cmp    %eax,-0x4(%rbp) groups=`['structural_role']` kinds=`['address_component']`
- `0x1739`     1739:	0f 8c 66 ff ff ff    	jl     16a5 <pmu_uops_print_results+0x14> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x173f`     173f:	90                   	nop groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 16. `imm_occurrence:0x1736:mem_scale:0:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0x1736:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0x1736', 'operand_index': None, 'raw_suffix': 'mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0x1736:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0x1736']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `[]`
- structural_role_pcs: `['0x1736']`
- anchor_pcs: `['0x1736']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0x172c', '0x1730', '0x1739', '0x173f']`
- all_mapped_pcs: `['0x172c', '0x1730', '0x1736', '0x1739', '0x173f']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x4]']`

#### PC Relation Entries

- `0x172c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1730` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1736` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0x1739` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x173f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0x1736`: `None` groups=`['structural_role']` kinds=`['address_component']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0x172c`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1730`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1739`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x173f`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0x172c`     172c:	83 45 fc 01          	addl   $0x1,-0x4(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1730`     1730:	8b 05 4a fa 20 00    	mov    0x20fa4a(%rip),%eax        # 211180 <uops_cnt> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1736`     1736:	39 45 fc             	cmp    %eax,-0x4(%rbp) groups=`['structural_role']` kinds=`['address_component']`
- `0x1739`     1739:	0f 8c 66 ff ff ff    	jl     16a5 <pmu_uops_print_results+0x14> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x173f`     173f:	90                   	nop groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 17. `imm_occurrence:0x1739:operand_imm:0:0x16a5:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0x1739:operand_imm:0:0x16a5/i64`
- Mapping kind: `comparison_constant`
- Confidence: `semantic`
- Object semantic tags: `['comparison_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0x1739', 'operand_index': None, 'raw_suffix': 'operand_imm:0:0x16a5/i64'}`
- Reason: 该 immediate 带有 comparison_constant 标签，更适合作为比较语义常量解释。
- Candidate program elements: `['imm@0x1739:operand_imm:0:0x16a5/i64']`
- direct_use_pcs: `['0x1739']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `['0x173f', '0x1740', '0x1741']`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `['0x1739']`
- structural_role_pcs: `['0x173f', '0x1740', '0x1741']`
- anchor_pcs: `['0x1739', '0x173f', '0x1740', '0x1741']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0x1730', '0x1736']`
- all_mapped_pcs: `['0x1730', '0x1736', '0x1739', '0x173f', '0x1740', '0x1741']`
- direct_parents: `[]`
- direct_children: `['reg:rbp', 'reg:rip', 'reg:rsp']`

#### PC Relation Entries

- `0x1730` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1736` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1739` kinds=`['direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['object_detail.used_by/instruction_details.use_objects']`
- `0x173f` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1740` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1741` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`

#### Direct Anchor Instruction Evidence

- PC `0x1739`: `None` groups=`['direct_operand']` kinds=`['direct_use']`
- PC `0x173f`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x1740`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x1741`: `None` groups=`['structural_role']` kinds=`['branch_condition']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0x1730`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1736`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0x1730`     1730:	8b 05 4a fa 20 00    	mov    0x20fa4a(%rip),%eax        # 211180 <uops_cnt> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1736`     1736:	39 45 fc             	cmp    %eax,-0x4(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1739`     1739:	0f 8c 66 ff ff ff    	jl     16a5 <pmu_uops_print_results+0x14> groups=`['direct_operand']` kinds=`['direct_use']`
- `0x173f`     173f:	90                   	nop groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1740`     1740:	c9                   	leaveq  groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1741`     1741:	c3                   	retq    groups=`['structural_role']` kinds=`['branch_condition']`

#### Source Evidence

_No source evidence found._

### 18. `imm_occurrence:0xa79:operand_imm:1:0xfffffffffffffff0:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xa79:operand_imm:1:0xfffffffffffffff0/i64 [stack_alignment_constant|structural_abi_constant]`
- Mapping kind: `stack_alignment_constant`
- Confidence: `semantic`
- Object semantic tags: `['stack_alignment_constant', 'structural_abi_constant']`
- Anchor instruction tags: `['stack_alignment']`
- Scaffolding tags: `['stack_alignment']`
- Occurrence: `{'occurrence_pc': '0xa79', 'operand_index': None, 'raw_suffix': 'operand_imm:1:0xfffffffffffffff0/i64 [stack_alignment_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 stack_alignment_constant 标签，更适合作为栈对齐常量解释。 检测到 ABI/脚手架标签：stack_alignment，应更偏向解释为结构性对象，而非优先可变异语义对象。
- Candidate program elements: `['imm@0xa79:operand_imm:1:0xfffffffffffffff0/i64 [stack_alignment_constant|structural_abi_constant]']`
- direct_use_pcs: `['0xa79']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xa79']`
- direct_operand_pcs: `['0xa79']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xa79']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xa75', '0xa76', '0xa7d', '0xa7e']`
- all_mapped_pcs: `['0xa75', '0xa76', '0xa79', '0xa7d', '0xa7e']`
- direct_parents: `[]`
- direct_children: `['reg:cf', 'reg:of', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf']`

#### PC Relation Entries

- `0xa75` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xa76` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xa79` kinds=`['direct_immediate_occurrence', 'direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.used_by/instruction_details.use_objects']`
- `0xa7d` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xa7e` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xa79`: `and rsp, 0xfffffffffffffff0` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
  - Source: `??:None` function=`_start`
  - instruction_semantic_tags: `['stack_alignment']`
  - use_objects: `['imm_occurrence:0xa79:operand_imm:1:0xfffffffffffffff0:i64', 'reg:rsp']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xa79:operand_imm:1:0xfffffffffffffff0:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xa75`: `pop rsi` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xa76`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xa7d`: `push rax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xa7e`: `push rsp` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xa75`      a75:	5e                   	pop    %rsi groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xa76`      a76:	48 89 e2             	mov    %rsp,%rdx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xa79`      a79:	48 83 e4 f0          	and    $0xfffffffffffffff0,%rsp groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
- `0xa7d`      a7d:	50                   	push   %rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xa7e`      a7e:	54                   	push   %rsp groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 19. `imm_occurrence:0xa94:mem_disp:0:0x202546:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xa94:mem_disp:0:0x202546/i64 [rip_relative_displacement|structural_abi_constant]`
- Mapping kind: `rip_relative_displacement`
- Confidence: `semantic`
- Object semantic tags: `['rip_relative_displacement', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xa94', 'operand_index': None, 'raw_suffix': 'mem_disp:0:0x202546/i64 [rip_relative_displacement|structural_abi_constant]'}`
- Reason: 该 immediate 带有 rip_relative_displacement 标签，更适合作为 RIP 相对寻址位移解释。
- Candidate program elements: `['imm@0xa94:mem_disp:0:0x202546/i64 [rip_relative_displacement|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xa94']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xa94']`
- direct_operand_pcs: `['0xa94']`
- structural_role_pcs: `['0xa94']`
- anchor_pcs: `['0xa94']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xa86', '0xa8d', '0xa9a', '0xa9b']`
- all_mapped_pcs: `['0xa86', '0xa8d', '0xa94', '0xa9a', '0xa9b']`
- direct_parents: `[]`
- direct_children: `['mem:0x202fe0']`

#### PC Relation Entries

- `0xa86` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xa8d` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xa94` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xa9a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xa9b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xa94`: `call qword ptr [rip + 0x202546]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `??:None` function=`_start`
  - call_target: `{'operand': 'qword ptr [rip + 0x202546]', 'resolved_symbol': '__libc_start_main@GLIBC_2.2.5', 'call_kind': 'indirect_call_through_memory', 'display_target': '__libc_start_main@GLIBC_2.2.5'}`
  - use_objects: `['mem:0x202fe0', 'reg:rip', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rsp+0x0]']`
  - addr_objects: `['imm_occurrence:0xa94:mem_disp:0:0x202546:i64', 'imm_occurrence:0xa94:mem_scale:0:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xa94:mem_disp:0:0x202546:i64', 'imm_occurrence:0xa94:mem_scale:0:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xa86`: `lea rcx, [rip + 0xf33]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xa8d`: `lea rdi, [rip + 0x2a7]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xa9a`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xa9b`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xa86`      a86:	48 8d 0d 33 0f 00 00 	lea    0xf33(%rip),%rcx        # 19c0 <__libc_csu_init> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xa8d`      a8d:	48 8d 3d a7 02 00 00 	lea    0x2a7(%rip),%rdi        # d3b <main> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xa94`      a94:	ff 15 46 25 20 00    	callq  *0x202546(%rip)        # 202fe0 <__libc_start_main@GLIBC_2.2.5> groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xa9a`      a9a:	f4                   	hlt     groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xa9b`      a9b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1) groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 20. `imm_occurrence:0xa94:mem_scale:0:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xa94:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xa94', 'operand_index': None, 'raw_suffix': 'mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xa94:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xa94']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xa94']`
- direct_operand_pcs: `['0xa94']`
- structural_role_pcs: `['0xa94']`
- anchor_pcs: `['0xa94']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xa86', '0xa8d', '0xa9a', '0xa9b']`
- all_mapped_pcs: `['0xa86', '0xa8d', '0xa94', '0xa9a', '0xa9b']`
- direct_parents: `[]`
- direct_children: `['mem:0x202fe0']`

#### PC Relation Entries

- `0xa86` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xa8d` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xa94` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xa9a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xa9b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xa94`: `call qword ptr [rip + 0x202546]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `??:None` function=`_start`
  - call_target: `{'operand': 'qword ptr [rip + 0x202546]', 'resolved_symbol': '__libc_start_main@GLIBC_2.2.5', 'call_kind': 'indirect_call_through_memory', 'display_target': '__libc_start_main@GLIBC_2.2.5'}`
  - use_objects: `['mem:0x202fe0', 'reg:rip', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rsp+0x0]']`
  - addr_objects: `['imm_occurrence:0xa94:mem_disp:0:0x202546:i64', 'imm_occurrence:0xa94:mem_scale:0:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xa94:mem_disp:0:0x202546:i64', 'imm_occurrence:0xa94:mem_scale:0:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xa86`: `lea rcx, [rip + 0xf33]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xa8d`: `lea rdi, [rip + 0x2a7]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xa9a`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xa9b`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xa86`      a86:	48 8d 0d 33 0f 00 00 	lea    0xf33(%rip),%rcx        # 19c0 <__libc_csu_init> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xa8d`      a8d:	48 8d 3d a7 02 00 00 	lea    0x2a7(%rip),%rdi        # d3b <main> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xa94`      a94:	ff 15 46 25 20 00    	callq  *0x202546(%rip)        # 202fe0 <__libc_start_main@GLIBC_2.2.5> groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xa9a`      a9a:	f4                   	hlt     groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xa9b`      a9b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1) groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 21. `imm_occurrence:0xb7e:operand_imm:1:0x10:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xb7e:operand_imm:1:0x10/i64 [stack_alignment_constant|structural_abi_constant]`
- Mapping kind: `stack_alignment_constant`
- Confidence: `semantic`
- Object semantic tags: `['stack_alignment_constant', 'structural_abi_constant']`
- Anchor instruction tags: `['prologue']`
- Scaffolding tags: `['prologue']`
- Occurrence: `{'occurrence_pc': '0xb7e', 'operand_index': None, 'raw_suffix': 'operand_imm:1:0x10/i64 [stack_alignment_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 stack_alignment_constant 标签，更适合作为栈对齐常量解释。 检测到 ABI/脚手架标签：prologue，应更偏向解释为结构性对象，而非优先可变异语义对象。
- Candidate program elements: `['imm@0xb7e:operand_imm:1:0x10/i64 [stack_alignment_constant|structural_abi_constant]']`
- direct_use_pcs: `['0xb7e']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xb7e']`
- direct_operand_pcs: `['0xb7e']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xb7e']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xb7a', '0xb7b', '0xb82']`
- all_mapped_pcs: `['0xb7a', '0xb7b', '0xb7e', '0xb82']`
- direct_parents: `[]`
- direct_children: `['reg:cf', 'reg:of', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf']`

#### PC Relation Entries

- `0xb7a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb7b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb7e` kinds=`['direct_immediate_occurrence', 'direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.used_by/instruction_details.use_objects']`
- `0xb82` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xb7e`: `sub rsp, 0x10` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
  - Source: `/root/src/spectre_stage1_2_auto.c:58` function=`spectre_function`
  - instruction_semantic_tags: `['prologue']`
  - use_objects: `['imm_occurrence:0xb7e:operand_imm:1:0x10:i64', 'reg:rsp']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xb7e:operand_imm:1:0x10:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xb7a`: `push rbp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xb7b`: `mov rbp, rsp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xb82`: `mov qword ptr [rbp - 8], rdi` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xb7a`      b7a:	55                   	push   %rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb7b`      b7b:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb7e`      b7e:	48 83 ec 10          	sub    $0x10,%rsp groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
- `0xb82`      b82:	48 89 7d f8          	mov    %rdi,-0x8(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:58` function=`spectre_function` pcs=`['0xb7a', '0xb7b', '0xb7e', '0xb82']` groups=`['direct_operand', 'evidence_only']` kinds=`['direct_immediate_occurrence', 'direct_use', 'evidence_only']`

```c
   56: ********************************************************************/
   57: __attribute__((noinline))
   58: void spectre_function(size_t x) {
   59: 
   60:   pmu_uops_snap_before();
```

### 22. `imm_occurrence:0xb82:mem_disp:0:0xfffffffffffffff8:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xb82:mem_disp:0:0xfffffffffffffff8/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `['argument_shuffle']`
- Scaffolding tags: `['argument_shuffle']`
- Occurrence: `{'occurrence_pc': '0xb82', 'operand_index': None, 'raw_suffix': 'mem_disp:0:0xfffffffffffffff8/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。 检测到 ABI/脚手架标签：argument_shuffle，应更偏向解释为结构性对象，而非优先可变异语义对象。
- Candidate program elements: `['imm@0xb82:mem_disp:0:0xfffffffffffffff8/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xb82']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xb82']`
- direct_operand_pcs: `['0xb82']`
- structural_role_pcs: `['0xb82']`
- anchor_pcs: `['0xb82']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xb7b', '0xb7e']`
- all_mapped_pcs: `['0xb7b', '0xb7e', '0xb82']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x8]']`

#### PC Relation Entries

- `0xb7b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb7e` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb82` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`

#### Direct Anchor Instruction Evidence

- PC `0xb82`: `mov qword ptr [rbp - 8], rdi` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:58` function=`spectre_function`
  - instruction_semantic_tags: `['argument_shuffle']`
  - use_objects: `['reg:rbp', 'reg:rdi']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x8]']`
  - addr_objects: `['imm_occurrence:0xb82:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xb82:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xb82:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xb82:mem_scale:0:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xb7b`: `mov rbp, rsp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xb7e`: `sub rsp, 0x10` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xb7b`      b7b:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb7e`      b7e:	48 83 ec 10          	sub    $0x10,%rsp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb82`      b82:	48 89 7d f8          	mov    %rdi,-0x8(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:58` function=`spectre_function` pcs=`['0xb7b', '0xb7e', '0xb82']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
   56: ********************************************************************/
   57: __attribute__((noinline))
   58: void spectre_function(size_t x) {
   59: 
   60:   pmu_uops_snap_before();
```

### 23. `imm_occurrence:0xb82:mem_scale:0:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xb82:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `['argument_shuffle']`
- Scaffolding tags: `['argument_shuffle']`
- Occurrence: `{'occurrence_pc': '0xb82', 'operand_index': None, 'raw_suffix': 'mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。 检测到 ABI/脚手架标签：argument_shuffle，应更偏向解释为结构性对象，而非优先可变异语义对象。
- Candidate program elements: `['imm@0xb82:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xb82']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xb82']`
- direct_operand_pcs: `['0xb82']`
- structural_role_pcs: `['0xb82']`
- anchor_pcs: `['0xb82']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xb7b', '0xb7e']`
- all_mapped_pcs: `['0xb7b', '0xb7e', '0xb82']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x8]']`

#### PC Relation Entries

- `0xb7b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb7e` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb82` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`

#### Direct Anchor Instruction Evidence

- PC `0xb82`: `mov qword ptr [rbp - 8], rdi` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:58` function=`spectre_function`
  - instruction_semantic_tags: `['argument_shuffle']`
  - use_objects: `['reg:rbp', 'reg:rdi']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x8]']`
  - addr_objects: `['imm_occurrence:0xb82:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xb82:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xb82:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xb82:mem_scale:0:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xb7b`: `mov rbp, rsp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xb7e`: `sub rsp, 0x10` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xb7b`      b7b:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb7e`      b7e:	48 83 ec 10          	sub    $0x10,%rsp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb82`      b82:	48 89 7d f8          	mov    %rdi,-0x8(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:58` function=`spectre_function` pcs=`['0xb7b', '0xb7e', '0xb82']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
   56: ********************************************************************/
   57: __attribute__((noinline))
   58: void spectre_function(size_t x) {
   59: 
   60:   pmu_uops_snap_before();
```

### 24. `imm_occurrence:0xb86:operand_imm:0:0x150b:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xb86:operand_imm:0:0x150b/i64 [call_target_constant|program_semantic_constant|store_constant]`
- Mapping kind: `store_constant`
- Confidence: `semantic`
- Object semantic tags: `['call_target_constant', 'program_semantic_constant', 'store_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xb86', 'operand_index': None, 'raw_suffix': 'operand_imm:0:0x150b/i64 [call_target_constant|program_semantic_constant|store_constant]'}`
- Reason: 该 immediate 带有 store_constant 标签，更适合作为写入值常量解释。
- Candidate program elements: `['imm@0xb86:operand_imm:0:0x150b/i64 [call_target_constant|program_semantic_constant|store_constant]']`
- direct_use_pcs: `['0xb86']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xb86']`
- direct_operand_pcs: `['0xb86']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xb86']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `[]`
- all_mapped_pcs: `['0xb86']`
- direct_parents: `[]`
- direct_children: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x18]']`

#### PC Relation Entries

- `0xb86` kinds=`['direct_immediate_occurrence', 'direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.used_by/instruction_details.use_objects']`

#### Direct Anchor Instruction Evidence

- PC `0xb86`: `call 0x150b` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
  - Source: `/root/src/spectre_stage1_2_auto.c:60` function=`spectre_function`
  - call_target: `{'operand': '0x150b', 'resolved_symbol': 'pmu_uops_snap_before', 'call_kind': 'direct_call_symbol', 'display_target': 'pmu_uops_snap_before'}`
  - use_objects: `['imm_occurrence:0xb86:operand_imm:0:0x150b:i64', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x18]']`
  - immediates: `['imm_occurrence:0xb86:operand_imm:0:0x150b:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

_No evidence-only instruction evidence._

#### Assembly References

- `0xb86`      b86:	e8 80 09 00 00       	callq  150b <pmu_uops_snap_before> groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:60` function=`spectre_function` pcs=`['0xb86']` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`

```c
   58: void spectre_function(size_t x) {
   59: 
   60:   pmu_uops_snap_before();
   61: 
   62:   asm volatile(".globl STAGE1_BEGIN\nSTAGE1_BEGIN:");
```

### 25. `imm_occurrence:0xb8b:mem_disp:1:0x20248f:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xb8b:mem_disp:1:0x20248f/i64 [rip_relative_displacement|structural_abi_constant]`
- Mapping kind: `rip_relative_displacement`
- Confidence: `semantic`
- Object semantic tags: `['rip_relative_displacement', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xb8b', 'operand_index': None, 'raw_suffix': 'mem_disp:1:0x20248f/i64 [rip_relative_displacement|structural_abi_constant]'}`
- Reason: 该 immediate 带有 rip_relative_displacement 标签，更适合作为 RIP 相对寻址位移解释。
- Candidate program elements: `['imm@0xb8b:mem_disp:1:0x20248f/i64 [rip_relative_displacement|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xb8b']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xb8b']`
- direct_operand_pcs: `['0xb8b']`
- structural_role_pcs: `['0xb8b']`
- anchor_pcs: `['0xb8b']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xb91', '0xb93']`
- all_mapped_pcs: `['0xb8b', '0xb91', '0xb93']`
- direct_parents: `[]`
- direct_children: `['var:array1_size']`

#### PC Relation Entries

- `0xb8b` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xb91` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb93` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xb8b`: `mov eax, dword ptr [rip + 0x20248f]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function`
  - use_objects: `['reg:rip', 'var:array1_size']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xb8b:mem_disp:1:0x20248f:i64', 'imm_occurrence:0xb8b:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xb8b:mem_disp:1:0x20248f:i64', 'imm_occurrence:0xb8b:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xb91`: `mov eax, eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xb93`: `cmp qword ptr [rbp - 8], rax` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xb8b`      b8b:	8b 05 8f 24 20 00    	mov    0x20248f(%rip),%eax        # 203020 <array1_size> groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xb91`      b91:	89 c0                	mov    %eax,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb93`      b93:	48 39 45 f8          	cmp    %rax,-0x8(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function` pcs=`['0xb8b', '0xb91', '0xb93']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
   61: 
   62:   asm volatile(".globl STAGE1_BEGIN\nSTAGE1_BEGIN:");
   63:   if (x < array1_size) {
   64:     NOP_REGION_BEGIN
   65:     temp &= array2[array1[x] * 512];
```

### 26. `imm_occurrence:0xb8b:mem_scale:1:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xb8b:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xb8b', 'operand_index': None, 'raw_suffix': 'mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xb8b:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xb8b']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xb8b']`
- direct_operand_pcs: `['0xb8b']`
- structural_role_pcs: `['0xb8b']`
- anchor_pcs: `['0xb8b']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xb91', '0xb93']`
- all_mapped_pcs: `['0xb8b', '0xb91', '0xb93']`
- direct_parents: `[]`
- direct_children: `['var:array1_size']`

#### PC Relation Entries

- `0xb8b` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xb91` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb93` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xb8b`: `mov eax, dword ptr [rip + 0x20248f]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function`
  - use_objects: `['reg:rip', 'var:array1_size']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xb8b:mem_disp:1:0x20248f:i64', 'imm_occurrence:0xb8b:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xb8b:mem_disp:1:0x20248f:i64', 'imm_occurrence:0xb8b:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xb91`: `mov eax, eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xb93`: `cmp qword ptr [rbp - 8], rax` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xb8b`      b8b:	8b 05 8f 24 20 00    	mov    0x20248f(%rip),%eax        # 203020 <array1_size> groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xb91`      b91:	89 c0                	mov    %eax,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb93`      b93:	48 39 45 f8          	cmp    %rax,-0x8(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function` pcs=`['0xb8b', '0xb91', '0xb93']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
   61: 
   62:   asm volatile(".globl STAGE1_BEGIN\nSTAGE1_BEGIN:");
   63:   if (x < array1_size) {
   64:     NOP_REGION_BEGIN
   65:     temp &= array2[array1[x] * 512];
```

### 27. `imm_occurrence:0xb93:mem_disp:0:0xfffffffffffffff8:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xb93:mem_disp:0:0xfffffffffffffff8/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xb93', 'operand_index': None, 'raw_suffix': 'mem_disp:0:0xfffffffffffffff8/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xb93:mem_disp:0:0xfffffffffffffff8/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xb93']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xb93']`
- direct_operand_pcs: `['0xb93']`
- structural_role_pcs: `['0xb93']`
- anchor_pcs: `['0xb93']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xb8b', '0xb91', '0xb97']`
- all_mapped_pcs: `['0xb8b', '0xb91', '0xb93', '0xb97']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x8]']`

#### PC Relation Entries

- `0xb8b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb91` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb93` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xb97` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xb93`: `cmp qword ptr [rbp - 8], rax` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x8]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xb93:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xb93:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xb93:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xb93:mem_scale:0:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xb8b`: `mov eax, dword ptr [rip + 0x20248f]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xb91`: `mov eax, eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xb97`: `jae 0xbcd` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xb8b`      b8b:	8b 05 8f 24 20 00    	mov    0x20248f(%rip),%eax        # 203020 <array1_size> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb91`      b91:	89 c0                	mov    %eax,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb93`      b93:	48 39 45 f8          	cmp    %rax,-0x8(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xb97`      b97:	73 34                	jae    bcd <STAGE1_END> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function` pcs=`['0xb8b', '0xb91', '0xb93', '0xb97']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
   61: 
   62:   asm volatile(".globl STAGE1_BEGIN\nSTAGE1_BEGIN:");
   63:   if (x < array1_size) {
   64:     NOP_REGION_BEGIN
   65:     temp &= array2[array1[x] * 512];
```

### 28. `imm_occurrence:0xb93:mem_scale:0:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xb93:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xb93', 'operand_index': None, 'raw_suffix': 'mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xb93:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xb93']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xb93']`
- direct_operand_pcs: `['0xb93']`
- structural_role_pcs: `['0xb93']`
- anchor_pcs: `['0xb93']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xb8b', '0xb91', '0xb97']`
- all_mapped_pcs: `['0xb8b', '0xb91', '0xb93', '0xb97']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x8]']`

#### PC Relation Entries

- `0xb8b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb91` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb93` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xb97` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xb93`: `cmp qword ptr [rbp - 8], rax` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x8]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xb93:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xb93:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xb93:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xb93:mem_scale:0:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xb8b`: `mov eax, dword ptr [rip + 0x20248f]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xb91`: `mov eax, eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xb97`: `jae 0xbcd` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xb8b`      b8b:	8b 05 8f 24 20 00    	mov    0x20248f(%rip),%eax        # 203020 <array1_size> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb91`      b91:	89 c0                	mov    %eax,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb93`      b93:	48 39 45 f8          	cmp    %rax,-0x8(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xb97`      b97:	73 34                	jae    bcd <STAGE1_END> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function` pcs=`['0xb8b', '0xb91', '0xb93', '0xb97']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
   61: 
   62:   asm volatile(".globl STAGE1_BEGIN\nSTAGE1_BEGIN:");
   63:   if (x < array1_size) {
   64:     NOP_REGION_BEGIN
   65:     temp &= array2[array1[x] * 512];
```

### 29. `imm_occurrence:0xb97:operand_imm:0:0xbcd:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xb97:operand_imm:0:0xbcd/i64`
- Mapping kind: `comparison_constant`
- Confidence: `semantic`
- Object semantic tags: `['comparison_constant']`
- Anchor instruction tags: `['callee_save_spill', 'conditional_branch', 'epilogue', 'prologue']`
- Scaffolding tags: `['callee_save_spill', 'epilogue', 'prologue']`
- Occurrence: `{'occurrence_pc': '0xb97', 'operand_index': None, 'raw_suffix': 'operand_imm:0:0xbcd/i64'}`
- Reason: 该 immediate 带有 comparison_constant 标签，更适合作为比较语义常量解释。 检测到 ABI/脚手架标签：callee_save_spill, epilogue, prologue，应更偏向解释为结构性对象，而非优先可变异语义对象。
- Candidate program elements: `['imm@0xb97:operand_imm:0:0xbcd/i64']`
- direct_use_pcs: `['0xb97']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `['0xb99', '0xba0', '0xba4', '0xba7', '0xbaa', '0xbad', '0xbb0', '0xbb3', '0xbba', '0xbbe', '0xbc5', '0xbc7', '0xbcd', '0xbd2', '0xbd3', '0xbd4', '0x157a', '0x157b', '0x157e', '0x1582', '0x1588', '0x158a', '0x168e', '0x168f', '0x1690']`
- direct_imm_pcs: `['0xb97']`
- direct_operand_pcs: `['0xb97']`
- structural_role_pcs: `['0xb99', '0xba0', '0xba4', '0xba7', '0xbaa', '0xbad', '0xbb0', '0xbb3', '0xbba', '0xbbe', '0xbc5', '0xbc7', '0xbcd', '0xbd2', '0xbd3', '0xbd4', '0x157a', '0x157b', '0x157e', '0x1582', '0x1588', '0x158a', '0x168e', '0x168f', '0x1690']`
- anchor_pcs: `['0xb97', '0xb99', '0xba0', '0xba4', '0xba7', '0xbaa', '0xbad', '0xbb0', '0xbb3', '0xbba', '0xbbe', '0xbc5', '0xbc7', '0xbcd', '0xbd2', '0xbd3', '0xbd4', '0x157a', '0x157b', '0x157e', '0x1582', '0x1588', '0x158a', '0x168e', '0x168f', '0x1690']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xb91', '0xb93', '0x1590', '0x1596', '0x1686', '0x168c']`
- all_mapped_pcs: `['0xb91', '0xb93', '0xb97', '0xb99', '0xba0', '0xba4', '0xba7', '0xbaa', '0xbad', '0xbb0', '0xbb3', '0xbba', '0xbbe', '0xbc5', '0xbc7', '0xbcd', '0xbd2', '0xbd3', '0xbd4', '0x157a', '0x157b', '0x157e', '0x1582', '0x1588', '0x158a', '0x1590', '0x1596', '0x1686', '0x168c', '0x168e', '0x168f', '0x1690']`
- direct_parents: `[]`
- direct_children: `['reg:cf', 'reg:of', 'reg:rax', 'reg:rbp', 'reg:rdx', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf', 'stack:[rbp-0x18]', 'stack:[rbp-0x20]', 'var:temp']`

#### PC Relation Entries

- `0xb91` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb93` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb97` kinds=`['direct_immediate_occurrence', 'direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.used_by/instruction_details.use_objects']`
- `0xb99` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xba0` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xba4` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xba7` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbaa` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbad` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbb0` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbb3` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbba` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbbe` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbc5` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbc7` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbcd` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbd2` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbd3` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbd4` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x157a` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x157b` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x157e` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1582` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1588` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x158a` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1590` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1596` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1686` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x168c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x168e` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x168f` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1690` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`

#### Direct Anchor Instruction Evidence

- PC `0xb97`: `jae 0xbcd` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
  - Source: `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function`
  - instruction_semantic_tags: `['conditional_branch']`
  - use_objects: `['imm_occurrence:0xb97:operand_imm:0:0xbcd:i64', 'reg:cf']`
  - def_objects: `['reg:rip']`
  - immediates: `['imm_occurrence:0xb97:operand_imm:0:0xbcd:i64']`
- PC `0xb99`: `lea rdx, [rip + 0x2024a0]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rip']`
  - def_objects: `['reg:rdx', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xb99:mem_disp:1:0x2024a0:i64', 'imm_occurrence:0xb99:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xb99:mem_disp:1:0x2024a0:i64', 'imm_occurrence:0xb99:mem_scale:1:0x1:i64']`
- PC `0xba0`: `mov rax, qword ptr [rbp - 8]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x8]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xba0:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xba0:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xba0:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xba0:mem_scale:1:0x1:i64']`
- PC `0xba4`: `add rax, rdx` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rdx']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0xba7`: `movzx eax, byte ptr [rax]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'var:array1']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xba7:mem_disp:1:0x0:i64', 'imm_occurrence:0xba7:mem_scale:1:0x1:i64', 'reg:rax', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xba7:mem_disp:1:0x0:i64', 'imm_occurrence:0xba7:mem_scale:1:0x1:i64']`
- PC `0xbaa`: `movzx eax, al` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:rax', 'reg:rip']`
- PC `0xbad`: `shl eax, 9` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['imm_occurrence:0xbad:operand_imm:1:0x9:i8', 'reg:rax']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xbad:operand_imm:1:0x9:i8']`
- PC `0xbb0`: `movsxd rdx, eax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:rdx', 'reg:rip']`
- PC `0xbb3`: `lea rax, [rip + 0x210706]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rip']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xbb3:mem_disp:1:0x210706:i64', 'imm_occurrence:0xbb3:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xbb3:mem_disp:1:0x210706:i64', 'imm_occurrence:0xbb3:mem_scale:1:0x1:i64']`
- PC `0xbba`: `movzx edx, byte ptr [rdx + rax]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rdx', 'var:array2']`
  - def_objects: `['reg:rdx', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xbba:mem_disp:1:0x0:i64', 'imm_occurrence:0xbba:mem_scale:1:0x1:i64', 'reg:rax', 'reg:rdx', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xbba:mem_disp:1:0x0:i64', 'imm_occurrence:0xbba:mem_scale:1:0x1:i64']`
- PC `0xbbe`: `movzx eax, byte ptr [rip + 0x202544]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rip', 'var:temp']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xbbe:mem_disp:1:0x202544:i64', 'imm_occurrence:0xbbe:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xbbe:mem_disp:1:0x202544:i64', 'imm_occurrence:0xbbe:mem_scale:1:0x1:i64']`
- PC `0xbc5`: `and eax, edx` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rdx']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0xbc7`: `mov byte ptr [rip + 0x20253c], al` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rip']`
  - def_objects: `['reg:rip', 'var:temp']`
  - addr_objects: `['imm_occurrence:0xbc7:mem_disp:0:0x20253c:i64', 'imm_occurrence:0xbc7:mem_scale:0:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xbc7:mem_disp:0:0x20253c:i64', 'imm_occurrence:0xbc7:mem_scale:0:0x1:i64']`
- PC `0xbcd`: `call 0x157a` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:70` function=`spectre_function`
  - call_target: `{'operand': '0x157a', 'resolved_symbol': 'pmu_uops_snap_after', 'call_kind': 'direct_call_symbol', 'display_target': 'pmu_uops_snap_after'}`
  - use_objects: `['imm_occurrence:0xbcd:operand_imm:0:0x157a:i64', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x18]']`
  - immediates: `['imm_occurrence:0xbcd:operand_imm:0:0x157a:i64']`
- PC `0xbd2`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xbd3`: `leave` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:71` function=`spectre_function`
  - instruction_semantic_tags: `['epilogue']`
  - use_objects: `['reg:rbp', 'reg:rsp', 'stack:[rbp-0x40]']`
  - def_objects: `['reg:rbp', 'reg:rip', 'reg:rsp']`
- PC `0xbd4`: `ret` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:71` function=`spectre_function`
  - use_objects: `['reg:rsp', 'stack:[rbp-0x38]']`
  - def_objects: `['reg:rip', 'reg:rsp']`
- PC `0x157a`: `push rbp` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - instruction_semantic_tags: `['callee_save_spill', 'prologue']`
  - use_objects: `['reg:rbp', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x20]']`
- PC `0x157b`: `mov rbp, rsp` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - instruction_semantic_tags: `['prologue']`
  - use_objects: `['reg:rsp']`
  - def_objects: `['reg:rbp', 'reg:rip']`
- PC `0x157e`: `sub rsp, 0x20` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - instruction_semantic_tags: `['prologue']`
  - use_objects: `['imm_occurrence:0x157e:operand_imm:1:0x20:i64', 'reg:rsp']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0x157e:operand_imm:1:0x20:i64']`
- PC `0x1582`: `mov eax, dword ptr [rip + 0x20fbfc]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - use_objects: `['reg:rip', 'var:uops_available']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0x1582:mem_disp:1:0x20fbfc:i64', 'imm_occurrence:0x1582:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0x1582:mem_disp:1:0x20fbfc:i64', 'imm_occurrence:0x1582:mem_scale:1:0x1:i64']`
- PC `0x1588`: `test eax, eax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0x158a`: `je 0x168e` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - instruction_semantic_tags: `['conditional_branch']`
  - use_objects: `['imm_occurrence:0x158a:operand_imm:0:0x168e:i64', 'reg:zf']`
  - def_objects: `['reg:rip']`
  - immediates: `['imm_occurrence:0x158a:operand_imm:0:0x168e:i64']`
- PC `0x168e`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x168f`: `leave` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - instruction_semantic_tags: `['epilogue']`
  - use_objects: `['reg:rbp', 'reg:rsp', 'stack:[rbp-0x20]']`
  - def_objects: `['reg:rbp', 'reg:rip', 'reg:rsp']`
- PC `0x1690`: `ret` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - use_objects: `['reg:rsp', 'stack:[rbp-0x18]']`
  - def_objects: `['reg:rip', 'reg:rsp']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xb91`: `mov eax, eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xb93`: `cmp qword ptr [rbp - 8], rax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1590`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1596`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1686`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x168c`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xb91`      b91:	89 c0                	mov    %eax,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb93`      b93:	48 39 45 f8          	cmp    %rax,-0x8(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb97`      b97:	73 34                	jae    bcd <STAGE1_END> groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
- `0xb99`      b99:	48 8d 15 a0 24 20 00 	lea    0x2024a0(%rip),%rdx        # 203040 <array1> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xba0`      ba0:	48 8b 45 f8          	mov    -0x8(%rbp),%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xba4`      ba4:	48 01 d0             	add    %rdx,%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xba7`      ba7:	0f b6 00             	movzbl (%rax),%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbaa`      baa:	0f b6 c0             	movzbl %al,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbad`      bad:	c1 e0 09             	shl    $0x9,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbb0`      bb0:	48 63 d0             	movslq %eax,%rdx groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbb3`      bb3:	48 8d 05 06 07 21 00 	lea    0x210706(%rip),%rax        # 2112c0 <array2> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbba`      bba:	0f b6 14 02          	movzbl (%rdx,%rax,1),%edx groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbbe`      bbe:	0f b6 05 44 25 20 00 	movzbl 0x202544(%rip),%eax        # 203109 <temp> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbc5`      bc5:	21 d0                	and    %edx,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbc7`      bc7:	88 05 3c 25 20 00    	mov    %al,0x20253c(%rip)        # 203109 <temp> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbcd`      bcd:	e8 a8 09 00 00       	callq  157a <pmu_uops_snap_after> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbd2`      bd2:	90                   	nop groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbd3`      bd3:	c9                   	leaveq  groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbd4`      bd4:	c3                   	retq    groups=`['structural_role']` kinds=`['branch_condition']`
- `0x157a`     157a:	55                   	push   %rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0x157b`     157b:	48 89 e5             	mov    %rsp,%rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0x157e`     157e:	48 83 ec 20          	sub    $0x20,%rsp groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1582`     1582:	8b 05 fc fb 20 00    	mov    0x20fbfc(%rip),%eax        # 211184 <uops_available> groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1588`     1588:	85 c0                	test   %eax,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0x158a`     158a:	0f 84 fe 00 00 00    	je     168e <pmu_uops_snap_after+0x114> groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1590`     1590:	8b 05 ca 3b 20 00    	mov    0x203bca(%rip),%eax        # 205160 <use_rdpmc> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1596`     1596:	85 c0                	test   %eax,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1686`     1686:	89 05 f4 fa 20 00    	mov    %eax,0x20faf4(%rip)        # 211180 <uops_cnt> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x168c`     168c:	eb 01                	jmp    168f <pmu_uops_snap_after+0x115> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x168e`     168e:	90                   	nop groups=`['structural_role']` kinds=`['branch_condition']`
- `0x168f`     168f:	c9                   	leaveq  groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1690`     1690:	c3                   	retq    groups=`['structural_role']` kinds=`['branch_condition']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function` pcs=`['0xb91', '0xb93', '0xb97']` groups=`['direct_operand', 'evidence_only']` kinds=`['direct_immediate_occurrence', 'direct_use', 'evidence_only']`

```c
   61: 
   62:   asm volatile(".globl STAGE1_BEGIN\nSTAGE1_BEGIN:");
   63:   if (x < array1_size) {
   64:     NOP_REGION_BEGIN
   65:     temp &= array2[array1[x] * 512];
```

- `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function` pcs=`['0xb99', '0xba0', '0xba4', '0xba7', '0xbaa', '0xbad', '0xbb0', '0xbb3', '0xbba', '0xbbe', '0xbc5', '0xbc7']` groups=`['structural_role']` kinds=`['branch_condition']`

```c
   63:   if (x < array1_size) {
   64:     NOP_REGION_BEGIN
   65:     temp &= array2[array1[x] * 512];
   66:     NOP_REGION_END
   67:   }
```

- `/root/src/spectre_stage1_2_auto.c:70` function=`spectre_function` pcs=`['0xbcd']` groups=`['structural_role']` kinds=`['branch_condition']`

```c
   68:   asm volatile(".globl STAGE1_END\nSTAGE1_END:");
   69: 
   70:   pmu_uops_snap_after();
   71: }
   72: 
```

- `/root/src/spectre_stage1_2_auto.c:71` function=`spectre_function` pcs=`['0xbd3', '0xbd4']` groups=`['structural_role']` kinds=`['branch_condition']`

```c
   69: 
   70:   pmu_uops_snap_after();
   71: }
   72: 
   73: /********************************************************************
```

### 30. `imm_occurrence:0xba0:mem_disp:1:0xfffffffffffffff8:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xba0:mem_disp:1:0xfffffffffffffff8/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xba0', 'operand_index': None, 'raw_suffix': 'mem_disp:1:0xfffffffffffffff8/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xba0:mem_disp:1:0xfffffffffffffff8/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xba0']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xba0']`
- direct_operand_pcs: `['0xba0']`
- structural_role_pcs: `['0xba0']`
- anchor_pcs: `['0xba0']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xb99', '0xba4', '0xba7']`
- all_mapped_pcs: `['0xb99', '0xba0', '0xba4', '0xba7']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x8]']`

#### PC Relation Entries

- `0xb99` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xba0` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xba4` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xba7` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xba0`: `mov rax, qword ptr [rbp - 8]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x8]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xba0:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xba0:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xba0:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xba0:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xb99`: `lea rdx, [rip + 0x2024a0]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xba4`: `add rax, rdx` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xba7`: `movzx eax, byte ptr [rax]` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xb99`      b99:	48 8d 15 a0 24 20 00 	lea    0x2024a0(%rip),%rdx        # 203040 <array1> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xba0`      ba0:	48 8b 45 f8          	mov    -0x8(%rbp),%rax groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xba4`      ba4:	48 01 d0             	add    %rdx,%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xba7`      ba7:	0f b6 00             	movzbl (%rax),%eax groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function` pcs=`['0xb99', '0xba0', '0xba4', '0xba7']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
   63:   if (x < array1_size) {
   64:     NOP_REGION_BEGIN
   65:     temp &= array2[array1[x] * 512];
   66:     NOP_REGION_END
   67:   }
```

### 31. `imm_occurrence:0xba0:mem_scale:1:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xba0:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xba0', 'operand_index': None, 'raw_suffix': 'mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xba0:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xba0']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xba0']`
- direct_operand_pcs: `['0xba0']`
- structural_role_pcs: `['0xba0']`
- anchor_pcs: `['0xba0']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xb99', '0xba4', '0xba7']`
- all_mapped_pcs: `['0xb99', '0xba0', '0xba4', '0xba7']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x8]']`

#### PC Relation Entries

- `0xb99` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xba0` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xba4` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xba7` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xba0`: `mov rax, qword ptr [rbp - 8]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x8]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xba0:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xba0:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xba0:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xba0:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xb99`: `lea rdx, [rip + 0x2024a0]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xba4`: `add rax, rdx` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xba7`: `movzx eax, byte ptr [rax]` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xb99`      b99:	48 8d 15 a0 24 20 00 	lea    0x2024a0(%rip),%rdx        # 203040 <array1> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xba0`      ba0:	48 8b 45 f8          	mov    -0x8(%rbp),%rax groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xba4`      ba4:	48 01 d0             	add    %rdx,%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xba7`      ba7:	0f b6 00             	movzbl (%rax),%eax groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function` pcs=`['0xb99', '0xba0', '0xba4', '0xba7']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
   63:   if (x < array1_size) {
   64:     NOP_REGION_BEGIN
   65:     temp &= array2[array1[x] * 512];
   66:     NOP_REGION_END
   67:   }
```

### 32. `imm_occurrence:0xba7:mem_disp:1:0x0:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xba7:mem_disp:1:0x0/i64 [structural_abi_constant]`
- Mapping kind: `constant_or_address_component`
- Confidence: `structural`
- Object semantic tags: `['structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xba7', 'operand_index': None, 'raw_suffix': 'mem_disp:1:0x0/i64 [structural_abi_constant]'}`
- Reason: 对象类型为 imm，更适合作为常量、位移、scale、比较值或地址组成部分解释。
- Candidate program elements: `['imm@0xba7:mem_disp:1:0x0/i64 [structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xba7']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xba7']`
- direct_operand_pcs: `['0xba7']`
- structural_role_pcs: `['0xba7']`
- anchor_pcs: `['0xba7']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xba0', '0xba4', '0xbaa', '0xbad']`
- all_mapped_pcs: `['0xba0', '0xba4', '0xba7', '0xbaa', '0xbad']`
- direct_parents: `[]`
- direct_children: `['var:array1']`

#### PC Relation Entries

- `0xba0` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xba4` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xba7` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xbaa` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbad` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xba7`: `movzx eax, byte ptr [rax]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'var:array1']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xba7:mem_disp:1:0x0:i64', 'imm_occurrence:0xba7:mem_scale:1:0x1:i64', 'reg:rax', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xba7:mem_disp:1:0x0:i64', 'imm_occurrence:0xba7:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xba0`: `mov rax, qword ptr [rbp - 8]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xba4`: `add rax, rdx` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbaa`: `movzx eax, al` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbad`: `shl eax, 9` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xba0`      ba0:	48 8b 45 f8          	mov    -0x8(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xba4`      ba4:	48 01 d0             	add    %rdx,%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xba7`      ba7:	0f b6 00             	movzbl (%rax),%eax groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xbaa`      baa:	0f b6 c0             	movzbl %al,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbad`      bad:	c1 e0 09             	shl    $0x9,%eax groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function` pcs=`['0xba0', '0xba4', '0xba7', '0xbaa', '0xbad']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
   63:   if (x < array1_size) {
   64:     NOP_REGION_BEGIN
   65:     temp &= array2[array1[x] * 512];
   66:     NOP_REGION_END
   67:   }
```

### 33. `imm_occurrence:0xba7:mem_scale:1:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xba7:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xba7', 'operand_index': None, 'raw_suffix': 'mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xba7:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xba7']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xba7']`
- direct_operand_pcs: `['0xba7']`
- structural_role_pcs: `['0xba7']`
- anchor_pcs: `['0xba7']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xba0', '0xba4', '0xbaa', '0xbad']`
- all_mapped_pcs: `['0xba0', '0xba4', '0xba7', '0xbaa', '0xbad']`
- direct_parents: `[]`
- direct_children: `['var:array1']`

#### PC Relation Entries

- `0xba0` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xba4` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xba7` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xbaa` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbad` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xba7`: `movzx eax, byte ptr [rax]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'var:array1']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xba7:mem_disp:1:0x0:i64', 'imm_occurrence:0xba7:mem_scale:1:0x1:i64', 'reg:rax', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xba7:mem_disp:1:0x0:i64', 'imm_occurrence:0xba7:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xba0`: `mov rax, qword ptr [rbp - 8]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xba4`: `add rax, rdx` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbaa`: `movzx eax, al` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbad`: `shl eax, 9` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xba0`      ba0:	48 8b 45 f8          	mov    -0x8(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xba4`      ba4:	48 01 d0             	add    %rdx,%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xba7`      ba7:	0f b6 00             	movzbl (%rax),%eax groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xbaa`      baa:	0f b6 c0             	movzbl %al,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbad`      bad:	c1 e0 09             	shl    $0x9,%eax groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function` pcs=`['0xba0', '0xba4', '0xba7', '0xbaa', '0xbad']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
   63:   if (x < array1_size) {
   64:     NOP_REGION_BEGIN
   65:     temp &= array2[array1[x] * 512];
   66:     NOP_REGION_END
   67:   }
```

### 34. `imm_occurrence:0xbad:operand_imm:1:0x9:i8`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xbad:operand_imm:1:0x9/i8`
- Mapping kind: `constant_or_address_component`
- Confidence: `structural`
- Object semantic tags: `[]`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xbad', 'operand_index': None, 'raw_suffix': 'operand_imm:1:0x9/i8'}`
- Reason: 对象类型为 imm，更适合作为常量、位移、scale、比较值或地址组成部分解释。
- Candidate program elements: `['imm@0xbad:operand_imm:1:0x9/i8']`
- direct_use_pcs: `['0xbad']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xbad']`
- direct_operand_pcs: `['0xbad']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xbad']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xba7', '0xbaa', '0xbb0', '0xbb3']`
- all_mapped_pcs: `['0xba7', '0xbaa', '0xbad', '0xbb0', '0xbb3']`
- direct_parents: `[]`
- direct_children: `['reg:cf', 'reg:of', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`

#### PC Relation Entries

- `0xba7` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbaa` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbad` kinds=`['direct_immediate_occurrence', 'direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.used_by/instruction_details.use_objects']`
- `0xbb0` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbb3` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xbad`: `shl eax, 9` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['imm_occurrence:0xbad:operand_imm:1:0x9:i8', 'reg:rax']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xbad:operand_imm:1:0x9:i8']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xba7`: `movzx eax, byte ptr [rax]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbaa`: `movzx eax, al` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbb0`: `movsxd rdx, eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbb3`: `lea rax, [rip + 0x210706]` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xba7`      ba7:	0f b6 00             	movzbl (%rax),%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbaa`      baa:	0f b6 c0             	movzbl %al,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbad`      bad:	c1 e0 09             	shl    $0x9,%eax groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
- `0xbb0`      bb0:	48 63 d0             	movslq %eax,%rdx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbb3`      bb3:	48 8d 05 06 07 21 00 	lea    0x210706(%rip),%rax        # 2112c0 <array2> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function` pcs=`['0xba7', '0xbaa', '0xbad', '0xbb0', '0xbb3']` groups=`['direct_operand', 'evidence_only']` kinds=`['direct_immediate_occurrence', 'direct_use', 'evidence_only']`

```c
   63:   if (x < array1_size) {
   64:     NOP_REGION_BEGIN
   65:     temp &= array2[array1[x] * 512];
   66:     NOP_REGION_END
   67:   }
```

### 35. `imm_occurrence:0xbba:mem_disp:1:0x0:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xbba:mem_disp:1:0x0/i64 [structural_abi_constant]`
- Mapping kind: `constant_or_address_component`
- Confidence: `structural`
- Object semantic tags: `['structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xbba', 'operand_index': None, 'raw_suffix': 'mem_disp:1:0x0/i64 [structural_abi_constant]'}`
- Reason: 对象类型为 imm，更适合作为常量、位移、scale、比较值或地址组成部分解释。
- Candidate program elements: `['imm@0xbba:mem_disp:1:0x0/i64 [structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xbba']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xbba']`
- direct_operand_pcs: `['0xbba']`
- structural_role_pcs: `['0xbba']`
- anchor_pcs: `['0xbba']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xbb0', '0xbb3', '0xbbe', '0xbc5']`
- all_mapped_pcs: `['0xbb0', '0xbb3', '0xbba', '0xbbe', '0xbc5']`
- direct_parents: `[]`
- direct_children: `['var:array2']`

#### PC Relation Entries

- `0xbb0` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbb3` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbba` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xbbe` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbc5` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xbba`: `movzx edx, byte ptr [rdx + rax]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rdx', 'var:array2']`
  - def_objects: `['reg:rdx', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xbba:mem_disp:1:0x0:i64', 'imm_occurrence:0xbba:mem_scale:1:0x1:i64', 'reg:rax', 'reg:rdx', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xbba:mem_disp:1:0x0:i64', 'imm_occurrence:0xbba:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xbb0`: `movsxd rdx, eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbb3`: `lea rax, [rip + 0x210706]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbbe`: `movzx eax, byte ptr [rip + 0x202544]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbc5`: `and eax, edx` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xbb0`      bb0:	48 63 d0             	movslq %eax,%rdx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbb3`      bb3:	48 8d 05 06 07 21 00 	lea    0x210706(%rip),%rax        # 2112c0 <array2> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbba`      bba:	0f b6 14 02          	movzbl (%rdx,%rax,1),%edx groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xbbe`      bbe:	0f b6 05 44 25 20 00 	movzbl 0x202544(%rip),%eax        # 203109 <temp> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbc5`      bc5:	21 d0                	and    %edx,%eax groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function` pcs=`['0xbb0', '0xbb3', '0xbba', '0xbbe', '0xbc5']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
   63:   if (x < array1_size) {
   64:     NOP_REGION_BEGIN
   65:     temp &= array2[array1[x] * 512];
   66:     NOP_REGION_END
   67:   }
```

### 36. `imm_occurrence:0xbba:mem_scale:1:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xbba:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xbba', 'operand_index': None, 'raw_suffix': 'mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xbba:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xbba']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xbba']`
- direct_operand_pcs: `['0xbba']`
- structural_role_pcs: `['0xbba']`
- anchor_pcs: `['0xbba']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xbb0', '0xbb3', '0xbbe', '0xbc5']`
- all_mapped_pcs: `['0xbb0', '0xbb3', '0xbba', '0xbbe', '0xbc5']`
- direct_parents: `[]`
- direct_children: `['var:array2']`

#### PC Relation Entries

- `0xbb0` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbb3` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbba` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xbbe` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbc5` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xbba`: `movzx edx, byte ptr [rdx + rax]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rdx', 'var:array2']`
  - def_objects: `['reg:rdx', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xbba:mem_disp:1:0x0:i64', 'imm_occurrence:0xbba:mem_scale:1:0x1:i64', 'reg:rax', 'reg:rdx', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xbba:mem_disp:1:0x0:i64', 'imm_occurrence:0xbba:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xbb0`: `movsxd rdx, eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbb3`: `lea rax, [rip + 0x210706]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbbe`: `movzx eax, byte ptr [rip + 0x202544]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbc5`: `and eax, edx` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xbb0`      bb0:	48 63 d0             	movslq %eax,%rdx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbb3`      bb3:	48 8d 05 06 07 21 00 	lea    0x210706(%rip),%rax        # 2112c0 <array2> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbba`      bba:	0f b6 14 02          	movzbl (%rdx,%rax,1),%edx groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xbbe`      bbe:	0f b6 05 44 25 20 00 	movzbl 0x202544(%rip),%eax        # 203109 <temp> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbc5`      bc5:	21 d0                	and    %edx,%eax groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function` pcs=`['0xbb0', '0xbb3', '0xbba', '0xbbe', '0xbc5']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
   63:   if (x < array1_size) {
   64:     NOP_REGION_BEGIN
   65:     temp &= array2[array1[x] * 512];
   66:     NOP_REGION_END
   67:   }
```

### 37. `imm_occurrence:0xbbe:mem_disp:1:0x202544:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xbbe:mem_disp:1:0x202544/i64 [rip_relative_displacement|structural_abi_constant]`
- Mapping kind: `rip_relative_displacement`
- Confidence: `semantic`
- Object semantic tags: `['rip_relative_displacement', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xbbe', 'operand_index': None, 'raw_suffix': 'mem_disp:1:0x202544/i64 [rip_relative_displacement|structural_abi_constant]'}`
- Reason: 该 immediate 带有 rip_relative_displacement 标签，更适合作为 RIP 相对寻址位移解释。
- Candidate program elements: `['imm@0xbbe:mem_disp:1:0x202544/i64 [rip_relative_displacement|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xbbe']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xbbe']`
- direct_operand_pcs: `['0xbbe']`
- structural_role_pcs: `['0xbbe']`
- anchor_pcs: `['0xbbe']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xbb3', '0xbba', '0xbc5', '0xbc7']`
- all_mapped_pcs: `['0xbb3', '0xbba', '0xbbe', '0xbc5', '0xbc7']`
- direct_parents: `[]`
- direct_children: `['var:temp']`

#### PC Relation Entries

- `0xbb3` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbba` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbbe` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xbc5` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbc7` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xbbe`: `movzx eax, byte ptr [rip + 0x202544]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rip', 'var:temp']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xbbe:mem_disp:1:0x202544:i64', 'imm_occurrence:0xbbe:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xbbe:mem_disp:1:0x202544:i64', 'imm_occurrence:0xbbe:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xbb3`: `lea rax, [rip + 0x210706]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbba`: `movzx edx, byte ptr [rdx + rax]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbc5`: `and eax, edx` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbc7`: `mov byte ptr [rip + 0x20253c], al` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xbb3`      bb3:	48 8d 05 06 07 21 00 	lea    0x210706(%rip),%rax        # 2112c0 <array2> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbba`      bba:	0f b6 14 02          	movzbl (%rdx,%rax,1),%edx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbbe`      bbe:	0f b6 05 44 25 20 00 	movzbl 0x202544(%rip),%eax        # 203109 <temp> groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xbc5`      bc5:	21 d0                	and    %edx,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbc7`      bc7:	88 05 3c 25 20 00    	mov    %al,0x20253c(%rip)        # 203109 <temp> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function` pcs=`['0xbb3', '0xbba', '0xbbe', '0xbc5', '0xbc7']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
   63:   if (x < array1_size) {
   64:     NOP_REGION_BEGIN
   65:     temp &= array2[array1[x] * 512];
   66:     NOP_REGION_END
   67:   }
```

### 38. `imm_occurrence:0xbbe:mem_scale:1:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xbbe:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xbbe', 'operand_index': None, 'raw_suffix': 'mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xbbe:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xbbe']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xbbe']`
- direct_operand_pcs: `['0xbbe']`
- structural_role_pcs: `['0xbbe']`
- anchor_pcs: `['0xbbe']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xbb3', '0xbba', '0xbc5', '0xbc7']`
- all_mapped_pcs: `['0xbb3', '0xbba', '0xbbe', '0xbc5', '0xbc7']`
- direct_parents: `[]`
- direct_children: `['var:temp']`

#### PC Relation Entries

- `0xbb3` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbba` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbbe` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xbc5` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbc7` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xbbe`: `movzx eax, byte ptr [rip + 0x202544]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rip', 'var:temp']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xbbe:mem_disp:1:0x202544:i64', 'imm_occurrence:0xbbe:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xbbe:mem_disp:1:0x202544:i64', 'imm_occurrence:0xbbe:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xbb3`: `lea rax, [rip + 0x210706]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbba`: `movzx edx, byte ptr [rdx + rax]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbc5`: `and eax, edx` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbc7`: `mov byte ptr [rip + 0x20253c], al` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xbb3`      bb3:	48 8d 05 06 07 21 00 	lea    0x210706(%rip),%rax        # 2112c0 <array2> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbba`      bba:	0f b6 14 02          	movzbl (%rdx,%rax,1),%edx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbbe`      bbe:	0f b6 05 44 25 20 00 	movzbl 0x202544(%rip),%eax        # 203109 <temp> groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xbc5`      bc5:	21 d0                	and    %edx,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbc7`      bc7:	88 05 3c 25 20 00    	mov    %al,0x20253c(%rip)        # 203109 <temp> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function` pcs=`['0xbb3', '0xbba', '0xbbe', '0xbc5', '0xbc7']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
   63:   if (x < array1_size) {
   64:     NOP_REGION_BEGIN
   65:     temp &= array2[array1[x] * 512];
   66:     NOP_REGION_END
   67:   }
```

### 39. `imm_occurrence:0xbc7:mem_disp:0:0x20253c:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xbc7:mem_disp:0:0x20253c/i64 [rip_relative_displacement|structural_abi_constant]`
- Mapping kind: `rip_relative_displacement`
- Confidence: `semantic`
- Object semantic tags: `['rip_relative_displacement', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xbc7', 'operand_index': None, 'raw_suffix': 'mem_disp:0:0x20253c/i64 [rip_relative_displacement|structural_abi_constant]'}`
- Reason: 该 immediate 带有 rip_relative_displacement 标签，更适合作为 RIP 相对寻址位移解释。
- Candidate program elements: `['imm@0xbc7:mem_disp:0:0x20253c/i64 [rip_relative_displacement|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xbc7']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xbc7']`
- direct_operand_pcs: `['0xbc7']`
- structural_role_pcs: `['0xbc7']`
- anchor_pcs: `['0xbc7']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xbbe', '0xbc5']`
- all_mapped_pcs: `['0xbbe', '0xbc5', '0xbc7']`
- direct_parents: `[]`
- direct_children: `['var:temp']`

#### PC Relation Entries

- `0xbbe` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbc5` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbc7` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`

#### Direct Anchor Instruction Evidence

- PC `0xbc7`: `mov byte ptr [rip + 0x20253c], al` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rip']`
  - def_objects: `['reg:rip', 'var:temp']`
  - addr_objects: `['imm_occurrence:0xbc7:mem_disp:0:0x20253c:i64', 'imm_occurrence:0xbc7:mem_scale:0:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xbc7:mem_disp:0:0x20253c:i64', 'imm_occurrence:0xbc7:mem_scale:0:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xbbe`: `movzx eax, byte ptr [rip + 0x202544]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbc5`: `and eax, edx` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xbbe`      bbe:	0f b6 05 44 25 20 00 	movzbl 0x202544(%rip),%eax        # 203109 <temp> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbc5`      bc5:	21 d0                	and    %edx,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbc7`      bc7:	88 05 3c 25 20 00    	mov    %al,0x20253c(%rip)        # 203109 <temp> groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function` pcs=`['0xbbe', '0xbc5', '0xbc7']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
   63:   if (x < array1_size) {
   64:     NOP_REGION_BEGIN
   65:     temp &= array2[array1[x] * 512];
   66:     NOP_REGION_END
   67:   }
```

### 40. `imm_occurrence:0xbc7:mem_scale:0:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xbc7:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xbc7', 'operand_index': None, 'raw_suffix': 'mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xbc7:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xbc7']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xbc7']`
- direct_operand_pcs: `['0xbc7']`
- structural_role_pcs: `['0xbc7']`
- anchor_pcs: `['0xbc7']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xbbe', '0xbc5']`
- all_mapped_pcs: `['0xbbe', '0xbc5', '0xbc7']`
- direct_parents: `[]`
- direct_children: `['var:temp']`

#### PC Relation Entries

- `0xbbe` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbc5` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbc7` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`

#### Direct Anchor Instruction Evidence

- PC `0xbc7`: `mov byte ptr [rip + 0x20253c], al` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rip']`
  - def_objects: `['reg:rip', 'var:temp']`
  - addr_objects: `['imm_occurrence:0xbc7:mem_disp:0:0x20253c:i64', 'imm_occurrence:0xbc7:mem_scale:0:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xbc7:mem_disp:0:0x20253c:i64', 'imm_occurrence:0xbc7:mem_scale:0:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xbbe`: `movzx eax, byte ptr [rip + 0x202544]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbc5`: `and eax, edx` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xbbe`      bbe:	0f b6 05 44 25 20 00 	movzbl 0x202544(%rip),%eax        # 203109 <temp> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbc5`      bc5:	21 d0                	and    %edx,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbc7`      bc7:	88 05 3c 25 20 00    	mov    %al,0x20253c(%rip)        # 203109 <temp> groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function` pcs=`['0xbbe', '0xbc5', '0xbc7']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
   63:   if (x < array1_size) {
   64:     NOP_REGION_BEGIN
   65:     temp &= array2[array1[x] * 512];
   66:     NOP_REGION_END
   67:   }
```

### 41. `imm_occurrence:0xbcd:operand_imm:0:0x157a:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xbcd:operand_imm:0:0x157a/i64 [call_target_constant|program_semantic_constant|store_constant]`
- Mapping kind: `store_constant`
- Confidence: `semantic`
- Object semantic tags: `['call_target_constant', 'program_semantic_constant', 'store_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xbcd', 'operand_index': None, 'raw_suffix': 'operand_imm:0:0x157a/i64 [call_target_constant|program_semantic_constant|store_constant]'}`
- Reason: 该 immediate 带有 store_constant 标签，更适合作为写入值常量解释。
- Candidate program elements: `['imm@0xbcd:operand_imm:0:0x157a/i64 [call_target_constant|program_semantic_constant|store_constant]']`
- direct_use_pcs: `['0xbcd']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xbcd']`
- direct_operand_pcs: `['0xbcd']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xbcd']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xbd2']`
- all_mapped_pcs: `['0xbcd', '0xbd2']`
- direct_parents: `[]`
- direct_children: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x18]']`

#### PC Relation Entries

- `0xbcd` kinds=`['direct_immediate_occurrence', 'direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.used_by/instruction_details.use_objects']`
- `0xbd2` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xbcd`: `call 0x157a` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
  - Source: `/root/src/spectre_stage1_2_auto.c:70` function=`spectre_function`
  - call_target: `{'operand': '0x157a', 'resolved_symbol': 'pmu_uops_snap_after', 'call_kind': 'direct_call_symbol', 'display_target': 'pmu_uops_snap_after'}`
  - use_objects: `['imm_occurrence:0xbcd:operand_imm:0:0x157a:i64', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x18]']`
  - immediates: `['imm_occurrence:0xbcd:operand_imm:0:0x157a:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xbd2`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xbcd`      bcd:	e8 a8 09 00 00       	callq  157a <pmu_uops_snap_after> groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
- `0xbd2`      bd2:	90                   	nop groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:70` function=`spectre_function` pcs=`['0xbcd']` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`

```c
   68:   asm volatile(".globl STAGE1_END\nSTAGE1_END:");
   69: 
   70:   pmu_uops_snap_after();
   71: }
   72: 
```

### 42. `imm_occurrence:0xbf9:operand_imm:1:0x30:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xbf9:operand_imm:1:0x30/i64 [stack_alignment_constant|structural_abi_constant]`
- Mapping kind: `stack_alignment_constant`
- Confidence: `semantic`
- Object semantic tags: `['stack_alignment_constant', 'structural_abi_constant']`
- Anchor instruction tags: `['prologue']`
- Scaffolding tags: `['prologue']`
- Occurrence: `{'occurrence_pc': '0xbf9', 'operand_index': None, 'raw_suffix': 'operand_imm:1:0x30/i64 [stack_alignment_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 stack_alignment_constant 标签，更适合作为栈对齐常量解释。 检测到 ABI/脚手架标签：prologue，应更偏向解释为结构性对象，而非优先可变异语义对象。
- Candidate program elements: `['imm@0xbf9:operand_imm:1:0x30/i64 [stack_alignment_constant|structural_abi_constant]']`
- direct_use_pcs: `['0xbf9']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xbf9']`
- direct_operand_pcs: `['0xbf9']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xbf9']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xbf5', '0xbf6', '0xbfd']`
- all_mapped_pcs: `['0xbf5', '0xbf6', '0xbf9', '0xbfd']`
- direct_parents: `[]`
- direct_children: `['reg:cf', 'reg:of', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf']`

#### PC Relation Entries

- `0xbf5` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbf6` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbf9` kinds=`['direct_immediate_occurrence', 'direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.used_by/instruction_details.use_objects']`
- `0xbfd` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xbf9`: `sub rsp, 0x30` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
  - Source: `/root/src/spectre_stage1_2_auto.c:88` function=`stage1_mistrain_trigger`
  - instruction_semantic_tags: `['prologue']`
  - use_objects: `['imm_occurrence:0xbf9:operand_imm:1:0x30:i64', 'reg:rsp']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xbf9:operand_imm:1:0x30:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xbf5`: `push rbp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbf6`: `mov rbp, rsp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbfd`: `mov qword ptr [rbp - 0x28], rdi` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xbf5`      bf5:	55                   	push   %rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbf6`      bf6:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbf9`      bf9:	48 83 ec 30          	sub    $0x30,%rsp groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
- `0xbfd`      bfd:	48 89 7d d8          	mov    %rdi,-0x28(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:88` function=`stage1_mistrain_trigger` pcs=`['0xbf5', '0xbf6', '0xbf9', '0xbfd']` groups=`['direct_operand', 'evidence_only']` kinds=`['direct_immediate_occurrence', 'direct_use', 'evidence_only']`

```c
   86: ********************************************************************/
   87: __attribute__((noinline))
   88: void stage1_mistrain_trigger(size_t malicious_x) {
   89:     int j;
   90:     size_t training_x, x;
```

### 43. `imm_occurrence:0xbfd:mem_disp:0:0xffffffffffffffd8:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xbfd:mem_disp:0:0xffffffffffffffd8/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `['argument_shuffle']`
- Scaffolding tags: `['argument_shuffle']`
- Occurrence: `{'occurrence_pc': '0xbfd', 'operand_index': None, 'raw_suffix': 'mem_disp:0:0xffffffffffffffd8/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。 检测到 ABI/脚手架标签：argument_shuffle，应更偏向解释为结构性对象，而非优先可变异语义对象。
- Candidate program elements: `['imm@0xbfd:mem_disp:0:0xffffffffffffffd8/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xbfd']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xbfd']`
- direct_operand_pcs: `['0xbfd']`
- structural_role_pcs: `['0xbfd']`
- anchor_pcs: `['0xbfd']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xbf6', '0xbf9']`
- all_mapped_pcs: `['0xbf6', '0xbf9', '0xbfd']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x28]']`

#### PC Relation Entries

- `0xbf6` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbf9` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbfd` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`

#### Direct Anchor Instruction Evidence

- PC `0xbfd`: `mov qword ptr [rbp - 0x28], rdi` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:88` function=`stage1_mistrain_trigger`
  - instruction_semantic_tags: `['argument_shuffle']`
  - use_objects: `['reg:rbp', 'reg:rdi']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x28]']`
  - addr_objects: `['imm_occurrence:0xbfd:mem_disp:0:0xffffffffffffffd8:i64', 'imm_occurrence:0xbfd:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xbfd:mem_disp:0:0xffffffffffffffd8:i64', 'imm_occurrence:0xbfd:mem_scale:0:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xbf6`: `mov rbp, rsp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbf9`: `sub rsp, 0x30` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xbf6`      bf6:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbf9`      bf9:	48 83 ec 30          	sub    $0x30,%rsp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbfd`      bfd:	48 89 7d d8          	mov    %rdi,-0x28(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:88` function=`stage1_mistrain_trigger` pcs=`['0xbf6', '0xbf9', '0xbfd']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
   86: ********************************************************************/
   87: __attribute__((noinline))
   88: void stage1_mistrain_trigger(size_t malicious_x) {
   89:     int j;
   90:     size_t training_x, x;
```

### 44. `imm_occurrence:0xbfd:mem_scale:0:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xbfd:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `['argument_shuffle']`
- Scaffolding tags: `['argument_shuffle']`
- Occurrence: `{'occurrence_pc': '0xbfd', 'operand_index': None, 'raw_suffix': 'mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。 检测到 ABI/脚手架标签：argument_shuffle，应更偏向解释为结构性对象，而非优先可变异语义对象。
- Candidate program elements: `['imm@0xbfd:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xbfd']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xbfd']`
- direct_operand_pcs: `['0xbfd']`
- structural_role_pcs: `['0xbfd']`
- anchor_pcs: `['0xbfd']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xbf6', '0xbf9']`
- all_mapped_pcs: `['0xbf6', '0xbf9', '0xbfd']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x28]']`

#### PC Relation Entries

- `0xbf6` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbf9` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbfd` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`

#### Direct Anchor Instruction Evidence

- PC `0xbfd`: `mov qword ptr [rbp - 0x28], rdi` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:88` function=`stage1_mistrain_trigger`
  - instruction_semantic_tags: `['argument_shuffle']`
  - use_objects: `['reg:rbp', 'reg:rdi']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x28]']`
  - addr_objects: `['imm_occurrence:0xbfd:mem_disp:0:0xffffffffffffffd8:i64', 'imm_occurrence:0xbfd:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xbfd:mem_disp:0:0xffffffffffffffd8:i64', 'imm_occurrence:0xbfd:mem_scale:0:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xbf6`: `mov rbp, rsp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbf9`: `sub rsp, 0x30` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xbf6`      bf6:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbf9`      bf9:	48 83 ec 30          	sub    $0x30,%rsp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbfd`      bfd:	48 89 7d d8          	mov    %rdi,-0x28(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:88` function=`stage1_mistrain_trigger` pcs=`['0xbf6', '0xbf9', '0xbfd']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
   86: ********************************************************************/
   87: __attribute__((noinline))
   88: void stage1_mistrain_trigger(size_t malicious_x) {
   89:     int j;
   90:     size_t training_x, x;
```

### 45. `imm_occurrence:0xc01:mem_disp:0:0xffffffffffffffe4:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc01:mem_disp:0:0xffffffffffffffe4/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc01', 'operand_index': None, 'raw_suffix': 'mem_disp:0:0xffffffffffffffe4/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xc01:mem_disp:0:0xffffffffffffffe4/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc01']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc01']`
- direct_operand_pcs: `['0xc01']`
- structural_role_pcs: `['0xc01']`
- anchor_pcs: `['0xc01']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc08']`
- all_mapped_pcs: `['0xc01', '0xc08']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x1c]']`

#### PC Relation Entries

- `0xc01` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc08` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc01`: `mov dword ptr [rbp - 0x1c], 0x1d` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:92` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc01:operand_imm:1:0x1d:i32', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x1c]']`
  - addr_objects: `['imm_occurrence:0xc01:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xc01:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc01:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xc01:mem_scale:0:0x1:i64', 'imm_occurrence:0xc01:operand_imm:1:0x1d:i32']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc08`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc01`      c01:	c7 45 e4 1d 00 00 00 	movl   $0x1d,-0x1c(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc08`      c08:	e9 9e 00 00 00       	jmpq   cab <stage1_mistrain_trigger+0xb6> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:92` function=`stage1_mistrain_trigger` pcs=`['0xc01']` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`

```c
   90:     size_t training_x, x;
   91: 
   92:     for (j = 29; j >= 0; j--) {
   93:         training_x = (size_t)(j % 16);
   94:         _mm_clflush(&array1_size);
```

### 46. `imm_occurrence:0xc01:mem_scale:0:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc01:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc01', 'operand_index': None, 'raw_suffix': 'mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xc01:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc01']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc01']`
- direct_operand_pcs: `['0xc01']`
- structural_role_pcs: `['0xc01']`
- anchor_pcs: `['0xc01']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc08']`
- all_mapped_pcs: `['0xc01', '0xc08']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x1c]']`

#### PC Relation Entries

- `0xc01` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc08` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc01`: `mov dword ptr [rbp - 0x1c], 0x1d` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:92` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc01:operand_imm:1:0x1d:i32', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x1c]']`
  - addr_objects: `['imm_occurrence:0xc01:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xc01:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc01:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xc01:mem_scale:0:0x1:i64', 'imm_occurrence:0xc01:operand_imm:1:0x1d:i32']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc08`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc01`      c01:	c7 45 e4 1d 00 00 00 	movl   $0x1d,-0x1c(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc08`      c08:	e9 9e 00 00 00       	jmpq   cab <stage1_mistrain_trigger+0xb6> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:92` function=`stage1_mistrain_trigger` pcs=`['0xc01']` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`

```c
   90:     size_t training_x, x;
   91: 
   92:     for (j = 29; j >= 0; j--) {
   93:         training_x = (size_t)(j % 16);
   94:         _mm_clflush(&array1_size);
```

### 47. `imm_occurrence:0xc01:operand_imm:1:0x1d:i32`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc01:operand_imm:1:0x1d/i32 [program_semantic_constant|store_constant]`
- Mapping kind: `store_constant`
- Confidence: `semantic`
- Object semantic tags: `['program_semantic_constant', 'store_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc01', 'operand_index': None, 'raw_suffix': 'operand_imm:1:0x1d/i32 [program_semantic_constant|store_constant]'}`
- Reason: 该 immediate 带有 store_constant 标签，更适合作为写入值常量解释。
- Candidate program elements: `['imm@0xc01:operand_imm:1:0x1d/i32 [program_semantic_constant|store_constant]']`
- direct_use_pcs: `['0xc01']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc01']`
- direct_operand_pcs: `['0xc01']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xc01']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc08']`
- all_mapped_pcs: `['0xc01', '0xc08']`
- direct_parents: `[]`
- direct_children: `['reg:rip', 'stack:[rbp-0x1c]']`

#### PC Relation Entries

- `0xc01` kinds=`['direct_immediate_occurrence', 'direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.used_by/instruction_details.use_objects']`
- `0xc08` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc01`: `mov dword ptr [rbp - 0x1c], 0x1d` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
  - Source: `/root/src/spectre_stage1_2_auto.c:92` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc01:operand_imm:1:0x1d:i32', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x1c]']`
  - addr_objects: `['imm_occurrence:0xc01:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xc01:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc01:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xc01:mem_scale:0:0x1:i64', 'imm_occurrence:0xc01:operand_imm:1:0x1d:i32']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc08`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc01`      c01:	c7 45 e4 1d 00 00 00 	movl   $0x1d,-0x1c(%rbp) groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
- `0xc08`      c08:	e9 9e 00 00 00       	jmpq   cab <stage1_mistrain_trigger+0xb6> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:92` function=`stage1_mistrain_trigger` pcs=`['0xc01']` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`

```c
   90:     size_t training_x, x;
   91: 
   92:     for (j = 29; j >= 0; j--) {
   93:         training_x = (size_t)(j % 16);
   94:         _mm_clflush(&array1_size);
```

### 48. `imm_occurrence:0xc08:operand_imm:0:0xcab:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc08:operand_imm:0:0xcab/i64`
- Mapping kind: `constant_or_address_component`
- Confidence: `structural`
- Object semantic tags: `[]`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc08', 'operand_index': None, 'raw_suffix': 'operand_imm:0:0xcab/i64'}`
- Reason: 对象类型为 imm，更适合作为常量、位移、scale、比较值或地址组成部分解释。
- Candidate program elements: `['imm@0xc08:operand_imm:0:0xcab/i64']`
- direct_use_pcs: `['0xc08']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `['0xc08']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xc08']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc01', '0xc0d']`
- all_mapped_pcs: `['0xc01', '0xc08', '0xc0d']`
- direct_parents: `[]`
- direct_children: `['reg:rip']`

#### PC Relation Entries

- `0xc01` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc08` kinds=`['direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['object_detail.used_by/instruction_details.use_objects']`
- `0xc0d` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc08`: `None` groups=`['direct_operand']` kinds=`['direct_use']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc01`: `mov dword ptr [rbp - 0x1c], 0x1d` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc0d`: `mov eax, dword ptr [rbp - 0x1c]` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc01`      c01:	c7 45 e4 1d 00 00 00 	movl   $0x1d,-0x1c(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc08`      c08:	e9 9e 00 00 00       	jmpq   cab <stage1_mistrain_trigger+0xb6> groups=`['direct_operand']` kinds=`['direct_use']`
- `0xc0d`      c0d:	8b 45 e4             	mov    -0x1c(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:92` function=`stage1_mistrain_trigger` pcs=`['0xc01']` groups=`['evidence_only']` kinds=`['evidence_only']`

```c
   90:     size_t training_x, x;
   91: 
   92:     for (j = 29; j >= 0; j--) {
   93:         training_x = (size_t)(j % 16);
   94:         _mm_clflush(&array1_size);
```

- `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger` pcs=`['0xc0d']` groups=`['evidence_only']` kinds=`['evidence_only']`

```c
   91: 
   92:     for (j = 29; j >= 0; j--) {
   93:         training_x = (size_t)(j % 16);
   94:         _mm_clflush(&array1_size);
   95:         for (volatile int z = 0; z < 200; z++) {}
```

### 49. `imm_occurrence:0xc0d:mem_disp:1:0xffffffffffffffe4:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc0d:mem_disp:1:0xffffffffffffffe4/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc0d', 'operand_index': None, 'raw_suffix': 'mem_disp:1:0xffffffffffffffe4/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xc0d:mem_disp:1:0xffffffffffffffe4/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc0d']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc0d']`
- direct_operand_pcs: `['0xc0d']`
- structural_role_pcs: `['0xc0d']`
- anchor_pcs: `['0xc0d']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc08', '0xc10', '0xc11']`
- all_mapped_pcs: `['0xc08', '0xc0d', '0xc10', '0xc11']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x1c]']`

#### PC Relation Entries

- `0xc08` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc0d` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc10` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc11` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc0d`: `mov eax, dword ptr [rbp - 0x1c]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x1c]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc0d:mem_disp:1:0xffffffffffffffe4:i64', 'imm_occurrence:0xc0d:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc0d:mem_disp:1:0xffffffffffffffe4:i64', 'imm_occurrence:0xc0d:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc08`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc10`: `cdq` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc11`: `shr edx, 0x1c` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc08`      c08:	e9 9e 00 00 00       	jmpq   cab <stage1_mistrain_trigger+0xb6> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc0d`      c0d:	8b 45 e4             	mov    -0x1c(%rbp),%eax groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc10`      c10:	99                   	cltd    groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc11`      c11:	c1 ea 1c             	shr    $0x1c,%edx groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger` pcs=`['0xc0d', '0xc10', '0xc11']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
   91: 
   92:     for (j = 29; j >= 0; j--) {
   93:         training_x = (size_t)(j % 16);
   94:         _mm_clflush(&array1_size);
   95:         for (volatile int z = 0; z < 200; z++) {}
```

### 50. `imm_occurrence:0xc0d:mem_scale:1:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc0d:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc0d', 'operand_index': None, 'raw_suffix': 'mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xc0d:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc0d']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc0d']`
- direct_operand_pcs: `['0xc0d']`
- structural_role_pcs: `['0xc0d']`
- anchor_pcs: `['0xc0d']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc08', '0xc10', '0xc11']`
- all_mapped_pcs: `['0xc08', '0xc0d', '0xc10', '0xc11']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x1c]']`

#### PC Relation Entries

- `0xc08` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc0d` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc10` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc11` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc0d`: `mov eax, dword ptr [rbp - 0x1c]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x1c]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc0d:mem_disp:1:0xffffffffffffffe4:i64', 'imm_occurrence:0xc0d:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc0d:mem_disp:1:0xffffffffffffffe4:i64', 'imm_occurrence:0xc0d:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc08`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc10`: `cdq` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc11`: `shr edx, 0x1c` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc08`      c08:	e9 9e 00 00 00       	jmpq   cab <stage1_mistrain_trigger+0xb6> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc0d`      c0d:	8b 45 e4             	mov    -0x1c(%rbp),%eax groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc10`      c10:	99                   	cltd    groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc11`      c11:	c1 ea 1c             	shr    $0x1c,%edx groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger` pcs=`['0xc0d', '0xc10', '0xc11']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
   91: 
   92:     for (j = 29; j >= 0; j--) {
   93:         training_x = (size_t)(j % 16);
   94:         _mm_clflush(&array1_size);
   95:         for (volatile int z = 0; z < 200; z++) {}
```

### 51. `imm_occurrence:0xc11:operand_imm:1:0x1c:i8`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc11:operand_imm:1:0x1c/i8`
- Mapping kind: `constant_or_address_component`
- Confidence: `structural`
- Object semantic tags: `[]`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc11', 'operand_index': None, 'raw_suffix': 'operand_imm:1:0x1c/i8'}`
- Reason: 对象类型为 imm，更适合作为常量、位移、scale、比较值或地址组成部分解释。
- Candidate program elements: `['imm@0xc11:operand_imm:1:0x1c/i8']`
- direct_use_pcs: `['0xc11']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc11']`
- direct_operand_pcs: `['0xc11']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xc11']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc0d', '0xc10', '0xc14', '0xc16']`
- all_mapped_pcs: `['0xc0d', '0xc10', '0xc11', '0xc14', '0xc16']`
- direct_parents: `[]`
- direct_children: `['reg:cf', 'reg:of', 'reg:rdx', 'reg:rip', 'reg:sf', 'reg:zf']`

#### PC Relation Entries

- `0xc0d` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc10` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc11` kinds=`['direct_immediate_occurrence', 'direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.used_by/instruction_details.use_objects']`
- `0xc14` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc16` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc11`: `shr edx, 0x1c` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc11:operand_imm:1:0x1c:i8', 'reg:rdx']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rdx', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xc11:operand_imm:1:0x1c:i8']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc0d`: `mov eax, dword ptr [rbp - 0x1c]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc10`: `cdq` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc14`: `add eax, edx` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc16`: `and eax, 0xf` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc0d`      c0d:	8b 45 e4             	mov    -0x1c(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc10`      c10:	99                   	cltd    groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc11`      c11:	c1 ea 1c             	shr    $0x1c,%edx groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
- `0xc14`      c14:	01 d0                	add    %edx,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc16`      c16:	83 e0 0f             	and    $0xf,%eax groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger` pcs=`['0xc0d', '0xc10', '0xc11', '0xc14', '0xc16']` groups=`['direct_operand', 'evidence_only']` kinds=`['direct_immediate_occurrence', 'direct_use', 'evidence_only']`

```c
   91: 
   92:     for (j = 29; j >= 0; j--) {
   93:         training_x = (size_t)(j % 16);
   94:         _mm_clflush(&array1_size);
   95:         for (volatile int z = 0; z < 200; z++) {}
```

### 52. `imm_occurrence:0xc16:operand_imm:1:0xf:i32`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc16:operand_imm:1:0xf/i32`
- Mapping kind: `constant_or_address_component`
- Confidence: `structural`
- Object semantic tags: `[]`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc16', 'operand_index': None, 'raw_suffix': 'operand_imm:1:0xf/i32'}`
- Reason: 对象类型为 imm，更适合作为常量、位移、scale、比较值或地址组成部分解释。
- Candidate program elements: `['imm@0xc16:operand_imm:1:0xf/i32']`
- direct_use_pcs: `['0xc16']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc16']`
- direct_operand_pcs: `['0xc16']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xc16']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc11', '0xc14', '0xc19', '0xc1b']`
- all_mapped_pcs: `['0xc11', '0xc14', '0xc16', '0xc19', '0xc1b']`
- direct_parents: `[]`
- direct_children: `['reg:cf', 'reg:of', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`

#### PC Relation Entries

- `0xc11` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc14` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc16` kinds=`['direct_immediate_occurrence', 'direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.used_by/instruction_details.use_objects']`
- `0xc19` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc1b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc16`: `and eax, 0xf` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc16:operand_imm:1:0xf:i32', 'reg:rax']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xc16:operand_imm:1:0xf:i32']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc11`: `shr edx, 0x1c` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc14`: `add eax, edx` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc19`: `sub eax, edx` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc1b`: `cdqe` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc11`      c11:	c1 ea 1c             	shr    $0x1c,%edx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc14`      c14:	01 d0                	add    %edx,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc16`      c16:	83 e0 0f             	and    $0xf,%eax groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
- `0xc19`      c19:	29 d0                	sub    %edx,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc1b`      c1b:	48 98                	cltq    groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger` pcs=`['0xc11', '0xc14', '0xc16', '0xc19', '0xc1b']` groups=`['direct_operand', 'evidence_only']` kinds=`['direct_immediate_occurrence', 'direct_use', 'evidence_only']`

```c
   91: 
   92:     for (j = 29; j >= 0; j--) {
   93:         training_x = (size_t)(j % 16);
   94:         _mm_clflush(&array1_size);
   95:         for (volatile int z = 0; z < 200; z++) {}
```

### 53. `imm_occurrence:0xc1d:mem_disp:0:0xffffffffffffffe8:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc1d:mem_disp:0:0xffffffffffffffe8/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc1d', 'operand_index': None, 'raw_suffix': 'mem_disp:0:0xffffffffffffffe8/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xc1d:mem_disp:0:0xffffffffffffffe8/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc1d']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc1d']`
- direct_operand_pcs: `['0xc1d']`
- structural_role_pcs: `['0xc1d']`
- anchor_pcs: `['0xc1d']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc19', '0xc1b', '0xc21', '0xc28']`
- all_mapped_pcs: `['0xc19', '0xc1b', '0xc1d', '0xc21', '0xc28']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x18]']`

#### PC Relation Entries

- `0xc19` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc1b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc1d` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc21` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc28` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc1d`: `mov qword ptr [rbp - 0x18], rax` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x18]']`
  - addr_objects: `['imm_occurrence:0xc1d:mem_disp:0:0xffffffffffffffe8:i64', 'imm_occurrence:0xc1d:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc1d:mem_disp:0:0xffffffffffffffe8:i64', 'imm_occurrence:0xc1d:mem_scale:0:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc19`: `sub eax, edx` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc1b`: `cdqe` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc21`: `lea rax, [rip + 0x2023f8]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc28`: `mov qword ptr [rbp - 8], rax` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc19`      c19:	29 d0                	sub    %edx,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc1b`      c1b:	48 98                	cltq    groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc1d`      c1d:	48 89 45 e8          	mov    %rax,-0x18(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc21`      c21:	48 8d 05 f8 23 20 00 	lea    0x2023f8(%rip),%rax        # 203020 <array1_size> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc28`      c28:	48 89 45 f8          	mov    %rax,-0x8(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger` pcs=`['0xc19', '0xc1b', '0xc1d', '0xc21', '0xc28']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
   91: 
   92:     for (j = 29; j >= 0; j--) {
   93:         training_x = (size_t)(j % 16);
   94:         _mm_clflush(&array1_size);
   95:         for (volatile int z = 0; z < 200; z++) {}
```

### 54. `imm_occurrence:0xc1d:mem_scale:0:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc1d:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc1d', 'operand_index': None, 'raw_suffix': 'mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xc1d:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc1d']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc1d']`
- direct_operand_pcs: `['0xc1d']`
- structural_role_pcs: `['0xc1d']`
- anchor_pcs: `['0xc1d']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc19', '0xc1b', '0xc21', '0xc28']`
- all_mapped_pcs: `['0xc19', '0xc1b', '0xc1d', '0xc21', '0xc28']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x18]']`

#### PC Relation Entries

- `0xc19` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc1b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc1d` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc21` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc28` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc1d`: `mov qword ptr [rbp - 0x18], rax` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x18]']`
  - addr_objects: `['imm_occurrence:0xc1d:mem_disp:0:0xffffffffffffffe8:i64', 'imm_occurrence:0xc1d:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc1d:mem_disp:0:0xffffffffffffffe8:i64', 'imm_occurrence:0xc1d:mem_scale:0:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc19`: `sub eax, edx` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc1b`: `cdqe` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc21`: `lea rax, [rip + 0x2023f8]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc28`: `mov qword ptr [rbp - 8], rax` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc19`      c19:	29 d0                	sub    %edx,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc1b`      c1b:	48 98                	cltq    groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc1d`      c1d:	48 89 45 e8          	mov    %rax,-0x18(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc21`      c21:	48 8d 05 f8 23 20 00 	lea    0x2023f8(%rip),%rax        # 203020 <array1_size> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc28`      c28:	48 89 45 f8          	mov    %rax,-0x8(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger` pcs=`['0xc19', '0xc1b', '0xc1d', '0xc21', '0xc28']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
   91: 
   92:     for (j = 29; j >= 0; j--) {
   93:         training_x = (size_t)(j % 16);
   94:         _mm_clflush(&array1_size);
   95:         for (volatile int z = 0; z < 200; z++) {}
```

### 55. `imm_occurrence:0xc28:mem_disp:0:0xfffffffffffffff8:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc28:mem_disp:0:0xfffffffffffffff8/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc28', 'operand_index': None, 'raw_suffix': 'mem_disp:0:0xfffffffffffffff8/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xc28:mem_disp:0:0xfffffffffffffff8/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc28']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc28']`
- direct_operand_pcs: `['0xc28']`
- structural_role_pcs: `['0xc28']`
- anchor_pcs: `['0xc28']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc1d', '0xc21']`
- all_mapped_pcs: `['0xc1d', '0xc21', '0xc28']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x8]']`

#### PC Relation Entries

- `0xc1d` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc21` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc28` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`

#### Direct Anchor Instruction Evidence

- PC `0xc28`: `mov qword ptr [rbp - 8], rax` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x8]']`
  - addr_objects: `['imm_occurrence:0xc28:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xc28:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc28:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xc28:mem_scale:0:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc1d`: `mov qword ptr [rbp - 0x18], rax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc21`: `lea rax, [rip + 0x2023f8]` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc1d`      c1d:	48 89 45 e8          	mov    %rax,-0x18(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc21`      c21:	48 8d 05 f8 23 20 00 	lea    0x2023f8(%rip),%rax        # 203020 <array1_size> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc28`      c28:	48 89 45 f8          	mov    %rax,-0x8(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger` pcs=`['0xc1d', '0xc21', '0xc28']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
   91: 
   92:     for (j = 29; j >= 0; j--) {
   93:         training_x = (size_t)(j % 16);
   94:         _mm_clflush(&array1_size);
   95:         for (volatile int z = 0; z < 200; z++) {}
```

### 56. `imm_occurrence:0xc28:mem_scale:0:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc28:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc28', 'operand_index': None, 'raw_suffix': 'mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xc28:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc28']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc28']`
- direct_operand_pcs: `['0xc28']`
- structural_role_pcs: `['0xc28']`
- anchor_pcs: `['0xc28']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc1d', '0xc21']`
- all_mapped_pcs: `['0xc1d', '0xc21', '0xc28']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x8]']`

#### PC Relation Entries

- `0xc1d` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc21` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc28` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`

#### Direct Anchor Instruction Evidence

- PC `0xc28`: `mov qword ptr [rbp - 8], rax` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x8]']`
  - addr_objects: `['imm_occurrence:0xc28:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xc28:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc28:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xc28:mem_scale:0:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc1d`: `mov qword ptr [rbp - 0x18], rax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc21`: `lea rax, [rip + 0x2023f8]` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc1d`      c1d:	48 89 45 e8          	mov    %rax,-0x18(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc21`      c21:	48 8d 05 f8 23 20 00 	lea    0x2023f8(%rip),%rax        # 203020 <array1_size> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc28`      c28:	48 89 45 f8          	mov    %rax,-0x8(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger` pcs=`['0xc1d', '0xc21', '0xc28']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
   91: 
   92:     for (j = 29; j >= 0; j--) {
   93:         training_x = (size_t)(j % 16);
   94:         _mm_clflush(&array1_size);
   95:         for (volatile int z = 0; z < 200; z++) {}
```

### 57. `imm_occurrence:0xc2c:mem_disp:1:0xfffffffffffffff8:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc2c:mem_disp:1:0xfffffffffffffff8/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc2c', 'operand_index': None, 'raw_suffix': 'mem_disp:1:0xfffffffffffffff8/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xc2c:mem_disp:1:0xfffffffffffffff8/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc2c']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc2c']`
- direct_operand_pcs: `['0xc2c']`
- structural_role_pcs: `['0xc2c']`
- anchor_pcs: `['0xc2c']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc30']`
- all_mapped_pcs: `['0xc2c', '0xc30']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x8]']`

#### PC Relation Entries

- `0xc2c` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc30` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc2c`: `mov rax, qword ptr [rbp - 8]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/usr/lib/gcc/x86_64-linux-gnu/7/include/emmintrin.h:1486` function=`_mm_clflush`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x8]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc2c:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xc2c:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc2c:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xc2c:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc30`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc2c`      c2c:	48 8b 45 f8          	mov    -0x8(%rbp),%rax groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc30`      c30:	0f ae 38             	clflush (%rax) groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/usr/lib/gcc/x86_64-linux-gnu/7/include/emmintrin.h:1486` function=`_mm_clflush` pcs=`['0xc2c']` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`

### 58. `imm_occurrence:0xc2c:mem_scale:1:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc2c:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc2c', 'operand_index': None, 'raw_suffix': 'mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xc2c:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc2c']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc2c']`
- direct_operand_pcs: `['0xc2c']`
- structural_role_pcs: `['0xc2c']`
- anchor_pcs: `['0xc2c']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc30']`
- all_mapped_pcs: `['0xc2c', '0xc30']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x8]']`

#### PC Relation Entries

- `0xc2c` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc30` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc2c`: `mov rax, qword ptr [rbp - 8]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/usr/lib/gcc/x86_64-linux-gnu/7/include/emmintrin.h:1486` function=`_mm_clflush`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x8]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc2c:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xc2c:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc2c:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xc2c:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc30`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc2c`      c2c:	48 8b 45 f8          	mov    -0x8(%rbp),%rax groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc30`      c30:	0f ae 38             	clflush (%rax) groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/usr/lib/gcc/x86_64-linux-gnu/7/include/emmintrin.h:1486` function=`_mm_clflush` pcs=`['0xc2c']` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`

### 59. `imm_occurrence:0xc33:mem_disp:0:0xffffffffffffffe0:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc33:mem_disp:0:0xffffffffffffffe0/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc33', 'operand_index': None, 'raw_suffix': 'mem_disp:0:0xffffffffffffffe0/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xc33:mem_disp:0:0xffffffffffffffe0/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc33']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc33']`
- direct_operand_pcs: `['0xc33']`
- structural_role_pcs: `['0xc33']`
- anchor_pcs: `['0xc33']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc3a', '0xc3c']`
- all_mapped_pcs: `['0xc33', '0xc3a', '0xc3c']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x20]']`

#### PC Relation Entries

- `0xc33` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc3a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc3c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc33`: `mov dword ptr [rbp - 0x20], 0` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:95` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc33:operand_imm:1:0x0:i32', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x20]']`
  - addr_objects: `['imm_occurrence:0xc33:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xc33:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc33:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xc33:mem_scale:0:0x1:i64', 'imm_occurrence:0xc33:operand_imm:1:0x0:i32']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc3a`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc3c`: `mov eax, dword ptr [rbp - 0x20]` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc33`      c33:	c7 45 e0 00 00 00 00 	movl   $0x0,-0x20(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc3a`      c3a:	eb 09                	jmp    c45 <stage1_mistrain_trigger+0x50> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc3c`      c3c:	8b 45 e0             	mov    -0x20(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:95` function=`stage1_mistrain_trigger` pcs=`['0xc33']` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`

```c
   93:         training_x = (size_t)(j % 16);
   94:         _mm_clflush(&array1_size);
   95:         for (volatile int z = 0; z < 200; z++) {}
   96: 
   97:         x = ((j % 6) - 1) & ~0xFFFF;
```

### 60. `imm_occurrence:0xc33:mem_scale:0:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc33:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc33', 'operand_index': None, 'raw_suffix': 'mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xc33:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc33']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc33']`
- direct_operand_pcs: `['0xc33']`
- structural_role_pcs: `['0xc33']`
- anchor_pcs: `['0xc33']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc3a', '0xc3c']`
- all_mapped_pcs: `['0xc33', '0xc3a', '0xc3c']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x20]']`

#### PC Relation Entries

- `0xc33` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc3a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc3c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc33`: `mov dword ptr [rbp - 0x20], 0` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:95` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc33:operand_imm:1:0x0:i32', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x20]']`
  - addr_objects: `['imm_occurrence:0xc33:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xc33:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc33:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xc33:mem_scale:0:0x1:i64', 'imm_occurrence:0xc33:operand_imm:1:0x0:i32']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc3a`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc3c`: `mov eax, dword ptr [rbp - 0x20]` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc33`      c33:	c7 45 e0 00 00 00 00 	movl   $0x0,-0x20(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc3a`      c3a:	eb 09                	jmp    c45 <stage1_mistrain_trigger+0x50> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc3c`      c3c:	8b 45 e0             	mov    -0x20(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:95` function=`stage1_mistrain_trigger` pcs=`['0xc33']` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`

```c
   93:         training_x = (size_t)(j % 16);
   94:         _mm_clflush(&array1_size);
   95:         for (volatile int z = 0; z < 200; z++) {}
   96: 
   97:         x = ((j % 6) - 1) & ~0xFFFF;
```

### 61. `imm_occurrence:0xc33:operand_imm:1:0x0:i32`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc33:operand_imm:1:0x0/i32 [program_semantic_constant|store_constant]`
- Mapping kind: `store_constant`
- Confidence: `semantic`
- Object semantic tags: `['program_semantic_constant', 'store_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc33', 'operand_index': None, 'raw_suffix': 'operand_imm:1:0x0/i32 [program_semantic_constant|store_constant]'}`
- Reason: 该 immediate 带有 store_constant 标签，更适合作为写入值常量解释。
- Candidate program elements: `['imm@0xc33:operand_imm:1:0x0/i32 [program_semantic_constant|store_constant]']`
- direct_use_pcs: `['0xc33']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc33']`
- direct_operand_pcs: `['0xc33']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xc33']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc3a', '0xc3c']`
- all_mapped_pcs: `['0xc33', '0xc3a', '0xc3c']`
- direct_parents: `[]`
- direct_children: `['reg:rip', 'stack:[rbp-0x20]']`

#### PC Relation Entries

- `0xc33` kinds=`['direct_immediate_occurrence', 'direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.used_by/instruction_details.use_objects']`
- `0xc3a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc3c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc33`: `mov dword ptr [rbp - 0x20], 0` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
  - Source: `/root/src/spectre_stage1_2_auto.c:95` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc33:operand_imm:1:0x0:i32', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x20]']`
  - addr_objects: `['imm_occurrence:0xc33:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xc33:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc33:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xc33:mem_scale:0:0x1:i64', 'imm_occurrence:0xc33:operand_imm:1:0x0:i32']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc3a`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc3c`: `mov eax, dword ptr [rbp - 0x20]` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc33`      c33:	c7 45 e0 00 00 00 00 	movl   $0x0,-0x20(%rbp) groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
- `0xc3a`      c3a:	eb 09                	jmp    c45 <stage1_mistrain_trigger+0x50> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc3c`      c3c:	8b 45 e0             	mov    -0x20(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:95` function=`stage1_mistrain_trigger` pcs=`['0xc33']` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`

```c
   93:         training_x = (size_t)(j % 16);
   94:         _mm_clflush(&array1_size);
   95:         for (volatile int z = 0; z < 200; z++) {}
   96: 
   97:         x = ((j % 6) - 1) & ~0xFFFF;
```

### 62. `imm_occurrence:0xc3a:operand_imm:0:0xc45:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc3a:operand_imm:0:0xc45/i64`
- Mapping kind: `constant_or_address_component`
- Confidence: `structural`
- Object semantic tags: `[]`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc3a', 'operand_index': None, 'raw_suffix': 'operand_imm:0:0xc45/i64'}`
- Reason: 对象类型为 imm，更适合作为常量、位移、scale、比较值或地址组成部分解释。
- Candidate program elements: `['imm@0xc3a:operand_imm:0:0xc45/i64']`
- direct_use_pcs: `['0xc3a']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `['0xc3a']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xc3a']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc33', '0xc3c', '0xc3f']`
- all_mapped_pcs: `['0xc33', '0xc3a', '0xc3c', '0xc3f']`
- direct_parents: `[]`
- direct_children: `['reg:rip']`

#### PC Relation Entries

- `0xc33` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc3a` kinds=`['direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['object_detail.used_by/instruction_details.use_objects']`
- `0xc3c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc3f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc3a`: `None` groups=`['direct_operand']` kinds=`['direct_use']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc33`: `mov dword ptr [rbp - 0x20], 0` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc3c`: `mov eax, dword ptr [rbp - 0x20]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc3f`: `add eax, 1` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc33`      c33:	c7 45 e0 00 00 00 00 	movl   $0x0,-0x20(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc3a`      c3a:	eb 09                	jmp    c45 <stage1_mistrain_trigger+0x50> groups=`['direct_operand']` kinds=`['direct_use']`
- `0xc3c`      c3c:	8b 45 e0             	mov    -0x20(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc3f`      c3f:	83 c0 01             	add    $0x1,%eax groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:95` function=`stage1_mistrain_trigger` pcs=`['0xc33']` groups=`['evidence_only']` kinds=`['evidence_only']`

```c
   93:         training_x = (size_t)(j % 16);
   94:         _mm_clflush(&array1_size);
   95:         for (volatile int z = 0; z < 200; z++) {}
   96: 
   97:         x = ((j % 6) - 1) & ~0xFFFF;
```

### 63. `imm_occurrence:0xc3c:mem_disp:1:0xffffffffffffffe0:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc3c:mem_disp:1:0xffffffffffffffe0/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc3c', 'operand_index': None, 'raw_suffix': 'mem_disp:1:0xffffffffffffffe0/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xc3c:mem_disp:1:0xffffffffffffffe0/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc3c']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc3c']`
- direct_operand_pcs: `['0xc3c']`
- structural_role_pcs: `['0xc3c']`
- anchor_pcs: `['0xc3c']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc33', '0xc3a', '0xc3f', '0xc42']`
- all_mapped_pcs: `['0xc33', '0xc3a', '0xc3c', '0xc3f', '0xc42']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x20]']`

#### PC Relation Entries

- `0xc33` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc3a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc3c` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc3f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc42` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc3c`: `mov eax, dword ptr [rbp - 0x20]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x20]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc3c:mem_disp:1:0xffffffffffffffe0:i64', 'imm_occurrence:0xc3c:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc3c:mem_disp:1:0xffffffffffffffe0:i64', 'imm_occurrence:0xc3c:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc33`: `mov dword ptr [rbp - 0x20], 0` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc3a`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc3f`: `add eax, 1` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc42`: `mov dword ptr [rbp - 0x20], eax` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc33`      c33:	c7 45 e0 00 00 00 00 	movl   $0x0,-0x20(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc3a`      c3a:	eb 09                	jmp    c45 <stage1_mistrain_trigger+0x50> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc3c`      c3c:	8b 45 e0             	mov    -0x20(%rbp),%eax groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc3f`      c3f:	83 c0 01             	add    $0x1,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc42`      c42:	89 45 e0             	mov    %eax,-0x20(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:95` function=`stage1_mistrain_trigger` pcs=`['0xc33']` groups=`['evidence_only']` kinds=`['evidence_only']`

```c
   93:         training_x = (size_t)(j % 16);
   94:         _mm_clflush(&array1_size);
   95:         for (volatile int z = 0; z < 200; z++) {}
   96: 
   97:         x = ((j % 6) - 1) & ~0xFFFF;
```

### 64. `imm_occurrence:0xc3c:mem_scale:1:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc3c:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc3c', 'operand_index': None, 'raw_suffix': 'mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xc3c:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc3c']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc3c']`
- direct_operand_pcs: `['0xc3c']`
- structural_role_pcs: `['0xc3c']`
- anchor_pcs: `['0xc3c']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc33', '0xc3a', '0xc3f', '0xc42']`
- all_mapped_pcs: `['0xc33', '0xc3a', '0xc3c', '0xc3f', '0xc42']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x20]']`

#### PC Relation Entries

- `0xc33` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc3a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc3c` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc3f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc42` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc3c`: `mov eax, dword ptr [rbp - 0x20]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x20]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc3c:mem_disp:1:0xffffffffffffffe0:i64', 'imm_occurrence:0xc3c:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc3c:mem_disp:1:0xffffffffffffffe0:i64', 'imm_occurrence:0xc3c:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc33`: `mov dword ptr [rbp - 0x20], 0` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc3a`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc3f`: `add eax, 1` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc42`: `mov dword ptr [rbp - 0x20], eax` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc33`      c33:	c7 45 e0 00 00 00 00 	movl   $0x0,-0x20(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc3a`      c3a:	eb 09                	jmp    c45 <stage1_mistrain_trigger+0x50> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc3c`      c3c:	8b 45 e0             	mov    -0x20(%rbp),%eax groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc3f`      c3f:	83 c0 01             	add    $0x1,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc42`      c42:	89 45 e0             	mov    %eax,-0x20(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:95` function=`stage1_mistrain_trigger` pcs=`['0xc33']` groups=`['evidence_only']` kinds=`['evidence_only']`

```c
   93:         training_x = (size_t)(j % 16);
   94:         _mm_clflush(&array1_size);
   95:         for (volatile int z = 0; z < 200; z++) {}
   96: 
   97:         x = ((j % 6) - 1) & ~0xFFFF;
```

### 65. `imm_occurrence:0xc3f:operand_imm:1:0x1:i32`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc3f:operand_imm:1:0x1/i32`
- Mapping kind: `constant_or_address_component`
- Confidence: `structural`
- Object semantic tags: `[]`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc3f', 'operand_index': None, 'raw_suffix': 'operand_imm:1:0x1/i32'}`
- Reason: 对象类型为 imm，更适合作为常量、位移、scale、比较值或地址组成部分解释。
- Candidate program elements: `['imm@0xc3f:operand_imm:1:0x1/i32']`
- direct_use_pcs: `['0xc3f']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc3f']`
- direct_operand_pcs: `['0xc3f']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xc3f']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc3a', '0xc3c', '0xc42', '0xc45']`
- all_mapped_pcs: `['0xc3a', '0xc3c', '0xc3f', '0xc42', '0xc45']`
- direct_parents: `[]`
- direct_children: `['reg:cf', 'reg:of', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`

#### PC Relation Entries

- `0xc3a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc3c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc3f` kinds=`['direct_immediate_occurrence', 'direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.used_by/instruction_details.use_objects']`
- `0xc42` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc45` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc3f`: `add eax, 1` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc3f:operand_imm:1:0x1:i32', 'reg:rax']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xc3f:operand_imm:1:0x1:i32']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc3a`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc3c`: `mov eax, dword ptr [rbp - 0x20]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc42`: `mov dword ptr [rbp - 0x20], eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc45`: `mov eax, dword ptr [rbp - 0x20]` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc3a`      c3a:	eb 09                	jmp    c45 <stage1_mistrain_trigger+0x50> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc3c`      c3c:	8b 45 e0             	mov    -0x20(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc3f`      c3f:	83 c0 01             	add    $0x1,%eax groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
- `0xc42`      c42:	89 45 e0             	mov    %eax,-0x20(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc45`      c45:	8b 45 e0             	mov    -0x20(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 66. `imm_occurrence:0xc42:mem_disp:0:0xffffffffffffffe0:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc42:mem_disp:0:0xffffffffffffffe0/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc42', 'operand_index': None, 'raw_suffix': 'mem_disp:0:0xffffffffffffffe0/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xc42:mem_disp:0:0xffffffffffffffe0/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc42']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc42']`
- direct_operand_pcs: `['0xc42']`
- structural_role_pcs: `['0xc42']`
- anchor_pcs: `['0xc42']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc3c', '0xc3f', '0xc45', '0xc48']`
- all_mapped_pcs: `['0xc3c', '0xc3f', '0xc42', '0xc45', '0xc48']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x20]']`

#### PC Relation Entries

- `0xc3c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc3f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc42` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc45` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc48` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc42`: `mov dword ptr [rbp - 0x20], eax` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x20]']`
  - addr_objects: `['imm_occurrence:0xc42:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xc42:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc42:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xc42:mem_scale:0:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc3c`: `mov eax, dword ptr [rbp - 0x20]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc3f`: `add eax, 1` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc45`: `mov eax, dword ptr [rbp - 0x20]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc48`: `cmp eax, 0xc7` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc3c`      c3c:	8b 45 e0             	mov    -0x20(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc3f`      c3f:	83 c0 01             	add    $0x1,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc42`      c42:	89 45 e0             	mov    %eax,-0x20(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc45`      c45:	8b 45 e0             	mov    -0x20(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc48`      c48:	3d c7 00 00 00       	cmp    $0xc7,%eax groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 67. `imm_occurrence:0xc42:mem_scale:0:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc42:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc42', 'operand_index': None, 'raw_suffix': 'mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xc42:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc42']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc42']`
- direct_operand_pcs: `['0xc42']`
- structural_role_pcs: `['0xc42']`
- anchor_pcs: `['0xc42']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc3c', '0xc3f', '0xc45', '0xc48']`
- all_mapped_pcs: `['0xc3c', '0xc3f', '0xc42', '0xc45', '0xc48']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x20]']`

#### PC Relation Entries

- `0xc3c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc3f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc42` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc45` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc48` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc42`: `mov dword ptr [rbp - 0x20], eax` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x20]']`
  - addr_objects: `['imm_occurrence:0xc42:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xc42:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc42:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xc42:mem_scale:0:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc3c`: `mov eax, dword ptr [rbp - 0x20]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc3f`: `add eax, 1` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc45`: `mov eax, dword ptr [rbp - 0x20]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc48`: `cmp eax, 0xc7` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc3c`      c3c:	8b 45 e0             	mov    -0x20(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc3f`      c3f:	83 c0 01             	add    $0x1,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc42`      c42:	89 45 e0             	mov    %eax,-0x20(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc45`      c45:	8b 45 e0             	mov    -0x20(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc48`      c48:	3d c7 00 00 00       	cmp    $0xc7,%eax groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 68. `imm_occurrence:0xc45:mem_disp:1:0xffffffffffffffe0:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc45:mem_disp:1:0xffffffffffffffe0/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc45', 'operand_index': None, 'raw_suffix': 'mem_disp:1:0xffffffffffffffe0/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xc45:mem_disp:1:0xffffffffffffffe0/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc45']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc45']`
- direct_operand_pcs: `['0xc45']`
- structural_role_pcs: `['0xc45']`
- anchor_pcs: `['0xc45']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc3f', '0xc42', '0xc48', '0xc4d']`
- all_mapped_pcs: `['0xc3f', '0xc42', '0xc45', '0xc48', '0xc4d']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x20]']`

#### PC Relation Entries

- `0xc3f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc42` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc45` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc48` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc4d` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc45`: `mov eax, dword ptr [rbp - 0x20]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x20]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc45:mem_disp:1:0xffffffffffffffe0:i64', 'imm_occurrence:0xc45:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc45:mem_disp:1:0xffffffffffffffe0:i64', 'imm_occurrence:0xc45:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc3f`: `add eax, 1` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc42`: `mov dword ptr [rbp - 0x20], eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc48`: `cmp eax, 0xc7` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc4d`: `jle 0xc3c` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc3f`      c3f:	83 c0 01             	add    $0x1,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc42`      c42:	89 45 e0             	mov    %eax,-0x20(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc45`      c45:	8b 45 e0             	mov    -0x20(%rbp),%eax groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc48`      c48:	3d c7 00 00 00       	cmp    $0xc7,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc4d`      c4d:	7e ed                	jle    c3c <stage1_mistrain_trigger+0x47> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 69. `imm_occurrence:0xc45:mem_scale:1:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc45:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc45', 'operand_index': None, 'raw_suffix': 'mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xc45:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc45']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc45']`
- direct_operand_pcs: `['0xc45']`
- structural_role_pcs: `['0xc45']`
- anchor_pcs: `['0xc45']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc3f', '0xc42', '0xc48', '0xc4d']`
- all_mapped_pcs: `['0xc3f', '0xc42', '0xc45', '0xc48', '0xc4d']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x20]']`

#### PC Relation Entries

- `0xc3f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc42` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc45` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc48` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc4d` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc45`: `mov eax, dword ptr [rbp - 0x20]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x20]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc45:mem_disp:1:0xffffffffffffffe0:i64', 'imm_occurrence:0xc45:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc45:mem_disp:1:0xffffffffffffffe0:i64', 'imm_occurrence:0xc45:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc3f`: `add eax, 1` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc42`: `mov dword ptr [rbp - 0x20], eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc48`: `cmp eax, 0xc7` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc4d`: `jle 0xc3c` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc3f`      c3f:	83 c0 01             	add    $0x1,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc42`      c42:	89 45 e0             	mov    %eax,-0x20(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc45`      c45:	8b 45 e0             	mov    -0x20(%rbp),%eax groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc48`      c48:	3d c7 00 00 00       	cmp    $0xc7,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc4d`      c4d:	7e ed                	jle    c3c <stage1_mistrain_trigger+0x47> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 70. `imm_occurrence:0xc48:operand_imm:1:0xc7:i32`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc48:operand_imm:1:0xc7/i32 [comparison_constant|program_semantic_constant]`
- Mapping kind: `comparison_constant`
- Confidence: `semantic`
- Object semantic tags: `['comparison_constant', 'loop_bound_constant', 'program_semantic_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc48', 'operand_index': None, 'raw_suffix': 'operand_imm:1:0xc7/i32 [comparison_constant|program_semantic_constant]'}`
- Reason: 该 immediate 带有 comparison_constant 标签，更适合作为比较语义常量解释。
- Candidate program elements: `['imm@0xc48:operand_imm:1:0xc7/i32 [comparison_constant|program_semantic_constant]']`
- direct_use_pcs: `['0xc48']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc48']`
- direct_operand_pcs: `['0xc48']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xc48']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc42', '0xc45', '0xc4d']`
- all_mapped_pcs: `['0xc42', '0xc45', '0xc48', '0xc4d']`
- direct_parents: `[]`
- direct_children: `['reg:cf', 'reg:of', 'reg:rip', 'reg:sf', 'reg:zf']`

#### PC Relation Entries

- `0xc42` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc45` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc48` kinds=`['direct_immediate_occurrence', 'direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.used_by/instruction_details.use_objects']`
- `0xc4d` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc48`: `cmp eax, 0xc7` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc48:operand_imm:1:0xc7:i32', 'reg:rax']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xc48:operand_imm:1:0xc7:i32']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc42`: `mov dword ptr [rbp - 0x20], eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc45`: `mov eax, dword ptr [rbp - 0x20]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc4d`: `jle 0xc3c` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc42`      c42:	89 45 e0             	mov    %eax,-0x20(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc45`      c45:	8b 45 e0             	mov    -0x20(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc48`      c48:	3d c7 00 00 00       	cmp    $0xc7,%eax groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
- `0xc4d`      c4d:	7e ed                	jle    c3c <stage1_mistrain_trigger+0x47> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 71. `imm_occurrence:0xc4d:operand_imm:0:0xc3c:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc4d:operand_imm:0:0xc3c/i64`
- Mapping kind: `comparison_constant`
- Confidence: `semantic`
- Object semantic tags: `['comparison_constant']`
- Anchor instruction tags: `['argument_shuffle', 'callee_save_restore', 'callee_save_spill', 'conditional_branch', 'epilogue', 'prologue']`
- Scaffolding tags: `['argument_shuffle', 'callee_save_restore', 'callee_save_spill', 'epilogue', 'prologue']`
- Occurrence: `{'occurrence_pc': '0xc4d', 'operand_index': None, 'raw_suffix': 'operand_imm:0:0xc3c/i64'}`
- Reason: 该 immediate 带有 comparison_constant 标签，更适合作为比较语义常量解释。 检测到 ABI/脚手架标签：argument_shuffle, callee_save_restore, callee_save_spill, epilogue, prologue，应更偏向解释为结构性对象，而非优先可变异语义对象。
- Candidate program elements: `['imm@0xc4d:operand_imm:0:0xc3c/i64']`
- direct_use_pcs: `['0xc4d']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `['0xb7a', '0xb7b', '0xb7e', '0xb82', '0xb86', '0xb8b', '0xb91', '0xb93', '0xb97', '0xb99', '0xba0', '0xba4', '0xba7', '0xbaa', '0xbad', '0xbb0', '0xbb3', '0xbba', '0xbbe', '0xbc5', '0xbc7', '0xbcd', '0xbd2', '0xbd3', '0xbd4', '0xc0d', '0xc10', '0xc11', '0xc14', '0xc16', '0xc19', '0xc1b', '0xc1d', '0xc21', '0xc28', '0xc2c', '0xc30', '0xc33', '0xc3a', '0xc3c', '0xc3f', '0xc42', '0xc45', '0xc48', '0xc4d', '0xc4f', '0xc52', '0xc57', '0xc59', '0xc5b', '0xc5d', '0xc60', '0xc62', '0xc64', '0xc66', '0xc68', '0xc6a', '0xc6c', '0xc6e', '0xc71', '0xc75', '0xc77', '0xc7b', '0xc7f', '0xc83', '0xc87', '0xc8b', '0xc8f', '0xc93', '0xc97', '0xc9b', '0xc9f', '0xca2', '0xca7', '0xcab', '0xcaf', '0xcb5', '0xcb6', '0xcb7', '0x150b', '0x150c', '0x150f', '0x1515', '0x1517', '0x1577', '0x1578', '0x1579', '0x157a', '0x157b', '0x157e', '0x1582', '0x1588', '0x158a', '0x168e', '0x168f', '0x1690']`
- direct_imm_pcs: `['0xc4d']`
- direct_operand_pcs: `['0xc4d']`
- structural_role_pcs: `['0xb7a', '0xb7b', '0xb7e', '0xb82', '0xb86', '0xb8b', '0xb91', '0xb93', '0xb97', '0xb99', '0xba0', '0xba4', '0xba7', '0xbaa', '0xbad', '0xbb0', '0xbb3', '0xbba', '0xbbe', '0xbc5', '0xbc7', '0xbcd', '0xbd2', '0xbd3', '0xbd4', '0xc0d', '0xc10', '0xc11', '0xc14', '0xc16', '0xc19', '0xc1b', '0xc1d', '0xc21', '0xc28', '0xc2c', '0xc30', '0xc33', '0xc3a', '0xc3c', '0xc3f', '0xc42', '0xc45', '0xc48', '0xc4d', '0xc4f', '0xc52', '0xc57', '0xc59', '0xc5b', '0xc5d', '0xc60', '0xc62', '0xc64', '0xc66', '0xc68', '0xc6a', '0xc6c', '0xc6e', '0xc71', '0xc75', '0xc77', '0xc7b', '0xc7f', '0xc83', '0xc87', '0xc8b', '0xc8f', '0xc93', '0xc97', '0xc9b', '0xc9f', '0xca2', '0xca7', '0xcab', '0xcaf', '0xcb5', '0xcb6', '0xcb7', '0x150b', '0x150c', '0x150f', '0x1515', '0x1517', '0x1577', '0x1578', '0x1579', '0x157a', '0x157b', '0x157e', '0x1582', '0x1588', '0x158a', '0x168e', '0x168f', '0x1690']`
- anchor_pcs: `['0xb7a', '0xb7b', '0xb7e', '0xb82', '0xb86', '0xb8b', '0xb91', '0xb93', '0xb97', '0xb99', '0xba0', '0xba4', '0xba7', '0xbaa', '0xbad', '0xbb0', '0xbb3', '0xbba', '0xbbe', '0xbc5', '0xbc7', '0xbcd', '0xbd2', '0xbd3', '0xbd4', '0xc0d', '0xc10', '0xc11', '0xc14', '0xc16', '0xc19', '0xc1b', '0xc1d', '0xc21', '0xc28', '0xc2c', '0xc30', '0xc33', '0xc3a', '0xc3c', '0xc3f', '0xc42', '0xc45', '0xc48', '0xc4d', '0xc4f', '0xc52', '0xc57', '0xc59', '0xc5b', '0xc5d', '0xc60', '0xc62', '0xc64', '0xc66', '0xc68', '0xc6a', '0xc6c', '0xc6e', '0xc71', '0xc75', '0xc77', '0xc7b', '0xc7f', '0xc83', '0xc87', '0xc8b', '0xc8f', '0xc93', '0xc97', '0xc9b', '0xc9f', '0xca2', '0xca7', '0xcab', '0xcaf', '0xcb5', '0xcb6', '0xcb7', '0x150b', '0x150c', '0x150f', '0x1515', '0x1517', '0x1577', '0x1578', '0x1579', '0x157a', '0x157b', '0x157e', '0x1582', '0x1588', '0x158a', '0x168e', '0x168f', '0x1690']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc08', '0x1519', '0x151f', '0x156e', '0x1575', '0x1590', '0x1596', '0x1686', '0x168c']`
- all_mapped_pcs: `['0xb7a', '0xb7b', '0xb7e', '0xb82', '0xb86', '0xb8b', '0xb91', '0xb93', '0xb97', '0xb99', '0xba0', '0xba4', '0xba7', '0xbaa', '0xbad', '0xbb0', '0xbb3', '0xbba', '0xbbe', '0xbc5', '0xbc7', '0xbcd', '0xbd2', '0xbd3', '0xbd4', '0xc08', '0xc0d', '0xc10', '0xc11', '0xc14', '0xc16', '0xc19', '0xc1b', '0xc1d', '0xc21', '0xc28', '0xc2c', '0xc30', '0xc33', '0xc3a', '0xc3c', '0xc3f', '0xc42', '0xc45', '0xc48', '0xc4d', '0xc4f', '0xc52', '0xc57', '0xc59', '0xc5b', '0xc5d', '0xc60', '0xc62', '0xc64', '0xc66', '0xc68', '0xc6a', '0xc6c', '0xc6e', '0xc71', '0xc75', '0xc77', '0xc7b', '0xc7f', '0xc83', '0xc87', '0xc8b', '0xc8f', '0xc93', '0xc97', '0xc9b', '0xc9f', '0xca2', '0xca7', '0xcab', '0xcaf', '0xcb5', '0xcb6', '0xcb7', '0x150b', '0x150c', '0x150f', '0x1515', '0x1517', '0x1519', '0x151f', '0x156e', '0x1575', '0x1577', '0x1578', '0x1579', '0x157a', '0x157b', '0x157e', '0x1582', '0x1588', '0x158a', '0x1590', '0x1596', '0x1686', '0x168c', '0x168e', '0x168f', '0x1690']`
- direct_parents: `[]`
- direct_children: `['reg:cf', 'reg:of', 'reg:rax', 'reg:rbp', 'reg:rcx', 'reg:rdi', 'reg:rdx', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf', 'stack:[rbp-0x10]', 'stack:[rbp-0x18]', 'stack:[rbp-0x1c]', 'stack:[rbp-0x20]', 'stack:[rbp-0x38]', 'stack:[rbp-0x40]', 'stack:[rbp-0x8]', 'var:temp']`

#### PC Relation Entries

- `0xb7a` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xb7b` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xb7e` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xb82` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xb86` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xb8b` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xb91` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xb93` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xb97` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xb99` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xba0` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xba4` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xba7` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbaa` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbad` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbb0` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbb3` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbba` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbbe` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbc5` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbc7` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbcd` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbd2` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbd3` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbd4` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc08` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc0d` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc10` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc11` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc14` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc16` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc19` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc1b` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc1d` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc21` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc28` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc2c` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc30` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc33` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc3a` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc3c` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc3f` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc42` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc45` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc48` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc4d` kinds=`['branch_condition', 'direct_immediate_occurrence', 'direct_use']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.ctrl_used_by', 'object_detail.used_by/instruction_details.use_objects']`
- `0xc4f` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc52` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc57` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc59` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc5b` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc5d` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc60` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc62` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc64` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc66` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc68` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc6a` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc6c` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc6e` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc71` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc75` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc77` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc7b` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc7f` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc83` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc87` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc8b` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc8f` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc93` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc97` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc9b` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc9f` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xca2` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xca7` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xcab` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xcaf` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xcb5` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xcb6` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xcb7` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x150b` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x150c` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x150f` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1515` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1517` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1519` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x151f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x156e` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1575` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1577` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1578` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1579` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x157a` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x157b` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x157e` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1582` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1588` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x158a` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1590` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1596` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1686` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x168c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x168e` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x168f` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1690` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`

#### Direct Anchor Instruction Evidence

- PC `0xb7a`: `push rbp` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:58` function=`spectre_function`
  - instruction_semantic_tags: `['callee_save_spill', 'prologue']`
  - use_objects: `['reg:rbp', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x40]']`
- PC `0xb7b`: `mov rbp, rsp` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:58` function=`spectre_function`
  - instruction_semantic_tags: `['prologue']`
  - use_objects: `['reg:rsp']`
  - def_objects: `['reg:rbp', 'reg:rip']`
- PC `0xb7e`: `sub rsp, 0x10` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:58` function=`spectre_function`
  - instruction_semantic_tags: `['prologue']`
  - use_objects: `['imm_occurrence:0xb7e:operand_imm:1:0x10:i64', 'reg:rsp']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xb7e:operand_imm:1:0x10:i64']`
- PC `0xb82`: `mov qword ptr [rbp - 8], rdi` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:58` function=`spectre_function`
  - instruction_semantic_tags: `['argument_shuffle']`
  - use_objects: `['reg:rbp', 'reg:rdi']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x8]']`
  - addr_objects: `['imm_occurrence:0xb82:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xb82:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xb82:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xb82:mem_scale:0:0x1:i64']`
- PC `0xb86`: `call 0x150b` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:60` function=`spectre_function`
  - call_target: `{'operand': '0x150b', 'resolved_symbol': 'pmu_uops_snap_before', 'call_kind': 'direct_call_symbol', 'display_target': 'pmu_uops_snap_before'}`
  - use_objects: `['imm_occurrence:0xb86:operand_imm:0:0x150b:i64', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x18]']`
  - immediates: `['imm_occurrence:0xb86:operand_imm:0:0x150b:i64']`
- PC `0xb8b`: `mov eax, dword ptr [rip + 0x20248f]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function`
  - use_objects: `['reg:rip', 'var:array1_size']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xb8b:mem_disp:1:0x20248f:i64', 'imm_occurrence:0xb8b:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xb8b:mem_disp:1:0x20248f:i64', 'imm_occurrence:0xb8b:mem_scale:1:0x1:i64']`
- PC `0xb91`: `mov eax, eax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:rax', 'reg:rip']`
- PC `0xb93`: `cmp qword ptr [rbp - 8], rax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x8]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xb93:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xb93:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xb93:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xb93:mem_scale:0:0x1:i64']`
- PC `0xb97`: `jae 0xbcd` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function`
  - instruction_semantic_tags: `['conditional_branch']`
  - use_objects: `['imm_occurrence:0xb97:operand_imm:0:0xbcd:i64', 'reg:cf']`
  - def_objects: `['reg:rip']`
  - immediates: `['imm_occurrence:0xb97:operand_imm:0:0xbcd:i64']`
- PC `0xb99`: `lea rdx, [rip + 0x2024a0]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rip']`
  - def_objects: `['reg:rdx', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xb99:mem_disp:1:0x2024a0:i64', 'imm_occurrence:0xb99:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xb99:mem_disp:1:0x2024a0:i64', 'imm_occurrence:0xb99:mem_scale:1:0x1:i64']`
- PC `0xba0`: `mov rax, qword ptr [rbp - 8]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x8]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xba0:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xba0:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xba0:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xba0:mem_scale:1:0x1:i64']`
- PC `0xba4`: `add rax, rdx` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rdx']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0xba7`: `movzx eax, byte ptr [rax]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'var:array1']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xba7:mem_disp:1:0x0:i64', 'imm_occurrence:0xba7:mem_scale:1:0x1:i64', 'reg:rax', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xba7:mem_disp:1:0x0:i64', 'imm_occurrence:0xba7:mem_scale:1:0x1:i64']`
- PC `0xbaa`: `movzx eax, al` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:rax', 'reg:rip']`
- PC `0xbad`: `shl eax, 9` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['imm_occurrence:0xbad:operand_imm:1:0x9:i8', 'reg:rax']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xbad:operand_imm:1:0x9:i8']`
- PC `0xbb0`: `movsxd rdx, eax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:rdx', 'reg:rip']`
- PC `0xbb3`: `lea rax, [rip + 0x210706]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rip']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xbb3:mem_disp:1:0x210706:i64', 'imm_occurrence:0xbb3:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xbb3:mem_disp:1:0x210706:i64', 'imm_occurrence:0xbb3:mem_scale:1:0x1:i64']`
- PC `0xbba`: `movzx edx, byte ptr [rdx + rax]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rdx', 'var:array2']`
  - def_objects: `['reg:rdx', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xbba:mem_disp:1:0x0:i64', 'imm_occurrence:0xbba:mem_scale:1:0x1:i64', 'reg:rax', 'reg:rdx', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xbba:mem_disp:1:0x0:i64', 'imm_occurrence:0xbba:mem_scale:1:0x1:i64']`
- PC `0xbbe`: `movzx eax, byte ptr [rip + 0x202544]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rip', 'var:temp']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xbbe:mem_disp:1:0x202544:i64', 'imm_occurrence:0xbbe:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xbbe:mem_disp:1:0x202544:i64', 'imm_occurrence:0xbbe:mem_scale:1:0x1:i64']`
- PC `0xbc5`: `and eax, edx` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rdx']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0xbc7`: `mov byte ptr [rip + 0x20253c], al` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rip']`
  - def_objects: `['reg:rip', 'var:temp']`
  - addr_objects: `['imm_occurrence:0xbc7:mem_disp:0:0x20253c:i64', 'imm_occurrence:0xbc7:mem_scale:0:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xbc7:mem_disp:0:0x20253c:i64', 'imm_occurrence:0xbc7:mem_scale:0:0x1:i64']`
- PC `0xbcd`: `call 0x157a` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:70` function=`spectre_function`
  - call_target: `{'operand': '0x157a', 'resolved_symbol': 'pmu_uops_snap_after', 'call_kind': 'direct_call_symbol', 'display_target': 'pmu_uops_snap_after'}`
  - use_objects: `['imm_occurrence:0xbcd:operand_imm:0:0x157a:i64', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x18]']`
  - immediates: `['imm_occurrence:0xbcd:operand_imm:0:0x157a:i64']`
- PC `0xbd2`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xbd3`: `leave` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:71` function=`spectre_function`
  - instruction_semantic_tags: `['epilogue']`
  - use_objects: `['reg:rbp', 'reg:rsp', 'stack:[rbp-0x40]']`
  - def_objects: `['reg:rbp', 'reg:rip', 'reg:rsp']`
- PC `0xbd4`: `ret` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:71` function=`spectre_function`
  - use_objects: `['reg:rsp', 'stack:[rbp-0x38]']`
  - def_objects: `['reg:rip', 'reg:rsp']`
- PC `0xc0d`: `mov eax, dword ptr [rbp - 0x1c]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x1c]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc0d:mem_disp:1:0xffffffffffffffe4:i64', 'imm_occurrence:0xc0d:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc0d:mem_disp:1:0xffffffffffffffe4:i64', 'imm_occurrence:0xc0d:mem_scale:1:0x1:i64']`
- PC `0xc10`: `cdq` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:rdx', 'reg:rip']`
- PC `0xc11`: `shr edx, 0x1c` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc11:operand_imm:1:0x1c:i8', 'reg:rdx']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rdx', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xc11:operand_imm:1:0x1c:i8']`
- PC `0xc14`: `add eax, edx` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rdx']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0xc16`: `and eax, 0xf` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc16:operand_imm:1:0xf:i32', 'reg:rax']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xc16:operand_imm:1:0xf:i32']`
- PC `0xc19`: `sub eax, edx` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rdx']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0xc1b`: `cdqe` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:rax', 'reg:rip']`
- PC `0xc1d`: `mov qword ptr [rbp - 0x18], rax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x18]']`
  - addr_objects: `['imm_occurrence:0xc1d:mem_disp:0:0xffffffffffffffe8:i64', 'imm_occurrence:0xc1d:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc1d:mem_disp:0:0xffffffffffffffe8:i64', 'imm_occurrence:0xc1d:mem_scale:0:0x1:i64']`
- PC `0xc21`: `lea rax, [rip + 0x2023f8]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rip']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc21:mem_disp:1:0x2023f8:i64', 'imm_occurrence:0xc21:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc21:mem_disp:1:0x2023f8:i64', 'imm_occurrence:0xc21:mem_scale:1:0x1:i64']`
- PC `0xc28`: `mov qword ptr [rbp - 8], rax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x8]']`
  - addr_objects: `['imm_occurrence:0xc28:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xc28:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc28:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xc28:mem_scale:0:0x1:i64']`
- PC `0xc2c`: `mov rax, qword ptr [rbp - 8]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/usr/lib/gcc/x86_64-linux-gnu/7/include/emmintrin.h:1486` function=`_mm_clflush`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x8]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc2c:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xc2c:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc2c:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xc2c:mem_scale:1:0x1:i64']`
- PC `0xc30`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc33`: `mov dword ptr [rbp - 0x20], 0` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:95` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc33:operand_imm:1:0x0:i32', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x20]']`
  - addr_objects: `['imm_occurrence:0xc33:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xc33:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc33:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xc33:mem_scale:0:0x1:i64', 'imm_occurrence:0xc33:operand_imm:1:0x0:i32']`
- PC `0xc3a`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc3c`: `mov eax, dword ptr [rbp - 0x20]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x20]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc3c:mem_disp:1:0xffffffffffffffe0:i64', 'imm_occurrence:0xc3c:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc3c:mem_disp:1:0xffffffffffffffe0:i64', 'imm_occurrence:0xc3c:mem_scale:1:0x1:i64']`
- PC `0xc3f`: `add eax, 1` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc3f:operand_imm:1:0x1:i32', 'reg:rax']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xc3f:operand_imm:1:0x1:i32']`
- PC `0xc42`: `mov dword ptr [rbp - 0x20], eax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x20]']`
  - addr_objects: `['imm_occurrence:0xc42:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xc42:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc42:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xc42:mem_scale:0:0x1:i64']`
- PC `0xc45`: `mov eax, dword ptr [rbp - 0x20]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x20]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc45:mem_disp:1:0xffffffffffffffe0:i64', 'imm_occurrence:0xc45:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc45:mem_disp:1:0xffffffffffffffe0:i64', 'imm_occurrence:0xc45:mem_scale:1:0x1:i64']`
- PC `0xc48`: `cmp eax, 0xc7` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc48:operand_imm:1:0xc7:i32', 'reg:rax']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xc48:operand_imm:1:0xc7:i32']`
- PC `0xc4d`: `jle 0xc3c` groups=`['direct_operand', 'structural_role']` kinds=`['branch_condition', 'direct_immediate_occurrence', 'direct_use']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - instruction_semantic_tags: `['conditional_branch']`
  - use_objects: `['imm_occurrence:0xc4d:operand_imm:0:0xc3c:i64', 'reg:of', 'reg:sf', 'reg:zf']`
  - def_objects: `['reg:rip']`
  - immediates: `['imm_occurrence:0xc4d:operand_imm:0:0xc3c:i64']`
- PC `0xc4f`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc52`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc57`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc59`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc5b`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc5d`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc60`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc62`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc64`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc66`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc68`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc6a`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc6c`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc6e`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc71`: `mov ax, 0` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc71:operand_imm:1:0x0:i16']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - immediates: `['imm_occurrence:0xc71:operand_imm:1:0x0:i16']`
- PC `0xc75`: `cdqe` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:rax', 'reg:rip']`
- PC `0xc77`: `mov qword ptr [rbp - 0x10], rax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x10]']`
  - addr_objects: `['imm_occurrence:0xc77:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc77:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc77:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc77:mem_scale:0:0x1:i64']`
- PC `0xc7b`: `mov rax, qword ptr [rbp - 0x10]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc7b:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc7b:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc7b:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc7b:mem_scale:1:0x1:i64']`
- PC `0xc7f`: `shr rax, 0x10` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc7f:operand_imm:1:0x10:i8', 'reg:rax']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xc7f:operand_imm:1:0x10:i8']`
- PC `0xc83`: `or qword ptr [rbp - 0x10], rax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf', 'stack:[rbp-0x10]']`
  - addr_objects: `['imm_occurrence:0xc83:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc83:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc83:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc83:mem_scale:0:0x1:i64']`
- PC `0xc87`: `mov rax, qword ptr [rbp - 0x28]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x28]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc87:mem_disp:1:0xffffffffffffffd8:i64', 'imm_occurrence:0xc87:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc87:mem_disp:1:0xffffffffffffffd8:i64', 'imm_occurrence:0xc87:mem_scale:1:0x1:i64']`
- PC `0xc8b`: `xor rax, qword ptr [rbp - 0x18]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x18]']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xc8b:mem_disp:1:0xffffffffffffffe8:i64', 'imm_occurrence:0xc8b:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc8b:mem_disp:1:0xffffffffffffffe8:i64', 'imm_occurrence:0xc8b:mem_scale:1:0x1:i64']`
- PC `0xc8f`: `and rax, qword ptr [rbp - 0x10]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xc8f:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc8f:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc8f:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc8f:mem_scale:1:0x1:i64']`
- PC `0xc93`: `xor rax, qword ptr [rbp - 0x18]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x18]']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xc93:mem_disp:1:0xffffffffffffffe8:i64', 'imm_occurrence:0xc93:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc93:mem_disp:1:0xffffffffffffffe8:i64', 'imm_occurrence:0xc93:mem_scale:1:0x1:i64']`
- PC `0xc97`: `mov qword ptr [rbp - 0x10], rax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x10]']`
  - addr_objects: `['imm_occurrence:0xc97:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc97:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc97:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc97:mem_scale:0:0x1:i64']`
- PC `0xc9b`: `mov rax, qword ptr [rbp - 0x10]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc9b:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc9b:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc9b:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc9b:mem_scale:1:0x1:i64']`
- PC `0xc9f`: `mov rdi, rax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:rdi', 'reg:rip']`
- PC `0xca2`: `call 0xb7a` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - call_target: `{'operand': '0xb7a', 'resolved_symbol': 'spectre_function', 'call_kind': 'direct_call_symbol', 'display_target': 'spectre_function'}`
  - use_objects: `['imm_occurrence:0xca2:operand_imm:0:0xb7a:i64', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x38]']`
  - immediates: `['imm_occurrence:0xca2:operand_imm:0:0xb7a:i64']`
- PC `0xca7`: `sub dword ptr [rbp - 0x1c], 1` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xca7:operand_imm:1:0x1:i32', 'reg:rbp', 'stack:[rbp-0x1c]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf', 'stack:[rbp-0x1c]']`
  - addr_objects: `['imm_occurrence:0xca7:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xca7:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xca7:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xca7:mem_scale:0:0x1:i64', 'imm_occurrence:0xca7:operand_imm:1:0x1:i32']`
- PC `0xcab`: `cmp dword ptr [rbp - 0x1c], 0` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xcab:operand_imm:1:0x0:i32', 'reg:rbp', 'stack:[rbp-0x1c]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xcab:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xcab:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xcab:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xcab:mem_scale:0:0x1:i64', 'imm_occurrence:0xcab:operand_imm:1:0x0:i32']`
- PC `0xcaf`: `jns 0xc0d` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - instruction_semantic_tags: `['conditional_branch']`
  - use_objects: `['imm_occurrence:0xcaf:operand_imm:0:0xc0d:i64', 'reg:sf']`
  - def_objects: `['reg:rip']`
  - immediates: `['imm_occurrence:0xcaf:operand_imm:0:0xc0d:i64']`
- PC `0xcb5`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xcb6`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xcb7`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x150b`: `push rbp` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_before`
  - instruction_semantic_tags: `['callee_save_spill', 'prologue']`
  - use_objects: `['reg:rbp', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x20]']`
- PC `0x150c`: `mov rbp, rsp` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_before`
  - instruction_semantic_tags: `['prologue']`
  - use_objects: `['reg:rsp']`
  - def_objects: `['reg:rbp', 'reg:rip']`
- PC `0x150f`: `mov eax, dword ptr [rip + 0x20fc6f]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_before`
  - use_objects: `['reg:rip', 'var:uops_available']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0x150f:mem_disp:1:0x20fc6f:i64', 'imm_occurrence:0x150f:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0x150f:mem_disp:1:0x20fc6f:i64', 'imm_occurrence:0x150f:mem_scale:1:0x1:i64']`
- PC `0x1515`: `test eax, eax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_before`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0x1517`: `je 0x1577` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_before`
  - instruction_semantic_tags: `['conditional_branch']`
  - use_objects: `['imm_occurrence:0x1517:operand_imm:0:0x1577:i64', 'reg:zf']`
  - def_objects: `['reg:rip']`
  - immediates: `['imm_occurrence:0x1517:operand_imm:0:0x1577:i64']`
- PC `0x1577`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x1578`: `pop rbp` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_before`
  - instruction_semantic_tags: `['callee_save_restore', 'epilogue']`
  - use_objects: `['reg:rsp', 'stack:[rbp-0x20]']`
  - def_objects: `['reg:rbp', 'reg:rip', 'reg:rsp']`
- PC `0x1579`: `ret` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_before`
  - use_objects: `['reg:rsp', 'stack:[rbp-0x18]']`
  - def_objects: `['reg:rip', 'reg:rsp']`
- PC `0x157a`: `push rbp` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - instruction_semantic_tags: `['callee_save_spill', 'prologue']`
  - use_objects: `['reg:rbp', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x20]']`
- PC `0x157b`: `mov rbp, rsp` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - instruction_semantic_tags: `['prologue']`
  - use_objects: `['reg:rsp']`
  - def_objects: `['reg:rbp', 'reg:rip']`
- PC `0x157e`: `sub rsp, 0x20` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - instruction_semantic_tags: `['prologue']`
  - use_objects: `['imm_occurrence:0x157e:operand_imm:1:0x20:i64', 'reg:rsp']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0x157e:operand_imm:1:0x20:i64']`
- PC `0x1582`: `mov eax, dword ptr [rip + 0x20fbfc]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - use_objects: `['reg:rip', 'var:uops_available']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0x1582:mem_disp:1:0x20fbfc:i64', 'imm_occurrence:0x1582:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0x1582:mem_disp:1:0x20fbfc:i64', 'imm_occurrence:0x1582:mem_scale:1:0x1:i64']`
- PC `0x1588`: `test eax, eax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0x158a`: `je 0x168e` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - instruction_semantic_tags: `['conditional_branch']`
  - use_objects: `['imm_occurrence:0x158a:operand_imm:0:0x168e:i64', 'reg:zf']`
  - def_objects: `['reg:rip']`
  - immediates: `['imm_occurrence:0x158a:operand_imm:0:0x168e:i64']`
- PC `0x168e`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x168f`: `leave` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - instruction_semantic_tags: `['epilogue']`
  - use_objects: `['reg:rbp', 'reg:rsp', 'stack:[rbp-0x20]']`
  - def_objects: `['reg:rbp', 'reg:rip', 'reg:rsp']`
- PC `0x1690`: `ret` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - use_objects: `['reg:rsp', 'stack:[rbp-0x18]']`
  - def_objects: `['reg:rip', 'reg:rsp']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc08`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1519`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x151f`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x156e`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1575`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1590`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1596`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1686`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x168c`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xb7a`      b7a:	55                   	push   %rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0xb7b`      b7b:	48 89 e5             	mov    %rsp,%rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0xb7e`      b7e:	48 83 ec 10          	sub    $0x10,%rsp groups=`['structural_role']` kinds=`['branch_condition']`
- `0xb82`      b82:	48 89 7d f8          	mov    %rdi,-0x8(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xb86`      b86:	e8 80 09 00 00       	callq  150b <pmu_uops_snap_before> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xb8b`      b8b:	8b 05 8f 24 20 00    	mov    0x20248f(%rip),%eax        # 203020 <array1_size> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xb91`      b91:	89 c0                	mov    %eax,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xb93`      b93:	48 39 45 f8          	cmp    %rax,-0x8(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xb97`      b97:	73 34                	jae    bcd <STAGE1_END> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xb99`      b99:	48 8d 15 a0 24 20 00 	lea    0x2024a0(%rip),%rdx        # 203040 <array1> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xba0`      ba0:	48 8b 45 f8          	mov    -0x8(%rbp),%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xba4`      ba4:	48 01 d0             	add    %rdx,%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xba7`      ba7:	0f b6 00             	movzbl (%rax),%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbaa`      baa:	0f b6 c0             	movzbl %al,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbad`      bad:	c1 e0 09             	shl    $0x9,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbb0`      bb0:	48 63 d0             	movslq %eax,%rdx groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbb3`      bb3:	48 8d 05 06 07 21 00 	lea    0x210706(%rip),%rax        # 2112c0 <array2> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbba`      bba:	0f b6 14 02          	movzbl (%rdx,%rax,1),%edx groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbbe`      bbe:	0f b6 05 44 25 20 00 	movzbl 0x202544(%rip),%eax        # 203109 <temp> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbc5`      bc5:	21 d0                	and    %edx,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbc7`      bc7:	88 05 3c 25 20 00    	mov    %al,0x20253c(%rip)        # 203109 <temp> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbcd`      bcd:	e8 a8 09 00 00       	callq  157a <pmu_uops_snap_after> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbd2`      bd2:	90                   	nop groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbd3`      bd3:	c9                   	leaveq  groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbd4`      bd4:	c3                   	retq    groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc08`      c08:	e9 9e 00 00 00       	jmpq   cab <stage1_mistrain_trigger+0xb6> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc0d`      c0d:	8b 45 e4             	mov    -0x1c(%rbp),%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc10`      c10:	99                   	cltd    groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc11`      c11:	c1 ea 1c             	shr    $0x1c,%edx groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc14`      c14:	01 d0                	add    %edx,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc16`      c16:	83 e0 0f             	and    $0xf,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc19`      c19:	29 d0                	sub    %edx,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc1b`      c1b:	48 98                	cltq    groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc1d`      c1d:	48 89 45 e8          	mov    %rax,-0x18(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc21`      c21:	48 8d 05 f8 23 20 00 	lea    0x2023f8(%rip),%rax        # 203020 <array1_size> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc28`      c28:	48 89 45 f8          	mov    %rax,-0x8(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc2c`      c2c:	48 8b 45 f8          	mov    -0x8(%rbp),%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc30`      c30:	0f ae 38             	clflush (%rax) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc33`      c33:	c7 45 e0 00 00 00 00 	movl   $0x0,-0x20(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc3a`      c3a:	eb 09                	jmp    c45 <stage1_mistrain_trigger+0x50> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc3c`      c3c:	8b 45 e0             	mov    -0x20(%rbp),%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc3f`      c3f:	83 c0 01             	add    $0x1,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc42`      c42:	89 45 e0             	mov    %eax,-0x20(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc45`      c45:	8b 45 e0             	mov    -0x20(%rbp),%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc48`      c48:	3d c7 00 00 00       	cmp    $0xc7,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc4d`      c4d:	7e ed                	jle    c3c <stage1_mistrain_trigger+0x47> groups=`['direct_operand', 'structural_role']` kinds=`['branch_condition', 'direct_immediate_occurrence', 'direct_use']`
- `0xc4f`      c4f:	8b 4d e4             	mov    -0x1c(%rbp),%ecx groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc52`      c52:	ba ab aa aa 2a       	mov    $0x2aaaaaab,%edx groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc57`      c57:	89 c8                	mov    %ecx,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc59`      c59:	f7 ea                	imul   %edx groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc5b`      c5b:	89 c8                	mov    %ecx,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc5d`      c5d:	c1 f8 1f             	sar    $0x1f,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc60`      c60:	29 c2                	sub    %eax,%edx groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc62`      c62:	89 d0                	mov    %edx,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc64`      c64:	01 c0                	add    %eax,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc66`      c66:	01 d0                	add    %edx,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc68`      c68:	01 c0                	add    %eax,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc6a`      c6a:	29 c1                	sub    %eax,%ecx groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc6c`      c6c:	89 ca                	mov    %ecx,%edx groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc6e`      c6e:	8d 42 ff             	lea    -0x1(%rdx),%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc71`      c71:	66 b8 00 00          	mov    $0x0,%ax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc75`      c75:	48 98                	cltq    groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc77`      c77:	48 89 45 f0          	mov    %rax,-0x10(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc7b`      c7b:	48 8b 45 f0          	mov    -0x10(%rbp),%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc7f`      c7f:	48 c1 e8 10          	shr    $0x10,%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc83`      c83:	48 09 45 f0          	or     %rax,-0x10(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc87`      c87:	48 8b 45 d8          	mov    -0x28(%rbp),%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc8b`      c8b:	48 33 45 e8          	xor    -0x18(%rbp),%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc8f`      c8f:	48 23 45 f0          	and    -0x10(%rbp),%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc93`      c93:	48 33 45 e8          	xor    -0x18(%rbp),%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc97`      c97:	48 89 45 f0          	mov    %rax,-0x10(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc9b`      c9b:	48 8b 45 f0          	mov    -0x10(%rbp),%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc9f`      c9f:	48 89 c7             	mov    %rax,%rdi groups=`['structural_role']` kinds=`['branch_condition']`
- `0xca2`      ca2:	e8 d3 fe ff ff       	callq  b7a <spectre_function> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xca7`      ca7:	83 6d e4 01          	subl   $0x1,-0x1c(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xcab`      cab:	83 7d e4 00          	cmpl   $0x0,-0x1c(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xcaf`      caf:	0f 89 58 ff ff ff    	jns    c0d <stage1_mistrain_trigger+0x18> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xcb5`      cb5:	90                   	nop groups=`['structural_role']` kinds=`['branch_condition']`
- `0xcb6`      cb6:	c9                   	leaveq  groups=`['structural_role']` kinds=`['branch_condition']`
- `0xcb7`      cb7:	c3                   	retq    groups=`['structural_role']` kinds=`['branch_condition']`
- `0x150b`     150b:	55                   	push   %rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0x150c`     150c:	48 89 e5             	mov    %rsp,%rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0x150f`     150f:	8b 05 6f fc 20 00    	mov    0x20fc6f(%rip),%eax        # 211184 <uops_available> groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1515`     1515:	85 c0                	test   %eax,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1517`     1517:	74 5e                	je     1577 <pmu_uops_snap_before+0x6c> groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1519`     1519:	8b 05 41 3c 20 00    	mov    0x203c41(%rip),%eax        # 205160 <use_rdpmc> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x151f`     151f:	85 c0                	test   %eax,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x156e`     156e:	48 89 05 03 3c 20 00 	mov    %rax,0x203c03(%rip)        # 205178 <snap_retired> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1575`     1575:	eb 01                	jmp    1578 <pmu_uops_snap_before+0x6d> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1577`     1577:	90                   	nop groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1578`     1578:	5d                   	pop    %rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1579`     1579:	c3                   	retq    groups=`['structural_role']` kinds=`['branch_condition']`
- `0x157a`     157a:	55                   	push   %rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0x157b`     157b:	48 89 e5             	mov    %rsp,%rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0x157e`     157e:	48 83 ec 20          	sub    $0x20,%rsp groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1582`     1582:	8b 05 fc fb 20 00    	mov    0x20fbfc(%rip),%eax        # 211184 <uops_available> groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1588`     1588:	85 c0                	test   %eax,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0x158a`     158a:	0f 84 fe 00 00 00    	je     168e <pmu_uops_snap_after+0x114> groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1590`     1590:	8b 05 ca 3b 20 00    	mov    0x203bca(%rip),%eax        # 205160 <use_rdpmc> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1596`     1596:	85 c0                	test   %eax,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1686`     1686:	89 05 f4 fa 20 00    	mov    %eax,0x20faf4(%rip)        # 211180 <uops_cnt> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x168c`     168c:	eb 01                	jmp    168f <pmu_uops_snap_after+0x115> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x168e`     168e:	90                   	nop groups=`['structural_role']` kinds=`['branch_condition']`
- `0x168f`     168f:	c9                   	leaveq  groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1690`     1690:	c3                   	retq    groups=`['structural_role']` kinds=`['branch_condition']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:58` function=`spectre_function` pcs=`['0xb7a', '0xb7b', '0xb7e', '0xb82']` groups=`['structural_role']` kinds=`['branch_condition']`

```c
   56: ********************************************************************/
   57: __attribute__((noinline))
   58: void spectre_function(size_t x) {
   59: 
   60:   pmu_uops_snap_before();
```

- `/root/src/spectre_stage1_2_auto.c:60` function=`spectre_function` pcs=`['0xb86']` groups=`['structural_role']` kinds=`['branch_condition']`

```c
   58: void spectre_function(size_t x) {
   59: 
   60:   pmu_uops_snap_before();
   61: 
   62:   asm volatile(".globl STAGE1_BEGIN\nSTAGE1_BEGIN:");
```

- `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function` pcs=`['0xb8b', '0xb91', '0xb93', '0xb97']` groups=`['structural_role']` kinds=`['branch_condition']`

```c
   61: 
   62:   asm volatile(".globl STAGE1_BEGIN\nSTAGE1_BEGIN:");
   63:   if (x < array1_size) {
   64:     NOP_REGION_BEGIN
   65:     temp &= array2[array1[x] * 512];
```

- `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function` pcs=`['0xb99', '0xba0', '0xba4', '0xba7', '0xbaa', '0xbad', '0xbb0', '0xbb3', '0xbba', '0xbbe', '0xbc5', '0xbc7']` groups=`['structural_role']` kinds=`['branch_condition']`

```c
   63:   if (x < array1_size) {
   64:     NOP_REGION_BEGIN
   65:     temp &= array2[array1[x] * 512];
   66:     NOP_REGION_END
   67:   }
```

- `/root/src/spectre_stage1_2_auto.c:70` function=`spectre_function` pcs=`['0xbcd']` groups=`['structural_role']` kinds=`['branch_condition']`

```c
   68:   asm volatile(".globl STAGE1_END\nSTAGE1_END:");
   69: 
   70:   pmu_uops_snap_after();
   71: }
   72: 
```

- `/root/src/spectre_stage1_2_auto.c:71` function=`spectre_function` pcs=`['0xbd3', '0xbd4']` groups=`['structural_role']` kinds=`['branch_condition']`

```c
   69: 
   70:   pmu_uops_snap_after();
   71: }
   72: 
   73: /********************************************************************
```

- `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger` pcs=`['0xc0d', '0xc10', '0xc11', '0xc14', '0xc16', '0xc19', '0xc1b', '0xc1d', '0xc21', '0xc28']` groups=`['structural_role']` kinds=`['branch_condition']`

```c
   91: 
   92:     for (j = 29; j >= 0; j--) {
   93:         training_x = (size_t)(j % 16);
   94:         _mm_clflush(&array1_size);
   95:         for (volatile int z = 0; z < 200; z++) {}
```

- `/root/src/spectre_stage1_2_auto.c:95` function=`stage1_mistrain_trigger` pcs=`['0xc33']` groups=`['structural_role']` kinds=`['branch_condition']`

```c
   93:         training_x = (size_t)(j % 16);
   94:         _mm_clflush(&array1_size);
   95:         for (volatile int z = 0; z < 200; z++) {}
   96: 
   97:         x = ((j % 6) - 1) & ~0xFFFF;
```

- `/usr/lib/gcc/x86_64-linux-gnu/7/include/emmintrin.h:1486` function=`_mm_clflush` pcs=`['0xc2c']` groups=`['structural_role']` kinds=`['branch_condition']`

### 72. `imm_occurrence:0xc4f:mem_disp:1:0xffffffffffffffe4:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc4f:mem_disp:1:0xffffffffffffffe4/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc4f', 'operand_index': None, 'raw_suffix': 'mem_disp:1:0xffffffffffffffe4/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xc4f:mem_disp:1:0xffffffffffffffe4/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc4f']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `[]`
- structural_role_pcs: `['0xc4f']`
- anchor_pcs: `['0xc4f']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc52', '0xc57']`
- all_mapped_pcs: `['0xc4f', '0xc52', '0xc57']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x1c]']`

#### PC Relation Entries

- `0xc4f` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc52` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc57` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc4f`: `None` groups=`['structural_role']` kinds=`['address_component']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc52`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc57`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc4f`      c4f:	8b 4d e4             	mov    -0x1c(%rbp),%ecx groups=`['structural_role']` kinds=`['address_component']`
- `0xc52`      c52:	ba ab aa aa 2a       	mov    $0x2aaaaaab,%edx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc57`      c57:	89 c8                	mov    %ecx,%eax groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 73. `imm_occurrence:0xc4f:mem_scale:1:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc4f:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc4f', 'operand_index': None, 'raw_suffix': 'mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xc4f:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc4f']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `[]`
- structural_role_pcs: `['0xc4f']`
- anchor_pcs: `['0xc4f']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc52', '0xc57']`
- all_mapped_pcs: `['0xc4f', '0xc52', '0xc57']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x1c]']`

#### PC Relation Entries

- `0xc4f` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc52` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc57` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc4f`: `None` groups=`['structural_role']` kinds=`['address_component']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc52`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc57`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc4f`      c4f:	8b 4d e4             	mov    -0x1c(%rbp),%ecx groups=`['structural_role']` kinds=`['address_component']`
- `0xc52`      c52:	ba ab aa aa 2a       	mov    $0x2aaaaaab,%edx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc57`      c57:	89 c8                	mov    %ecx,%eax groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 74. `imm_occurrence:0xc52:operand_imm:1:0x2aaaaaab:i32`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc52:operand_imm:1:0x2aaaaaab/i32`
- Mapping kind: `constant_or_address_component`
- Confidence: `structural`
- Object semantic tags: `[]`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc52', 'operand_index': None, 'raw_suffix': 'operand_imm:1:0x2aaaaaab/i32'}`
- Reason: 对象类型为 imm，更适合作为常量、位移、scale、比较值或地址组成部分解释。
- Candidate program elements: `['imm@0xc52:operand_imm:1:0x2aaaaaab/i32']`
- direct_use_pcs: `['0xc52']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `['0xc52']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xc52']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc4f', '0xc57', '0xc59']`
- all_mapped_pcs: `['0xc4f', '0xc52', '0xc57', '0xc59']`
- direct_parents: `[]`
- direct_children: `['reg:rdx', 'reg:rip']`

#### PC Relation Entries

- `0xc4f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc52` kinds=`['direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['object_detail.used_by/instruction_details.use_objects']`
- `0xc57` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc59` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc52`: `None` groups=`['direct_operand']` kinds=`['direct_use']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc4f`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc57`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc59`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc4f`      c4f:	8b 4d e4             	mov    -0x1c(%rbp),%ecx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc52`      c52:	ba ab aa aa 2a       	mov    $0x2aaaaaab,%edx groups=`['direct_operand']` kinds=`['direct_use']`
- `0xc57`      c57:	89 c8                	mov    %ecx,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc59`      c59:	f7 ea                	imul   %edx groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 75. `imm_occurrence:0xc5d:operand_imm:1:0x1f:i8`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc5d:operand_imm:1:0x1f/i8`
- Mapping kind: `constant_or_address_component`
- Confidence: `structural`
- Object semantic tags: `[]`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc5d', 'operand_index': None, 'raw_suffix': 'operand_imm:1:0x1f/i8'}`
- Reason: 对象类型为 imm，更适合作为常量、位移、scale、比较值或地址组成部分解释。
- Candidate program elements: `['imm@0xc5d:operand_imm:1:0x1f/i8']`
- direct_use_pcs: `['0xc5d']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `['0xc5d']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xc5d']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc59', '0xc5b', '0xc60', '0xc62']`
- all_mapped_pcs: `['0xc59', '0xc5b', '0xc5d', '0xc60', '0xc62']`
- direct_parents: `[]`
- direct_children: `['reg:cf', 'reg:of', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`

#### PC Relation Entries

- `0xc59` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc5b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc5d` kinds=`['direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['object_detail.used_by/instruction_details.use_objects']`
- `0xc60` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc62` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc5d`: `None` groups=`['direct_operand']` kinds=`['direct_use']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc59`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc5b`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc60`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc62`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc59`      c59:	f7 ea                	imul   %edx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc5b`      c5b:	89 c8                	mov    %ecx,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc5d`      c5d:	c1 f8 1f             	sar    $0x1f,%eax groups=`['direct_operand']` kinds=`['direct_use']`
- `0xc60`      c60:	29 c2                	sub    %eax,%edx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc62`      c62:	89 d0                	mov    %edx,%eax groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 76. `imm_occurrence:0xc71:operand_imm:1:0x0:i16`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc71:operand_imm:1:0x0/i16`
- Mapping kind: `constant_or_address_component`
- Confidence: `structural`
- Object semantic tags: `[]`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc71', 'operand_index': None, 'raw_suffix': 'operand_imm:1:0x0/i16'}`
- Reason: 对象类型为 imm，更适合作为常量、位移、scale、比较值或地址组成部分解释。
- Candidate program elements: `['imm@0xc71:operand_imm:1:0x0/i16']`
- direct_use_pcs: `['0xc71']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc71']`
- direct_operand_pcs: `['0xc71']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xc71']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc6c', '0xc6e', '0xc75', '0xc77']`
- all_mapped_pcs: `['0xc6c', '0xc6e', '0xc71', '0xc75', '0xc77']`
- direct_parents: `[]`
- direct_children: `['reg:rax', 'reg:rip']`

#### PC Relation Entries

- `0xc6c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc6e` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc71` kinds=`['direct_immediate_occurrence', 'direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.used_by/instruction_details.use_objects']`
- `0xc75` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc77` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc71`: `mov ax, 0` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc71:operand_imm:1:0x0:i16']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - immediates: `['imm_occurrence:0xc71:operand_imm:1:0x0:i16']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc6c`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc6e`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc75`: `cdqe` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc77`: `mov qword ptr [rbp - 0x10], rax` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc6c`      c6c:	89 ca                	mov    %ecx,%edx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc6e`      c6e:	8d 42 ff             	lea    -0x1(%rdx),%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc71`      c71:	66 b8 00 00          	mov    $0x0,%ax groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
- `0xc75`      c75:	48 98                	cltq    groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc77`      c77:	48 89 45 f0          	mov    %rax,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 77. `imm_occurrence:0xc77:mem_disp:0:0xfffffffffffffff0:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc77:mem_disp:0:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc77', 'operand_index': None, 'raw_suffix': 'mem_disp:0:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xc77:mem_disp:0:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc77']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc77']`
- direct_operand_pcs: `['0xc77']`
- structural_role_pcs: `['0xc77']`
- anchor_pcs: `['0xc77']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc71', '0xc75', '0xc7b']`
- all_mapped_pcs: `['0xc71', '0xc75', '0xc77', '0xc7b']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x10]']`

#### PC Relation Entries

- `0xc71` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc75` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc77` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc7b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc77`: `mov qword ptr [rbp - 0x10], rax` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x10]']`
  - addr_objects: `['imm_occurrence:0xc77:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc77:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc77:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc77:mem_scale:0:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc71`: `mov ax, 0` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc75`: `cdqe` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc7b`: `mov rax, qword ptr [rbp - 0x10]` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc71`      c71:	66 b8 00 00          	mov    $0x0,%ax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc75`      c75:	48 98                	cltq    groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc77`      c77:	48 89 45 f0          	mov    %rax,-0x10(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc7b`      c7b:	48 8b 45 f0          	mov    -0x10(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 78. `imm_occurrence:0xc77:mem_scale:0:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc77:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc77', 'operand_index': None, 'raw_suffix': 'mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xc77:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc77']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc77']`
- direct_operand_pcs: `['0xc77']`
- structural_role_pcs: `['0xc77']`
- anchor_pcs: `['0xc77']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc71', '0xc75', '0xc7b']`
- all_mapped_pcs: `['0xc71', '0xc75', '0xc77', '0xc7b']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x10]']`

#### PC Relation Entries

- `0xc71` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc75` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc77` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc7b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc77`: `mov qword ptr [rbp - 0x10], rax` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x10]']`
  - addr_objects: `['imm_occurrence:0xc77:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc77:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc77:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc77:mem_scale:0:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc71`: `mov ax, 0` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc75`: `cdqe` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc7b`: `mov rax, qword ptr [rbp - 0x10]` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc71`      c71:	66 b8 00 00          	mov    $0x0,%ax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc75`      c75:	48 98                	cltq    groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc77`      c77:	48 89 45 f0          	mov    %rax,-0x10(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc7b`      c7b:	48 8b 45 f0          	mov    -0x10(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 79. `imm_occurrence:0xc7b:mem_disp:1:0xfffffffffffffff0:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc7b:mem_disp:1:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc7b', 'operand_index': None, 'raw_suffix': 'mem_disp:1:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xc7b:mem_disp:1:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc7b']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc7b']`
- direct_operand_pcs: `['0xc7b']`
- structural_role_pcs: `['0xc7b']`
- anchor_pcs: `['0xc7b']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc77', '0xc7f', '0xc83']`
- all_mapped_pcs: `['0xc77', '0xc7b', '0xc7f', '0xc83']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x10]']`

#### PC Relation Entries

- `0xc77` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc7b` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc7f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc83` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc7b`: `mov rax, qword ptr [rbp - 0x10]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc7b:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc7b:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc7b:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc7b:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc77`: `mov qword ptr [rbp - 0x10], rax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc7f`: `shr rax, 0x10` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc83`: `or qword ptr [rbp - 0x10], rax` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc77`      c77:	48 89 45 f0          	mov    %rax,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc7b`      c7b:	48 8b 45 f0          	mov    -0x10(%rbp),%rax groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc7f`      c7f:	48 c1 e8 10          	shr    $0x10,%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc83`      c83:	48 09 45 f0          	or     %rax,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 80. `imm_occurrence:0xc7b:mem_scale:1:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc7b:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc7b', 'operand_index': None, 'raw_suffix': 'mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xc7b:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc7b']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc7b']`
- direct_operand_pcs: `['0xc7b']`
- structural_role_pcs: `['0xc7b']`
- anchor_pcs: `['0xc7b']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc77', '0xc7f', '0xc83']`
- all_mapped_pcs: `['0xc77', '0xc7b', '0xc7f', '0xc83']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x10]']`

#### PC Relation Entries

- `0xc77` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc7b` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc7f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc83` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc7b`: `mov rax, qword ptr [rbp - 0x10]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc7b:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc7b:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc7b:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc7b:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc77`: `mov qword ptr [rbp - 0x10], rax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc7f`: `shr rax, 0x10` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc83`: `or qword ptr [rbp - 0x10], rax` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc77`      c77:	48 89 45 f0          	mov    %rax,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc7b`      c7b:	48 8b 45 f0          	mov    -0x10(%rbp),%rax groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc7f`      c7f:	48 c1 e8 10          	shr    $0x10,%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc83`      c83:	48 09 45 f0          	or     %rax,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 81. `imm_occurrence:0xc7f:operand_imm:1:0x10:i8`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc7f:operand_imm:1:0x10/i8`
- Mapping kind: `constant_or_address_component`
- Confidence: `structural`
- Object semantic tags: `[]`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc7f', 'operand_index': None, 'raw_suffix': 'operand_imm:1:0x10/i8'}`
- Reason: 对象类型为 imm，更适合作为常量、位移、scale、比较值或地址组成部分解释。
- Candidate program elements: `['imm@0xc7f:operand_imm:1:0x10/i8']`
- direct_use_pcs: `['0xc7f']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc7f']`
- direct_operand_pcs: `['0xc7f']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xc7f']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc7b', '0xc83']`
- all_mapped_pcs: `['0xc7b', '0xc7f', '0xc83']`
- direct_parents: `[]`
- direct_children: `['reg:cf', 'reg:of', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`

#### PC Relation Entries

- `0xc7b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc7f` kinds=`['direct_immediate_occurrence', 'direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.used_by/instruction_details.use_objects']`
- `0xc83` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc7f`: `shr rax, 0x10` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc7f:operand_imm:1:0x10:i8', 'reg:rax']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xc7f:operand_imm:1:0x10:i8']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc7b`: `mov rax, qword ptr [rbp - 0x10]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc83`: `or qword ptr [rbp - 0x10], rax` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc7b`      c7b:	48 8b 45 f0          	mov    -0x10(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc7f`      c7f:	48 c1 e8 10          	shr    $0x10,%rax groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
- `0xc83`      c83:	48 09 45 f0          	or     %rax,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 82. `imm_occurrence:0xc83:mem_disp:0:0xfffffffffffffff0:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc83:mem_disp:0:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc83', 'operand_index': None, 'raw_suffix': 'mem_disp:0:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xc83:mem_disp:0:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc83']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc83']`
- direct_operand_pcs: `['0xc83']`
- structural_role_pcs: `['0xc83']`
- anchor_pcs: `['0xc83']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc7b', '0xc7f', '0xc87']`
- all_mapped_pcs: `['0xc7b', '0xc7f', '0xc83', '0xc87']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x10]']`

#### PC Relation Entries

- `0xc7b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc7f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc83` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc87` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc83`: `or qword ptr [rbp - 0x10], rax` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf', 'stack:[rbp-0x10]']`
  - addr_objects: `['imm_occurrence:0xc83:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc83:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc83:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc83:mem_scale:0:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc7b`: `mov rax, qword ptr [rbp - 0x10]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc7f`: `shr rax, 0x10` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc87`: `mov rax, qword ptr [rbp - 0x28]` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc7b`      c7b:	48 8b 45 f0          	mov    -0x10(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc7f`      c7f:	48 c1 e8 10          	shr    $0x10,%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc83`      c83:	48 09 45 f0          	or     %rax,-0x10(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc87`      c87:	48 8b 45 d8          	mov    -0x28(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 83. `imm_occurrence:0xc83:mem_scale:0:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc83:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc83', 'operand_index': None, 'raw_suffix': 'mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xc83:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc83']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc83']`
- direct_operand_pcs: `['0xc83']`
- structural_role_pcs: `['0xc83']`
- anchor_pcs: `['0xc83']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc7b', '0xc7f', '0xc87']`
- all_mapped_pcs: `['0xc7b', '0xc7f', '0xc83', '0xc87']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x10]']`

#### PC Relation Entries

- `0xc7b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc7f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc83` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc87` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc83`: `or qword ptr [rbp - 0x10], rax` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf', 'stack:[rbp-0x10]']`
  - addr_objects: `['imm_occurrence:0xc83:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc83:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc83:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc83:mem_scale:0:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc7b`: `mov rax, qword ptr [rbp - 0x10]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc7f`: `shr rax, 0x10` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc87`: `mov rax, qword ptr [rbp - 0x28]` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc7b`      c7b:	48 8b 45 f0          	mov    -0x10(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc7f`      c7f:	48 c1 e8 10          	shr    $0x10,%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc83`      c83:	48 09 45 f0          	or     %rax,-0x10(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc87`      c87:	48 8b 45 d8          	mov    -0x28(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 84. `imm_occurrence:0xc87:mem_disp:1:0xffffffffffffffd8:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc87:mem_disp:1:0xffffffffffffffd8/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc87', 'operand_index': None, 'raw_suffix': 'mem_disp:1:0xffffffffffffffd8/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xc87:mem_disp:1:0xffffffffffffffd8/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc87']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc87']`
- direct_operand_pcs: `['0xc87']`
- structural_role_pcs: `['0xc87']`
- anchor_pcs: `['0xc87']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc83', '0xc8b', '0xc8f']`
- all_mapped_pcs: `['0xc83', '0xc87', '0xc8b', '0xc8f']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x28]']`

#### PC Relation Entries

- `0xc83` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc87` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc8b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc8f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc87`: `mov rax, qword ptr [rbp - 0x28]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x28]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc87:mem_disp:1:0xffffffffffffffd8:i64', 'imm_occurrence:0xc87:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc87:mem_disp:1:0xffffffffffffffd8:i64', 'imm_occurrence:0xc87:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc83`: `or qword ptr [rbp - 0x10], rax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc8b`: `xor rax, qword ptr [rbp - 0x18]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc8f`: `and rax, qword ptr [rbp - 0x10]` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc83`      c83:	48 09 45 f0          	or     %rax,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc87`      c87:	48 8b 45 d8          	mov    -0x28(%rbp),%rax groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc8b`      c8b:	48 33 45 e8          	xor    -0x18(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc8f`      c8f:	48 23 45 f0          	and    -0x10(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 85. `imm_occurrence:0xc87:mem_scale:1:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc87:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc87', 'operand_index': None, 'raw_suffix': 'mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xc87:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc87']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc87']`
- direct_operand_pcs: `['0xc87']`
- structural_role_pcs: `['0xc87']`
- anchor_pcs: `['0xc87']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc83', '0xc8b', '0xc8f']`
- all_mapped_pcs: `['0xc83', '0xc87', '0xc8b', '0xc8f']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x28]']`

#### PC Relation Entries

- `0xc83` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc87` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc8b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc8f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc87`: `mov rax, qword ptr [rbp - 0x28]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x28]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc87:mem_disp:1:0xffffffffffffffd8:i64', 'imm_occurrence:0xc87:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc87:mem_disp:1:0xffffffffffffffd8:i64', 'imm_occurrence:0xc87:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc83`: `or qword ptr [rbp - 0x10], rax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc8b`: `xor rax, qword ptr [rbp - 0x18]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc8f`: `and rax, qword ptr [rbp - 0x10]` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc83`      c83:	48 09 45 f0          	or     %rax,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc87`      c87:	48 8b 45 d8          	mov    -0x28(%rbp),%rax groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc8b`      c8b:	48 33 45 e8          	xor    -0x18(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc8f`      c8f:	48 23 45 f0          	and    -0x10(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 86. `imm_occurrence:0xc8b:mem_disp:1:0xffffffffffffffe8:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc8b:mem_disp:1:0xffffffffffffffe8/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc8b', 'operand_index': None, 'raw_suffix': 'mem_disp:1:0xffffffffffffffe8/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xc8b:mem_disp:1:0xffffffffffffffe8/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc8b']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc8b']`
- direct_operand_pcs: `['0xc8b']`
- structural_role_pcs: `['0xc8b']`
- anchor_pcs: `['0xc8b']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc87', '0xc8f', '0xc93']`
- all_mapped_pcs: `['0xc87', '0xc8b', '0xc8f', '0xc93']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x18]']`

#### PC Relation Entries

- `0xc87` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc8b` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc8f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc93` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc8b`: `xor rax, qword ptr [rbp - 0x18]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x18]']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xc8b:mem_disp:1:0xffffffffffffffe8:i64', 'imm_occurrence:0xc8b:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc8b:mem_disp:1:0xffffffffffffffe8:i64', 'imm_occurrence:0xc8b:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc87`: `mov rax, qword ptr [rbp - 0x28]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc8f`: `and rax, qword ptr [rbp - 0x10]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc93`: `xor rax, qword ptr [rbp - 0x18]` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc87`      c87:	48 8b 45 d8          	mov    -0x28(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc8b`      c8b:	48 33 45 e8          	xor    -0x18(%rbp),%rax groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc8f`      c8f:	48 23 45 f0          	and    -0x10(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc93`      c93:	48 33 45 e8          	xor    -0x18(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 87. `imm_occurrence:0xc8b:mem_scale:1:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc8b:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc8b', 'operand_index': None, 'raw_suffix': 'mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xc8b:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc8b']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc8b']`
- direct_operand_pcs: `['0xc8b']`
- structural_role_pcs: `['0xc8b']`
- anchor_pcs: `['0xc8b']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc87', '0xc8f', '0xc93']`
- all_mapped_pcs: `['0xc87', '0xc8b', '0xc8f', '0xc93']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x18]']`

#### PC Relation Entries

- `0xc87` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc8b` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc8f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc93` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc8b`: `xor rax, qword ptr [rbp - 0x18]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x18]']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xc8b:mem_disp:1:0xffffffffffffffe8:i64', 'imm_occurrence:0xc8b:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc8b:mem_disp:1:0xffffffffffffffe8:i64', 'imm_occurrence:0xc8b:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc87`: `mov rax, qword ptr [rbp - 0x28]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc8f`: `and rax, qword ptr [rbp - 0x10]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc93`: `xor rax, qword ptr [rbp - 0x18]` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc87`      c87:	48 8b 45 d8          	mov    -0x28(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc8b`      c8b:	48 33 45 e8          	xor    -0x18(%rbp),%rax groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc8f`      c8f:	48 23 45 f0          	and    -0x10(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc93`      c93:	48 33 45 e8          	xor    -0x18(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 88. `imm_occurrence:0xc8f:mem_disp:1:0xfffffffffffffff0:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc8f:mem_disp:1:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc8f', 'operand_index': None, 'raw_suffix': 'mem_disp:1:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xc8f:mem_disp:1:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc8f']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc8f']`
- direct_operand_pcs: `['0xc8f']`
- structural_role_pcs: `['0xc8f']`
- anchor_pcs: `['0xc8f']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc87', '0xc8b', '0xc93', '0xc97']`
- all_mapped_pcs: `['0xc87', '0xc8b', '0xc8f', '0xc93', '0xc97']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x10]']`

#### PC Relation Entries

- `0xc87` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc8b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc8f` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc93` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc97` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc8f`: `and rax, qword ptr [rbp - 0x10]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xc8f:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc8f:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc8f:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc8f:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc87`: `mov rax, qword ptr [rbp - 0x28]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc8b`: `xor rax, qword ptr [rbp - 0x18]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc93`: `xor rax, qword ptr [rbp - 0x18]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc97`: `mov qword ptr [rbp - 0x10], rax` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc87`      c87:	48 8b 45 d8          	mov    -0x28(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc8b`      c8b:	48 33 45 e8          	xor    -0x18(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc8f`      c8f:	48 23 45 f0          	and    -0x10(%rbp),%rax groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc93`      c93:	48 33 45 e8          	xor    -0x18(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc97`      c97:	48 89 45 f0          	mov    %rax,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 89. `imm_occurrence:0xc8f:mem_scale:1:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc8f:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc8f', 'operand_index': None, 'raw_suffix': 'mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xc8f:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc8f']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc8f']`
- direct_operand_pcs: `['0xc8f']`
- structural_role_pcs: `['0xc8f']`
- anchor_pcs: `['0xc8f']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc87', '0xc8b', '0xc93', '0xc97']`
- all_mapped_pcs: `['0xc87', '0xc8b', '0xc8f', '0xc93', '0xc97']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x10]']`

#### PC Relation Entries

- `0xc87` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc8b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc8f` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc93` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc97` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc8f`: `and rax, qword ptr [rbp - 0x10]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xc8f:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc8f:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc8f:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc8f:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc87`: `mov rax, qword ptr [rbp - 0x28]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc8b`: `xor rax, qword ptr [rbp - 0x18]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc93`: `xor rax, qword ptr [rbp - 0x18]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc97`: `mov qword ptr [rbp - 0x10], rax` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc87`      c87:	48 8b 45 d8          	mov    -0x28(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc8b`      c8b:	48 33 45 e8          	xor    -0x18(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc8f`      c8f:	48 23 45 f0          	and    -0x10(%rbp),%rax groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc93`      c93:	48 33 45 e8          	xor    -0x18(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc97`      c97:	48 89 45 f0          	mov    %rax,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 90. `imm_occurrence:0xc93:mem_disp:1:0xffffffffffffffe8:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc93:mem_disp:1:0xffffffffffffffe8/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc93', 'operand_index': None, 'raw_suffix': 'mem_disp:1:0xffffffffffffffe8/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xc93:mem_disp:1:0xffffffffffffffe8/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc93']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc93']`
- direct_operand_pcs: `['0xc93']`
- structural_role_pcs: `['0xc93']`
- anchor_pcs: `['0xc93']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc8b', '0xc8f', '0xc97']`
- all_mapped_pcs: `['0xc8b', '0xc8f', '0xc93', '0xc97']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x18]']`

#### PC Relation Entries

- `0xc8b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc8f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc93` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc97` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc93`: `xor rax, qword ptr [rbp - 0x18]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x18]']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xc93:mem_disp:1:0xffffffffffffffe8:i64', 'imm_occurrence:0xc93:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc93:mem_disp:1:0xffffffffffffffe8:i64', 'imm_occurrence:0xc93:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc8b`: `xor rax, qword ptr [rbp - 0x18]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc8f`: `and rax, qword ptr [rbp - 0x10]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc97`: `mov qword ptr [rbp - 0x10], rax` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc8b`      c8b:	48 33 45 e8          	xor    -0x18(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc8f`      c8f:	48 23 45 f0          	and    -0x10(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc93`      c93:	48 33 45 e8          	xor    -0x18(%rbp),%rax groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc97`      c97:	48 89 45 f0          	mov    %rax,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 91. `imm_occurrence:0xc93:mem_scale:1:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc93:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc93', 'operand_index': None, 'raw_suffix': 'mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xc93:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc93']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc93']`
- direct_operand_pcs: `['0xc93']`
- structural_role_pcs: `['0xc93']`
- anchor_pcs: `['0xc93']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc8b', '0xc8f', '0xc97']`
- all_mapped_pcs: `['0xc8b', '0xc8f', '0xc93', '0xc97']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x18]']`

#### PC Relation Entries

- `0xc8b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc8f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc93` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc97` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc93`: `xor rax, qword ptr [rbp - 0x18]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x18]']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xc93:mem_disp:1:0xffffffffffffffe8:i64', 'imm_occurrence:0xc93:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc93:mem_disp:1:0xffffffffffffffe8:i64', 'imm_occurrence:0xc93:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc8b`: `xor rax, qword ptr [rbp - 0x18]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc8f`: `and rax, qword ptr [rbp - 0x10]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc97`: `mov qword ptr [rbp - 0x10], rax` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc8b`      c8b:	48 33 45 e8          	xor    -0x18(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc8f`      c8f:	48 23 45 f0          	and    -0x10(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc93`      c93:	48 33 45 e8          	xor    -0x18(%rbp),%rax groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc97`      c97:	48 89 45 f0          	mov    %rax,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 92. `imm_occurrence:0xc97:mem_disp:0:0xfffffffffffffff0:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc97:mem_disp:0:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc97', 'operand_index': None, 'raw_suffix': 'mem_disp:0:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xc97:mem_disp:0:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc97']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc97']`
- direct_operand_pcs: `['0xc97']`
- structural_role_pcs: `['0xc97']`
- anchor_pcs: `['0xc97']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc8f', '0xc93']`
- all_mapped_pcs: `['0xc8f', '0xc93', '0xc97']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x10]']`

#### PC Relation Entries

- `0xc8f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc93` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc97` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`

#### Direct Anchor Instruction Evidence

- PC `0xc97`: `mov qword ptr [rbp - 0x10], rax` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x10]']`
  - addr_objects: `['imm_occurrence:0xc97:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc97:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc97:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc97:mem_scale:0:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc8f`: `and rax, qword ptr [rbp - 0x10]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc93`: `xor rax, qword ptr [rbp - 0x18]` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc8f`      c8f:	48 23 45 f0          	and    -0x10(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc93`      c93:	48 33 45 e8          	xor    -0x18(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc97`      c97:	48 89 45 f0          	mov    %rax,-0x10(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`

#### Source Evidence

_No source evidence found._

### 93. `imm_occurrence:0xc97:mem_scale:0:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc97:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc97', 'operand_index': None, 'raw_suffix': 'mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xc97:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc97']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc97']`
- direct_operand_pcs: `['0xc97']`
- structural_role_pcs: `['0xc97']`
- anchor_pcs: `['0xc97']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc8f', '0xc93']`
- all_mapped_pcs: `['0xc8f', '0xc93', '0xc97']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x10]']`

#### PC Relation Entries

- `0xc8f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc93` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc97` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`

#### Direct Anchor Instruction Evidence

- PC `0xc97`: `mov qword ptr [rbp - 0x10], rax` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x10]']`
  - addr_objects: `['imm_occurrence:0xc97:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc97:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc97:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc97:mem_scale:0:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc8f`: `and rax, qword ptr [rbp - 0x10]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc93`: `xor rax, qword ptr [rbp - 0x18]` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc8f`      c8f:	48 23 45 f0          	and    -0x10(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc93`      c93:	48 33 45 e8          	xor    -0x18(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc97`      c97:	48 89 45 f0          	mov    %rax,-0x10(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`

#### Source Evidence

_No source evidence found._

### 94. `imm_occurrence:0xc9b:mem_disp:1:0xfffffffffffffff0:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc9b:mem_disp:1:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc9b', 'operand_index': None, 'raw_suffix': 'mem_disp:1:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xc9b:mem_disp:1:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc9b']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc9b']`
- direct_operand_pcs: `['0xc9b']`
- structural_role_pcs: `['0xc9b']`
- anchor_pcs: `['0xc9b']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc9f', '0xca2']`
- all_mapped_pcs: `['0xc9b', '0xc9f', '0xca2']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x10]']`

#### PC Relation Entries

- `0xc9b` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc9f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xca2` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc9b`: `mov rax, qword ptr [rbp - 0x10]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc9b:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc9b:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc9b:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc9b:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc9f`: `mov rdi, rax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xca2`: `call 0xb7a` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc9b`      c9b:	48 8b 45 f0          	mov    -0x10(%rbp),%rax groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc9f`      c9f:	48 89 c7             	mov    %rax,%rdi groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xca2`      ca2:	e8 d3 fe ff ff       	callq  b7a <spectre_function> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 95. `imm_occurrence:0xc9b:mem_scale:1:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xc9b:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xc9b', 'operand_index': None, 'raw_suffix': 'mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xc9b:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xc9b']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xc9b']`
- direct_operand_pcs: `['0xc9b']`
- structural_role_pcs: `['0xc9b']`
- anchor_pcs: `['0xc9b']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc9f', '0xca2']`
- all_mapped_pcs: `['0xc9b', '0xc9f', '0xca2']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x10]']`

#### PC Relation Entries

- `0xc9b` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc9f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xca2` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xc9b`: `mov rax, qword ptr [rbp - 0x10]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc9b:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc9b:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc9b:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc9b:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc9f`: `mov rdi, rax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xca2`: `call 0xb7a` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc9b`      c9b:	48 8b 45 f0          	mov    -0x10(%rbp),%rax groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xc9f`      c9f:	48 89 c7             	mov    %rax,%rdi groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xca2`      ca2:	e8 d3 fe ff ff       	callq  b7a <spectre_function> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 96. `imm_occurrence:0xca2:operand_imm:0:0xb7a:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xca2:operand_imm:0:0xb7a/i64 [call_target_constant|program_semantic_constant|store_constant]`
- Mapping kind: `store_constant`
- Confidence: `semantic`
- Object semantic tags: `['call_target_constant', 'program_semantic_constant', 'store_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xca2', 'operand_index': None, 'raw_suffix': 'operand_imm:0:0xb7a/i64 [call_target_constant|program_semantic_constant|store_constant]'}`
- Reason: 该 immediate 带有 store_constant 标签，更适合作为写入值常量解释。
- Candidate program elements: `['imm@0xca2:operand_imm:0:0xb7a/i64 [call_target_constant|program_semantic_constant|store_constant]']`
- direct_use_pcs: `['0xca2']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xca2']`
- direct_operand_pcs: `['0xca2']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xca2']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc9b', '0xc9f', '0xca7']`
- all_mapped_pcs: `['0xc9b', '0xc9f', '0xca2', '0xca7']`
- direct_parents: `[]`
- direct_children: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x38]']`

#### PC Relation Entries

- `0xc9b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc9f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xca2` kinds=`['direct_immediate_occurrence', 'direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.used_by/instruction_details.use_objects']`
- `0xca7` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xca2`: `call 0xb7a` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - call_target: `{'operand': '0xb7a', 'resolved_symbol': 'spectre_function', 'call_kind': 'direct_call_symbol', 'display_target': 'spectre_function'}`
  - use_objects: `['imm_occurrence:0xca2:operand_imm:0:0xb7a:i64', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x38]']`
  - immediates: `['imm_occurrence:0xca2:operand_imm:0:0xb7a:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc9b`: `mov rax, qword ptr [rbp - 0x10]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc9f`: `mov rdi, rax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xca7`: `sub dword ptr [rbp - 0x1c], 1` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xc9b`      c9b:	48 8b 45 f0          	mov    -0x10(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc9f`      c9f:	48 89 c7             	mov    %rax,%rdi groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xca2`      ca2:	e8 d3 fe ff ff       	callq  b7a <spectre_function> groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
- `0xca7`      ca7:	83 6d e4 01          	subl   $0x1,-0x1c(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 97. `imm_occurrence:0xca7:mem_disp:0:0xffffffffffffffe4:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xca7:mem_disp:0:0xffffffffffffffe4/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xca7', 'operand_index': None, 'raw_suffix': 'mem_disp:0:0xffffffffffffffe4/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xca7:mem_disp:0:0xffffffffffffffe4/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xca7']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xca7']`
- direct_operand_pcs: `['0xca7']`
- structural_role_pcs: `['0xca7']`
- anchor_pcs: `['0xca7']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xca2', '0xcab', '0xcaf']`
- all_mapped_pcs: `['0xca2', '0xca7', '0xcab', '0xcaf']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x1c]']`

#### PC Relation Entries

- `0xca2` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xca7` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xcab` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xcaf` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xca7`: `sub dword ptr [rbp - 0x1c], 1` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xca7:operand_imm:1:0x1:i32', 'reg:rbp', 'stack:[rbp-0x1c]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf', 'stack:[rbp-0x1c]']`
  - addr_objects: `['imm_occurrence:0xca7:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xca7:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xca7:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xca7:mem_scale:0:0x1:i64', 'imm_occurrence:0xca7:operand_imm:1:0x1:i32']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xca2`: `call 0xb7a` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xcab`: `cmp dword ptr [rbp - 0x1c], 0` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xcaf`: `jns 0xc0d` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xca2`      ca2:	e8 d3 fe ff ff       	callq  b7a <spectre_function> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xca7`      ca7:	83 6d e4 01          	subl   $0x1,-0x1c(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xcab`      cab:	83 7d e4 00          	cmpl   $0x0,-0x1c(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xcaf`      caf:	0f 89 58 ff ff ff    	jns    c0d <stage1_mistrain_trigger+0x18> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 98. `imm_occurrence:0xca7:mem_scale:0:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xca7:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xca7', 'operand_index': None, 'raw_suffix': 'mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xca7:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xca7']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xca7']`
- direct_operand_pcs: `['0xca7']`
- structural_role_pcs: `['0xca7']`
- anchor_pcs: `['0xca7']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xca2', '0xcab', '0xcaf']`
- all_mapped_pcs: `['0xca2', '0xca7', '0xcab', '0xcaf']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x1c]']`

#### PC Relation Entries

- `0xca2` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xca7` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xcab` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xcaf` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xca7`: `sub dword ptr [rbp - 0x1c], 1` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xca7:operand_imm:1:0x1:i32', 'reg:rbp', 'stack:[rbp-0x1c]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf', 'stack:[rbp-0x1c]']`
  - addr_objects: `['imm_occurrence:0xca7:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xca7:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xca7:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xca7:mem_scale:0:0x1:i64', 'imm_occurrence:0xca7:operand_imm:1:0x1:i32']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xca2`: `call 0xb7a` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xcab`: `cmp dword ptr [rbp - 0x1c], 0` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xcaf`: `jns 0xc0d` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xca2`      ca2:	e8 d3 fe ff ff       	callq  b7a <spectre_function> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xca7`      ca7:	83 6d e4 01          	subl   $0x1,-0x1c(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xcab`      cab:	83 7d e4 00          	cmpl   $0x0,-0x1c(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xcaf`      caf:	0f 89 58 ff ff ff    	jns    c0d <stage1_mistrain_trigger+0x18> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 99. `imm_occurrence:0xca7:operand_imm:1:0x1:i32`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xca7:operand_imm:1:0x1/i32 [program_semantic_constant|store_constant]`
- Mapping kind: `store_constant`
- Confidence: `semantic`
- Object semantic tags: `['program_semantic_constant', 'store_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xca7', 'operand_index': None, 'raw_suffix': 'operand_imm:1:0x1/i32 [program_semantic_constant|store_constant]'}`
- Reason: 该 immediate 带有 store_constant 标签，更适合作为写入值常量解释。
- Candidate program elements: `['imm@0xca7:operand_imm:1:0x1/i32 [program_semantic_constant|store_constant]']`
- direct_use_pcs: `['0xca7']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xca7']`
- direct_operand_pcs: `['0xca7']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xca7']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xca2', '0xcab', '0xcaf']`
- all_mapped_pcs: `['0xca2', '0xca7', '0xcab', '0xcaf']`
- direct_parents: `[]`
- direct_children: `['reg:cf', 'reg:of', 'reg:rip', 'reg:sf', 'reg:zf', 'stack:[rbp-0x1c]']`

#### PC Relation Entries

- `0xca2` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xca7` kinds=`['direct_immediate_occurrence', 'direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.used_by/instruction_details.use_objects']`
- `0xcab` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xcaf` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xca7`: `sub dword ptr [rbp - 0x1c], 1` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xca7:operand_imm:1:0x1:i32', 'reg:rbp', 'stack:[rbp-0x1c]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf', 'stack:[rbp-0x1c]']`
  - addr_objects: `['imm_occurrence:0xca7:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xca7:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xca7:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xca7:mem_scale:0:0x1:i64', 'imm_occurrence:0xca7:operand_imm:1:0x1:i32']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xca2`: `call 0xb7a` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xcab`: `cmp dword ptr [rbp - 0x1c], 0` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xcaf`: `jns 0xc0d` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xca2`      ca2:	e8 d3 fe ff ff       	callq  b7a <spectre_function> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xca7`      ca7:	83 6d e4 01          	subl   $0x1,-0x1c(%rbp) groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
- `0xcab`      cab:	83 7d e4 00          	cmpl   $0x0,-0x1c(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xcaf`      caf:	0f 89 58 ff ff ff    	jns    c0d <stage1_mistrain_trigger+0x18> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 100. `imm_occurrence:0xcab:mem_disp:0:0xffffffffffffffe4:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xcab:mem_disp:0:0xffffffffffffffe4/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xcab', 'operand_index': None, 'raw_suffix': 'mem_disp:0:0xffffffffffffffe4/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xcab:mem_disp:0:0xffffffffffffffe4/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xcab']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xcab']`
- direct_operand_pcs: `['0xcab']`
- structural_role_pcs: `['0xcab']`
- anchor_pcs: `['0xcab']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xca7', '0xcaf']`
- all_mapped_pcs: `['0xca7', '0xcab', '0xcaf']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x1c]']`

#### PC Relation Entries

- `0xca7` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xcab` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xcaf` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xcab`: `cmp dword ptr [rbp - 0x1c], 0` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xcab:operand_imm:1:0x0:i32', 'reg:rbp', 'stack:[rbp-0x1c]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xcab:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xcab:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xcab:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xcab:mem_scale:0:0x1:i64', 'imm_occurrence:0xcab:operand_imm:1:0x0:i32']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xca7`: `sub dword ptr [rbp - 0x1c], 1` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xcaf`: `jns 0xc0d` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xca7`      ca7:	83 6d e4 01          	subl   $0x1,-0x1c(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xcab`      cab:	83 7d e4 00          	cmpl   $0x0,-0x1c(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xcaf`      caf:	0f 89 58 ff ff ff    	jns    c0d <stage1_mistrain_trigger+0x18> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 101. `imm_occurrence:0xcab:mem_scale:0:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xcab:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xcab', 'operand_index': None, 'raw_suffix': 'mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xcab:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xcab']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xcab']`
- direct_operand_pcs: `['0xcab']`
- structural_role_pcs: `['0xcab']`
- anchor_pcs: `['0xcab']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xca7', '0xcaf']`
- all_mapped_pcs: `['0xca7', '0xcab', '0xcaf']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x1c]']`

#### PC Relation Entries

- `0xca7` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xcab` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xcaf` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xcab`: `cmp dword ptr [rbp - 0x1c], 0` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xcab:operand_imm:1:0x0:i32', 'reg:rbp', 'stack:[rbp-0x1c]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xcab:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xcab:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xcab:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xcab:mem_scale:0:0x1:i64', 'imm_occurrence:0xcab:operand_imm:1:0x0:i32']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xca7`: `sub dword ptr [rbp - 0x1c], 1` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xcaf`: `jns 0xc0d` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xca7`      ca7:	83 6d e4 01          	subl   $0x1,-0x1c(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xcab`      cab:	83 7d e4 00          	cmpl   $0x0,-0x1c(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xcaf`      caf:	0f 89 58 ff ff ff    	jns    c0d <stage1_mistrain_trigger+0x18> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 102. `imm_occurrence:0xcab:operand_imm:1:0x0:i32`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xcab:operand_imm:1:0x0/i32 [comparison_constant|program_semantic_constant]`
- Mapping kind: `comparison_constant`
- Confidence: `semantic`
- Object semantic tags: `['comparison_constant', 'loop_bound_constant', 'program_semantic_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xcab', 'operand_index': None, 'raw_suffix': 'operand_imm:1:0x0/i32 [comparison_constant|program_semantic_constant]'}`
- Reason: 该 immediate 带有 comparison_constant 标签，更适合作为比较语义常量解释。
- Candidate program elements: `['imm@0xcab:operand_imm:1:0x0/i32 [comparison_constant|program_semantic_constant]']`
- direct_use_pcs: `['0xcab']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xcab']`
- direct_operand_pcs: `['0xcab']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xcab']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xca7', '0xcaf']`
- all_mapped_pcs: `['0xca7', '0xcab', '0xcaf']`
- direct_parents: `[]`
- direct_children: `['reg:cf', 'reg:of', 'reg:rip', 'reg:sf', 'reg:zf']`

#### PC Relation Entries

- `0xca7` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xcab` kinds=`['direct_immediate_occurrence', 'direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.used_by/instruction_details.use_objects']`
- `0xcaf` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xcab`: `cmp dword ptr [rbp - 0x1c], 0` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xcab:operand_imm:1:0x0:i32', 'reg:rbp', 'stack:[rbp-0x1c]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xcab:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xcab:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xcab:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xcab:mem_scale:0:0x1:i64', 'imm_occurrence:0xcab:operand_imm:1:0x0:i32']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xca7`: `sub dword ptr [rbp - 0x1c], 1` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xcaf`: `jns 0xc0d` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xca7`      ca7:	83 6d e4 01          	subl   $0x1,-0x1c(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xcab`      cab:	83 7d e4 00          	cmpl   $0x0,-0x1c(%rbp) groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
- `0xcaf`      caf:	0f 89 58 ff ff ff    	jns    c0d <stage1_mistrain_trigger+0x18> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 103. `imm_occurrence:0xcaf:operand_imm:0:0xc0d:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xcaf:operand_imm:0:0xc0d/i64`
- Mapping kind: `comparison_constant`
- Confidence: `semantic`
- Object semantic tags: `['comparison_constant']`
- Anchor instruction tags: `['argument_shuffle', 'callee_save_restore', 'callee_save_spill', 'conditional_branch', 'epilogue', 'prologue']`
- Scaffolding tags: `['argument_shuffle', 'callee_save_restore', 'callee_save_spill', 'epilogue', 'prologue']`
- Occurrence: `{'occurrence_pc': '0xcaf', 'operand_index': None, 'raw_suffix': 'operand_imm:0:0xc0d/i64'}`
- Reason: 该 immediate 带有 comparison_constant 标签，更适合作为比较语义常量解释。 检测到 ABI/脚手架标签：argument_shuffle, callee_save_restore, callee_save_spill, epilogue, prologue，应更偏向解释为结构性对象，而非优先可变异语义对象。
- Candidate program elements: `['imm@0xcaf:operand_imm:0:0xc0d/i64']`
- direct_use_pcs: `['0xcaf']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `['0xb7a', '0xb7b', '0xb7e', '0xb82', '0xb86', '0xb8b', '0xb91', '0xb93', '0xb97', '0xb99', '0xba0', '0xba4', '0xba7', '0xbaa', '0xbad', '0xbb0', '0xbb3', '0xbba', '0xbbe', '0xbc5', '0xbc7', '0xbcd', '0xbd2', '0xbd3', '0xbd4', '0xc0d', '0xc10', '0xc11', '0xc14', '0xc16', '0xc19', '0xc1b', '0xc1d', '0xc21', '0xc28', '0xc2c', '0xc30', '0xc33', '0xc3a', '0xc3c', '0xc3f', '0xc42', '0xc45', '0xc48', '0xc4d', '0xc4f', '0xc52', '0xc57', '0xc59', '0xc5b', '0xc5d', '0xc60', '0xc62', '0xc64', '0xc66', '0xc68', '0xc6a', '0xc6c', '0xc6e', '0xc71', '0xc75', '0xc77', '0xc7b', '0xc7f', '0xc83', '0xc87', '0xc8b', '0xc8f', '0xc93', '0xc97', '0xc9b', '0xc9f', '0xca2', '0xca7', '0xcab', '0xcaf', '0xcb5', '0xcb6', '0xcb7', '0x150b', '0x150c', '0x150f', '0x1515', '0x1517', '0x1577', '0x1578', '0x1579', '0x157a', '0x157b', '0x157e', '0x1582', '0x1588', '0x158a', '0x168e', '0x168f', '0x1690']`
- direct_imm_pcs: `['0xcaf']`
- direct_operand_pcs: `['0xcaf']`
- structural_role_pcs: `['0xb7a', '0xb7b', '0xb7e', '0xb82', '0xb86', '0xb8b', '0xb91', '0xb93', '0xb97', '0xb99', '0xba0', '0xba4', '0xba7', '0xbaa', '0xbad', '0xbb0', '0xbb3', '0xbba', '0xbbe', '0xbc5', '0xbc7', '0xbcd', '0xbd2', '0xbd3', '0xbd4', '0xc0d', '0xc10', '0xc11', '0xc14', '0xc16', '0xc19', '0xc1b', '0xc1d', '0xc21', '0xc28', '0xc2c', '0xc30', '0xc33', '0xc3a', '0xc3c', '0xc3f', '0xc42', '0xc45', '0xc48', '0xc4d', '0xc4f', '0xc52', '0xc57', '0xc59', '0xc5b', '0xc5d', '0xc60', '0xc62', '0xc64', '0xc66', '0xc68', '0xc6a', '0xc6c', '0xc6e', '0xc71', '0xc75', '0xc77', '0xc7b', '0xc7f', '0xc83', '0xc87', '0xc8b', '0xc8f', '0xc93', '0xc97', '0xc9b', '0xc9f', '0xca2', '0xca7', '0xcab', '0xcaf', '0xcb5', '0xcb6', '0xcb7', '0x150b', '0x150c', '0x150f', '0x1515', '0x1517', '0x1577', '0x1578', '0x1579', '0x157a', '0x157b', '0x157e', '0x1582', '0x1588', '0x158a', '0x168e', '0x168f', '0x1690']`
- anchor_pcs: `['0xb7a', '0xb7b', '0xb7e', '0xb82', '0xb86', '0xb8b', '0xb91', '0xb93', '0xb97', '0xb99', '0xba0', '0xba4', '0xba7', '0xbaa', '0xbad', '0xbb0', '0xbb3', '0xbba', '0xbbe', '0xbc5', '0xbc7', '0xbcd', '0xbd2', '0xbd3', '0xbd4', '0xc0d', '0xc10', '0xc11', '0xc14', '0xc16', '0xc19', '0xc1b', '0xc1d', '0xc21', '0xc28', '0xc2c', '0xc30', '0xc33', '0xc3a', '0xc3c', '0xc3f', '0xc42', '0xc45', '0xc48', '0xc4d', '0xc4f', '0xc52', '0xc57', '0xc59', '0xc5b', '0xc5d', '0xc60', '0xc62', '0xc64', '0xc66', '0xc68', '0xc6a', '0xc6c', '0xc6e', '0xc71', '0xc75', '0xc77', '0xc7b', '0xc7f', '0xc83', '0xc87', '0xc8b', '0xc8f', '0xc93', '0xc97', '0xc9b', '0xc9f', '0xca2', '0xca7', '0xcab', '0xcaf', '0xcb5', '0xcb6', '0xcb7', '0x150b', '0x150c', '0x150f', '0x1515', '0x1517', '0x1577', '0x1578', '0x1579', '0x157a', '0x157b', '0x157e', '0x1582', '0x1588', '0x158a', '0x168e', '0x168f', '0x1690']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xc08', '0x1519', '0x151f', '0x156e', '0x1575', '0x1590', '0x1596', '0x1686', '0x168c']`
- all_mapped_pcs: `['0xb7a', '0xb7b', '0xb7e', '0xb82', '0xb86', '0xb8b', '0xb91', '0xb93', '0xb97', '0xb99', '0xba0', '0xba4', '0xba7', '0xbaa', '0xbad', '0xbb0', '0xbb3', '0xbba', '0xbbe', '0xbc5', '0xbc7', '0xbcd', '0xbd2', '0xbd3', '0xbd4', '0xc08', '0xc0d', '0xc10', '0xc11', '0xc14', '0xc16', '0xc19', '0xc1b', '0xc1d', '0xc21', '0xc28', '0xc2c', '0xc30', '0xc33', '0xc3a', '0xc3c', '0xc3f', '0xc42', '0xc45', '0xc48', '0xc4d', '0xc4f', '0xc52', '0xc57', '0xc59', '0xc5b', '0xc5d', '0xc60', '0xc62', '0xc64', '0xc66', '0xc68', '0xc6a', '0xc6c', '0xc6e', '0xc71', '0xc75', '0xc77', '0xc7b', '0xc7f', '0xc83', '0xc87', '0xc8b', '0xc8f', '0xc93', '0xc97', '0xc9b', '0xc9f', '0xca2', '0xca7', '0xcab', '0xcaf', '0xcb5', '0xcb6', '0xcb7', '0x150b', '0x150c', '0x150f', '0x1515', '0x1517', '0x1519', '0x151f', '0x156e', '0x1575', '0x1577', '0x1578', '0x1579', '0x157a', '0x157b', '0x157e', '0x1582', '0x1588', '0x158a', '0x1590', '0x1596', '0x1686', '0x168c', '0x168e', '0x168f', '0x1690']`
- direct_parents: `[]`
- direct_children: `['reg:cf', 'reg:of', 'reg:rax', 'reg:rbp', 'reg:rcx', 'reg:rdi', 'reg:rdx', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf', 'stack:[rbp-0x10]', 'stack:[rbp-0x18]', 'stack:[rbp-0x1c]', 'stack:[rbp-0x20]', 'stack:[rbp-0x38]', 'stack:[rbp-0x40]', 'stack:[rbp-0x8]', 'var:temp']`

#### PC Relation Entries

- `0xb7a` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xb7b` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xb7e` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xb82` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xb86` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xb8b` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xb91` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xb93` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xb97` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xb99` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xba0` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xba4` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xba7` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbaa` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbad` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbb0` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbb3` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbba` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbbe` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbc5` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbc7` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbcd` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbd2` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbd3` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbd4` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc08` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc0d` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc10` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc11` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc14` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc16` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc19` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc1b` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc1d` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc21` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc28` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc2c` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc30` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc33` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc3a` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc3c` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc3f` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc42` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc45` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc48` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc4d` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc4f` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc52` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc57` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc59` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc5b` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc5d` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc60` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc62` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc64` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc66` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc68` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc6a` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc6c` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc6e` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc71` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc75` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc77` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc7b` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc7f` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc83` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc87` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc8b` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc8f` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc93` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc97` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc9b` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc9f` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xca2` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xca7` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xcab` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xcaf` kinds=`['branch_condition', 'direct_immediate_occurrence', 'direct_use']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.ctrl_used_by', 'object_detail.used_by/instruction_details.use_objects']`
- `0xcb5` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xcb6` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xcb7` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x150b` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x150c` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x150f` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1515` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1517` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1519` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x151f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x156e` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1575` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1577` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1578` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1579` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x157a` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x157b` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x157e` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1582` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1588` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x158a` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1590` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1596` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1686` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x168c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x168e` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x168f` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1690` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`

#### Direct Anchor Instruction Evidence

- PC `0xb7a`: `push rbp` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:58` function=`spectre_function`
  - instruction_semantic_tags: `['callee_save_spill', 'prologue']`
  - use_objects: `['reg:rbp', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x40]']`
- PC `0xb7b`: `mov rbp, rsp` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:58` function=`spectre_function`
  - instruction_semantic_tags: `['prologue']`
  - use_objects: `['reg:rsp']`
  - def_objects: `['reg:rbp', 'reg:rip']`
- PC `0xb7e`: `sub rsp, 0x10` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:58` function=`spectre_function`
  - instruction_semantic_tags: `['prologue']`
  - use_objects: `['imm_occurrence:0xb7e:operand_imm:1:0x10:i64', 'reg:rsp']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xb7e:operand_imm:1:0x10:i64']`
- PC `0xb82`: `mov qword ptr [rbp - 8], rdi` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:58` function=`spectre_function`
  - instruction_semantic_tags: `['argument_shuffle']`
  - use_objects: `['reg:rbp', 'reg:rdi']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x8]']`
  - addr_objects: `['imm_occurrence:0xb82:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xb82:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xb82:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xb82:mem_scale:0:0x1:i64']`
- PC `0xb86`: `call 0x150b` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:60` function=`spectre_function`
  - call_target: `{'operand': '0x150b', 'resolved_symbol': 'pmu_uops_snap_before', 'call_kind': 'direct_call_symbol', 'display_target': 'pmu_uops_snap_before'}`
  - use_objects: `['imm_occurrence:0xb86:operand_imm:0:0x150b:i64', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x18]']`
  - immediates: `['imm_occurrence:0xb86:operand_imm:0:0x150b:i64']`
- PC `0xb8b`: `mov eax, dword ptr [rip + 0x20248f]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function`
  - use_objects: `['reg:rip', 'var:array1_size']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xb8b:mem_disp:1:0x20248f:i64', 'imm_occurrence:0xb8b:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xb8b:mem_disp:1:0x20248f:i64', 'imm_occurrence:0xb8b:mem_scale:1:0x1:i64']`
- PC `0xb91`: `mov eax, eax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:rax', 'reg:rip']`
- PC `0xb93`: `cmp qword ptr [rbp - 8], rax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x8]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xb93:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xb93:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xb93:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xb93:mem_scale:0:0x1:i64']`
- PC `0xb97`: `jae 0xbcd` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function`
  - instruction_semantic_tags: `['conditional_branch']`
  - use_objects: `['imm_occurrence:0xb97:operand_imm:0:0xbcd:i64', 'reg:cf']`
  - def_objects: `['reg:rip']`
  - immediates: `['imm_occurrence:0xb97:operand_imm:0:0xbcd:i64']`
- PC `0xb99`: `lea rdx, [rip + 0x2024a0]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rip']`
  - def_objects: `['reg:rdx', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xb99:mem_disp:1:0x2024a0:i64', 'imm_occurrence:0xb99:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xb99:mem_disp:1:0x2024a0:i64', 'imm_occurrence:0xb99:mem_scale:1:0x1:i64']`
- PC `0xba0`: `mov rax, qword ptr [rbp - 8]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x8]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xba0:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xba0:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xba0:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xba0:mem_scale:1:0x1:i64']`
- PC `0xba4`: `add rax, rdx` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rdx']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0xba7`: `movzx eax, byte ptr [rax]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'var:array1']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xba7:mem_disp:1:0x0:i64', 'imm_occurrence:0xba7:mem_scale:1:0x1:i64', 'reg:rax', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xba7:mem_disp:1:0x0:i64', 'imm_occurrence:0xba7:mem_scale:1:0x1:i64']`
- PC `0xbaa`: `movzx eax, al` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:rax', 'reg:rip']`
- PC `0xbad`: `shl eax, 9` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['imm_occurrence:0xbad:operand_imm:1:0x9:i8', 'reg:rax']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xbad:operand_imm:1:0x9:i8']`
- PC `0xbb0`: `movsxd rdx, eax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:rdx', 'reg:rip']`
- PC `0xbb3`: `lea rax, [rip + 0x210706]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rip']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xbb3:mem_disp:1:0x210706:i64', 'imm_occurrence:0xbb3:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xbb3:mem_disp:1:0x210706:i64', 'imm_occurrence:0xbb3:mem_scale:1:0x1:i64']`
- PC `0xbba`: `movzx edx, byte ptr [rdx + rax]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rdx', 'var:array2']`
  - def_objects: `['reg:rdx', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xbba:mem_disp:1:0x0:i64', 'imm_occurrence:0xbba:mem_scale:1:0x1:i64', 'reg:rax', 'reg:rdx', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xbba:mem_disp:1:0x0:i64', 'imm_occurrence:0xbba:mem_scale:1:0x1:i64']`
- PC `0xbbe`: `movzx eax, byte ptr [rip + 0x202544]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rip', 'var:temp']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xbbe:mem_disp:1:0x202544:i64', 'imm_occurrence:0xbbe:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xbbe:mem_disp:1:0x202544:i64', 'imm_occurrence:0xbbe:mem_scale:1:0x1:i64']`
- PC `0xbc5`: `and eax, edx` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rdx']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0xbc7`: `mov byte ptr [rip + 0x20253c], al` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rip']`
  - def_objects: `['reg:rip', 'var:temp']`
  - addr_objects: `['imm_occurrence:0xbc7:mem_disp:0:0x20253c:i64', 'imm_occurrence:0xbc7:mem_scale:0:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xbc7:mem_disp:0:0x20253c:i64', 'imm_occurrence:0xbc7:mem_scale:0:0x1:i64']`
- PC `0xbcd`: `call 0x157a` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:70` function=`spectre_function`
  - call_target: `{'operand': '0x157a', 'resolved_symbol': 'pmu_uops_snap_after', 'call_kind': 'direct_call_symbol', 'display_target': 'pmu_uops_snap_after'}`
  - use_objects: `['imm_occurrence:0xbcd:operand_imm:0:0x157a:i64', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x18]']`
  - immediates: `['imm_occurrence:0xbcd:operand_imm:0:0x157a:i64']`
- PC `0xbd2`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xbd3`: `leave` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:71` function=`spectre_function`
  - instruction_semantic_tags: `['epilogue']`
  - use_objects: `['reg:rbp', 'reg:rsp', 'stack:[rbp-0x40]']`
  - def_objects: `['reg:rbp', 'reg:rip', 'reg:rsp']`
- PC `0xbd4`: `ret` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:71` function=`spectre_function`
  - use_objects: `['reg:rsp', 'stack:[rbp-0x38]']`
  - def_objects: `['reg:rip', 'reg:rsp']`
- PC `0xc0d`: `mov eax, dword ptr [rbp - 0x1c]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x1c]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc0d:mem_disp:1:0xffffffffffffffe4:i64', 'imm_occurrence:0xc0d:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc0d:mem_disp:1:0xffffffffffffffe4:i64', 'imm_occurrence:0xc0d:mem_scale:1:0x1:i64']`
- PC `0xc10`: `cdq` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:rdx', 'reg:rip']`
- PC `0xc11`: `shr edx, 0x1c` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc11:operand_imm:1:0x1c:i8', 'reg:rdx']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rdx', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xc11:operand_imm:1:0x1c:i8']`
- PC `0xc14`: `add eax, edx` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rdx']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0xc16`: `and eax, 0xf` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc16:operand_imm:1:0xf:i32', 'reg:rax']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xc16:operand_imm:1:0xf:i32']`
- PC `0xc19`: `sub eax, edx` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rdx']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0xc1b`: `cdqe` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:rax', 'reg:rip']`
- PC `0xc1d`: `mov qword ptr [rbp - 0x18], rax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x18]']`
  - addr_objects: `['imm_occurrence:0xc1d:mem_disp:0:0xffffffffffffffe8:i64', 'imm_occurrence:0xc1d:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc1d:mem_disp:0:0xffffffffffffffe8:i64', 'imm_occurrence:0xc1d:mem_scale:0:0x1:i64']`
- PC `0xc21`: `lea rax, [rip + 0x2023f8]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rip']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc21:mem_disp:1:0x2023f8:i64', 'imm_occurrence:0xc21:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc21:mem_disp:1:0x2023f8:i64', 'imm_occurrence:0xc21:mem_scale:1:0x1:i64']`
- PC `0xc28`: `mov qword ptr [rbp - 8], rax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x8]']`
  - addr_objects: `['imm_occurrence:0xc28:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xc28:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc28:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xc28:mem_scale:0:0x1:i64']`
- PC `0xc2c`: `mov rax, qword ptr [rbp - 8]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/usr/lib/gcc/x86_64-linux-gnu/7/include/emmintrin.h:1486` function=`_mm_clflush`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x8]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc2c:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xc2c:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc2c:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xc2c:mem_scale:1:0x1:i64']`
- PC `0xc30`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc33`: `mov dword ptr [rbp - 0x20], 0` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:95` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc33:operand_imm:1:0x0:i32', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x20]']`
  - addr_objects: `['imm_occurrence:0xc33:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xc33:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc33:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xc33:mem_scale:0:0x1:i64', 'imm_occurrence:0xc33:operand_imm:1:0x0:i32']`
- PC `0xc3a`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc3c`: `mov eax, dword ptr [rbp - 0x20]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x20]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc3c:mem_disp:1:0xffffffffffffffe0:i64', 'imm_occurrence:0xc3c:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc3c:mem_disp:1:0xffffffffffffffe0:i64', 'imm_occurrence:0xc3c:mem_scale:1:0x1:i64']`
- PC `0xc3f`: `add eax, 1` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc3f:operand_imm:1:0x1:i32', 'reg:rax']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xc3f:operand_imm:1:0x1:i32']`
- PC `0xc42`: `mov dword ptr [rbp - 0x20], eax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x20]']`
  - addr_objects: `['imm_occurrence:0xc42:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xc42:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc42:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xc42:mem_scale:0:0x1:i64']`
- PC `0xc45`: `mov eax, dword ptr [rbp - 0x20]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x20]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc45:mem_disp:1:0xffffffffffffffe0:i64', 'imm_occurrence:0xc45:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc45:mem_disp:1:0xffffffffffffffe0:i64', 'imm_occurrence:0xc45:mem_scale:1:0x1:i64']`
- PC `0xc48`: `cmp eax, 0xc7` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc48:operand_imm:1:0xc7:i32', 'reg:rax']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xc48:operand_imm:1:0xc7:i32']`
- PC `0xc4d`: `jle 0xc3c` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - instruction_semantic_tags: `['conditional_branch']`
  - use_objects: `['imm_occurrence:0xc4d:operand_imm:0:0xc3c:i64', 'reg:of', 'reg:sf', 'reg:zf']`
  - def_objects: `['reg:rip']`
  - immediates: `['imm_occurrence:0xc4d:operand_imm:0:0xc3c:i64']`
- PC `0xc4f`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc52`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc57`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc59`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc5b`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc5d`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc60`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc62`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc64`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc66`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc68`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc6a`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc6c`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc6e`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc71`: `mov ax, 0` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc71:operand_imm:1:0x0:i16']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - immediates: `['imm_occurrence:0xc71:operand_imm:1:0x0:i16']`
- PC `0xc75`: `cdqe` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:rax', 'reg:rip']`
- PC `0xc77`: `mov qword ptr [rbp - 0x10], rax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x10]']`
  - addr_objects: `['imm_occurrence:0xc77:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc77:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc77:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc77:mem_scale:0:0x1:i64']`
- PC `0xc7b`: `mov rax, qword ptr [rbp - 0x10]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc7b:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc7b:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc7b:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc7b:mem_scale:1:0x1:i64']`
- PC `0xc7f`: `shr rax, 0x10` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc7f:operand_imm:1:0x10:i8', 'reg:rax']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xc7f:operand_imm:1:0x10:i8']`
- PC `0xc83`: `or qword ptr [rbp - 0x10], rax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf', 'stack:[rbp-0x10]']`
  - addr_objects: `['imm_occurrence:0xc83:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc83:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc83:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc83:mem_scale:0:0x1:i64']`
- PC `0xc87`: `mov rax, qword ptr [rbp - 0x28]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x28]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc87:mem_disp:1:0xffffffffffffffd8:i64', 'imm_occurrence:0xc87:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc87:mem_disp:1:0xffffffffffffffd8:i64', 'imm_occurrence:0xc87:mem_scale:1:0x1:i64']`
- PC `0xc8b`: `xor rax, qword ptr [rbp - 0x18]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x18]']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xc8b:mem_disp:1:0xffffffffffffffe8:i64', 'imm_occurrence:0xc8b:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc8b:mem_disp:1:0xffffffffffffffe8:i64', 'imm_occurrence:0xc8b:mem_scale:1:0x1:i64']`
- PC `0xc8f`: `and rax, qword ptr [rbp - 0x10]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xc8f:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc8f:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc8f:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc8f:mem_scale:1:0x1:i64']`
- PC `0xc93`: `xor rax, qword ptr [rbp - 0x18]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x18]']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xc93:mem_disp:1:0xffffffffffffffe8:i64', 'imm_occurrence:0xc93:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc93:mem_disp:1:0xffffffffffffffe8:i64', 'imm_occurrence:0xc93:mem_scale:1:0x1:i64']`
- PC `0xc97`: `mov qword ptr [rbp - 0x10], rax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x10]']`
  - addr_objects: `['imm_occurrence:0xc97:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc97:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc97:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc97:mem_scale:0:0x1:i64']`
- PC `0xc9b`: `mov rax, qword ptr [rbp - 0x10]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc9b:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc9b:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc9b:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc9b:mem_scale:1:0x1:i64']`
- PC `0xc9f`: `mov rdi, rax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:rdi', 'reg:rip']`
- PC `0xca2`: `call 0xb7a` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - call_target: `{'operand': '0xb7a', 'resolved_symbol': 'spectre_function', 'call_kind': 'direct_call_symbol', 'display_target': 'spectre_function'}`
  - use_objects: `['imm_occurrence:0xca2:operand_imm:0:0xb7a:i64', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x38]']`
  - immediates: `['imm_occurrence:0xca2:operand_imm:0:0xb7a:i64']`
- PC `0xca7`: `sub dword ptr [rbp - 0x1c], 1` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xca7:operand_imm:1:0x1:i32', 'reg:rbp', 'stack:[rbp-0x1c]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf', 'stack:[rbp-0x1c]']`
  - addr_objects: `['imm_occurrence:0xca7:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xca7:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xca7:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xca7:mem_scale:0:0x1:i64', 'imm_occurrence:0xca7:operand_imm:1:0x1:i32']`
- PC `0xcab`: `cmp dword ptr [rbp - 0x1c], 0` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xcab:operand_imm:1:0x0:i32', 'reg:rbp', 'stack:[rbp-0x1c]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xcab:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xcab:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xcab:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xcab:mem_scale:0:0x1:i64', 'imm_occurrence:0xcab:operand_imm:1:0x0:i32']`
- PC `0xcaf`: `jns 0xc0d` groups=`['direct_operand', 'structural_role']` kinds=`['branch_condition', 'direct_immediate_occurrence', 'direct_use']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - instruction_semantic_tags: `['conditional_branch']`
  - use_objects: `['imm_occurrence:0xcaf:operand_imm:0:0xc0d:i64', 'reg:sf']`
  - def_objects: `['reg:rip']`
  - immediates: `['imm_occurrence:0xcaf:operand_imm:0:0xc0d:i64']`
- PC `0xcb5`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xcb6`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xcb7`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x150b`: `push rbp` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_before`
  - instruction_semantic_tags: `['callee_save_spill', 'prologue']`
  - use_objects: `['reg:rbp', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x20]']`
- PC `0x150c`: `mov rbp, rsp` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_before`
  - instruction_semantic_tags: `['prologue']`
  - use_objects: `['reg:rsp']`
  - def_objects: `['reg:rbp', 'reg:rip']`
- PC `0x150f`: `mov eax, dword ptr [rip + 0x20fc6f]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_before`
  - use_objects: `['reg:rip', 'var:uops_available']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0x150f:mem_disp:1:0x20fc6f:i64', 'imm_occurrence:0x150f:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0x150f:mem_disp:1:0x20fc6f:i64', 'imm_occurrence:0x150f:mem_scale:1:0x1:i64']`
- PC `0x1515`: `test eax, eax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_before`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0x1517`: `je 0x1577` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_before`
  - instruction_semantic_tags: `['conditional_branch']`
  - use_objects: `['imm_occurrence:0x1517:operand_imm:0:0x1577:i64', 'reg:zf']`
  - def_objects: `['reg:rip']`
  - immediates: `['imm_occurrence:0x1517:operand_imm:0:0x1577:i64']`
- PC `0x1577`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x1578`: `pop rbp` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_before`
  - instruction_semantic_tags: `['callee_save_restore', 'epilogue']`
  - use_objects: `['reg:rsp', 'stack:[rbp-0x20]']`
  - def_objects: `['reg:rbp', 'reg:rip', 'reg:rsp']`
- PC `0x1579`: `ret` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_before`
  - use_objects: `['reg:rsp', 'stack:[rbp-0x18]']`
  - def_objects: `['reg:rip', 'reg:rsp']`
- PC `0x157a`: `push rbp` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - instruction_semantic_tags: `['callee_save_spill', 'prologue']`
  - use_objects: `['reg:rbp', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x20]']`
- PC `0x157b`: `mov rbp, rsp` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - instruction_semantic_tags: `['prologue']`
  - use_objects: `['reg:rsp']`
  - def_objects: `['reg:rbp', 'reg:rip']`
- PC `0x157e`: `sub rsp, 0x20` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - instruction_semantic_tags: `['prologue']`
  - use_objects: `['imm_occurrence:0x157e:operand_imm:1:0x20:i64', 'reg:rsp']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0x157e:operand_imm:1:0x20:i64']`
- PC `0x1582`: `mov eax, dword ptr [rip + 0x20fbfc]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - use_objects: `['reg:rip', 'var:uops_available']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0x1582:mem_disp:1:0x20fbfc:i64', 'imm_occurrence:0x1582:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0x1582:mem_disp:1:0x20fbfc:i64', 'imm_occurrence:0x1582:mem_scale:1:0x1:i64']`
- PC `0x1588`: `test eax, eax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0x158a`: `je 0x168e` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - instruction_semantic_tags: `['conditional_branch']`
  - use_objects: `['imm_occurrence:0x158a:operand_imm:0:0x168e:i64', 'reg:zf']`
  - def_objects: `['reg:rip']`
  - immediates: `['imm_occurrence:0x158a:operand_imm:0:0x168e:i64']`
- PC `0x168e`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x168f`: `leave` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - instruction_semantic_tags: `['epilogue']`
  - use_objects: `['reg:rbp', 'reg:rsp', 'stack:[rbp-0x20]']`
  - def_objects: `['reg:rbp', 'reg:rip', 'reg:rsp']`
- PC `0x1690`: `ret` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - use_objects: `['reg:rsp', 'stack:[rbp-0x18]']`
  - def_objects: `['reg:rip', 'reg:rsp']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xc08`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1519`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x151f`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x156e`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1575`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1590`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1596`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1686`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x168c`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xb7a`      b7a:	55                   	push   %rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0xb7b`      b7b:	48 89 e5             	mov    %rsp,%rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0xb7e`      b7e:	48 83 ec 10          	sub    $0x10,%rsp groups=`['structural_role']` kinds=`['branch_condition']`
- `0xb82`      b82:	48 89 7d f8          	mov    %rdi,-0x8(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xb86`      b86:	e8 80 09 00 00       	callq  150b <pmu_uops_snap_before> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xb8b`      b8b:	8b 05 8f 24 20 00    	mov    0x20248f(%rip),%eax        # 203020 <array1_size> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xb91`      b91:	89 c0                	mov    %eax,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xb93`      b93:	48 39 45 f8          	cmp    %rax,-0x8(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xb97`      b97:	73 34                	jae    bcd <STAGE1_END> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xb99`      b99:	48 8d 15 a0 24 20 00 	lea    0x2024a0(%rip),%rdx        # 203040 <array1> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xba0`      ba0:	48 8b 45 f8          	mov    -0x8(%rbp),%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xba4`      ba4:	48 01 d0             	add    %rdx,%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xba7`      ba7:	0f b6 00             	movzbl (%rax),%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbaa`      baa:	0f b6 c0             	movzbl %al,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbad`      bad:	c1 e0 09             	shl    $0x9,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbb0`      bb0:	48 63 d0             	movslq %eax,%rdx groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbb3`      bb3:	48 8d 05 06 07 21 00 	lea    0x210706(%rip),%rax        # 2112c0 <array2> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbba`      bba:	0f b6 14 02          	movzbl (%rdx,%rax,1),%edx groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbbe`      bbe:	0f b6 05 44 25 20 00 	movzbl 0x202544(%rip),%eax        # 203109 <temp> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbc5`      bc5:	21 d0                	and    %edx,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbc7`      bc7:	88 05 3c 25 20 00    	mov    %al,0x20253c(%rip)        # 203109 <temp> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbcd`      bcd:	e8 a8 09 00 00       	callq  157a <pmu_uops_snap_after> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbd2`      bd2:	90                   	nop groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbd3`      bd3:	c9                   	leaveq  groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbd4`      bd4:	c3                   	retq    groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc08`      c08:	e9 9e 00 00 00       	jmpq   cab <stage1_mistrain_trigger+0xb6> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc0d`      c0d:	8b 45 e4             	mov    -0x1c(%rbp),%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc10`      c10:	99                   	cltd    groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc11`      c11:	c1 ea 1c             	shr    $0x1c,%edx groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc14`      c14:	01 d0                	add    %edx,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc16`      c16:	83 e0 0f             	and    $0xf,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc19`      c19:	29 d0                	sub    %edx,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc1b`      c1b:	48 98                	cltq    groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc1d`      c1d:	48 89 45 e8          	mov    %rax,-0x18(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc21`      c21:	48 8d 05 f8 23 20 00 	lea    0x2023f8(%rip),%rax        # 203020 <array1_size> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc28`      c28:	48 89 45 f8          	mov    %rax,-0x8(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc2c`      c2c:	48 8b 45 f8          	mov    -0x8(%rbp),%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc30`      c30:	0f ae 38             	clflush (%rax) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc33`      c33:	c7 45 e0 00 00 00 00 	movl   $0x0,-0x20(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc3a`      c3a:	eb 09                	jmp    c45 <stage1_mistrain_trigger+0x50> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc3c`      c3c:	8b 45 e0             	mov    -0x20(%rbp),%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc3f`      c3f:	83 c0 01             	add    $0x1,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc42`      c42:	89 45 e0             	mov    %eax,-0x20(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc45`      c45:	8b 45 e0             	mov    -0x20(%rbp),%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc48`      c48:	3d c7 00 00 00       	cmp    $0xc7,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc4d`      c4d:	7e ed                	jle    c3c <stage1_mistrain_trigger+0x47> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc4f`      c4f:	8b 4d e4             	mov    -0x1c(%rbp),%ecx groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc52`      c52:	ba ab aa aa 2a       	mov    $0x2aaaaaab,%edx groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc57`      c57:	89 c8                	mov    %ecx,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc59`      c59:	f7 ea                	imul   %edx groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc5b`      c5b:	89 c8                	mov    %ecx,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc5d`      c5d:	c1 f8 1f             	sar    $0x1f,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc60`      c60:	29 c2                	sub    %eax,%edx groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc62`      c62:	89 d0                	mov    %edx,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc64`      c64:	01 c0                	add    %eax,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc66`      c66:	01 d0                	add    %edx,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc68`      c68:	01 c0                	add    %eax,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc6a`      c6a:	29 c1                	sub    %eax,%ecx groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc6c`      c6c:	89 ca                	mov    %ecx,%edx groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc6e`      c6e:	8d 42 ff             	lea    -0x1(%rdx),%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc71`      c71:	66 b8 00 00          	mov    $0x0,%ax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc75`      c75:	48 98                	cltq    groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc77`      c77:	48 89 45 f0          	mov    %rax,-0x10(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc7b`      c7b:	48 8b 45 f0          	mov    -0x10(%rbp),%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc7f`      c7f:	48 c1 e8 10          	shr    $0x10,%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc83`      c83:	48 09 45 f0          	or     %rax,-0x10(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc87`      c87:	48 8b 45 d8          	mov    -0x28(%rbp),%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc8b`      c8b:	48 33 45 e8          	xor    -0x18(%rbp),%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc8f`      c8f:	48 23 45 f0          	and    -0x10(%rbp),%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc93`      c93:	48 33 45 e8          	xor    -0x18(%rbp),%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc97`      c97:	48 89 45 f0          	mov    %rax,-0x10(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc9b`      c9b:	48 8b 45 f0          	mov    -0x10(%rbp),%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc9f`      c9f:	48 89 c7             	mov    %rax,%rdi groups=`['structural_role']` kinds=`['branch_condition']`
- `0xca2`      ca2:	e8 d3 fe ff ff       	callq  b7a <spectre_function> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xca7`      ca7:	83 6d e4 01          	subl   $0x1,-0x1c(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xcab`      cab:	83 7d e4 00          	cmpl   $0x0,-0x1c(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xcaf`      caf:	0f 89 58 ff ff ff    	jns    c0d <stage1_mistrain_trigger+0x18> groups=`['direct_operand', 'structural_role']` kinds=`['branch_condition', 'direct_immediate_occurrence', 'direct_use']`
- `0xcb5`      cb5:	90                   	nop groups=`['structural_role']` kinds=`['branch_condition']`
- `0xcb6`      cb6:	c9                   	leaveq  groups=`['structural_role']` kinds=`['branch_condition']`
- `0xcb7`      cb7:	c3                   	retq    groups=`['structural_role']` kinds=`['branch_condition']`
- `0x150b`     150b:	55                   	push   %rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0x150c`     150c:	48 89 e5             	mov    %rsp,%rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0x150f`     150f:	8b 05 6f fc 20 00    	mov    0x20fc6f(%rip),%eax        # 211184 <uops_available> groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1515`     1515:	85 c0                	test   %eax,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1517`     1517:	74 5e                	je     1577 <pmu_uops_snap_before+0x6c> groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1519`     1519:	8b 05 41 3c 20 00    	mov    0x203c41(%rip),%eax        # 205160 <use_rdpmc> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x151f`     151f:	85 c0                	test   %eax,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x156e`     156e:	48 89 05 03 3c 20 00 	mov    %rax,0x203c03(%rip)        # 205178 <snap_retired> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1575`     1575:	eb 01                	jmp    1578 <pmu_uops_snap_before+0x6d> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1577`     1577:	90                   	nop groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1578`     1578:	5d                   	pop    %rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1579`     1579:	c3                   	retq    groups=`['structural_role']` kinds=`['branch_condition']`
- `0x157a`     157a:	55                   	push   %rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0x157b`     157b:	48 89 e5             	mov    %rsp,%rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0x157e`     157e:	48 83 ec 20          	sub    $0x20,%rsp groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1582`     1582:	8b 05 fc fb 20 00    	mov    0x20fbfc(%rip),%eax        # 211184 <uops_available> groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1588`     1588:	85 c0                	test   %eax,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0x158a`     158a:	0f 84 fe 00 00 00    	je     168e <pmu_uops_snap_after+0x114> groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1590`     1590:	8b 05 ca 3b 20 00    	mov    0x203bca(%rip),%eax        # 205160 <use_rdpmc> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1596`     1596:	85 c0                	test   %eax,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1686`     1686:	89 05 f4 fa 20 00    	mov    %eax,0x20faf4(%rip)        # 211180 <uops_cnt> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x168c`     168c:	eb 01                	jmp    168f <pmu_uops_snap_after+0x115> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x168e`     168e:	90                   	nop groups=`['structural_role']` kinds=`['branch_condition']`
- `0x168f`     168f:	c9                   	leaveq  groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1690`     1690:	c3                   	retq    groups=`['structural_role']` kinds=`['branch_condition']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:58` function=`spectre_function` pcs=`['0xb7a', '0xb7b', '0xb7e', '0xb82']` groups=`['structural_role']` kinds=`['branch_condition']`

```c
   56: ********************************************************************/
   57: __attribute__((noinline))
   58: void spectre_function(size_t x) {
   59: 
   60:   pmu_uops_snap_before();
```

- `/root/src/spectre_stage1_2_auto.c:60` function=`spectre_function` pcs=`['0xb86']` groups=`['structural_role']` kinds=`['branch_condition']`

```c
   58: void spectre_function(size_t x) {
   59: 
   60:   pmu_uops_snap_before();
   61: 
   62:   asm volatile(".globl STAGE1_BEGIN\nSTAGE1_BEGIN:");
```

- `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function` pcs=`['0xb8b', '0xb91', '0xb93', '0xb97']` groups=`['structural_role']` kinds=`['branch_condition']`

```c
   61: 
   62:   asm volatile(".globl STAGE1_BEGIN\nSTAGE1_BEGIN:");
   63:   if (x < array1_size) {
   64:     NOP_REGION_BEGIN
   65:     temp &= array2[array1[x] * 512];
```

- `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function` pcs=`['0xb99', '0xba0', '0xba4', '0xba7', '0xbaa', '0xbad', '0xbb0', '0xbb3', '0xbba', '0xbbe', '0xbc5', '0xbc7']` groups=`['structural_role']` kinds=`['branch_condition']`

```c
   63:   if (x < array1_size) {
   64:     NOP_REGION_BEGIN
   65:     temp &= array2[array1[x] * 512];
   66:     NOP_REGION_END
   67:   }
```

- `/root/src/spectre_stage1_2_auto.c:70` function=`spectre_function` pcs=`['0xbcd']` groups=`['structural_role']` kinds=`['branch_condition']`

```c
   68:   asm volatile(".globl STAGE1_END\nSTAGE1_END:");
   69: 
   70:   pmu_uops_snap_after();
   71: }
   72: 
```

- `/root/src/spectre_stage1_2_auto.c:71` function=`spectre_function` pcs=`['0xbd3', '0xbd4']` groups=`['structural_role']` kinds=`['branch_condition']`

```c
   69: 
   70:   pmu_uops_snap_after();
   71: }
   72: 
   73: /********************************************************************
```

- `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger` pcs=`['0xc0d', '0xc10', '0xc11', '0xc14', '0xc16', '0xc19', '0xc1b', '0xc1d', '0xc21', '0xc28']` groups=`['structural_role']` kinds=`['branch_condition']`

```c
   91: 
   92:     for (j = 29; j >= 0; j--) {
   93:         training_x = (size_t)(j % 16);
   94:         _mm_clflush(&array1_size);
   95:         for (volatile int z = 0; z < 200; z++) {}
```

- `/root/src/spectre_stage1_2_auto.c:95` function=`stage1_mistrain_trigger` pcs=`['0xc33']` groups=`['structural_role']` kinds=`['branch_condition']`

```c
   93:         training_x = (size_t)(j % 16);
   94:         _mm_clflush(&array1_size);
   95:         for (volatile int z = 0; z < 200; z++) {}
   96: 
   97:         x = ((j % 6) - 1) & ~0xFFFF;
```

- `/usr/lib/gcc/x86_64-linux-gnu/7/include/emmintrin.h:1486` function=`_mm_clflush` pcs=`['0xc2c']` groups=`['structural_role']` kinds=`['branch_condition']`

### 104. `imm_occurrence:0xd3f:operand_imm:1:0x20:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xd3f:operand_imm:1:0x20/i64 [stack_alignment_constant|structural_abi_constant]`
- Mapping kind: `stack_alignment_constant`
- Confidence: `semantic`
- Object semantic tags: `['stack_alignment_constant', 'structural_abi_constant']`
- Anchor instruction tags: `['prologue']`
- Scaffolding tags: `['prologue']`
- Occurrence: `{'occurrence_pc': '0xd3f', 'operand_index': None, 'raw_suffix': 'operand_imm:1:0x20/i64 [stack_alignment_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 stack_alignment_constant 标签，更适合作为栈对齐常量解释。 检测到 ABI/脚手架标签：prologue，应更偏向解释为结构性对象，而非优先可变异语义对象。
- Candidate program elements: `['imm@0xd3f:operand_imm:1:0x20/i64 [stack_alignment_constant|structural_abi_constant]']`
- direct_use_pcs: `['0xd3f']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xd3f']`
- direct_operand_pcs: `['0xd3f']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xd3f']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd3b', '0xd3c', '0xd43', '0xd46']`
- all_mapped_pcs: `['0xd3b', '0xd3c', '0xd3f', '0xd43', '0xd46']`
- direct_parents: `[]`
- direct_children: `['reg:cf', 'reg:of', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf']`

#### PC Relation Entries

- `0xd3b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd3c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd3f` kinds=`['direct_immediate_occurrence', 'direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.used_by/instruction_details.use_objects']`
- `0xd43` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd46` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xd3f`: `sub rsp, 0x20` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
  - Source: `/root/src/spectre_stage1_2_auto.c:124` function=`main`
  - instruction_semantic_tags: `['prologue']`
  - use_objects: `['imm_occurrence:0xd3f:operand_imm:1:0x20:i64', 'reg:rsp']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xd3f:operand_imm:1:0x20:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd3b`: `push rbp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd3c`: `mov rbp, rsp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd43`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd46`: `mov qword ptr [rbp - 0x20], rsi` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd3b`      d3b:	55                   	push   %rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd3c`      d3c:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd3f`      d3f:	48 83 ec 20          	sub    $0x20,%rsp groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
- `0xd43`      d43:	89 7d ec             	mov    %edi,-0x14(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd46`      d46:	48 89 75 e0          	mov    %rsi,-0x20(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:124` function=`main` pcs=`['0xd3b', '0xd3c', '0xd3f', '0xd46']` groups=`['direct_operand', 'evidence_only']` kinds=`['direct_immediate_occurrence', 'direct_use', 'evidence_only']`

```c
  122: ********************************************************************/
  123: #ifndef STAGE2_TEST_MAIN
  124: int main(int argc, const char **argv) {
  125:     size_t malicious_x = (size_t)(secret - (char *)array1);
  126:     int i;
```

### 105. `imm_occurrence:0xd46:mem_disp:0:0xffffffffffffffe0:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xd46:mem_disp:0:0xffffffffffffffe0/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `['argument_shuffle']`
- Scaffolding tags: `['argument_shuffle']`
- Occurrence: `{'occurrence_pc': '0xd46', 'operand_index': None, 'raw_suffix': 'mem_disp:0:0xffffffffffffffe0/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。 检测到 ABI/脚手架标签：argument_shuffle，应更偏向解释为结构性对象，而非优先可变异语义对象。
- Candidate program elements: `['imm@0xd46:mem_disp:0:0xffffffffffffffe0/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xd46']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xd46']`
- direct_operand_pcs: `['0xd46']`
- structural_role_pcs: `['0xd46']`
- anchor_pcs: `['0xd46']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd3f', '0xd43', '0xd4a']`
- all_mapped_pcs: `['0xd3f', '0xd43', '0xd46', '0xd4a']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x20]']`

#### PC Relation Entries

- `0xd3f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd43` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd46` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xd4a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xd46`: `mov qword ptr [rbp - 0x20], rsi` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:124` function=`main`
  - instruction_semantic_tags: `['argument_shuffle']`
  - use_objects: `['reg:rbp', 'reg:rsi']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x20]']`
  - addr_objects: `['imm_occurrence:0xd46:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xd46:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd46:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xd46:mem_scale:0:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd3f`: `sub rsp, 0x20` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd43`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd4a`: `mov rax, qword ptr [rip + 0x20238f]` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd3f`      d3f:	48 83 ec 20          	sub    $0x20,%rsp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd43`      d43:	89 7d ec             	mov    %edi,-0x14(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd46`      d46:	48 89 75 e0          	mov    %rsi,-0x20(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xd4a`      d4a:	48 8b 05 8f 23 20 00 	mov    0x20238f(%rip),%rax        # 2030e0 <secret> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:124` function=`main` pcs=`['0xd3f', '0xd46']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
  122: ********************************************************************/
  123: #ifndef STAGE2_TEST_MAIN
  124: int main(int argc, const char **argv) {
  125:     size_t malicious_x = (size_t)(secret - (char *)array1);
  126:     int i;
```

- `/root/src/spectre_stage1_2_auto.c:125` function=`main` pcs=`['0xd4a']` groups=`['evidence_only']` kinds=`['evidence_only']`

```c
  123: #ifndef STAGE2_TEST_MAIN
  124: int main(int argc, const char **argv) {
  125:     size_t malicious_x = (size_t)(secret - (char *)array1);
  126:     int i;
  127: 
```

### 106. `imm_occurrence:0xd46:mem_scale:0:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xd46:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `['argument_shuffle']`
- Scaffolding tags: `['argument_shuffle']`
- Occurrence: `{'occurrence_pc': '0xd46', 'operand_index': None, 'raw_suffix': 'mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。 检测到 ABI/脚手架标签：argument_shuffle，应更偏向解释为结构性对象，而非优先可变异语义对象。
- Candidate program elements: `['imm@0xd46:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xd46']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xd46']`
- direct_operand_pcs: `['0xd46']`
- structural_role_pcs: `['0xd46']`
- anchor_pcs: `['0xd46']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd3f', '0xd43', '0xd4a']`
- all_mapped_pcs: `['0xd3f', '0xd43', '0xd46', '0xd4a']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x20]']`

#### PC Relation Entries

- `0xd3f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd43` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd46` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xd4a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xd46`: `mov qword ptr [rbp - 0x20], rsi` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:124` function=`main`
  - instruction_semantic_tags: `['argument_shuffle']`
  - use_objects: `['reg:rbp', 'reg:rsi']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x20]']`
  - addr_objects: `['imm_occurrence:0xd46:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xd46:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd46:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xd46:mem_scale:0:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd3f`: `sub rsp, 0x20` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd43`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd4a`: `mov rax, qword ptr [rip + 0x20238f]` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd3f`      d3f:	48 83 ec 20          	sub    $0x20,%rsp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd43`      d43:	89 7d ec             	mov    %edi,-0x14(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd46`      d46:	48 89 75 e0          	mov    %rsi,-0x20(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xd4a`      d4a:	48 8b 05 8f 23 20 00 	mov    0x20238f(%rip),%rax        # 2030e0 <secret> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:124` function=`main` pcs=`['0xd3f', '0xd46']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
  122: ********************************************************************/
  123: #ifndef STAGE2_TEST_MAIN
  124: int main(int argc, const char **argv) {
  125:     size_t malicious_x = (size_t)(secret - (char *)array1);
  126:     int i;
```

- `/root/src/spectre_stage1_2_auto.c:125` function=`main` pcs=`['0xd4a']` groups=`['evidence_only']` kinds=`['evidence_only']`

```c
  123: #ifndef STAGE2_TEST_MAIN
  124: int main(int argc, const char **argv) {
  125:     size_t malicious_x = (size_t)(secret - (char *)array1);
  126:     int i;
  127: 
```

### 107. `imm_occurrence:0xd4a:mem_disp:1:0x20238f:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xd4a:mem_disp:1:0x20238f/i64 [rip_relative_displacement|structural_abi_constant]`
- Mapping kind: `rip_relative_displacement`
- Confidence: `semantic`
- Object semantic tags: `['rip_relative_displacement', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xd4a', 'operand_index': None, 'raw_suffix': 'mem_disp:1:0x20238f/i64 [rip_relative_displacement|structural_abi_constant]'}`
- Reason: 该 immediate 带有 rip_relative_displacement 标签，更适合作为 RIP 相对寻址位移解释。
- Candidate program elements: `['imm@0xd4a:mem_disp:1:0x20238f/i64 [rip_relative_displacement|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xd4a']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xd4a']`
- direct_operand_pcs: `['0xd4a']`
- structural_role_pcs: `['0xd4a']`
- anchor_pcs: `['0xd4a']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd46', '0xd51', '0xd54']`
- all_mapped_pcs: `['0xd46', '0xd4a', '0xd51', '0xd54']`
- direct_parents: `[]`
- direct_children: `['var:secret']`

#### PC Relation Entries

- `0xd46` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd4a` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xd51` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd54` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xd4a`: `mov rax, qword ptr [rip + 0x20238f]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:125` function=`main`
  - use_objects: `['reg:rip', 'var:secret']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xd4a:mem_disp:1:0x20238f:i64', 'imm_occurrence:0xd4a:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd4a:mem_disp:1:0x20238f:i64', 'imm_occurrence:0xd4a:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd46`: `mov qword ptr [rbp - 0x20], rsi` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd51`: `mov rdx, rax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd54`: `lea rax, [rip + 0x2022e5]` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd46`      d46:	48 89 75 e0          	mov    %rsi,-0x20(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd4a`      d4a:	48 8b 05 8f 23 20 00 	mov    0x20238f(%rip),%rax        # 2030e0 <secret> groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xd51`      d51:	48 89 c2             	mov    %rax,%rdx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd54`      d54:	48 8d 05 e5 22 20 00 	lea    0x2022e5(%rip),%rax        # 203040 <array1> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:124` function=`main` pcs=`['0xd46']` groups=`['evidence_only']` kinds=`['evidence_only']`

```c
  122: ********************************************************************/
  123: #ifndef STAGE2_TEST_MAIN
  124: int main(int argc, const char **argv) {
  125:     size_t malicious_x = (size_t)(secret - (char *)array1);
  126:     int i;
```

- `/root/src/spectre_stage1_2_auto.c:125` function=`main` pcs=`['0xd4a', '0xd51', '0xd54']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
  123: #ifndef STAGE2_TEST_MAIN
  124: int main(int argc, const char **argv) {
  125:     size_t malicious_x = (size_t)(secret - (char *)array1);
  126:     int i;
  127: 
```

### 108. `imm_occurrence:0xd4a:mem_scale:1:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xd4a:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xd4a', 'operand_index': None, 'raw_suffix': 'mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xd4a:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xd4a']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xd4a']`
- direct_operand_pcs: `['0xd4a']`
- structural_role_pcs: `['0xd4a']`
- anchor_pcs: `['0xd4a']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd46', '0xd51', '0xd54']`
- all_mapped_pcs: `['0xd46', '0xd4a', '0xd51', '0xd54']`
- direct_parents: `[]`
- direct_children: `['var:secret']`

#### PC Relation Entries

- `0xd46` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd4a` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xd51` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd54` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xd4a`: `mov rax, qword ptr [rip + 0x20238f]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:125` function=`main`
  - use_objects: `['reg:rip', 'var:secret']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xd4a:mem_disp:1:0x20238f:i64', 'imm_occurrence:0xd4a:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd4a:mem_disp:1:0x20238f:i64', 'imm_occurrence:0xd4a:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd46`: `mov qword ptr [rbp - 0x20], rsi` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd51`: `mov rdx, rax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd54`: `lea rax, [rip + 0x2022e5]` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd46`      d46:	48 89 75 e0          	mov    %rsi,-0x20(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd4a`      d4a:	48 8b 05 8f 23 20 00 	mov    0x20238f(%rip),%rax        # 2030e0 <secret> groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xd51`      d51:	48 89 c2             	mov    %rax,%rdx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd54`      d54:	48 8d 05 e5 22 20 00 	lea    0x2022e5(%rip),%rax        # 203040 <array1> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:124` function=`main` pcs=`['0xd46']` groups=`['evidence_only']` kinds=`['evidence_only']`

```c
  122: ********************************************************************/
  123: #ifndef STAGE2_TEST_MAIN
  124: int main(int argc, const char **argv) {
  125:     size_t malicious_x = (size_t)(secret - (char *)array1);
  126:     int i;
```

- `/root/src/spectre_stage1_2_auto.c:125` function=`main` pcs=`['0xd4a', '0xd51', '0xd54']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
  123: #ifndef STAGE2_TEST_MAIN
  124: int main(int argc, const char **argv) {
  125:     size_t malicious_x = (size_t)(secret - (char *)array1);
  126:     int i;
  127: 
```

### 109. `imm_occurrence:0xd61:mem_disp:0:0xfffffffffffffff8:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xd61:mem_disp:0:0xfffffffffffffff8/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xd61', 'operand_index': None, 'raw_suffix': 'mem_disp:0:0xfffffffffffffff8/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xd61:mem_disp:0:0xfffffffffffffff8/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xd61']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xd61']`
- direct_operand_pcs: `['0xd61']`
- structural_role_pcs: `['0xd61']`
- anchor_pcs: `['0xd61']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd5b', '0xd5e']`
- all_mapped_pcs: `['0xd5b', '0xd5e', '0xd61']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x8]']`

#### PC Relation Entries

- `0xd5b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd5e` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd61` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`

#### Direct Anchor Instruction Evidence

- PC `0xd61`: `mov qword ptr [rbp - 8], rax` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:125` function=`main`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x8]']`
  - addr_objects: `['imm_occurrence:0xd61:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xd61:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd61:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xd61:mem_scale:0:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd5b`: `sub rdx, rax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd5e`: `mov rax, rdx` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd5b`      d5b:	48 29 c2             	sub    %rax,%rdx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd5e`      d5e:	48 89 d0             	mov    %rdx,%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd61`      d61:	48 89 45 f8          	mov    %rax,-0x8(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:125` function=`main` pcs=`['0xd5b', '0xd5e', '0xd61']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
  123: #ifndef STAGE2_TEST_MAIN
  124: int main(int argc, const char **argv) {
  125:     size_t malicious_x = (size_t)(secret - (char *)array1);
  126:     int i;
  127: 
```

### 110. `imm_occurrence:0xd61:mem_scale:0:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xd61:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xd61', 'operand_index': None, 'raw_suffix': 'mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xd61:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xd61']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xd61']`
- direct_operand_pcs: `['0xd61']`
- structural_role_pcs: `['0xd61']`
- anchor_pcs: `['0xd61']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd5b', '0xd5e']`
- all_mapped_pcs: `['0xd5b', '0xd5e', '0xd61']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x8]']`

#### PC Relation Entries

- `0xd5b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd5e` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd61` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`

#### Direct Anchor Instruction Evidence

- PC `0xd61`: `mov qword ptr [rbp - 8], rax` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:125` function=`main`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x8]']`
  - addr_objects: `['imm_occurrence:0xd61:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xd61:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd61:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xd61:mem_scale:0:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd5b`: `sub rdx, rax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd5e`: `mov rax, rdx` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd5b`      d5b:	48 29 c2             	sub    %rax,%rdx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd5e`      d5e:	48 89 d0             	mov    %rdx,%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd61`      d61:	48 89 45 f8          	mov    %rax,-0x8(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:125` function=`main` pcs=`['0xd5b', '0xd5e', '0xd61']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
  123: #ifndef STAGE2_TEST_MAIN
  124: int main(int argc, const char **argv) {
  125:     size_t malicious_x = (size_t)(secret - (char *)array1);
  126:     int i;
  127: 
```

### 111. `imm_occurrence:0xd65:mem_disp:0:0xfffffffffffffff0:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xd65:mem_disp:0:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xd65', 'operand_index': None, 'raw_suffix': 'mem_disp:0:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xd65:mem_disp:0:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xd65']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xd65']`
- direct_operand_pcs: `['0xd65']`
- structural_role_pcs: `['0xd65']`
- anchor_pcs: `['0xd65']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd6c']`
- all_mapped_pcs: `['0xd65', '0xd6c']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x10]']`

#### PC Relation Entries

- `0xd65` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xd6c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xd65`: `mov dword ptr [rbp - 0x10], 0` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:129` function=`main`
  - use_objects: `['imm_occurrence:0xd65:operand_imm:1:0x0:i32', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x10]']`
  - addr_objects: `['imm_occurrence:0xd65:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd65:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd65:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd65:mem_scale:0:0x1:i64', 'imm_occurrence:0xd65:operand_imm:1:0x0:i32']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd6c`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd65`      d65:	c7 45 f0 00 00 00 00 	movl   $0x0,-0x10(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xd6c`      d6c:	eb 15                	jmp    d83 <main+0x48> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:129` function=`main` pcs=`['0xd65']` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`

```c
  127: 
  128:     /* 初始化 array2 */
  129:     for (i = 0; i < (int)sizeof(array2); i++) {
  130:         array2[i] = 1;
  131:     }
```

### 112. `imm_occurrence:0xd65:mem_scale:0:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xd65:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xd65', 'operand_index': None, 'raw_suffix': 'mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xd65:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xd65']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xd65']`
- direct_operand_pcs: `['0xd65']`
- structural_role_pcs: `['0xd65']`
- anchor_pcs: `['0xd65']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd6c']`
- all_mapped_pcs: `['0xd65', '0xd6c']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x10]']`

#### PC Relation Entries

- `0xd65` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xd6c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xd65`: `mov dword ptr [rbp - 0x10], 0` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:129` function=`main`
  - use_objects: `['imm_occurrence:0xd65:operand_imm:1:0x0:i32', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x10]']`
  - addr_objects: `['imm_occurrence:0xd65:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd65:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd65:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd65:mem_scale:0:0x1:i64', 'imm_occurrence:0xd65:operand_imm:1:0x0:i32']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd6c`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd65`      d65:	c7 45 f0 00 00 00 00 	movl   $0x0,-0x10(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xd6c`      d6c:	eb 15                	jmp    d83 <main+0x48> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:129` function=`main` pcs=`['0xd65']` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`

```c
  127: 
  128:     /* 初始化 array2 */
  129:     for (i = 0; i < (int)sizeof(array2); i++) {
  130:         array2[i] = 1;
  131:     }
```

### 113. `imm_occurrence:0xd65:operand_imm:1:0x0:i32`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xd65:operand_imm:1:0x0/i32 [program_semantic_constant|store_constant]`
- Mapping kind: `store_constant`
- Confidence: `semantic`
- Object semantic tags: `['program_semantic_constant', 'store_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xd65', 'operand_index': None, 'raw_suffix': 'operand_imm:1:0x0/i32 [program_semantic_constant|store_constant]'}`
- Reason: 该 immediate 带有 store_constant 标签，更适合作为写入值常量解释。
- Candidate program elements: `['imm@0xd65:operand_imm:1:0x0/i32 [program_semantic_constant|store_constant]']`
- direct_use_pcs: `['0xd65']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xd65']`
- direct_operand_pcs: `['0xd65']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xd65']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd6c']`
- all_mapped_pcs: `['0xd65', '0xd6c']`
- direct_parents: `[]`
- direct_children: `['reg:rip', 'stack:[rbp-0x10]']`

#### PC Relation Entries

- `0xd65` kinds=`['direct_immediate_occurrence', 'direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.used_by/instruction_details.use_objects']`
- `0xd6c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xd65`: `mov dword ptr [rbp - 0x10], 0` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
  - Source: `/root/src/spectre_stage1_2_auto.c:129` function=`main`
  - use_objects: `['imm_occurrence:0xd65:operand_imm:1:0x0:i32', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x10]']`
  - addr_objects: `['imm_occurrence:0xd65:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd65:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd65:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd65:mem_scale:0:0x1:i64', 'imm_occurrence:0xd65:operand_imm:1:0x0:i32']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd6c`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd65`      d65:	c7 45 f0 00 00 00 00 	movl   $0x0,-0x10(%rbp) groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
- `0xd6c`      d6c:	eb 15                	jmp    d83 <main+0x48> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:129` function=`main` pcs=`['0xd65']` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`

```c
  127: 
  128:     /* 初始化 array2 */
  129:     for (i = 0; i < (int)sizeof(array2); i++) {
  130:         array2[i] = 1;
  131:     }
```

### 114. `imm_occurrence:0xd6c:operand_imm:0:0xd83:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xd6c:operand_imm:0:0xd83/i64`
- Mapping kind: `constant_or_address_component`
- Confidence: `structural`
- Object semantic tags: `[]`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xd6c', 'operand_index': None, 'raw_suffix': 'operand_imm:0:0xd83/i64'}`
- Reason: 对象类型为 imm，更适合作为常量、位移、scale、比较值或地址组成部分解释。
- Candidate program elements: `['imm@0xd6c:operand_imm:0:0xd83/i64']`
- direct_use_pcs: `['0xd6c']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `['0xd6c']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xd6c']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd65', '0xd6e']`
- all_mapped_pcs: `['0xd65', '0xd6c', '0xd6e']`
- direct_parents: `[]`
- direct_children: `['reg:rip']`

#### PC Relation Entries

- `0xd65` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd6c` kinds=`['direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['object_detail.used_by/instruction_details.use_objects']`
- `0xd6e` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xd6c`: `None` groups=`['direct_operand']` kinds=`['direct_use']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd65`: `mov dword ptr [rbp - 0x10], 0` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd6e`: `mov eax, dword ptr [rbp - 0x10]` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd65`      d65:	c7 45 f0 00 00 00 00 	movl   $0x0,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd6c`      d6c:	eb 15                	jmp    d83 <main+0x48> groups=`['direct_operand']` kinds=`['direct_use']`
- `0xd6e`      d6e:	8b 45 f0             	mov    -0x10(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:129` function=`main` pcs=`['0xd65']` groups=`['evidence_only']` kinds=`['evidence_only']`

```c
  127: 
  128:     /* 初始化 array2 */
  129:     for (i = 0; i < (int)sizeof(array2); i++) {
  130:         array2[i] = 1;
  131:     }
```

### 115. `imm_occurrence:0xd6e:mem_disp:1:0xfffffffffffffff0:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xd6e:mem_disp:1:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xd6e', 'operand_index': None, 'raw_suffix': 'mem_disp:1:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xd6e:mem_disp:1:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xd6e']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xd6e']`
- direct_operand_pcs: `['0xd6e']`
- structural_role_pcs: `['0xd6e']`
- anchor_pcs: `['0xd6e']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd6c', '0xd71', '0xd74']`
- all_mapped_pcs: `['0xd6c', '0xd6e', '0xd71', '0xd74']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x10]']`

#### PC Relation Entries

- `0xd6c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd6e` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xd71` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd74` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xd6e`: `mov eax, dword ptr [rbp - 0x10]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`main`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xd6e:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xd6e:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd6e:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xd6e:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd6c`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd71`: `movsxd rdx, eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd74`: `lea rax, [rip + 0x210545]` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd6c`      d6c:	eb 15                	jmp    d83 <main+0x48> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd6e`      d6e:	8b 45 f0             	mov    -0x10(%rbp),%eax groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xd71`      d71:	48 63 d0             	movslq %eax,%rdx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd74`      d74:	48 8d 05 45 05 21 00 	lea    0x210545(%rip),%rax        # 2112c0 <array2> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 116. `imm_occurrence:0xd6e:mem_scale:1:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xd6e:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xd6e', 'operand_index': None, 'raw_suffix': 'mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xd6e:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xd6e']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xd6e']`
- direct_operand_pcs: `['0xd6e']`
- structural_role_pcs: `['0xd6e']`
- anchor_pcs: `['0xd6e']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd6c', '0xd71', '0xd74']`
- all_mapped_pcs: `['0xd6c', '0xd6e', '0xd71', '0xd74']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x10]']`

#### PC Relation Entries

- `0xd6c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd6e` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xd71` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd74` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xd6e`: `mov eax, dword ptr [rbp - 0x10]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`main`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xd6e:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xd6e:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd6e:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xd6e:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd6c`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd71`: `movsxd rdx, eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd74`: `lea rax, [rip + 0x210545]` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd6c`      d6c:	eb 15                	jmp    d83 <main+0x48> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd6e`      d6e:	8b 45 f0             	mov    -0x10(%rbp),%eax groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xd71`      d71:	48 63 d0             	movslq %eax,%rdx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd74`      d74:	48 8d 05 45 05 21 00 	lea    0x210545(%rip),%rax        # 2112c0 <array2> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 117. `imm_occurrence:0xd7b:mem_disp:0:0x0:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xd7b:mem_disp:0:0x0/i64 [structural_abi_constant]`
- Mapping kind: `constant_or_address_component`
- Confidence: `structural`
- Object semantic tags: `['structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xd7b', 'operand_index': None, 'raw_suffix': 'mem_disp:0:0x0/i64 [structural_abi_constant]'}`
- Reason: 对象类型为 imm，更适合作为常量、位移、scale、比较值或地址组成部分解释。
- Candidate program elements: `['imm@0xd7b:mem_disp:0:0x0/i64 [structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xd7b']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xd7b']`
- direct_operand_pcs: `['0xd7b']`
- structural_role_pcs: `['0xd7b']`
- anchor_pcs: `['0xd7b']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd71', '0xd74', '0xd7f']`
- all_mapped_pcs: `['0xd71', '0xd74', '0xd7b', '0xd7f']`
- direct_parents: `[]`
- direct_children: `['var:array2']`

#### PC Relation Entries

- `0xd71` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd74` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd7b` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xd7f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xd7b`: `mov byte ptr [rdx + rax], 1` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`main`
  - use_objects: `['imm_occurrence:0xd7b:operand_imm:1:0x1:i8', 'reg:rax', 'reg:rdx']`
  - def_objects: `['reg:rip', 'var:array2']`
  - addr_objects: `['imm_occurrence:0xd7b:mem_disp:0:0x0:i64', 'imm_occurrence:0xd7b:mem_scale:0:0x1:i64', 'reg:rax', 'reg:rdx', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd7b:mem_disp:0:0x0:i64', 'imm_occurrence:0xd7b:mem_scale:0:0x1:i64', 'imm_occurrence:0xd7b:operand_imm:1:0x1:i8']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd71`: `movsxd rdx, eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd74`: `lea rax, [rip + 0x210545]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd7f`: `add dword ptr [rbp - 0x10], 1` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd71`      d71:	48 63 d0             	movslq %eax,%rdx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd74`      d74:	48 8d 05 45 05 21 00 	lea    0x210545(%rip),%rax        # 2112c0 <array2> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd7b`      d7b:	c6 04 02 01          	movb   $0x1,(%rdx,%rax,1) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xd7f`      d7f:	83 45 f0 01          	addl   $0x1,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 118. `imm_occurrence:0xd7b:mem_scale:0:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xd7b:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xd7b', 'operand_index': None, 'raw_suffix': 'mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xd7b:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xd7b']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xd7b']`
- direct_operand_pcs: `['0xd7b']`
- structural_role_pcs: `['0xd7b']`
- anchor_pcs: `['0xd7b']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd71', '0xd74', '0xd7f']`
- all_mapped_pcs: `['0xd71', '0xd74', '0xd7b', '0xd7f']`
- direct_parents: `[]`
- direct_children: `['var:array2']`

#### PC Relation Entries

- `0xd71` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd74` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd7b` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xd7f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xd7b`: `mov byte ptr [rdx + rax], 1` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`main`
  - use_objects: `['imm_occurrence:0xd7b:operand_imm:1:0x1:i8', 'reg:rax', 'reg:rdx']`
  - def_objects: `['reg:rip', 'var:array2']`
  - addr_objects: `['imm_occurrence:0xd7b:mem_disp:0:0x0:i64', 'imm_occurrence:0xd7b:mem_scale:0:0x1:i64', 'reg:rax', 'reg:rdx', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd7b:mem_disp:0:0x0:i64', 'imm_occurrence:0xd7b:mem_scale:0:0x1:i64', 'imm_occurrence:0xd7b:operand_imm:1:0x1:i8']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd71`: `movsxd rdx, eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd74`: `lea rax, [rip + 0x210545]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd7f`: `add dword ptr [rbp - 0x10], 1` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd71`      d71:	48 63 d0             	movslq %eax,%rdx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd74`      d74:	48 8d 05 45 05 21 00 	lea    0x210545(%rip),%rax        # 2112c0 <array2> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd7b`      d7b:	c6 04 02 01          	movb   $0x1,(%rdx,%rax,1) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xd7f`      d7f:	83 45 f0 01          	addl   $0x1,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 119. `imm_occurrence:0xd7b:operand_imm:1:0x1:i8`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xd7b:operand_imm:1:0x1/i8 [program_semantic_constant|store_constant]`
- Mapping kind: `store_constant`
- Confidence: `semantic`
- Object semantic tags: `['program_semantic_constant', 'store_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xd7b', 'operand_index': None, 'raw_suffix': 'operand_imm:1:0x1/i8 [program_semantic_constant|store_constant]'}`
- Reason: 该 immediate 带有 store_constant 标签，更适合作为写入值常量解释。
- Candidate program elements: `['imm@0xd7b:operand_imm:1:0x1/i8 [program_semantic_constant|store_constant]']`
- direct_use_pcs: `['0xd7b']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xd7b']`
- direct_operand_pcs: `['0xd7b']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xd7b']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd71', '0xd74', '0xd7f']`
- all_mapped_pcs: `['0xd71', '0xd74', '0xd7b', '0xd7f']`
- direct_parents: `[]`
- direct_children: `['reg:rip', 'var:array2']`

#### PC Relation Entries

- `0xd71` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd74` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd7b` kinds=`['direct_immediate_occurrence', 'direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.used_by/instruction_details.use_objects']`
- `0xd7f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xd7b`: `mov byte ptr [rdx + rax], 1` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`main`
  - use_objects: `['imm_occurrence:0xd7b:operand_imm:1:0x1:i8', 'reg:rax', 'reg:rdx']`
  - def_objects: `['reg:rip', 'var:array2']`
  - addr_objects: `['imm_occurrence:0xd7b:mem_disp:0:0x0:i64', 'imm_occurrence:0xd7b:mem_scale:0:0x1:i64', 'reg:rax', 'reg:rdx', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd7b:mem_disp:0:0x0:i64', 'imm_occurrence:0xd7b:mem_scale:0:0x1:i64', 'imm_occurrence:0xd7b:operand_imm:1:0x1:i8']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd71`: `movsxd rdx, eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd74`: `lea rax, [rip + 0x210545]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd7f`: `add dword ptr [rbp - 0x10], 1` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd71`      d71:	48 63 d0             	movslq %eax,%rdx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd74`      d74:	48 8d 05 45 05 21 00 	lea    0x210545(%rip),%rax        # 2112c0 <array2> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd7b`      d7b:	c6 04 02 01          	movb   $0x1,(%rdx,%rax,1) groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
- `0xd7f`      d7f:	83 45 f0 01          	addl   $0x1,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 120. `imm_occurrence:0xd7f:mem_disp:0:0xfffffffffffffff0:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xd7f:mem_disp:0:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xd7f', 'operand_index': None, 'raw_suffix': 'mem_disp:0:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xd7f:mem_disp:0:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xd7f']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xd7f']`
- direct_operand_pcs: `['0xd7f']`
- structural_role_pcs: `['0xd7f']`
- anchor_pcs: `['0xd7f']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd7b', '0xd83', '0xd8a']`
- all_mapped_pcs: `['0xd7b', '0xd7f', '0xd83', '0xd8a']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x10]']`

#### PC Relation Entries

- `0xd7b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd7f` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xd83` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd8a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xd7f`: `add dword ptr [rbp - 0x10], 1` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`main`
  - use_objects: `['imm_occurrence:0xd7f:operand_imm:1:0x1:i32', 'reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf', 'stack:[rbp-0x10]']`
  - addr_objects: `['imm_occurrence:0xd7f:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd7f:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd7f:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd7f:mem_scale:0:0x1:i64', 'imm_occurrence:0xd7f:operand_imm:1:0x1:i32']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd7b`: `mov byte ptr [rdx + rax], 1` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd83`: `cmp dword ptr [rbp - 0x10], 0x1ffff` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd8a`: `jle 0xd6e` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd7b`      d7b:	c6 04 02 01          	movb   $0x1,(%rdx,%rax,1) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd7f`      d7f:	83 45 f0 01          	addl   $0x1,-0x10(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xd83`      d83:	81 7d f0 ff ff 01 00 	cmpl   $0x1ffff,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd8a`      d8a:	7e e2                	jle    d6e <main+0x33> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 121. `imm_occurrence:0xd7f:mem_scale:0:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xd7f:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xd7f', 'operand_index': None, 'raw_suffix': 'mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xd7f:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xd7f']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xd7f']`
- direct_operand_pcs: `['0xd7f']`
- structural_role_pcs: `['0xd7f']`
- anchor_pcs: `['0xd7f']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd7b', '0xd83', '0xd8a']`
- all_mapped_pcs: `['0xd7b', '0xd7f', '0xd83', '0xd8a']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x10]']`

#### PC Relation Entries

- `0xd7b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd7f` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xd83` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd8a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xd7f`: `add dword ptr [rbp - 0x10], 1` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`main`
  - use_objects: `['imm_occurrence:0xd7f:operand_imm:1:0x1:i32', 'reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf', 'stack:[rbp-0x10]']`
  - addr_objects: `['imm_occurrence:0xd7f:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd7f:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd7f:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd7f:mem_scale:0:0x1:i64', 'imm_occurrence:0xd7f:operand_imm:1:0x1:i32']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd7b`: `mov byte ptr [rdx + rax], 1` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd83`: `cmp dword ptr [rbp - 0x10], 0x1ffff` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd8a`: `jle 0xd6e` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd7b`      d7b:	c6 04 02 01          	movb   $0x1,(%rdx,%rax,1) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd7f`      d7f:	83 45 f0 01          	addl   $0x1,-0x10(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xd83`      d83:	81 7d f0 ff ff 01 00 	cmpl   $0x1ffff,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd8a`      d8a:	7e e2                	jle    d6e <main+0x33> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 122. `imm_occurrence:0xd7f:operand_imm:1:0x1:i32`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xd7f:operand_imm:1:0x1/i32 [program_semantic_constant|store_constant]`
- Mapping kind: `store_constant`
- Confidence: `semantic`
- Object semantic tags: `['program_semantic_constant', 'store_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xd7f', 'operand_index': None, 'raw_suffix': 'operand_imm:1:0x1/i32 [program_semantic_constant|store_constant]'}`
- Reason: 该 immediate 带有 store_constant 标签，更适合作为写入值常量解释。
- Candidate program elements: `['imm@0xd7f:operand_imm:1:0x1/i32 [program_semantic_constant|store_constant]']`
- direct_use_pcs: `['0xd7f']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xd7f']`
- direct_operand_pcs: `['0xd7f']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xd7f']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd7b', '0xd83', '0xd8a']`
- all_mapped_pcs: `['0xd7b', '0xd7f', '0xd83', '0xd8a']`
- direct_parents: `[]`
- direct_children: `['reg:cf', 'reg:of', 'reg:rip', 'reg:sf', 'reg:zf', 'stack:[rbp-0x10]']`

#### PC Relation Entries

- `0xd7b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd7f` kinds=`['direct_immediate_occurrence', 'direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.used_by/instruction_details.use_objects']`
- `0xd83` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd8a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xd7f`: `add dword ptr [rbp - 0x10], 1` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`main`
  - use_objects: `['imm_occurrence:0xd7f:operand_imm:1:0x1:i32', 'reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf', 'stack:[rbp-0x10]']`
  - addr_objects: `['imm_occurrence:0xd7f:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd7f:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd7f:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd7f:mem_scale:0:0x1:i64', 'imm_occurrence:0xd7f:operand_imm:1:0x1:i32']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd7b`: `mov byte ptr [rdx + rax], 1` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd83`: `cmp dword ptr [rbp - 0x10], 0x1ffff` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd8a`: `jle 0xd6e` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd7b`      d7b:	c6 04 02 01          	movb   $0x1,(%rdx,%rax,1) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd7f`      d7f:	83 45 f0 01          	addl   $0x1,-0x10(%rbp) groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
- `0xd83`      d83:	81 7d f0 ff ff 01 00 	cmpl   $0x1ffff,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd8a`      d8a:	7e e2                	jle    d6e <main+0x33> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 123. `imm_occurrence:0xd83:mem_disp:0:0xfffffffffffffff0:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xd83:mem_disp:0:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xd83', 'operand_index': None, 'raw_suffix': 'mem_disp:0:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xd83:mem_disp:0:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xd83']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xd83']`
- direct_operand_pcs: `['0xd83']`
- structural_role_pcs: `['0xd83']`
- anchor_pcs: `['0xd83']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd7f', '0xd8a']`
- all_mapped_pcs: `['0xd7f', '0xd83', '0xd8a']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x10]']`

#### PC Relation Entries

- `0xd7f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd83` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xd8a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xd83`: `cmp dword ptr [rbp - 0x10], 0x1ffff` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`main`
  - use_objects: `['imm_occurrence:0xd83:operand_imm:1:0x1ffff:i32', 'reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xd83:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd83:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd83:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd83:mem_scale:0:0x1:i64', 'imm_occurrence:0xd83:operand_imm:1:0x1ffff:i32']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd7f`: `add dword ptr [rbp - 0x10], 1` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd8a`: `jle 0xd6e` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd7f`      d7f:	83 45 f0 01          	addl   $0x1,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd83`      d83:	81 7d f0 ff ff 01 00 	cmpl   $0x1ffff,-0x10(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xd8a`      d8a:	7e e2                	jle    d6e <main+0x33> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 124. `imm_occurrence:0xd83:mem_scale:0:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xd83:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xd83', 'operand_index': None, 'raw_suffix': 'mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xd83:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xd83']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xd83']`
- direct_operand_pcs: `['0xd83']`
- structural_role_pcs: `['0xd83']`
- anchor_pcs: `['0xd83']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd7f', '0xd8a']`
- all_mapped_pcs: `['0xd7f', '0xd83', '0xd8a']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x10]']`

#### PC Relation Entries

- `0xd7f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd83` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xd8a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xd83`: `cmp dword ptr [rbp - 0x10], 0x1ffff` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`main`
  - use_objects: `['imm_occurrence:0xd83:operand_imm:1:0x1ffff:i32', 'reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xd83:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd83:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd83:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd83:mem_scale:0:0x1:i64', 'imm_occurrence:0xd83:operand_imm:1:0x1ffff:i32']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd7f`: `add dword ptr [rbp - 0x10], 1` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd8a`: `jle 0xd6e` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd7f`      d7f:	83 45 f0 01          	addl   $0x1,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd83`      d83:	81 7d f0 ff ff 01 00 	cmpl   $0x1ffff,-0x10(%rbp) groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xd8a`      d8a:	7e e2                	jle    d6e <main+0x33> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 125. `imm_occurrence:0xd83:operand_imm:1:0x1ffff:i32`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xd83:operand_imm:1:0x1ffff/i32 [comparison_constant|program_semantic_constant]`
- Mapping kind: `comparison_constant`
- Confidence: `semantic`
- Object semantic tags: `['comparison_constant', 'loop_bound_constant', 'program_semantic_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xd83', 'operand_index': None, 'raw_suffix': 'operand_imm:1:0x1ffff/i32 [comparison_constant|program_semantic_constant]'}`
- Reason: 该 immediate 带有 comparison_constant 标签，更适合作为比较语义常量解释。
- Candidate program elements: `['imm@0xd83:operand_imm:1:0x1ffff/i32 [comparison_constant|program_semantic_constant]']`
- direct_use_pcs: `['0xd83']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xd83']`
- direct_operand_pcs: `['0xd83']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xd83']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd7f', '0xd8a']`
- all_mapped_pcs: `['0xd7f', '0xd83', '0xd8a']`
- direct_parents: `[]`
- direct_children: `['reg:cf', 'reg:of', 'reg:rip', 'reg:sf', 'reg:zf']`

#### PC Relation Entries

- `0xd7f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd83` kinds=`['direct_immediate_occurrence', 'direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.used_by/instruction_details.use_objects']`
- `0xd8a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xd83`: `cmp dword ptr [rbp - 0x10], 0x1ffff` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`main`
  - use_objects: `['imm_occurrence:0xd83:operand_imm:1:0x1ffff:i32', 'reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xd83:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd83:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd83:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd83:mem_scale:0:0x1:i64', 'imm_occurrence:0xd83:operand_imm:1:0x1ffff:i32']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd7f`: `add dword ptr [rbp - 0x10], 1` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd8a`: `jle 0xd6e` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd7f`      d7f:	83 45 f0 01          	addl   $0x1,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd83`      d83:	81 7d f0 ff ff 01 00 	cmpl   $0x1ffff,-0x10(%rbp) groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
- `0xd8a`      d8a:	7e e2                	jle    d6e <main+0x33> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 126. `imm_occurrence:0xd8a:operand_imm:0:0xd6e:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xd8a:operand_imm:0:0xd6e/i64`
- Mapping kind: `comparison_constant`
- Confidence: `semantic`
- Object semantic tags: `['comparison_constant']`
- Anchor instruction tags: `['argument_shuffle', 'callee_save_restore', 'callee_save_spill', 'conditional_branch', 'epilogue', 'prologue']`
- Scaffolding tags: `['argument_shuffle', 'callee_save_restore', 'callee_save_spill', 'epilogue', 'prologue']`
- Occurrence: `{'occurrence_pc': '0xd8a', 'operand_index': None, 'raw_suffix': 'operand_imm:0:0xd6e/i64'}`
- Reason: 该 immediate 带有 comparison_constant 标签，更适合作为比较语义常量解释。 检测到 ABI/脚手架标签：argument_shuffle, callee_save_restore, callee_save_spill, epilogue, prologue，应更偏向解释为结构性对象，而非优先可变异语义对象。
- Candidate program elements: `['imm@0xd8a:operand_imm:0:0xd6e/i64']`
- direct_use_pcs: `['0xd8a']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `['0xb7a', '0xb7b', '0xb7e', '0xb82', '0xb86', '0xb8b', '0xb91', '0xb93', '0xb97', '0xb99', '0xba0', '0xba4', '0xba7', '0xbaa', '0xbad', '0xbb0', '0xbb3', '0xbba', '0xbbe', '0xbc5', '0xbc7', '0xbcd', '0xbd2', '0xbd3', '0xbd4', '0xbf5', '0xbf6', '0xbf9', '0xbfd', '0xc01', '0xc08', '0xc0d', '0xc10', '0xc11', '0xc14', '0xc16', '0xc19', '0xc1b', '0xc1d', '0xc21', '0xc28', '0xc2c', '0xc30', '0xc33', '0xc3a', '0xc3c', '0xc3f', '0xc42', '0xc45', '0xc48', '0xc4d', '0xc4f', '0xc52', '0xc57', '0xc59', '0xc5b', '0xc5d', '0xc60', '0xc62', '0xc64', '0xc66', '0xc68', '0xc6a', '0xc6c', '0xc6e', '0xc71', '0xc75', '0xc77', '0xc7b', '0xc7f', '0xc83', '0xc87', '0xc8b', '0xc8f', '0xc93', '0xc97', '0xc9b', '0xc9f', '0xca2', '0xca7', '0xcab', '0xcaf', '0xcb5', '0xcb6', '0xcb7', '0xd6e', '0xd71', '0xd74', '0xd7b', '0xd7f', '0xd83', '0xd8c', '0xd90', '0xd93', '0xd98', '0xd9d', '0xda0', '0xda7', '0xdd0', '0xdd3', '0xdd6', '0xdd8', '0xddd', '0xde2', '0xde3', '0xf0c', '0xf0d', '0xf10', '0xf16', '0xf17', '0x150b', '0x150c', '0x150f', '0x1515', '0x1517', '0x1577', '0x1578', '0x1579', '0x157a', '0x157b', '0x157e', '0x1582', '0x1588', '0x158a', '0x168e', '0x168f', '0x1690', '0x1691', '0x1692', '0x1695', '0x1699', '0x16a0', '0x1730', '0x1736', '0x1739', '0x173f', '0x1740', '0x1741']`
- direct_imm_pcs: `['0xd8a']`
- direct_operand_pcs: `['0xd8a']`
- structural_role_pcs: `['0xb7a', '0xb7b', '0xb7e', '0xb82', '0xb86', '0xb8b', '0xb91', '0xb93', '0xb97', '0xb99', '0xba0', '0xba4', '0xba7', '0xbaa', '0xbad', '0xbb0', '0xbb3', '0xbba', '0xbbe', '0xbc5', '0xbc7', '0xbcd', '0xbd2', '0xbd3', '0xbd4', '0xbf5', '0xbf6', '0xbf9', '0xbfd', '0xc01', '0xc08', '0xc0d', '0xc10', '0xc11', '0xc14', '0xc16', '0xc19', '0xc1b', '0xc1d', '0xc21', '0xc28', '0xc2c', '0xc30', '0xc33', '0xc3a', '0xc3c', '0xc3f', '0xc42', '0xc45', '0xc48', '0xc4d', '0xc4f', '0xc52', '0xc57', '0xc59', '0xc5b', '0xc5d', '0xc60', '0xc62', '0xc64', '0xc66', '0xc68', '0xc6a', '0xc6c', '0xc6e', '0xc71', '0xc75', '0xc77', '0xc7b', '0xc7f', '0xc83', '0xc87', '0xc8b', '0xc8f', '0xc93', '0xc97', '0xc9b', '0xc9f', '0xca2', '0xca7', '0xcab', '0xcaf', '0xcb5', '0xcb6', '0xcb7', '0xd6e', '0xd71', '0xd74', '0xd7b', '0xd7f', '0xd83', '0xd8c', '0xd90', '0xd93', '0xd98', '0xd9d', '0xda0', '0xda7', '0xdd0', '0xdd3', '0xdd6', '0xdd8', '0xddd', '0xde2', '0xde3', '0xf0c', '0xf0d', '0xf10', '0xf16', '0xf17', '0x150b', '0x150c', '0x150f', '0x1515', '0x1517', '0x1577', '0x1578', '0x1579', '0x157a', '0x157b', '0x157e', '0x1582', '0x1588', '0x158a', '0x168e', '0x168f', '0x1690', '0x1691', '0x1692', '0x1695', '0x1699', '0x16a0', '0x1730', '0x1736', '0x1739', '0x173f', '0x1740', '0x1741']`
- anchor_pcs: `['0xb7a', '0xb7b', '0xb7e', '0xb82', '0xb86', '0xb8b', '0xb91', '0xb93', '0xb97', '0xb99', '0xba0', '0xba4', '0xba7', '0xbaa', '0xbad', '0xbb0', '0xbb3', '0xbba', '0xbbe', '0xbc5', '0xbc7', '0xbcd', '0xbd2', '0xbd3', '0xbd4', '0xbf5', '0xbf6', '0xbf9', '0xbfd', '0xc01', '0xc08', '0xc0d', '0xc10', '0xc11', '0xc14', '0xc16', '0xc19', '0xc1b', '0xc1d', '0xc21', '0xc28', '0xc2c', '0xc30', '0xc33', '0xc3a', '0xc3c', '0xc3f', '0xc42', '0xc45', '0xc48', '0xc4d', '0xc4f', '0xc52', '0xc57', '0xc59', '0xc5b', '0xc5d', '0xc60', '0xc62', '0xc64', '0xc66', '0xc68', '0xc6a', '0xc6c', '0xc6e', '0xc71', '0xc75', '0xc77', '0xc7b', '0xc7f', '0xc83', '0xc87', '0xc8b', '0xc8f', '0xc93', '0xc97', '0xc9b', '0xc9f', '0xca2', '0xca7', '0xcab', '0xcaf', '0xcb5', '0xcb6', '0xcb7', '0xd6e', '0xd71', '0xd74', '0xd7b', '0xd7f', '0xd83', '0xd8a', '0xd8c', '0xd90', '0xd93', '0xd98', '0xd9d', '0xda0', '0xda7', '0xdd0', '0xdd3', '0xdd6', '0xdd8', '0xddd', '0xde2', '0xde3', '0xf0c', '0xf0d', '0xf10', '0xf16', '0xf17', '0x150b', '0x150c', '0x150f', '0x1515', '0x1517', '0x1577', '0x1578', '0x1579', '0x157a', '0x157b', '0x157e', '0x1582', '0x1588', '0x158a', '0x168e', '0x168f', '0x1690', '0x1691', '0x1692', '0x1695', '0x1699', '0x16a0', '0x1730', '0x1736', '0x1739', '0x173f', '0x1740', '0x1741']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd6c', '0xdcc', '0x1519', '0x151f', '0x156e', '0x1575', '0x1590', '0x1596', '0x1686', '0x168c', '0x16a5', '0x16a8', '0x1727', '0x172c']`
- all_mapped_pcs: `['0xb7a', '0xb7b', '0xb7e', '0xb82', '0xb86', '0xb8b', '0xb91', '0xb93', '0xb97', '0xb99', '0xba0', '0xba4', '0xba7', '0xbaa', '0xbad', '0xbb0', '0xbb3', '0xbba', '0xbbe', '0xbc5', '0xbc7', '0xbcd', '0xbd2', '0xbd3', '0xbd4', '0xbf5', '0xbf6', '0xbf9', '0xbfd', '0xc01', '0xc08', '0xc0d', '0xc10', '0xc11', '0xc14', '0xc16', '0xc19', '0xc1b', '0xc1d', '0xc21', '0xc28', '0xc2c', '0xc30', '0xc33', '0xc3a', '0xc3c', '0xc3f', '0xc42', '0xc45', '0xc48', '0xc4d', '0xc4f', '0xc52', '0xc57', '0xc59', '0xc5b', '0xc5d', '0xc60', '0xc62', '0xc64', '0xc66', '0xc68', '0xc6a', '0xc6c', '0xc6e', '0xc71', '0xc75', '0xc77', '0xc7b', '0xc7f', '0xc83', '0xc87', '0xc8b', '0xc8f', '0xc93', '0xc97', '0xc9b', '0xc9f', '0xca2', '0xca7', '0xcab', '0xcaf', '0xcb5', '0xcb6', '0xcb7', '0xd6c', '0xd6e', '0xd71', '0xd74', '0xd7b', '0xd7f', '0xd83', '0xd8a', '0xd8c', '0xd90', '0xd93', '0xd98', '0xd9d', '0xda0', '0xda7', '0xdcc', '0xdd0', '0xdd3', '0xdd6', '0xdd8', '0xddd', '0xde2', '0xde3', '0xf0c', '0xf0d', '0xf10', '0xf16', '0xf17', '0x150b', '0x150c', '0x150f', '0x1515', '0x1517', '0x1519', '0x151f', '0x156e', '0x1575', '0x1577', '0x1578', '0x1579', '0x157a', '0x157b', '0x157e', '0x1582', '0x1588', '0x158a', '0x1590', '0x1596', '0x1686', '0x168c', '0x168e', '0x168f', '0x1690', '0x1691', '0x1692', '0x1695', '0x1699', '0x16a0', '0x16a5', '0x16a8', '0x1727', '0x172c', '0x1730', '0x1736', '0x1739', '0x173f', '0x1740', '0x1741']`
- direct_parents: `[]`
- direct_children: `['reg:cf', 'reg:of', 'reg:rax', 'reg:rbp', 'reg:rcx', 'reg:rdi', 'reg:rdx', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf', 'stack:[rbp-0x10]', 'stack:[rbp-0x18]', 'stack:[rbp-0x1c]', 'stack:[rbp-0x20]', 'stack:[rbp-0x28]', 'stack:[rbp-0x30]', 'stack:[rbp-0x38]', 'stack:[rbp-0x40]', 'stack:[rbp-0x4]', 'stack:[rbp-0x8]', 'stack:[rbp-0xc]', 'var:array2', 'var:temp']`

#### PC Relation Entries

- `0xb7a` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xb7b` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xb7e` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xb82` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xb86` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xb8b` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xb91` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xb93` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xb97` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xb99` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xba0` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xba4` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xba7` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbaa` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbad` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbb0` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbb3` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbba` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbbe` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbc5` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbc7` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbcd` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbd2` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbd3` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbd4` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbf5` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbf6` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbf9` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xbfd` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc01` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc08` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc0d` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc10` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc11` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc14` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc16` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc19` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc1b` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc1d` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc21` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc28` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc2c` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc30` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc33` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc3a` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc3c` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc3f` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc42` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc45` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc48` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc4d` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc4f` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc52` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc57` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc59` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc5b` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc5d` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc60` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc62` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc64` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc66` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc68` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc6a` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc6c` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc6e` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc71` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc75` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc77` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc7b` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc7f` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc83` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc87` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc8b` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc8f` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc93` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc97` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc9b` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xc9f` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xca2` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xca7` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xcab` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xcaf` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xcb5` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xcb6` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xcb7` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xd6c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd6e` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xd71` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xd74` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xd7b` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xd7f` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xd83` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xd8a` kinds=`['direct_immediate_occurrence', 'direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.used_by/instruction_details.use_objects']`
- `0xd8c` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xd90` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xd93` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xd98` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xd9d` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xda0` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xda7` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xdcc` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xdd0` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xdd3` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xdd6` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xdd8` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xddd` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xde2` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xde3` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xf0c` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xf0d` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xf10` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xf16` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xf17` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x150b` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x150c` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x150f` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1515` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1517` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1519` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x151f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x156e` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1575` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1577` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1578` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1579` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x157a` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x157b` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x157e` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1582` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1588` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x158a` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1590` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1596` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1686` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x168c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x168e` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x168f` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1690` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1691` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1692` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1695` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1699` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x16a0` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x16a5` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x16a8` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1727` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x172c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1730` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1736` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1739` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x173f` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1740` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1741` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`

#### Direct Anchor Instruction Evidence

- PC `0xb7a`: `push rbp` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:58` function=`spectre_function`
  - instruction_semantic_tags: `['callee_save_spill', 'prologue']`
  - use_objects: `['reg:rbp', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x40]']`
- PC `0xb7b`: `mov rbp, rsp` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:58` function=`spectre_function`
  - instruction_semantic_tags: `['prologue']`
  - use_objects: `['reg:rsp']`
  - def_objects: `['reg:rbp', 'reg:rip']`
- PC `0xb7e`: `sub rsp, 0x10` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:58` function=`spectre_function`
  - instruction_semantic_tags: `['prologue']`
  - use_objects: `['imm_occurrence:0xb7e:operand_imm:1:0x10:i64', 'reg:rsp']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xb7e:operand_imm:1:0x10:i64']`
- PC `0xb82`: `mov qword ptr [rbp - 8], rdi` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:58` function=`spectre_function`
  - instruction_semantic_tags: `['argument_shuffle']`
  - use_objects: `['reg:rbp', 'reg:rdi']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x8]']`
  - addr_objects: `['imm_occurrence:0xb82:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xb82:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xb82:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xb82:mem_scale:0:0x1:i64']`
- PC `0xb86`: `call 0x150b` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:60` function=`spectre_function`
  - call_target: `{'operand': '0x150b', 'resolved_symbol': 'pmu_uops_snap_before', 'call_kind': 'direct_call_symbol', 'display_target': 'pmu_uops_snap_before'}`
  - use_objects: `['imm_occurrence:0xb86:operand_imm:0:0x150b:i64', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x18]']`
  - immediates: `['imm_occurrence:0xb86:operand_imm:0:0x150b:i64']`
- PC `0xb8b`: `mov eax, dword ptr [rip + 0x20248f]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function`
  - use_objects: `['reg:rip', 'var:array1_size']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xb8b:mem_disp:1:0x20248f:i64', 'imm_occurrence:0xb8b:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xb8b:mem_disp:1:0x20248f:i64', 'imm_occurrence:0xb8b:mem_scale:1:0x1:i64']`
- PC `0xb91`: `mov eax, eax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:rax', 'reg:rip']`
- PC `0xb93`: `cmp qword ptr [rbp - 8], rax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x8]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xb93:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xb93:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xb93:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xb93:mem_scale:0:0x1:i64']`
- PC `0xb97`: `jae 0xbcd` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function`
  - instruction_semantic_tags: `['conditional_branch']`
  - use_objects: `['imm_occurrence:0xb97:operand_imm:0:0xbcd:i64', 'reg:cf']`
  - def_objects: `['reg:rip']`
  - immediates: `['imm_occurrence:0xb97:operand_imm:0:0xbcd:i64']`
- PC `0xb99`: `lea rdx, [rip + 0x2024a0]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rip']`
  - def_objects: `['reg:rdx', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xb99:mem_disp:1:0x2024a0:i64', 'imm_occurrence:0xb99:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xb99:mem_disp:1:0x2024a0:i64', 'imm_occurrence:0xb99:mem_scale:1:0x1:i64']`
- PC `0xba0`: `mov rax, qword ptr [rbp - 8]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x8]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xba0:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xba0:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xba0:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xba0:mem_scale:1:0x1:i64']`
- PC `0xba4`: `add rax, rdx` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rdx']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0xba7`: `movzx eax, byte ptr [rax]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'var:array1']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xba7:mem_disp:1:0x0:i64', 'imm_occurrence:0xba7:mem_scale:1:0x1:i64', 'reg:rax', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xba7:mem_disp:1:0x0:i64', 'imm_occurrence:0xba7:mem_scale:1:0x1:i64']`
- PC `0xbaa`: `movzx eax, al` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:rax', 'reg:rip']`
- PC `0xbad`: `shl eax, 9` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['imm_occurrence:0xbad:operand_imm:1:0x9:i8', 'reg:rax']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xbad:operand_imm:1:0x9:i8']`
- PC `0xbb0`: `movsxd rdx, eax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:rdx', 'reg:rip']`
- PC `0xbb3`: `lea rax, [rip + 0x210706]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rip']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xbb3:mem_disp:1:0x210706:i64', 'imm_occurrence:0xbb3:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xbb3:mem_disp:1:0x210706:i64', 'imm_occurrence:0xbb3:mem_scale:1:0x1:i64']`
- PC `0xbba`: `movzx edx, byte ptr [rdx + rax]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rdx', 'var:array2']`
  - def_objects: `['reg:rdx', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xbba:mem_disp:1:0x0:i64', 'imm_occurrence:0xbba:mem_scale:1:0x1:i64', 'reg:rax', 'reg:rdx', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xbba:mem_disp:1:0x0:i64', 'imm_occurrence:0xbba:mem_scale:1:0x1:i64']`
- PC `0xbbe`: `movzx eax, byte ptr [rip + 0x202544]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rip', 'var:temp']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xbbe:mem_disp:1:0x202544:i64', 'imm_occurrence:0xbbe:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xbbe:mem_disp:1:0x202544:i64', 'imm_occurrence:0xbbe:mem_scale:1:0x1:i64']`
- PC `0xbc5`: `and eax, edx` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rdx']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0xbc7`: `mov byte ptr [rip + 0x20253c], al` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rip']`
  - def_objects: `['reg:rip', 'var:temp']`
  - addr_objects: `['imm_occurrence:0xbc7:mem_disp:0:0x20253c:i64', 'imm_occurrence:0xbc7:mem_scale:0:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xbc7:mem_disp:0:0x20253c:i64', 'imm_occurrence:0xbc7:mem_scale:0:0x1:i64']`
- PC `0xbcd`: `call 0x157a` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:70` function=`spectre_function`
  - call_target: `{'operand': '0x157a', 'resolved_symbol': 'pmu_uops_snap_after', 'call_kind': 'direct_call_symbol', 'display_target': 'pmu_uops_snap_after'}`
  - use_objects: `['imm_occurrence:0xbcd:operand_imm:0:0x157a:i64', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x18]']`
  - immediates: `['imm_occurrence:0xbcd:operand_imm:0:0x157a:i64']`
- PC `0xbd2`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xbd3`: `leave` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:71` function=`spectre_function`
  - instruction_semantic_tags: `['epilogue']`
  - use_objects: `['reg:rbp', 'reg:rsp', 'stack:[rbp-0x40]']`
  - def_objects: `['reg:rbp', 'reg:rip', 'reg:rsp']`
- PC `0xbd4`: `ret` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:71` function=`spectre_function`
  - use_objects: `['reg:rsp', 'stack:[rbp-0x38]']`
  - def_objects: `['reg:rip', 'reg:rsp']`
- PC `0xbf5`: `push rbp` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:88` function=`stage1_mistrain_trigger`
  - instruction_semantic_tags: `['callee_save_spill', 'prologue']`
  - use_objects: `['reg:rbp', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x30]']`
- PC `0xbf6`: `mov rbp, rsp` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:88` function=`stage1_mistrain_trigger`
  - instruction_semantic_tags: `['prologue']`
  - use_objects: `['reg:rsp']`
  - def_objects: `['reg:rbp', 'reg:rip']`
- PC `0xbf9`: `sub rsp, 0x30` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:88` function=`stage1_mistrain_trigger`
  - instruction_semantic_tags: `['prologue']`
  - use_objects: `['imm_occurrence:0xbf9:operand_imm:1:0x30:i64', 'reg:rsp']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xbf9:operand_imm:1:0x30:i64']`
- PC `0xbfd`: `mov qword ptr [rbp - 0x28], rdi` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:88` function=`stage1_mistrain_trigger`
  - instruction_semantic_tags: `['argument_shuffle']`
  - use_objects: `['reg:rbp', 'reg:rdi']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x28]']`
  - addr_objects: `['imm_occurrence:0xbfd:mem_disp:0:0xffffffffffffffd8:i64', 'imm_occurrence:0xbfd:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xbfd:mem_disp:0:0xffffffffffffffd8:i64', 'imm_occurrence:0xbfd:mem_scale:0:0x1:i64']`
- PC `0xc01`: `mov dword ptr [rbp - 0x1c], 0x1d` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:92` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc01:operand_imm:1:0x1d:i32', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x1c]']`
  - addr_objects: `['imm_occurrence:0xc01:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xc01:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc01:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xc01:mem_scale:0:0x1:i64', 'imm_occurrence:0xc01:operand_imm:1:0x1d:i32']`
- PC `0xc08`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc0d`: `mov eax, dword ptr [rbp - 0x1c]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x1c]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc0d:mem_disp:1:0xffffffffffffffe4:i64', 'imm_occurrence:0xc0d:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc0d:mem_disp:1:0xffffffffffffffe4:i64', 'imm_occurrence:0xc0d:mem_scale:1:0x1:i64']`
- PC `0xc10`: `cdq` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:rdx', 'reg:rip']`
- PC `0xc11`: `shr edx, 0x1c` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc11:operand_imm:1:0x1c:i8', 'reg:rdx']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rdx', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xc11:operand_imm:1:0x1c:i8']`
- PC `0xc14`: `add eax, edx` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rdx']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0xc16`: `and eax, 0xf` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc16:operand_imm:1:0xf:i32', 'reg:rax']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xc16:operand_imm:1:0xf:i32']`
- PC `0xc19`: `sub eax, edx` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rdx']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0xc1b`: `cdqe` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:rax', 'reg:rip']`
- PC `0xc1d`: `mov qword ptr [rbp - 0x18], rax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x18]']`
  - addr_objects: `['imm_occurrence:0xc1d:mem_disp:0:0xffffffffffffffe8:i64', 'imm_occurrence:0xc1d:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc1d:mem_disp:0:0xffffffffffffffe8:i64', 'imm_occurrence:0xc1d:mem_scale:0:0x1:i64']`
- PC `0xc21`: `lea rax, [rip + 0x2023f8]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rip']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc21:mem_disp:1:0x2023f8:i64', 'imm_occurrence:0xc21:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc21:mem_disp:1:0x2023f8:i64', 'imm_occurrence:0xc21:mem_scale:1:0x1:i64']`
- PC `0xc28`: `mov qword ptr [rbp - 8], rax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x8]']`
  - addr_objects: `['imm_occurrence:0xc28:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xc28:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc28:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xc28:mem_scale:0:0x1:i64']`
- PC `0xc2c`: `mov rax, qword ptr [rbp - 8]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/usr/lib/gcc/x86_64-linux-gnu/7/include/emmintrin.h:1486` function=`_mm_clflush`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x8]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc2c:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xc2c:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc2c:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xc2c:mem_scale:1:0x1:i64']`
- PC `0xc30`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc33`: `mov dword ptr [rbp - 0x20], 0` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:95` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc33:operand_imm:1:0x0:i32', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x20]']`
  - addr_objects: `['imm_occurrence:0xc33:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xc33:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc33:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xc33:mem_scale:0:0x1:i64', 'imm_occurrence:0xc33:operand_imm:1:0x0:i32']`
- PC `0xc3a`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc3c`: `mov eax, dword ptr [rbp - 0x20]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x20]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc3c:mem_disp:1:0xffffffffffffffe0:i64', 'imm_occurrence:0xc3c:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc3c:mem_disp:1:0xffffffffffffffe0:i64', 'imm_occurrence:0xc3c:mem_scale:1:0x1:i64']`
- PC `0xc3f`: `add eax, 1` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc3f:operand_imm:1:0x1:i32', 'reg:rax']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xc3f:operand_imm:1:0x1:i32']`
- PC `0xc42`: `mov dword ptr [rbp - 0x20], eax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x20]']`
  - addr_objects: `['imm_occurrence:0xc42:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xc42:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc42:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xc42:mem_scale:0:0x1:i64']`
- PC `0xc45`: `mov eax, dword ptr [rbp - 0x20]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x20]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc45:mem_disp:1:0xffffffffffffffe0:i64', 'imm_occurrence:0xc45:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc45:mem_disp:1:0xffffffffffffffe0:i64', 'imm_occurrence:0xc45:mem_scale:1:0x1:i64']`
- PC `0xc48`: `cmp eax, 0xc7` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc48:operand_imm:1:0xc7:i32', 'reg:rax']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xc48:operand_imm:1:0xc7:i32']`
- PC `0xc4d`: `jle 0xc3c` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - instruction_semantic_tags: `['conditional_branch']`
  - use_objects: `['imm_occurrence:0xc4d:operand_imm:0:0xc3c:i64', 'reg:of', 'reg:sf', 'reg:zf']`
  - def_objects: `['reg:rip']`
  - immediates: `['imm_occurrence:0xc4d:operand_imm:0:0xc3c:i64']`
- PC `0xc4f`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc52`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc57`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc59`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc5b`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc5d`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc60`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc62`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc64`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc66`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc68`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc6a`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc6c`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc6e`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xc71`: `mov ax, 0` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc71:operand_imm:1:0x0:i16']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - immediates: `['imm_occurrence:0xc71:operand_imm:1:0x0:i16']`
- PC `0xc75`: `cdqe` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:rax', 'reg:rip']`
- PC `0xc77`: `mov qword ptr [rbp - 0x10], rax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x10]']`
  - addr_objects: `['imm_occurrence:0xc77:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc77:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc77:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc77:mem_scale:0:0x1:i64']`
- PC `0xc7b`: `mov rax, qword ptr [rbp - 0x10]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc7b:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc7b:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc7b:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc7b:mem_scale:1:0x1:i64']`
- PC `0xc7f`: `shr rax, 0x10` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc7f:operand_imm:1:0x10:i8', 'reg:rax']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xc7f:operand_imm:1:0x10:i8']`
- PC `0xc83`: `or qword ptr [rbp - 0x10], rax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf', 'stack:[rbp-0x10]']`
  - addr_objects: `['imm_occurrence:0xc83:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc83:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc83:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc83:mem_scale:0:0x1:i64']`
- PC `0xc87`: `mov rax, qword ptr [rbp - 0x28]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x28]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc87:mem_disp:1:0xffffffffffffffd8:i64', 'imm_occurrence:0xc87:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc87:mem_disp:1:0xffffffffffffffd8:i64', 'imm_occurrence:0xc87:mem_scale:1:0x1:i64']`
- PC `0xc8b`: `xor rax, qword ptr [rbp - 0x18]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x18]']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xc8b:mem_disp:1:0xffffffffffffffe8:i64', 'imm_occurrence:0xc8b:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc8b:mem_disp:1:0xffffffffffffffe8:i64', 'imm_occurrence:0xc8b:mem_scale:1:0x1:i64']`
- PC `0xc8f`: `and rax, qword ptr [rbp - 0x10]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xc8f:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc8f:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc8f:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc8f:mem_scale:1:0x1:i64']`
- PC `0xc93`: `xor rax, qword ptr [rbp - 0x18]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x18]']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xc93:mem_disp:1:0xffffffffffffffe8:i64', 'imm_occurrence:0xc93:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc93:mem_disp:1:0xffffffffffffffe8:i64', 'imm_occurrence:0xc93:mem_scale:1:0x1:i64']`
- PC `0xc97`: `mov qword ptr [rbp - 0x10], rax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x10]']`
  - addr_objects: `['imm_occurrence:0xc97:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc97:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc97:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc97:mem_scale:0:0x1:i64']`
- PC `0xc9b`: `mov rax, qword ptr [rbp - 0x10]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc9b:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc9b:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc9b:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc9b:mem_scale:1:0x1:i64']`
- PC `0xc9f`: `mov rdi, rax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:rdi', 'reg:rip']`
- PC `0xca2`: `call 0xb7a` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - call_target: `{'operand': '0xb7a', 'resolved_symbol': 'spectre_function', 'call_kind': 'direct_call_symbol', 'display_target': 'spectre_function'}`
  - use_objects: `['imm_occurrence:0xca2:operand_imm:0:0xb7a:i64', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x38]']`
  - immediates: `['imm_occurrence:0xca2:operand_imm:0:0xb7a:i64']`
- PC `0xca7`: `sub dword ptr [rbp - 0x1c], 1` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xca7:operand_imm:1:0x1:i32', 'reg:rbp', 'stack:[rbp-0x1c]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf', 'stack:[rbp-0x1c]']`
  - addr_objects: `['imm_occurrence:0xca7:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xca7:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xca7:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xca7:mem_scale:0:0x1:i64', 'imm_occurrence:0xca7:operand_imm:1:0x1:i32']`
- PC `0xcab`: `cmp dword ptr [rbp - 0x1c], 0` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xcab:operand_imm:1:0x0:i32', 'reg:rbp', 'stack:[rbp-0x1c]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xcab:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xcab:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xcab:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xcab:mem_scale:0:0x1:i64', 'imm_occurrence:0xcab:operand_imm:1:0x0:i32']`
- PC `0xcaf`: `jns 0xc0d` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - instruction_semantic_tags: `['conditional_branch']`
  - use_objects: `['imm_occurrence:0xcaf:operand_imm:0:0xc0d:i64', 'reg:sf']`
  - def_objects: `['reg:rip']`
  - immediates: `['imm_occurrence:0xcaf:operand_imm:0:0xc0d:i64']`
- PC `0xcb5`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xcb6`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xcb7`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xd6e`: `mov eax, dword ptr [rbp - 0x10]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`main`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xd6e:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xd6e:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd6e:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xd6e:mem_scale:1:0x1:i64']`
- PC `0xd71`: `movsxd rdx, eax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`main`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:rdx', 'reg:rip']`
- PC `0xd74`: `lea rax, [rip + 0x210545]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`main`
  - use_objects: `['reg:rip']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xd74:mem_disp:1:0x210545:i64', 'imm_occurrence:0xd74:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd74:mem_disp:1:0x210545:i64', 'imm_occurrence:0xd74:mem_scale:1:0x1:i64']`
- PC `0xd7b`: `mov byte ptr [rdx + rax], 1` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`main`
  - use_objects: `['imm_occurrence:0xd7b:operand_imm:1:0x1:i8', 'reg:rax', 'reg:rdx']`
  - def_objects: `['reg:rip', 'var:array2']`
  - addr_objects: `['imm_occurrence:0xd7b:mem_disp:0:0x0:i64', 'imm_occurrence:0xd7b:mem_scale:0:0x1:i64', 'reg:rax', 'reg:rdx', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd7b:mem_disp:0:0x0:i64', 'imm_occurrence:0xd7b:mem_scale:0:0x1:i64', 'imm_occurrence:0xd7b:operand_imm:1:0x1:i8']`
- PC `0xd7f`: `add dword ptr [rbp - 0x10], 1` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`main`
  - use_objects: `['imm_occurrence:0xd7f:operand_imm:1:0x1:i32', 'reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf', 'stack:[rbp-0x10]']`
  - addr_objects: `['imm_occurrence:0xd7f:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd7f:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd7f:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd7f:mem_scale:0:0x1:i64', 'imm_occurrence:0xd7f:operand_imm:1:0x1:i32']`
- PC `0xd83`: `cmp dword ptr [rbp - 0x10], 0x1ffff` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`main`
  - use_objects: `['imm_occurrence:0xd83:operand_imm:1:0x1ffff:i32', 'reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xd83:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd83:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd83:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd83:mem_scale:0:0x1:i64', 'imm_occurrence:0xd83:operand_imm:1:0x1ffff:i32']`
- PC `0xd8a`: `jle 0xd6e` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`main`
  - instruction_semantic_tags: `['conditional_branch']`
  - use_objects: `['imm_occurrence:0xd8a:operand_imm:0:0xd6e:i64', 'reg:of', 'reg:sf', 'reg:zf']`
  - def_objects: `['reg:rip']`
  - immediates: `['imm_occurrence:0xd8a:operand_imm:0:0xd6e:i64']`
- PC `0xd8c`: `mov rax, qword ptr [rbp - 8]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:134` function=`main`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x8]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xd8c:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xd8c:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd8c:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xd8c:mem_scale:1:0x1:i64']`
- PC `0xd90`: `mov rdi, rax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:134` function=`main`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:rdi', 'reg:rip']`
- PC `0xd93`: `call 0xbf5` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `/root/src/spectre_stage1_2_auto.c:134` function=`main`
  - call_target: `{'operand': '0xbf5', 'resolved_symbol': 'stage1_mistrain_trigger', 'call_kind': 'direct_call_symbol', 'display_target': 'stage1_mistrain_trigger'}`
  - use_objects: `['imm_occurrence:0xd93:operand_imm:0:0xbf5:i64', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x28]']`
  - immediates: `['imm_occurrence:0xd93:operand_imm:0:0xbf5:i64']`
- PC `0xd98`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xd9d`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xda0`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xda7`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xdd0`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xdd3`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xdd6`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xdd8`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xddd`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xde2`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xde3`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xf0c`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xf0d`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xf10`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xf16`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xf17`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x150b`: `push rbp` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_before`
  - instruction_semantic_tags: `['callee_save_spill', 'prologue']`
  - use_objects: `['reg:rbp', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x20]']`
- PC `0x150c`: `mov rbp, rsp` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_before`
  - instruction_semantic_tags: `['prologue']`
  - use_objects: `['reg:rsp']`
  - def_objects: `['reg:rbp', 'reg:rip']`
- PC `0x150f`: `mov eax, dword ptr [rip + 0x20fc6f]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_before`
  - use_objects: `['reg:rip', 'var:uops_available']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0x150f:mem_disp:1:0x20fc6f:i64', 'imm_occurrence:0x150f:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0x150f:mem_disp:1:0x20fc6f:i64', 'imm_occurrence:0x150f:mem_scale:1:0x1:i64']`
- PC `0x1515`: `test eax, eax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_before`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0x1517`: `je 0x1577` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_before`
  - instruction_semantic_tags: `['conditional_branch']`
  - use_objects: `['imm_occurrence:0x1517:operand_imm:0:0x1577:i64', 'reg:zf']`
  - def_objects: `['reg:rip']`
  - immediates: `['imm_occurrence:0x1517:operand_imm:0:0x1577:i64']`
- PC `0x1577`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x1578`: `pop rbp` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_before`
  - instruction_semantic_tags: `['callee_save_restore', 'epilogue']`
  - use_objects: `['reg:rsp', 'stack:[rbp-0x20]']`
  - def_objects: `['reg:rbp', 'reg:rip', 'reg:rsp']`
- PC `0x1579`: `ret` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_before`
  - use_objects: `['reg:rsp', 'stack:[rbp-0x18]']`
  - def_objects: `['reg:rip', 'reg:rsp']`
- PC `0x157a`: `push rbp` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - instruction_semantic_tags: `['callee_save_spill', 'prologue']`
  - use_objects: `['reg:rbp', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x20]']`
- PC `0x157b`: `mov rbp, rsp` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - instruction_semantic_tags: `['prologue']`
  - use_objects: `['reg:rsp']`
  - def_objects: `['reg:rbp', 'reg:rip']`
- PC `0x157e`: `sub rsp, 0x20` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - instruction_semantic_tags: `['prologue']`
  - use_objects: `['imm_occurrence:0x157e:operand_imm:1:0x20:i64', 'reg:rsp']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0x157e:operand_imm:1:0x20:i64']`
- PC `0x1582`: `mov eax, dword ptr [rip + 0x20fbfc]` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - use_objects: `['reg:rip', 'var:uops_available']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0x1582:mem_disp:1:0x20fbfc:i64', 'imm_occurrence:0x1582:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0x1582:mem_disp:1:0x20fbfc:i64', 'imm_occurrence:0x1582:mem_scale:1:0x1:i64']`
- PC `0x1588`: `test eax, eax` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0x158a`: `je 0x168e` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - instruction_semantic_tags: `['conditional_branch']`
  - use_objects: `['imm_occurrence:0x158a:operand_imm:0:0x168e:i64', 'reg:zf']`
  - def_objects: `['reg:rip']`
  - immediates: `['imm_occurrence:0x158a:operand_imm:0:0x168e:i64']`
- PC `0x168e`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x168f`: `leave` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - instruction_semantic_tags: `['epilogue']`
  - use_objects: `['reg:rbp', 'reg:rsp', 'stack:[rbp-0x20]']`
  - def_objects: `['reg:rbp', 'reg:rip', 'reg:rsp']`
- PC `0x1690`: `ret` groups=`['structural_role']` kinds=`['branch_condition']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - use_objects: `['reg:rsp', 'stack:[rbp-0x18]']`
  - def_objects: `['reg:rip', 'reg:rsp']`
- PC `0x1691`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x1692`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x1695`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x1699`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x16a0`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x1730`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x1736`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x1739`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x173f`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x1740`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x1741`: `None` groups=`['structural_role']` kinds=`['branch_condition']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd6c`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xdcc`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1519`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x151f`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x156e`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1575`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1590`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1596`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1686`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x168c`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x16a5`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x16a8`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1727`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x172c`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xb7a`      b7a:	55                   	push   %rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0xb7b`      b7b:	48 89 e5             	mov    %rsp,%rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0xb7e`      b7e:	48 83 ec 10          	sub    $0x10,%rsp groups=`['structural_role']` kinds=`['branch_condition']`
- `0xb82`      b82:	48 89 7d f8          	mov    %rdi,-0x8(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xb86`      b86:	e8 80 09 00 00       	callq  150b <pmu_uops_snap_before> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xb8b`      b8b:	8b 05 8f 24 20 00    	mov    0x20248f(%rip),%eax        # 203020 <array1_size> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xb91`      b91:	89 c0                	mov    %eax,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xb93`      b93:	48 39 45 f8          	cmp    %rax,-0x8(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xb97`      b97:	73 34                	jae    bcd <STAGE1_END> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xb99`      b99:	48 8d 15 a0 24 20 00 	lea    0x2024a0(%rip),%rdx        # 203040 <array1> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xba0`      ba0:	48 8b 45 f8          	mov    -0x8(%rbp),%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xba4`      ba4:	48 01 d0             	add    %rdx,%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xba7`      ba7:	0f b6 00             	movzbl (%rax),%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbaa`      baa:	0f b6 c0             	movzbl %al,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbad`      bad:	c1 e0 09             	shl    $0x9,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbb0`      bb0:	48 63 d0             	movslq %eax,%rdx groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbb3`      bb3:	48 8d 05 06 07 21 00 	lea    0x210706(%rip),%rax        # 2112c0 <array2> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbba`      bba:	0f b6 14 02          	movzbl (%rdx,%rax,1),%edx groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbbe`      bbe:	0f b6 05 44 25 20 00 	movzbl 0x202544(%rip),%eax        # 203109 <temp> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbc5`      bc5:	21 d0                	and    %edx,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbc7`      bc7:	88 05 3c 25 20 00    	mov    %al,0x20253c(%rip)        # 203109 <temp> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbcd`      bcd:	e8 a8 09 00 00       	callq  157a <pmu_uops_snap_after> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbd2`      bd2:	90                   	nop groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbd3`      bd3:	c9                   	leaveq  groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbd4`      bd4:	c3                   	retq    groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbf5`      bf5:	55                   	push   %rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbf6`      bf6:	48 89 e5             	mov    %rsp,%rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbf9`      bf9:	48 83 ec 30          	sub    $0x30,%rsp groups=`['structural_role']` kinds=`['branch_condition']`
- `0xbfd`      bfd:	48 89 7d d8          	mov    %rdi,-0x28(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc01`      c01:	c7 45 e4 1d 00 00 00 	movl   $0x1d,-0x1c(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc08`      c08:	e9 9e 00 00 00       	jmpq   cab <stage1_mistrain_trigger+0xb6> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc0d`      c0d:	8b 45 e4             	mov    -0x1c(%rbp),%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc10`      c10:	99                   	cltd    groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc11`      c11:	c1 ea 1c             	shr    $0x1c,%edx groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc14`      c14:	01 d0                	add    %edx,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc16`      c16:	83 e0 0f             	and    $0xf,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc19`      c19:	29 d0                	sub    %edx,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc1b`      c1b:	48 98                	cltq    groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc1d`      c1d:	48 89 45 e8          	mov    %rax,-0x18(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc21`      c21:	48 8d 05 f8 23 20 00 	lea    0x2023f8(%rip),%rax        # 203020 <array1_size> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc28`      c28:	48 89 45 f8          	mov    %rax,-0x8(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc2c`      c2c:	48 8b 45 f8          	mov    -0x8(%rbp),%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc30`      c30:	0f ae 38             	clflush (%rax) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc33`      c33:	c7 45 e0 00 00 00 00 	movl   $0x0,-0x20(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc3a`      c3a:	eb 09                	jmp    c45 <stage1_mistrain_trigger+0x50> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc3c`      c3c:	8b 45 e0             	mov    -0x20(%rbp),%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc3f`      c3f:	83 c0 01             	add    $0x1,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc42`      c42:	89 45 e0             	mov    %eax,-0x20(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc45`      c45:	8b 45 e0             	mov    -0x20(%rbp),%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc48`      c48:	3d c7 00 00 00       	cmp    $0xc7,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc4d`      c4d:	7e ed                	jle    c3c <stage1_mistrain_trigger+0x47> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc4f`      c4f:	8b 4d e4             	mov    -0x1c(%rbp),%ecx groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc52`      c52:	ba ab aa aa 2a       	mov    $0x2aaaaaab,%edx groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc57`      c57:	89 c8                	mov    %ecx,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc59`      c59:	f7 ea                	imul   %edx groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc5b`      c5b:	89 c8                	mov    %ecx,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc5d`      c5d:	c1 f8 1f             	sar    $0x1f,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc60`      c60:	29 c2                	sub    %eax,%edx groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc62`      c62:	89 d0                	mov    %edx,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc64`      c64:	01 c0                	add    %eax,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc66`      c66:	01 d0                	add    %edx,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc68`      c68:	01 c0                	add    %eax,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc6a`      c6a:	29 c1                	sub    %eax,%ecx groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc6c`      c6c:	89 ca                	mov    %ecx,%edx groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc6e`      c6e:	8d 42 ff             	lea    -0x1(%rdx),%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc71`      c71:	66 b8 00 00          	mov    $0x0,%ax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc75`      c75:	48 98                	cltq    groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc77`      c77:	48 89 45 f0          	mov    %rax,-0x10(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc7b`      c7b:	48 8b 45 f0          	mov    -0x10(%rbp),%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc7f`      c7f:	48 c1 e8 10          	shr    $0x10,%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc83`      c83:	48 09 45 f0          	or     %rax,-0x10(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc87`      c87:	48 8b 45 d8          	mov    -0x28(%rbp),%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc8b`      c8b:	48 33 45 e8          	xor    -0x18(%rbp),%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc8f`      c8f:	48 23 45 f0          	and    -0x10(%rbp),%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc93`      c93:	48 33 45 e8          	xor    -0x18(%rbp),%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc97`      c97:	48 89 45 f0          	mov    %rax,-0x10(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc9b`      c9b:	48 8b 45 f0          	mov    -0x10(%rbp),%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xc9f`      c9f:	48 89 c7             	mov    %rax,%rdi groups=`['structural_role']` kinds=`['branch_condition']`
- `0xca2`      ca2:	e8 d3 fe ff ff       	callq  b7a <spectre_function> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xca7`      ca7:	83 6d e4 01          	subl   $0x1,-0x1c(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xcab`      cab:	83 7d e4 00          	cmpl   $0x0,-0x1c(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xcaf`      caf:	0f 89 58 ff ff ff    	jns    c0d <stage1_mistrain_trigger+0x18> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xcb5`      cb5:	90                   	nop groups=`['structural_role']` kinds=`['branch_condition']`
- `0xcb6`      cb6:	c9                   	leaveq  groups=`['structural_role']` kinds=`['branch_condition']`
- `0xcb7`      cb7:	c3                   	retq    groups=`['structural_role']` kinds=`['branch_condition']`
- `0xd6c`      d6c:	eb 15                	jmp    d83 <main+0x48> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd6e`      d6e:	8b 45 f0             	mov    -0x10(%rbp),%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xd71`      d71:	48 63 d0             	movslq %eax,%rdx groups=`['structural_role']` kinds=`['branch_condition']`
- `0xd74`      d74:	48 8d 05 45 05 21 00 	lea    0x210545(%rip),%rax        # 2112c0 <array2> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xd7b`      d7b:	c6 04 02 01          	movb   $0x1,(%rdx,%rax,1) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xd7f`      d7f:	83 45 f0 01          	addl   $0x1,-0x10(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xd83`      d83:	81 7d f0 ff ff 01 00 	cmpl   $0x1ffff,-0x10(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xd8a`      d8a:	7e e2                	jle    d6e <main+0x33> groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
- `0xd8c`      d8c:	48 8b 45 f8          	mov    -0x8(%rbp),%rax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xd90`      d90:	48 89 c7             	mov    %rax,%rdi groups=`['structural_role']` kinds=`['branch_condition']`
- `0xd93`      d93:	e8 5d fe ff ff       	callq  bf5 <stage1_mistrain_trigger> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xd98`      d98:	e8 6f 01 00 00       	callq  f0c <pmu_stage1_get_count> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xd9d`      d9d:	89 45 f4             	mov    %eax,-0xc(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xda0`      da0:	c7 45 f0 00 00 00 00 	movl   $0x0,-0x10(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0xda7`      da7:	eb 27                	jmp    dd0 <main+0x95> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xdcc`      dcc:	83 45 f0 01          	addl   $0x1,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xdd0`      dd0:	8b 45 f0             	mov    -0x10(%rbp),%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xdd3`      dd3:	3b 45 f4             	cmp    -0xc(%rbp),%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xdd6`      dd6:	7c d1                	jl     da9 <main+0x6e> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xdd8`      dd8:	e8 b4 08 00 00       	callq  1691 <pmu_uops_print_results> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xddd`      ddd:	b8 00 00 00 00       	mov    $0x0,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xde2`      de2:	c9                   	leaveq  groups=`['structural_role']` kinds=`['branch_condition']`
- `0xde3`      de3:	c3                   	retq    groups=`['structural_role']` kinds=`['branch_condition']`
- `0xf0c`      f0c:	55                   	push   %rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0xf0d`      f0d:	48 89 e5             	mov    %rsp,%rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0xf10`      f10:	8b 05 2a 42 20 00    	mov    0x20422a(%rip),%eax        # 205140 <stage1_count> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xf16`      f16:	5d                   	pop    %rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0xf17`      f17:	c3                   	retq    groups=`['structural_role']` kinds=`['branch_condition']`
- `0x150b`     150b:	55                   	push   %rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0x150c`     150c:	48 89 e5             	mov    %rsp,%rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0x150f`     150f:	8b 05 6f fc 20 00    	mov    0x20fc6f(%rip),%eax        # 211184 <uops_available> groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1515`     1515:	85 c0                	test   %eax,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1517`     1517:	74 5e                	je     1577 <pmu_uops_snap_before+0x6c> groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1519`     1519:	8b 05 41 3c 20 00    	mov    0x203c41(%rip),%eax        # 205160 <use_rdpmc> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x151f`     151f:	85 c0                	test   %eax,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x156e`     156e:	48 89 05 03 3c 20 00 	mov    %rax,0x203c03(%rip)        # 205178 <snap_retired> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1575`     1575:	eb 01                	jmp    1578 <pmu_uops_snap_before+0x6d> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1577`     1577:	90                   	nop groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1578`     1578:	5d                   	pop    %rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1579`     1579:	c3                   	retq    groups=`['structural_role']` kinds=`['branch_condition']`
- `0x157a`     157a:	55                   	push   %rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0x157b`     157b:	48 89 e5             	mov    %rsp,%rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0x157e`     157e:	48 83 ec 20          	sub    $0x20,%rsp groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1582`     1582:	8b 05 fc fb 20 00    	mov    0x20fbfc(%rip),%eax        # 211184 <uops_available> groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1588`     1588:	85 c0                	test   %eax,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0x158a`     158a:	0f 84 fe 00 00 00    	je     168e <pmu_uops_snap_after+0x114> groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1590`     1590:	8b 05 ca 3b 20 00    	mov    0x203bca(%rip),%eax        # 205160 <use_rdpmc> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1596`     1596:	85 c0                	test   %eax,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1686`     1686:	89 05 f4 fa 20 00    	mov    %eax,0x20faf4(%rip)        # 211180 <uops_cnt> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x168c`     168c:	eb 01                	jmp    168f <pmu_uops_snap_after+0x115> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x168e`     168e:	90                   	nop groups=`['structural_role']` kinds=`['branch_condition']`
- `0x168f`     168f:	c9                   	leaveq  groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1690`     1690:	c3                   	retq    groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1691`     1691:	55                   	push   %rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1692`     1692:	48 89 e5             	mov    %rsp,%rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1695`     1695:	48 83 ec 10          	sub    $0x10,%rsp groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1699`     1699:	c7 45 fc 00 00 00 00 	movl   $0x0,-0x4(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0x16a0`     16a0:	e9 8b 00 00 00       	jmpq   1730 <pmu_uops_print_results+0x9f> groups=`['structural_role']` kinds=`['branch_condition']`
- `0x16a5`     16a5:	8b 45 fc             	mov    -0x4(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x16a8`     16a8:	48 98                	cltq    groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1727`     1727:	e8 74 f2 ff ff       	callq  9a0 <printf@plt> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x172c`     172c:	83 45 fc 01          	addl   $0x1,-0x4(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1730`     1730:	8b 05 4a fa 20 00    	mov    0x20fa4a(%rip),%eax        # 211180 <uops_cnt> groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1736`     1736:	39 45 fc             	cmp    %eax,-0x4(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1739`     1739:	0f 8c 66 ff ff ff    	jl     16a5 <pmu_uops_print_results+0x14> groups=`['structural_role']` kinds=`['branch_condition']`
- `0x173f`     173f:	90                   	nop groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1740`     1740:	c9                   	leaveq  groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1741`     1741:	c3                   	retq    groups=`['structural_role']` kinds=`['branch_condition']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:58` function=`spectre_function` pcs=`['0xb7a', '0xb7b', '0xb7e', '0xb82']` groups=`['structural_role']` kinds=`['branch_condition']`

```c
   56: ********************************************************************/
   57: __attribute__((noinline))
   58: void spectre_function(size_t x) {
   59: 
   60:   pmu_uops_snap_before();
```

- `/root/src/spectre_stage1_2_auto.c:60` function=`spectre_function` pcs=`['0xb86']` groups=`['structural_role']` kinds=`['branch_condition']`

```c
   58: void spectre_function(size_t x) {
   59: 
   60:   pmu_uops_snap_before();
   61: 
   62:   asm volatile(".globl STAGE1_BEGIN\nSTAGE1_BEGIN:");
```

- `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function` pcs=`['0xb8b', '0xb91', '0xb93', '0xb97']` groups=`['structural_role']` kinds=`['branch_condition']`

```c
   61: 
   62:   asm volatile(".globl STAGE1_BEGIN\nSTAGE1_BEGIN:");
   63:   if (x < array1_size) {
   64:     NOP_REGION_BEGIN
   65:     temp &= array2[array1[x] * 512];
```

- `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function` pcs=`['0xb99', '0xba0', '0xba4', '0xba7', '0xbaa', '0xbad', '0xbb0', '0xbb3', '0xbba', '0xbbe', '0xbc5', '0xbc7']` groups=`['structural_role']` kinds=`['branch_condition']`

```c
   63:   if (x < array1_size) {
   64:     NOP_REGION_BEGIN
   65:     temp &= array2[array1[x] * 512];
   66:     NOP_REGION_END
   67:   }
```

- `/root/src/spectre_stage1_2_auto.c:70` function=`spectre_function` pcs=`['0xbcd']` groups=`['structural_role']` kinds=`['branch_condition']`

```c
   68:   asm volatile(".globl STAGE1_END\nSTAGE1_END:");
   69: 
   70:   pmu_uops_snap_after();
   71: }
   72: 
```

- `/root/src/spectre_stage1_2_auto.c:71` function=`spectre_function` pcs=`['0xbd3', '0xbd4']` groups=`['structural_role']` kinds=`['branch_condition']`

```c
   69: 
   70:   pmu_uops_snap_after();
   71: }
   72: 
   73: /********************************************************************
```

- `/root/src/spectre_stage1_2_auto.c:88` function=`stage1_mistrain_trigger` pcs=`['0xbf5', '0xbf6', '0xbf9', '0xbfd']` groups=`['structural_role']` kinds=`['branch_condition']`

```c
   86: ********************************************************************/
   87: __attribute__((noinline))
   88: void stage1_mistrain_trigger(size_t malicious_x) {
   89:     int j;
   90:     size_t training_x, x;
```

- `/root/src/spectre_stage1_2_auto.c:92` function=`stage1_mistrain_trigger` pcs=`['0xc01']` groups=`['structural_role']` kinds=`['branch_condition']`

```c
   90:     size_t training_x, x;
   91: 
   92:     for (j = 29; j >= 0; j--) {
   93:         training_x = (size_t)(j % 16);
   94:         _mm_clflush(&array1_size);
```

- `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger` pcs=`['0xc0d', '0xc10', '0xc11', '0xc14', '0xc16', '0xc19', '0xc1b', '0xc1d', '0xc21', '0xc28']` groups=`['structural_role']` kinds=`['branch_condition']`

```c
   91: 
   92:     for (j = 29; j >= 0; j--) {
   93:         training_x = (size_t)(j % 16);
   94:         _mm_clflush(&array1_size);
   95:         for (volatile int z = 0; z < 200; z++) {}
```

- `/root/src/spectre_stage1_2_auto.c:95` function=`stage1_mistrain_trigger` pcs=`['0xc33']` groups=`['structural_role']` kinds=`['branch_condition']`

```c
   93:         training_x = (size_t)(j % 16);
   94:         _mm_clflush(&array1_size);
   95:         for (volatile int z = 0; z < 200; z++) {}
   96: 
   97:         x = ((j % 6) - 1) & ~0xFFFF;
```

- `/root/src/spectre_stage1_2_auto.c:134` function=`main` pcs=`['0xd8c', '0xd90', '0xd93']` groups=`['structural_role']` kinds=`['branch_condition']`

```c
  132: 
  133:     /* 执行阶段1 */
  134:     stage1_mistrain_trigger(malicious_x);
  135: 
  136:     /* Stage1 BR_MISP 数据 */
```

- `/usr/lib/gcc/x86_64-linux-gnu/7/include/emmintrin.h:1486` function=`_mm_clflush` pcs=`['0xc2c']` groups=`['structural_role']` kinds=`['branch_condition']`

### 127. `imm_occurrence:0xd8c:mem_disp:1:0xfffffffffffffff8:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xd8c:mem_disp:1:0xfffffffffffffff8/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xd8c', 'operand_index': None, 'raw_suffix': 'mem_disp:1:0xfffffffffffffff8/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xd8c:mem_disp:1:0xfffffffffffffff8/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xd8c']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xd8c']`
- direct_operand_pcs: `['0xd8c']`
- structural_role_pcs: `['0xd8c']`
- anchor_pcs: `['0xd8c']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd90', '0xd93']`
- all_mapped_pcs: `['0xd8c', '0xd90', '0xd93']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x8]']`

#### PC Relation Entries

- `0xd8c` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xd90` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd93` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xd8c`: `mov rax, qword ptr [rbp - 8]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:134` function=`main`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x8]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xd8c:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xd8c:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd8c:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xd8c:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd90`: `mov rdi, rax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd93`: `call 0xbf5` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd8c`      d8c:	48 8b 45 f8          	mov    -0x8(%rbp),%rax groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xd90`      d90:	48 89 c7             	mov    %rax,%rdi groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd93`      d93:	e8 5d fe ff ff       	callq  bf5 <stage1_mistrain_trigger> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:134` function=`main` pcs=`['0xd8c', '0xd90', '0xd93']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
  132: 
  133:     /* 执行阶段1 */
  134:     stage1_mistrain_trigger(malicious_x);
  135: 
  136:     /* Stage1 BR_MISP 数据 */
```

### 128. `imm_occurrence:0xd8c:mem_scale:1:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xd8c:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xd8c', 'operand_index': None, 'raw_suffix': 'mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xd8c:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xd8c']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xd8c']`
- direct_operand_pcs: `['0xd8c']`
- structural_role_pcs: `['0xd8c']`
- anchor_pcs: `['0xd8c']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd90', '0xd93']`
- all_mapped_pcs: `['0xd8c', '0xd90', '0xd93']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x8]']`

#### PC Relation Entries

- `0xd8c` kinds=`['address_component', 'direct_immediate_occurrence']` groups=`['direct_operand', 'structural_role']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xd90` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd93` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xd8c`: `mov rax, qword ptr [rbp - 8]` groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
  - Source: `/root/src/spectre_stage1_2_auto.c:134` function=`main`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x8]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xd8c:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xd8c:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd8c:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xd8c:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd90`: `mov rdi, rax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd93`: `call 0xbf5` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd8c`      d8c:	48 8b 45 f8          	mov    -0x8(%rbp),%rax groups=`['direct_operand', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence']`
- `0xd90`      d90:	48 89 c7             	mov    %rax,%rdi groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd93`      d93:	e8 5d fe ff ff       	callq  bf5 <stage1_mistrain_trigger> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:134` function=`main` pcs=`['0xd8c', '0xd90', '0xd93']` groups=`['direct_operand', 'evidence_only', 'structural_role']` kinds=`['address_component', 'direct_immediate_occurrence', 'evidence_only']`

```c
  132: 
  133:     /* 执行阶段1 */
  134:     stage1_mistrain_trigger(malicious_x);
  135: 
  136:     /* Stage1 BR_MISP 数据 */
```

### 129. `imm_occurrence:0xd93:operand_imm:0:0xbf5:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xd93:operand_imm:0:0xbf5/i64 [call_target_constant|program_semantic_constant|store_constant]`
- Mapping kind: `store_constant`
- Confidence: `semantic`
- Object semantic tags: `['call_target_constant', 'program_semantic_constant', 'store_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xd93', 'operand_index': None, 'raw_suffix': 'operand_imm:0:0xbf5/i64 [call_target_constant|program_semantic_constant|store_constant]'}`
- Reason: 该 immediate 带有 store_constant 标签，更适合作为写入值常量解释。
- Candidate program elements: `['imm@0xd93:operand_imm:0:0xbf5/i64 [call_target_constant|program_semantic_constant|store_constant]']`
- direct_use_pcs: `['0xd93']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `['0xd93']`
- direct_operand_pcs: `['0xd93']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xd93']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd8c', '0xd90']`
- all_mapped_pcs: `['0xd8c', '0xd90', '0xd93']`
- direct_parents: `[]`
- direct_children: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x28]']`

#### PC Relation Entries

- `0xd8c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd90` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd93` kinds=`['direct_immediate_occurrence', 'direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['instruction_details.immediates', 'object_detail.used_by/instruction_details.use_objects']`

#### Direct Anchor Instruction Evidence

- PC `0xd93`: `call 0xbf5` groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`
  - Source: `/root/src/spectre_stage1_2_auto.c:134` function=`main`
  - call_target: `{'operand': '0xbf5', 'resolved_symbol': 'stage1_mistrain_trigger', 'call_kind': 'direct_call_symbol', 'display_target': 'stage1_mistrain_trigger'}`
  - use_objects: `['imm_occurrence:0xd93:operand_imm:0:0xbf5:i64', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x28]']`
  - immediates: `['imm_occurrence:0xd93:operand_imm:0:0xbf5:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd8c`: `mov rax, qword ptr [rbp - 8]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd90`: `mov rdi, rax` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd8c`      d8c:	48 8b 45 f8          	mov    -0x8(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd90`      d90:	48 89 c7             	mov    %rax,%rdi groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd93`      d93:	e8 5d fe ff ff       	callq  bf5 <stage1_mistrain_trigger> groups=`['direct_operand']` kinds=`['direct_immediate_occurrence', 'direct_use']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:134` function=`main` pcs=`['0xd8c', '0xd90', '0xd93']` groups=`['direct_operand', 'evidence_only']` kinds=`['direct_immediate_occurrence', 'direct_use', 'evidence_only']`

```c
  132: 
  133:     /* 执行阶段1 */
  134:     stage1_mistrain_trigger(malicious_x);
  135: 
  136:     /* Stage1 BR_MISP 数据 */
```

### 130. `imm_occurrence:0xd98:operand_imm:0:0xf0c:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xd98:operand_imm:0:0xf0c/i64 [call_target_constant|program_semantic_constant|store_constant]`
- Mapping kind: `store_constant`
- Confidence: `semantic`
- Object semantic tags: `['call_target_constant', 'program_semantic_constant', 'store_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xd98', 'operand_index': None, 'raw_suffix': 'operand_imm:0:0xf0c/i64 [call_target_constant|program_semantic_constant|store_constant]'}`
- Reason: 该 immediate 带有 store_constant 标签，更适合作为写入值常量解释。
- Candidate program elements: `['imm@0xd98:operand_imm:0:0xf0c/i64 [call_target_constant|program_semantic_constant|store_constant]']`
- direct_use_pcs: `['0xd98']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `['0xd98']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xd98']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd9d']`
- all_mapped_pcs: `['0xd98', '0xd9d']`
- direct_parents: `[]`
- direct_children: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x28]']`

#### PC Relation Entries

- `0xd98` kinds=`['direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['object_detail.used_by/instruction_details.use_objects']`
- `0xd9d` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xd98`: `None` groups=`['direct_operand']` kinds=`['direct_use']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd9d`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd98`      d98:	e8 6f 01 00 00       	callq  f0c <pmu_stage1_get_count> groups=`['direct_operand']` kinds=`['direct_use']`
- `0xd9d`      d9d:	89 45 f4             	mov    %eax,-0xc(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 131. `imm_occurrence:0xd9d:mem_disp:0:0xfffffffffffffff4:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xd9d:mem_disp:0:0xfffffffffffffff4/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xd9d', 'operand_index': None, 'raw_suffix': 'mem_disp:0:0xfffffffffffffff4/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xd9d:mem_disp:0:0xfffffffffffffff4/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xd9d']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `[]`
- structural_role_pcs: `['0xd9d']`
- anchor_pcs: `['0xd9d']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd98', '0xda0']`
- all_mapped_pcs: `['0xd98', '0xd9d', '0xda0']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0xc]']`

#### PC Relation Entries

- `0xd98` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd9d` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xda0` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xd9d`: `None` groups=`['structural_role']` kinds=`['address_component']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd98`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xda0`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd98`      d98:	e8 6f 01 00 00       	callq  f0c <pmu_stage1_get_count> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd9d`      d9d:	89 45 f4             	mov    %eax,-0xc(%rbp) groups=`['structural_role']` kinds=`['address_component']`
- `0xda0`      da0:	c7 45 f0 00 00 00 00 	movl   $0x0,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 132. `imm_occurrence:0xd9d:mem_scale:0:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xd9d:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xd9d', 'operand_index': None, 'raw_suffix': 'mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xd9d:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xd9d']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `[]`
- structural_role_pcs: `['0xd9d']`
- anchor_pcs: `['0xd9d']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd98', '0xda0']`
- all_mapped_pcs: `['0xd98', '0xd9d', '0xda0']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0xc]']`

#### PC Relation Entries

- `0xd98` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd9d` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xda0` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xd9d`: `None` groups=`['structural_role']` kinds=`['address_component']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd98`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xda0`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd98`      d98:	e8 6f 01 00 00       	callq  f0c <pmu_stage1_get_count> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd9d`      d9d:	89 45 f4             	mov    %eax,-0xc(%rbp) groups=`['structural_role']` kinds=`['address_component']`
- `0xda0`      da0:	c7 45 f0 00 00 00 00 	movl   $0x0,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 133. `imm_occurrence:0xda0:mem_disp:0:0xfffffffffffffff0:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xda0:mem_disp:0:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xda0', 'operand_index': None, 'raw_suffix': 'mem_disp:0:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xda0:mem_disp:0:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xda0']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `[]`
- structural_role_pcs: `['0xda0']`
- anchor_pcs: `['0xda0']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd9d', '0xda7']`
- all_mapped_pcs: `['0xd9d', '0xda0', '0xda7']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x10]']`

#### PC Relation Entries

- `0xd9d` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xda0` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xda7` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xda0`: `None` groups=`['structural_role']` kinds=`['address_component']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd9d`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xda7`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd9d`      d9d:	89 45 f4             	mov    %eax,-0xc(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xda0`      da0:	c7 45 f0 00 00 00 00 	movl   $0x0,-0x10(%rbp) groups=`['structural_role']` kinds=`['address_component']`
- `0xda7`      da7:	eb 27                	jmp    dd0 <main+0x95> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 134. `imm_occurrence:0xda0:mem_scale:0:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xda0:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xda0', 'operand_index': None, 'raw_suffix': 'mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xda0:mem_scale:0:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xda0']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `[]`
- structural_role_pcs: `['0xda0']`
- anchor_pcs: `['0xda0']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd9d', '0xda7']`
- all_mapped_pcs: `['0xd9d', '0xda0', '0xda7']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x10]']`

#### PC Relation Entries

- `0xd9d` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xda0` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xda7` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xda0`: `None` groups=`['structural_role']` kinds=`['address_component']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd9d`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xda7`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd9d`      d9d:	89 45 f4             	mov    %eax,-0xc(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xda0`      da0:	c7 45 f0 00 00 00 00 	movl   $0x0,-0x10(%rbp) groups=`['structural_role']` kinds=`['address_component']`
- `0xda7`      da7:	eb 27                	jmp    dd0 <main+0x95> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 135. `imm_occurrence:0xda0:operand_imm:1:0x0:i32`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xda0:operand_imm:1:0x0/i32 [program_semantic_constant|store_constant]`
- Mapping kind: `store_constant`
- Confidence: `semantic`
- Object semantic tags: `['program_semantic_constant', 'store_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xda0', 'operand_index': None, 'raw_suffix': 'operand_imm:1:0x0/i32 [program_semantic_constant|store_constant]'}`
- Reason: 该 immediate 带有 store_constant 标签，更适合作为写入值常量解释。
- Candidate program elements: `['imm@0xda0:operand_imm:1:0x0/i32 [program_semantic_constant|store_constant]']`
- direct_use_pcs: `['0xda0']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `['0xda0']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xda0']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd9d', '0xda7']`
- all_mapped_pcs: `['0xd9d', '0xda0', '0xda7']`
- direct_parents: `[]`
- direct_children: `['reg:rip', 'stack:[rbp-0x10]']`

#### PC Relation Entries

- `0xd9d` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xda0` kinds=`['direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['object_detail.used_by/instruction_details.use_objects']`
- `0xda7` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xda0`: `None` groups=`['direct_operand']` kinds=`['direct_use']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd9d`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xda7`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd9d`      d9d:	89 45 f4             	mov    %eax,-0xc(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xda0`      da0:	c7 45 f0 00 00 00 00 	movl   $0x0,-0x10(%rbp) groups=`['direct_operand']` kinds=`['direct_use']`
- `0xda7`      da7:	eb 27                	jmp    dd0 <main+0x95> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 136. `imm_occurrence:0xda7:operand_imm:0:0xdd0:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xda7:operand_imm:0:0xdd0/i64`
- Mapping kind: `constant_or_address_component`
- Confidence: `structural`
- Object semantic tags: `[]`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xda7', 'operand_index': None, 'raw_suffix': 'operand_imm:0:0xdd0/i64'}`
- Reason: 对象类型为 imm，更适合作为常量、位移、scale、比较值或地址组成部分解释。
- Candidate program elements: `['imm@0xda7:operand_imm:0:0xdd0/i64']`
- direct_use_pcs: `['0xda7']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `['0xda7']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xda7']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xda0']`
- all_mapped_pcs: `['0xda0', '0xda7']`
- direct_parents: `[]`
- direct_children: `['reg:rip']`

#### PC Relation Entries

- `0xda0` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xda7` kinds=`['direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['object_detail.used_by/instruction_details.use_objects']`

#### Direct Anchor Instruction Evidence

- PC `0xda7`: `None` groups=`['direct_operand']` kinds=`['direct_use']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xda0`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xda0`      da0:	c7 45 f0 00 00 00 00 	movl   $0x0,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xda7`      da7:	eb 27                	jmp    dd0 <main+0x95> groups=`['direct_operand']` kinds=`['direct_use']`

#### Source Evidence

_No source evidence found._

### 137. `imm_occurrence:0xdd0:mem_disp:1:0xfffffffffffffff0:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xdd0:mem_disp:1:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xdd0', 'operand_index': None, 'raw_suffix': 'mem_disp:1:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xdd0:mem_disp:1:0xfffffffffffffff0/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xdd0']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `[]`
- structural_role_pcs: `['0xdd0']`
- anchor_pcs: `['0xdd0']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xdcc', '0xdd3', '0xdd6']`
- all_mapped_pcs: `['0xdcc', '0xdd0', '0xdd3', '0xdd6']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x10]']`

#### PC Relation Entries

- `0xdcc` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xdd0` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xdd3` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xdd6` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xdd0`: `None` groups=`['structural_role']` kinds=`['address_component']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xdcc`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xdd3`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xdd6`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xdcc`      dcc:	83 45 f0 01          	addl   $0x1,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xdd0`      dd0:	8b 45 f0             	mov    -0x10(%rbp),%eax groups=`['structural_role']` kinds=`['address_component']`
- `0xdd3`      dd3:	3b 45 f4             	cmp    -0xc(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xdd6`      dd6:	7c d1                	jl     da9 <main+0x6e> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 138. `imm_occurrence:0xdd0:mem_scale:1:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xdd0:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xdd0', 'operand_index': None, 'raw_suffix': 'mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xdd0:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xdd0']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `[]`
- structural_role_pcs: `['0xdd0']`
- anchor_pcs: `['0xdd0']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xdcc', '0xdd3', '0xdd6']`
- all_mapped_pcs: `['0xdcc', '0xdd0', '0xdd3', '0xdd6']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0x10]']`

#### PC Relation Entries

- `0xdcc` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xdd0` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xdd3` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xdd6` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xdd0`: `None` groups=`['structural_role']` kinds=`['address_component']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xdcc`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xdd3`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xdd6`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xdcc`      dcc:	83 45 f0 01          	addl   $0x1,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xdd0`      dd0:	8b 45 f0             	mov    -0x10(%rbp),%eax groups=`['structural_role']` kinds=`['address_component']`
- `0xdd3`      dd3:	3b 45 f4             	cmp    -0xc(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xdd6`      dd6:	7c d1                	jl     da9 <main+0x6e> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 139. `imm_occurrence:0xdd3:mem_disp:1:0xfffffffffffffff4:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xdd3:mem_disp:1:0xfffffffffffffff4/i64 [frame_offset_constant|structural_abi_constant]`
- Mapping kind: `frame_offset_constant`
- Confidence: `semantic`
- Object semantic tags: `['frame_offset_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xdd3', 'operand_index': None, 'raw_suffix': 'mem_disp:1:0xfffffffffffffff4/i64 [frame_offset_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。
- Candidate program elements: `['imm@0xdd3:mem_disp:1:0xfffffffffffffff4/i64 [frame_offset_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xdd3']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `[]`
- structural_role_pcs: `['0xdd3']`
- anchor_pcs: `['0xdd3']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xdcc', '0xdd0', '0xdd6']`
- all_mapped_pcs: `['0xdcc', '0xdd0', '0xdd3', '0xdd6']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0xc]']`

#### PC Relation Entries

- `0xdcc` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xdd0` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xdd3` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xdd6` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xdd3`: `None` groups=`['structural_role']` kinds=`['address_component']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xdcc`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xdd0`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xdd6`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xdcc`      dcc:	83 45 f0 01          	addl   $0x1,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xdd0`      dd0:	8b 45 f0             	mov    -0x10(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xdd3`      dd3:	3b 45 f4             	cmp    -0xc(%rbp),%eax groups=`['structural_role']` kinds=`['address_component']`
- `0xdd6`      dd6:	7c d1                	jl     da9 <main+0x6e> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 140. `imm_occurrence:0xdd3:mem_scale:1:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xdd3:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xdd3', 'operand_index': None, 'raw_suffix': 'mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xdd3:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xdd3']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `[]`
- structural_role_pcs: `['0xdd3']`
- anchor_pcs: `['0xdd3']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xdcc', '0xdd0', '0xdd6']`
- all_mapped_pcs: `['0xdcc', '0xdd0', '0xdd3', '0xdd6']`
- direct_parents: `[]`
- direct_children: `['stack:[rbp-0xc]']`

#### PC Relation Entries

- `0xdcc` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xdd0` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xdd3` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xdd6` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xdd3`: `None` groups=`['structural_role']` kinds=`['address_component']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xdcc`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xdd0`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xdd6`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xdcc`      dcc:	83 45 f0 01          	addl   $0x1,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xdd0`      dd0:	8b 45 f0             	mov    -0x10(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xdd3`      dd3:	3b 45 f4             	cmp    -0xc(%rbp),%eax groups=`['structural_role']` kinds=`['address_component']`
- `0xdd6`      dd6:	7c d1                	jl     da9 <main+0x6e> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 141. `imm_occurrence:0xdd6:operand_imm:0:0xda9:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xdd6:operand_imm:0:0xda9/i64`
- Mapping kind: `comparison_constant`
- Confidence: `semantic`
- Object semantic tags: `['comparison_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xdd6', 'operand_index': None, 'raw_suffix': 'operand_imm:0:0xda9/i64'}`
- Reason: 该 immediate 带有 comparison_constant 标签，更适合作为比较语义常量解释。
- Candidate program elements: `['imm@0xdd6:operand_imm:0:0xda9/i64']`
- direct_use_pcs: `['0xdd6']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `['0xdd8', '0xddd', '0xde2', '0xde3', '0x1691', '0x1692', '0x1695', '0x1699', '0x16a0', '0x1730', '0x1736', '0x1739', '0x173f', '0x1740', '0x1741']`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `['0xdd6']`
- structural_role_pcs: `['0xdd8', '0xddd', '0xde2', '0xde3', '0x1691', '0x1692', '0x1695', '0x1699', '0x16a0', '0x1730', '0x1736', '0x1739', '0x173f', '0x1740', '0x1741']`
- anchor_pcs: `['0xdd6', '0xdd8', '0xddd', '0xde2', '0xde3', '0x1691', '0x1692', '0x1695', '0x1699', '0x16a0', '0x1730', '0x1736', '0x1739', '0x173f', '0x1740', '0x1741']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xdd0', '0xdd3', '0x16a5', '0x16a8', '0x1727', '0x172c']`
- all_mapped_pcs: `['0xdd0', '0xdd3', '0xdd6', '0xdd8', '0xddd', '0xde2', '0xde3', '0x1691', '0x1692', '0x1695', '0x1699', '0x16a0', '0x16a5', '0x16a8', '0x1727', '0x172c', '0x1730', '0x1736', '0x1739', '0x173f', '0x1740', '0x1741']`
- direct_parents: `[]`
- direct_children: `['reg:cf', 'reg:of', 'reg:rax', 'reg:rbp', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf', 'stack:[rbp-0x28]', 'stack:[rbp-0x30]', 'stack:[rbp-0x4]']`

#### PC Relation Entries

- `0xdd0` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xdd3` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xdd6` kinds=`['direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['object_detail.used_by/instruction_details.use_objects']`
- `0xdd8` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xddd` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xde2` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0xde3` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1691` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1692` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1695` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1699` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x16a0` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x16a5` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x16a8` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1727` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x172c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1730` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1736` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1739` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x173f` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1740` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`
- `0x1741` kinds=`['branch_condition']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.ctrl_used_by']`

#### Direct Anchor Instruction Evidence

- PC `0xdd6`: `None` groups=`['direct_operand']` kinds=`['direct_use']`
- PC `0xdd8`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xddd`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xde2`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0xde3`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x1691`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x1692`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x1695`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x1699`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x16a0`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x1730`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x1736`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x1739`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x173f`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x1740`: `None` groups=`['structural_role']` kinds=`['branch_condition']`
- PC `0x1741`: `None` groups=`['structural_role']` kinds=`['branch_condition']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xdd0`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xdd3`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x16a5`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x16a8`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1727`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x172c`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xdd0`      dd0:	8b 45 f0             	mov    -0x10(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xdd3`      dd3:	3b 45 f4             	cmp    -0xc(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xdd6`      dd6:	7c d1                	jl     da9 <main+0x6e> groups=`['direct_operand']` kinds=`['direct_use']`
- `0xdd8`      dd8:	e8 b4 08 00 00       	callq  1691 <pmu_uops_print_results> groups=`['structural_role']` kinds=`['branch_condition']`
- `0xddd`      ddd:	b8 00 00 00 00       	mov    $0x0,%eax groups=`['structural_role']` kinds=`['branch_condition']`
- `0xde2`      de2:	c9                   	leaveq  groups=`['structural_role']` kinds=`['branch_condition']`
- `0xde3`      de3:	c3                   	retq    groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1691`     1691:	55                   	push   %rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1692`     1692:	48 89 e5             	mov    %rsp,%rbp groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1695`     1695:	48 83 ec 10          	sub    $0x10,%rsp groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1699`     1699:	c7 45 fc 00 00 00 00 	movl   $0x0,-0x4(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0x16a0`     16a0:	e9 8b 00 00 00       	jmpq   1730 <pmu_uops_print_results+0x9f> groups=`['structural_role']` kinds=`['branch_condition']`
- `0x16a5`     16a5:	8b 45 fc             	mov    -0x4(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x16a8`     16a8:	48 98                	cltq    groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1727`     1727:	e8 74 f2 ff ff       	callq  9a0 <printf@plt> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x172c`     172c:	83 45 fc 01          	addl   $0x1,-0x4(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1730`     1730:	8b 05 4a fa 20 00    	mov    0x20fa4a(%rip),%eax        # 211180 <uops_cnt> groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1736`     1736:	39 45 fc             	cmp    %eax,-0x4(%rbp) groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1739`     1739:	0f 8c 66 ff ff ff    	jl     16a5 <pmu_uops_print_results+0x14> groups=`['structural_role']` kinds=`['branch_condition']`
- `0x173f`     173f:	90                   	nop groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1740`     1740:	c9                   	leaveq  groups=`['structural_role']` kinds=`['branch_condition']`
- `0x1741`     1741:	c3                   	retq    groups=`['structural_role']` kinds=`['branch_condition']`

#### Source Evidence

_No source evidence found._

### 142. `imm_occurrence:0xdd8:operand_imm:0:0x1691:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xdd8:operand_imm:0:0x1691/i64 [call_target_constant|program_semantic_constant|store_constant]`
- Mapping kind: `store_constant`
- Confidence: `semantic`
- Object semantic tags: `['call_target_constant', 'program_semantic_constant', 'store_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xdd8', 'operand_index': None, 'raw_suffix': 'operand_imm:0:0x1691/i64 [call_target_constant|program_semantic_constant|store_constant]'}`
- Reason: 该 immediate 带有 store_constant 标签，更适合作为写入值常量解释。
- Candidate program elements: `['imm@0xdd8:operand_imm:0:0x1691/i64 [call_target_constant|program_semantic_constant|store_constant]']`
- direct_use_pcs: `['0xdd8']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `['0xdd8']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xdd8']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `[]`
- all_mapped_pcs: `['0xdd8']`
- direct_parents: `[]`
- direct_children: `['reg:rip', 'reg:rsp', 'stack:[rbp-0x28]']`

#### PC Relation Entries

- `0xdd8` kinds=`['direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['object_detail.used_by/instruction_details.use_objects']`

#### Direct Anchor Instruction Evidence

- PC `0xdd8`: `None` groups=`['direct_operand']` kinds=`['direct_use']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

_No evidence-only instruction evidence._

#### Assembly References

- `0xdd8`      dd8:	e8 b4 08 00 00       	callq  1691 <pmu_uops_print_results> groups=`['direct_operand']` kinds=`['direct_use']`

#### Source Evidence

_No source evidence found._

### 143. `imm_occurrence:0xddd:operand_imm:1:0x0:i32`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xddd:operand_imm:1:0x0/i32`
- Mapping kind: `constant_or_address_component`
- Confidence: `structural`
- Object semantic tags: `[]`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xddd', 'operand_index': None, 'raw_suffix': 'operand_imm:1:0x0/i32'}`
- Reason: 对象类型为 imm，更适合作为常量、位移、scale、比较值或地址组成部分解释。
- Candidate program elements: `['imm@0xddd:operand_imm:1:0x0/i32']`
- direct_use_pcs: `['0xddd']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `['0xddd']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xddd']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xde2']`
- all_mapped_pcs: `['0xddd', '0xde2']`
- direct_parents: `[]`
- direct_children: `['reg:rax', 'reg:rip']`

#### PC Relation Entries

- `0xddd` kinds=`['direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['object_detail.used_by/instruction_details.use_objects']`
- `0xde2` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xddd`: `None` groups=`['direct_operand']` kinds=`['direct_use']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xde2`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xddd`      ddd:	b8 00 00 00 00       	mov    $0x0,%eax groups=`['direct_operand']` kinds=`['direct_use']`
- `0xde2`      de2:	c9                   	leaveq  groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 144. `imm_occurrence:0xf10:mem_disp:1:0x20422a:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xf10:mem_disp:1:0x20422a/i64 [rip_relative_displacement|structural_abi_constant]`
- Mapping kind: `rip_relative_displacement`
- Confidence: `semantic`
- Object semantic tags: `['rip_relative_displacement', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xf10', 'operand_index': None, 'raw_suffix': 'mem_disp:1:0x20422a/i64 [rip_relative_displacement|structural_abi_constant]'}`
- Reason: 该 immediate 带有 rip_relative_displacement 标签，更适合作为 RIP 相对寻址位移解释。
- Candidate program elements: `['imm@0xf10:mem_disp:1:0x20422a/i64 [rip_relative_displacement|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xf10']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `[]`
- structural_role_pcs: `['0xf10']`
- anchor_pcs: `['0xf10']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xf0c', '0xf0d', '0xf16', '0xf17']`
- all_mapped_pcs: `['0xf0c', '0xf0d', '0xf10', '0xf16', '0xf17']`
- direct_parents: `[]`
- direct_children: `['var:stage1_count']`

#### PC Relation Entries

- `0xf0c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xf0d` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xf10` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xf16` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xf17` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xf10`: `None` groups=`['structural_role']` kinds=`['address_component']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xf0c`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xf0d`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xf16`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xf17`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xf0c`      f0c:	55                   	push   %rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xf0d`      f0d:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xf10`      f10:	8b 05 2a 42 20 00    	mov    0x20422a(%rip),%eax        # 205140 <stage1_count> groups=`['structural_role']` kinds=`['address_component']`
- `0xf16`      f16:	5d                   	pop    %rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xf17`      f17:	c3                   	retq    groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 145. `imm_occurrence:0xf10:mem_scale:1:0x1:i64`

- Role: `backward_leaf`
- Type: `imm`
- Label: `imm@0xf10:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]`
- Mapping kind: `address_scale_constant`
- Confidence: `semantic`
- Object semantic tags: `['address_scale_constant', 'structural_abi_constant']`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Occurrence: `{'occurrence_pc': '0xf10', 'operand_index': None, 'raw_suffix': 'mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]'}`
- Reason: 该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。
- Candidate program elements: `['imm@0xf10:mem_scale:1:0x1/i64 [address_scale_constant|structural_abi_constant]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xf10']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `[]`
- structural_role_pcs: `['0xf10']`
- anchor_pcs: `['0xf10']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xf0c', '0xf0d', '0xf16', '0xf17']`
- all_mapped_pcs: `['0xf0c', '0xf0d', '0xf10', '0xf16', '0xf17']`
- direct_parents: `[]`
- direct_children: `['var:stage1_count']`

#### PC Relation Entries

- `0xf0c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xf0d` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xf10` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xf16` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xf17` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xf10`: `None` groups=`['structural_role']` kinds=`['address_component']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xf0c`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xf0d`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xf16`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xf17`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xf0c`      f0c:	55                   	push   %rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xf0d`      f0d:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xf10`      f10:	8b 05 2a 42 20 00    	mov    0x20422a(%rip),%eax        # 205140 <stage1_count> groups=`['structural_role']` kinds=`['address_component']`
- `0xf16`      f16:	5d                   	pop    %rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xf17`      f17:	c3                   	retq    groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 146. `reg:unknown`

- Role: `backward_leaf`
- Type: `reg`
- Label: `unknown`
- Mapping kind: `address_computation_register`
- Confidence: `semantic`
- Object semantic tags: `['address_index', 'address_segment']`
- Anchor instruction tags: `['argument_shuffle']`
- Scaffolding tags: `['argument_shuffle']`
- Reason: 寄存器带有 address_base/address_index 标签，更适合作为地址计算寄存器解释。 检测到 ABI/脚手架标签：argument_shuffle，应更偏向解释为结构性对象，而非优先可变异语义对象。
- Candidate program elements: `['unknown']`
- direct_use_pcs: `[]`
- direct_def_pcs: `[]`
- direct_addr_pcs: `['0xa7f', '0xa86', '0xa8d', '0xa94', '0xb82', '0xb8b', '0xb93', '0xb99', '0xba0', '0xba7', '0xbb3', '0xbba', '0xbbe', '0xbc7', '0xbfd', '0xc01', '0xc0d', '0xc1d', '0xc21', '0xc28', '0xc2c', '0xc33', '0xc3c', '0xc42', '0xc45', '0xc4f', '0xc6e', '0xc77', '0xc7b', '0xc83', '0xc87', '0xc8b', '0xc8f', '0xc93', '0xc97', '0xc9b', '0xca7', '0xcab', '0xd43', '0xd46', '0xd4a', '0xd54', '0xd61', '0xd65', '0xd6e', '0xd74', '0xd7b', '0xd7f', '0xd83', '0xd8c', '0xd9d', '0xda0', '0xdd0', '0xdd3', '0xf10', '0x150f', '0x1582', '0x1699', '0x1730', '0x1736']`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `[]`
- structural_role_pcs: `['0xa7f', '0xa86', '0xa8d', '0xa94', '0xb82', '0xb8b', '0xb93', '0xb99', '0xba0', '0xba7', '0xbb3', '0xbba', '0xbbe', '0xbc7', '0xbfd', '0xc01', '0xc0d', '0xc1d', '0xc21', '0xc28', '0xc2c', '0xc33', '0xc3c', '0xc42', '0xc45', '0xc4f', '0xc6e', '0xc77', '0xc7b', '0xc83', '0xc87', '0xc8b', '0xc8f', '0xc93', '0xc97', '0xc9b', '0xca7', '0xcab', '0xd43', '0xd46', '0xd4a', '0xd54', '0xd61', '0xd65', '0xd6e', '0xd74', '0xd7b', '0xd7f', '0xd83', '0xd8c', '0xd9d', '0xda0', '0xdd0', '0xdd3', '0xf10', '0x150f', '0x1582', '0x1699', '0x1730', '0x1736']`
- anchor_pcs: `['0xa7f', '0xa86', '0xa8d', '0xa94', '0xb82', '0xb8b', '0xb93', '0xb99', '0xba0', '0xba7', '0xbb3', '0xbba', '0xbbe', '0xbc7', '0xbfd', '0xc01', '0xc0d', '0xc1d', '0xc21', '0xc28', '0xc2c', '0xc33', '0xc3c', '0xc42', '0xc45', '0xc4f', '0xc6e', '0xc77', '0xc7b', '0xc83', '0xc87', '0xc8b', '0xc8f', '0xc93', '0xc97', '0xc9b', '0xca7', '0xcab', '0xd43', '0xd46', '0xd4a', '0xd54', '0xd61', '0xd65', '0xd6e', '0xd74', '0xd7b', '0xd7f', '0xd83', '0xd8c', '0xd9d', '0xda0', '0xdd0', '0xdd3', '0xf10', '0x150f', '0x1582', '0x1699', '0x1730', '0x1736']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xa7d', '0xa7e', '0xa9a', '0xa9b', '0xb7b', '0xb7e', '0xb91', '0xb97', '0xba4', '0xbaa', '0xbad', '0xbb0', '0xbc5', '0xbf6', '0xbf9', '0xc08', '0xc10', '0xc11', '0xc19', '0xc1b', '0xc30', '0xc3a', '0xc3f', '0xc48', '0xc4d', '0xc52', '0xc57', '0xc6a', '0xc6c', '0xc71', '0xc75', '0xc7f', '0xc9f', '0xca2', '0xcaf', '0xd3c', '0xd3f', '0xd51', '0xd5b', '0xd5e', '0xd6c', '0xd71', '0xd8a', '0xd90', '0xd93', '0xd98', '0xda7', '0xdcc', '0xdd6', '0xf0c', '0xf0d', '0xf16', '0xf17', '0x150b', '0x150c', '0x1515', '0x1517', '0x157b', '0x157e', '0x1588', '0x158a', '0x1692', '0x1695', '0x16a0', '0x16a5', '0x1727', '0x172c', '0x1739', '0x173f']`
- all_mapped_pcs: `['0xa7d', '0xa7e', '0xa7f', '0xa86', '0xa8d', '0xa94', '0xa9a', '0xa9b', '0xb7b', '0xb7e', '0xb82', '0xb8b', '0xb91', '0xb93', '0xb97', '0xb99', '0xba0', '0xba4', '0xba7', '0xbaa', '0xbad', '0xbb0', '0xbb3', '0xbba', '0xbbe', '0xbc5', '0xbc7', '0xbf6', '0xbf9', '0xbfd', '0xc01', '0xc08', '0xc0d', '0xc10', '0xc11', '0xc19', '0xc1b', '0xc1d', '0xc21', '0xc28', '0xc2c', '0xc30', '0xc33', '0xc3a', '0xc3c', '0xc3f', '0xc42', '0xc45', '0xc48', '0xc4d', '0xc4f', '0xc52', '0xc57', '0xc6a', '0xc6c', '0xc6e', '0xc71', '0xc75', '0xc77', '0xc7b', '0xc7f', '0xc83', '0xc87', '0xc8b', '0xc8f', '0xc93', '0xc97', '0xc9b', '0xc9f', '0xca2', '0xca7', '0xcab', '0xcaf', '0xd3c', '0xd3f', '0xd43', '0xd46', '0xd4a', '0xd51', '0xd54', '0xd5b', '0xd5e', '0xd61', '0xd65', '0xd6c', '0xd6e', '0xd71', '0xd74', '0xd7b', '0xd7f', '0xd83', '0xd8a', '0xd8c', '0xd90', '0xd93', '0xd98', '0xd9d', '0xda0', '0xda7', '0xdcc', '0xdd0', '0xdd3', '0xdd6', '0xf0c', '0xf0d', '0xf10', '0xf16', '0xf17', '0x150b', '0x150c', '0x150f', '0x1515', '0x1517', '0x157b', '0x157e', '0x1582', '0x1588', '0x158a', '0x1692', '0x1695', '0x1699', '0x16a0', '0x16a5', '0x1727', '0x172c', '0x1730', '0x1736', '0x1739', '0x173f']`
- direct_parents: `[]`
- direct_children: `['mem:0x202fe0', 'stack:[rbp-0x10]', 'stack:[rbp-0x18]', 'stack:[rbp-0x1c]', 'stack:[rbp-0x20]', 'stack:[rbp-0x28]', 'stack:[rbp-0x4]', 'stack:[rbp-0x8]', 'stack:[rbp-0xc]', 'var:array1', 'var:array1_size', 'var:array2', 'var:secret', 'var:stage1_count', 'var:temp', 'var:uops_available', 'var:uops_cnt']`

#### PC Relation Entries

- `0xa7d` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xa7e` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xa7f` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xa86` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xa8d` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xa94` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xa9a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xa9b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb7b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb7e` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb82` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xb8b` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xb91` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb93` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xb97` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb99` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xba0` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xba4` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xba7` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xbaa` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbad` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbb0` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbb3` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xbba` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xbbe` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xbc5` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbc7` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xbf6` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbf9` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbfd` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc01` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc08` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc0d` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc10` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc11` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc19` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc1b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc1d` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc21` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc28` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc2c` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc30` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc33` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc3a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc3c` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc3f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc42` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc45` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc48` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc4d` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc4f` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc52` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc57` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc6a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc6c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc6e` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc71` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc75` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc77` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc7b` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc7f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc83` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc87` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc8b` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc8f` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc93` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc97` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc9b` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xc9f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xca2` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xca7` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xcab` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xcaf` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd3c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd3f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd43` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xd46` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xd4a` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xd51` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd54` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xd5b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd5e` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd61` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xd65` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xd6c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd6e` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xd71` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd74` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xd7b` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xd7f` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xd83` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xd8a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd8c` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xd90` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd93` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd98` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd9d` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xda0` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xda7` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xdcc` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xdd0` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xdd3` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xdd6` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xf0c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xf0d` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xf10` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0xf16` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xf17` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x150b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x150c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x150f` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0x1515` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1517` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x157b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x157e` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1582` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0x1588` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x158a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1692` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1695` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1699` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0x16a0` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x16a5` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1727` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x172c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1730` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0x1736` kinds=`['address_component']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.addr_used_by/instruction_details.addr_objects']`
- `0x1739` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x173f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xa7f`: `lea r8, [rip + 0xfaa]` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `??:None` function=`_start`
  - use_objects: `['reg:rip']`
  - def_objects: `['reg:r8', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xa7f:mem_disp:1:0xfaa:i64', 'imm_occurrence:0xa7f:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xa7f:mem_disp:1:0xfaa:i64', 'imm_occurrence:0xa7f:mem_scale:1:0x1:i64']`
- PC `0xa86`: `lea rcx, [rip + 0xf33]` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `??:None` function=`_start`
  - use_objects: `['reg:rip']`
  - def_objects: `['reg:rcx', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xa86:mem_disp:1:0xf33:i64', 'imm_occurrence:0xa86:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xa86:mem_disp:1:0xf33:i64', 'imm_occurrence:0xa86:mem_scale:1:0x1:i64']`
- PC `0xa8d`: `lea rdi, [rip + 0x2a7]` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `??:None` function=`_start`
  - use_objects: `['reg:rip']`
  - def_objects: `['reg:rdi', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xa8d:mem_disp:1:0x2a7:i64', 'imm_occurrence:0xa8d:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xa8d:mem_disp:1:0x2a7:i64', 'imm_occurrence:0xa8d:mem_scale:1:0x1:i64']`
- PC `0xa94`: `call qword ptr [rip + 0x202546]` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `??:None` function=`_start`
  - call_target: `{'operand': 'qword ptr [rip + 0x202546]', 'resolved_symbol': '__libc_start_main@GLIBC_2.2.5', 'call_kind': 'indirect_call_through_memory', 'display_target': '__libc_start_main@GLIBC_2.2.5'}`
  - use_objects: `['mem:0x202fe0', 'reg:rip', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rsp+0x0]']`
  - addr_objects: `['imm_occurrence:0xa94:mem_disp:0:0x202546:i64', 'imm_occurrence:0xa94:mem_scale:0:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xa94:mem_disp:0:0x202546:i64', 'imm_occurrence:0xa94:mem_scale:0:0x1:i64']`
- PC `0xb82`: `mov qword ptr [rbp - 8], rdi` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:58` function=`spectre_function`
  - instruction_semantic_tags: `['argument_shuffle']`
  - use_objects: `['reg:rbp', 'reg:rdi']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x8]']`
  - addr_objects: `['imm_occurrence:0xb82:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xb82:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xb82:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xb82:mem_scale:0:0x1:i64']`
- PC `0xb8b`: `mov eax, dword ptr [rip + 0x20248f]` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function`
  - use_objects: `['reg:rip', 'var:array1_size']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xb8b:mem_disp:1:0x20248f:i64', 'imm_occurrence:0xb8b:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xb8b:mem_disp:1:0x20248f:i64', 'imm_occurrence:0xb8b:mem_scale:1:0x1:i64']`
- PC `0xb93`: `cmp qword ptr [rbp - 8], rax` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x8]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xb93:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xb93:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xb93:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xb93:mem_scale:0:0x1:i64']`
- PC `0xb99`: `lea rdx, [rip + 0x2024a0]` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rip']`
  - def_objects: `['reg:rdx', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xb99:mem_disp:1:0x2024a0:i64', 'imm_occurrence:0xb99:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xb99:mem_disp:1:0x2024a0:i64', 'imm_occurrence:0xb99:mem_scale:1:0x1:i64']`
- PC `0xba0`: `mov rax, qword ptr [rbp - 8]` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x8]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xba0:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xba0:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xba0:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xba0:mem_scale:1:0x1:i64']`
- PC `0xba7`: `movzx eax, byte ptr [rax]` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'var:array1']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xba7:mem_disp:1:0x0:i64', 'imm_occurrence:0xba7:mem_scale:1:0x1:i64', 'reg:rax', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xba7:mem_disp:1:0x0:i64', 'imm_occurrence:0xba7:mem_scale:1:0x1:i64']`
- PC `0xbb3`: `lea rax, [rip + 0x210706]` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rip']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xbb3:mem_disp:1:0x210706:i64', 'imm_occurrence:0xbb3:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xbb3:mem_disp:1:0x210706:i64', 'imm_occurrence:0xbb3:mem_scale:1:0x1:i64']`
- PC `0xbba`: `movzx edx, byte ptr [rdx + rax]` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rdx', 'var:array2']`
  - def_objects: `['reg:rdx', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xbba:mem_disp:1:0x0:i64', 'imm_occurrence:0xbba:mem_scale:1:0x1:i64', 'reg:rax', 'reg:rdx', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xbba:mem_disp:1:0x0:i64', 'imm_occurrence:0xbba:mem_scale:1:0x1:i64']`
- PC `0xbbe`: `movzx eax, byte ptr [rip + 0x202544]` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rip', 'var:temp']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xbbe:mem_disp:1:0x202544:i64', 'imm_occurrence:0xbbe:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xbbe:mem_disp:1:0x202544:i64', 'imm_occurrence:0xbbe:mem_scale:1:0x1:i64']`
- PC `0xbc7`: `mov byte ptr [rip + 0x20253c], al` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rip']`
  - def_objects: `['reg:rip', 'var:temp']`
  - addr_objects: `['imm_occurrence:0xbc7:mem_disp:0:0x20253c:i64', 'imm_occurrence:0xbc7:mem_scale:0:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xbc7:mem_disp:0:0x20253c:i64', 'imm_occurrence:0xbc7:mem_scale:0:0x1:i64']`
- PC `0xbfd`: `mov qword ptr [rbp - 0x28], rdi` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:88` function=`stage1_mistrain_trigger`
  - instruction_semantic_tags: `['argument_shuffle']`
  - use_objects: `['reg:rbp', 'reg:rdi']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x28]']`
  - addr_objects: `['imm_occurrence:0xbfd:mem_disp:0:0xffffffffffffffd8:i64', 'imm_occurrence:0xbfd:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xbfd:mem_disp:0:0xffffffffffffffd8:i64', 'imm_occurrence:0xbfd:mem_scale:0:0x1:i64']`
- PC `0xc01`: `mov dword ptr [rbp - 0x1c], 0x1d` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:92` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc01:operand_imm:1:0x1d:i32', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x1c]']`
  - addr_objects: `['imm_occurrence:0xc01:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xc01:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc01:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xc01:mem_scale:0:0x1:i64', 'imm_occurrence:0xc01:operand_imm:1:0x1d:i32']`
- PC `0xc0d`: `mov eax, dword ptr [rbp - 0x1c]` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x1c]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc0d:mem_disp:1:0xffffffffffffffe4:i64', 'imm_occurrence:0xc0d:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc0d:mem_disp:1:0xffffffffffffffe4:i64', 'imm_occurrence:0xc0d:mem_scale:1:0x1:i64']`
- PC `0xc1d`: `mov qword ptr [rbp - 0x18], rax` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x18]']`
  - addr_objects: `['imm_occurrence:0xc1d:mem_disp:0:0xffffffffffffffe8:i64', 'imm_occurrence:0xc1d:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc1d:mem_disp:0:0xffffffffffffffe8:i64', 'imm_occurrence:0xc1d:mem_scale:0:0x1:i64']`
- PC `0xc21`: `lea rax, [rip + 0x2023f8]` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rip']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc21:mem_disp:1:0x2023f8:i64', 'imm_occurrence:0xc21:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc21:mem_disp:1:0x2023f8:i64', 'imm_occurrence:0xc21:mem_scale:1:0x1:i64']`
- PC `0xc28`: `mov qword ptr [rbp - 8], rax` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x8]']`
  - addr_objects: `['imm_occurrence:0xc28:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xc28:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc28:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xc28:mem_scale:0:0x1:i64']`
- PC `0xc2c`: `mov rax, qword ptr [rbp - 8]` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/usr/lib/gcc/x86_64-linux-gnu/7/include/emmintrin.h:1486` function=`_mm_clflush`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x8]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc2c:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xc2c:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc2c:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xc2c:mem_scale:1:0x1:i64']`
- PC `0xc33`: `mov dword ptr [rbp - 0x20], 0` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:95` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc33:operand_imm:1:0x0:i32', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x20]']`
  - addr_objects: `['imm_occurrence:0xc33:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xc33:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc33:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xc33:mem_scale:0:0x1:i64', 'imm_occurrence:0xc33:operand_imm:1:0x0:i32']`
- PC `0xc3c`: `mov eax, dword ptr [rbp - 0x20]` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x20]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc3c:mem_disp:1:0xffffffffffffffe0:i64', 'imm_occurrence:0xc3c:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc3c:mem_disp:1:0xffffffffffffffe0:i64', 'imm_occurrence:0xc3c:mem_scale:1:0x1:i64']`
- PC `0xc42`: `mov dword ptr [rbp - 0x20], eax` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x20]']`
  - addr_objects: `['imm_occurrence:0xc42:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xc42:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc42:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xc42:mem_scale:0:0x1:i64']`
- PC `0xc45`: `mov eax, dword ptr [rbp - 0x20]` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x20]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc45:mem_disp:1:0xffffffffffffffe0:i64', 'imm_occurrence:0xc45:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc45:mem_disp:1:0xffffffffffffffe0:i64', 'imm_occurrence:0xc45:mem_scale:1:0x1:i64']`
- PC `0xc4f`: `None` groups=`['structural_role']` kinds=`['address_component']`
- PC `0xc6e`: `None` groups=`['structural_role']` kinds=`['address_component']`
- PC `0xc77`: `mov qword ptr [rbp - 0x10], rax` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x10]']`
  - addr_objects: `['imm_occurrence:0xc77:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc77:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc77:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc77:mem_scale:0:0x1:i64']`
- PC `0xc7b`: `mov rax, qword ptr [rbp - 0x10]` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc7b:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc7b:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc7b:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc7b:mem_scale:1:0x1:i64']`
- PC `0xc83`: `or qword ptr [rbp - 0x10], rax` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf', 'stack:[rbp-0x10]']`
  - addr_objects: `['imm_occurrence:0xc83:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc83:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc83:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc83:mem_scale:0:0x1:i64']`
- PC `0xc87`: `mov rax, qword ptr [rbp - 0x28]` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x28]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc87:mem_disp:1:0xffffffffffffffd8:i64', 'imm_occurrence:0xc87:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc87:mem_disp:1:0xffffffffffffffd8:i64', 'imm_occurrence:0xc87:mem_scale:1:0x1:i64']`
- PC `0xc8b`: `xor rax, qword ptr [rbp - 0x18]` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x18]']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xc8b:mem_disp:1:0xffffffffffffffe8:i64', 'imm_occurrence:0xc8b:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc8b:mem_disp:1:0xffffffffffffffe8:i64', 'imm_occurrence:0xc8b:mem_scale:1:0x1:i64']`
- PC `0xc8f`: `and rax, qword ptr [rbp - 0x10]` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xc8f:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc8f:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc8f:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc8f:mem_scale:1:0x1:i64']`
- PC `0xc93`: `xor rax, qword ptr [rbp - 0x18]` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x18]']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xc93:mem_disp:1:0xffffffffffffffe8:i64', 'imm_occurrence:0xc93:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc93:mem_disp:1:0xffffffffffffffe8:i64', 'imm_occurrence:0xc93:mem_scale:1:0x1:i64']`
- PC `0xc97`: `mov qword ptr [rbp - 0x10], rax` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x10]']`
  - addr_objects: `['imm_occurrence:0xc97:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc97:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc97:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc97:mem_scale:0:0x1:i64']`
- PC `0xc9b`: `mov rax, qword ptr [rbp - 0x10]` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xc9b:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc9b:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc9b:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc9b:mem_scale:1:0x1:i64']`
- PC `0xca7`: `sub dword ptr [rbp - 0x1c], 1` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xca7:operand_imm:1:0x1:i32', 'reg:rbp', 'stack:[rbp-0x1c]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf', 'stack:[rbp-0x1c]']`
  - addr_objects: `['imm_occurrence:0xca7:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xca7:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xca7:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xca7:mem_scale:0:0x1:i64', 'imm_occurrence:0xca7:operand_imm:1:0x1:i32']`
- PC `0xcab`: `cmp dword ptr [rbp - 0x1c], 0` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xcab:operand_imm:1:0x0:i32', 'reg:rbp', 'stack:[rbp-0x1c]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xcab:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xcab:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xcab:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xcab:mem_scale:0:0x1:i64', 'imm_occurrence:0xcab:operand_imm:1:0x0:i32']`
- PC `0xd43`: `None` groups=`['structural_role']` kinds=`['address_component']`
- PC `0xd46`: `mov qword ptr [rbp - 0x20], rsi` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:124` function=`main`
  - instruction_semantic_tags: `['argument_shuffle']`
  - use_objects: `['reg:rbp', 'reg:rsi']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x20]']`
  - addr_objects: `['imm_occurrence:0xd46:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xd46:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd46:mem_disp:0:0xffffffffffffffe0:i64', 'imm_occurrence:0xd46:mem_scale:0:0x1:i64']`
- PC `0xd4a`: `mov rax, qword ptr [rip + 0x20238f]` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:125` function=`main`
  - use_objects: `['reg:rip', 'var:secret']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xd4a:mem_disp:1:0x20238f:i64', 'imm_occurrence:0xd4a:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd4a:mem_disp:1:0x20238f:i64', 'imm_occurrence:0xd4a:mem_scale:1:0x1:i64']`
- PC `0xd54`: `lea rax, [rip + 0x2022e5]` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:125` function=`main`
  - use_objects: `['reg:rip']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xd54:mem_disp:1:0x2022e5:i64', 'imm_occurrence:0xd54:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd54:mem_disp:1:0x2022e5:i64', 'imm_occurrence:0xd54:mem_scale:1:0x1:i64']`
- PC `0xd61`: `mov qword ptr [rbp - 8], rax` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:125` function=`main`
  - use_objects: `['reg:rax', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x8]']`
  - addr_objects: `['imm_occurrence:0xd61:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xd61:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd61:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xd61:mem_scale:0:0x1:i64']`
- PC `0xd65`: `mov dword ptr [rbp - 0x10], 0` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:129` function=`main`
  - use_objects: `['imm_occurrence:0xd65:operand_imm:1:0x0:i32', 'reg:rbp']`
  - def_objects: `['reg:rip', 'stack:[rbp-0x10]']`
  - addr_objects: `['imm_occurrence:0xd65:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd65:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd65:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd65:mem_scale:0:0x1:i64', 'imm_occurrence:0xd65:operand_imm:1:0x0:i32']`
- PC `0xd6e`: `mov eax, dword ptr [rbp - 0x10]` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`main`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xd6e:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xd6e:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd6e:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xd6e:mem_scale:1:0x1:i64']`
- PC `0xd74`: `lea rax, [rip + 0x210545]` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`main`
  - use_objects: `['reg:rip']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xd74:mem_disp:1:0x210545:i64', 'imm_occurrence:0xd74:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd74:mem_disp:1:0x210545:i64', 'imm_occurrence:0xd74:mem_scale:1:0x1:i64']`
- PC `0xd7b`: `mov byte ptr [rdx + rax], 1` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`main`
  - use_objects: `['imm_occurrence:0xd7b:operand_imm:1:0x1:i8', 'reg:rax', 'reg:rdx']`
  - def_objects: `['reg:rip', 'var:array2']`
  - addr_objects: `['imm_occurrence:0xd7b:mem_disp:0:0x0:i64', 'imm_occurrence:0xd7b:mem_scale:0:0x1:i64', 'reg:rax', 'reg:rdx', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd7b:mem_disp:0:0x0:i64', 'imm_occurrence:0xd7b:mem_scale:0:0x1:i64', 'imm_occurrence:0xd7b:operand_imm:1:0x1:i8']`
- PC `0xd7f`: `add dword ptr [rbp - 0x10], 1` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`main`
  - use_objects: `['imm_occurrence:0xd7f:operand_imm:1:0x1:i32', 'reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf', 'stack:[rbp-0x10]']`
  - addr_objects: `['imm_occurrence:0xd7f:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd7f:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd7f:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd7f:mem_scale:0:0x1:i64', 'imm_occurrence:0xd7f:operand_imm:1:0x1:i32']`
- PC `0xd83`: `cmp dword ptr [rbp - 0x10], 0x1ffff` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`main`
  - use_objects: `['imm_occurrence:0xd83:operand_imm:1:0x1ffff:i32', 'reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xd83:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd83:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd83:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd83:mem_scale:0:0x1:i64', 'imm_occurrence:0xd83:operand_imm:1:0x1ffff:i32']`
- PC `0xd8c`: `mov rax, qword ptr [rbp - 8]` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `/root/src/spectre_stage1_2_auto.c:134` function=`main`
  - use_objects: `['reg:rbp', 'stack:[rbp-0x8]']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xd8c:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xd8c:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd8c:mem_disp:1:0xfffffffffffffff8:i64', 'imm_occurrence:0xd8c:mem_scale:1:0x1:i64']`
- PC `0xd9d`: `None` groups=`['structural_role']` kinds=`['address_component']`
- PC `0xda0`: `None` groups=`['structural_role']` kinds=`['address_component']`
- PC `0xdd0`: `None` groups=`['structural_role']` kinds=`['address_component']`
- PC `0xdd3`: `None` groups=`['structural_role']` kinds=`['address_component']`
- PC `0xf10`: `None` groups=`['structural_role']` kinds=`['address_component']`
- PC `0x150f`: `mov eax, dword ptr [rip + 0x20fc6f]` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `??:None` function=`pmu_uops_snap_before`
  - use_objects: `['reg:rip', 'var:uops_available']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0x150f:mem_disp:1:0x20fc6f:i64', 'imm_occurrence:0x150f:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0x150f:mem_disp:1:0x20fc6f:i64', 'imm_occurrence:0x150f:mem_scale:1:0x1:i64']`
- PC `0x1582`: `mov eax, dword ptr [rip + 0x20fbfc]` groups=`['structural_role']` kinds=`['address_component']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - use_objects: `['reg:rip', 'var:uops_available']`
  - def_objects: `['reg:rax', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0x1582:mem_disp:1:0x20fbfc:i64', 'imm_occurrence:0x1582:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0x1582:mem_disp:1:0x20fbfc:i64', 'imm_occurrence:0x1582:mem_scale:1:0x1:i64']`
- PC `0x1699`: `None` groups=`['structural_role']` kinds=`['address_component']`
- PC `0x1730`: `None` groups=`['structural_role']` kinds=`['address_component']`
- PC `0x1736`: `None` groups=`['structural_role']` kinds=`['address_component']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xa7d`: `push rax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xa7e`: `push rsp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xa9a`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xa9b`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xb7b`: `mov rbp, rsp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xb7e`: `sub rsp, 0x10` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xb91`: `mov eax, eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xb97`: `jae 0xbcd` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xba4`: `add rax, rdx` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbaa`: `movzx eax, al` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbad`: `shl eax, 9` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbb0`: `movsxd rdx, eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbc5`: `and eax, edx` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbf6`: `mov rbp, rsp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbf9`: `sub rsp, 0x30` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc08`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc10`: `cdq` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc11`: `shr edx, 0x1c` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc19`: `sub eax, edx` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc1b`: `cdqe` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc30`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc3a`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc3f`: `add eax, 1` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc48`: `cmp eax, 0xc7` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc4d`: `jle 0xc3c` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc52`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc57`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc6a`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc6c`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc71`: `mov ax, 0` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc75`: `cdqe` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc7f`: `shr rax, 0x10` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc9f`: `mov rdi, rax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xca2`: `call 0xb7a` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xcaf`: `jns 0xc0d` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd3c`: `mov rbp, rsp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd3f`: `sub rsp, 0x20` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd51`: `mov rdx, rax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd5b`: `sub rdx, rax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd5e`: `mov rax, rdx` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd6c`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd71`: `movsxd rdx, eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd8a`: `jle 0xd6e` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd90`: `mov rdi, rax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd93`: `call 0xbf5` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd98`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xda7`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xdcc`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xdd6`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xf0c`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xf0d`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xf16`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xf17`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x150b`: `push rbp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x150c`: `mov rbp, rsp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1515`: `test eax, eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1517`: `je 0x1577` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x157b`: `mov rbp, rsp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x157e`: `sub rsp, 0x20` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1588`: `test eax, eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x158a`: `je 0x168e` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1692`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1695`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x16a0`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x16a5`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1727`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x172c`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1739`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x173f`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xa7d`      a7d:	50                   	push   %rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xa7e`      a7e:	54                   	push   %rsp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xa7f`      a7f:	4c 8d 05 aa 0f 00 00 	lea    0xfaa(%rip),%r8        # 1a30 <__libc_csu_fini> groups=`['structural_role']` kinds=`['address_component']`
- `0xa86`      a86:	48 8d 0d 33 0f 00 00 	lea    0xf33(%rip),%rcx        # 19c0 <__libc_csu_init> groups=`['structural_role']` kinds=`['address_component']`
- `0xa8d`      a8d:	48 8d 3d a7 02 00 00 	lea    0x2a7(%rip),%rdi        # d3b <main> groups=`['structural_role']` kinds=`['address_component']`
- `0xa94`      a94:	ff 15 46 25 20 00    	callq  *0x202546(%rip)        # 202fe0 <__libc_start_main@GLIBC_2.2.5> groups=`['structural_role']` kinds=`['address_component']`
- `0xa9a`      a9a:	f4                   	hlt     groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xa9b`      a9b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb7b`      b7b:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb7e`      b7e:	48 83 ec 10          	sub    $0x10,%rsp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb82`      b82:	48 89 7d f8          	mov    %rdi,-0x8(%rbp) groups=`['structural_role']` kinds=`['address_component']`
- `0xb8b`      b8b:	8b 05 8f 24 20 00    	mov    0x20248f(%rip),%eax        # 203020 <array1_size> groups=`['structural_role']` kinds=`['address_component']`
- `0xb91`      b91:	89 c0                	mov    %eax,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb93`      b93:	48 39 45 f8          	cmp    %rax,-0x8(%rbp) groups=`['structural_role']` kinds=`['address_component']`
- `0xb97`      b97:	73 34                	jae    bcd <STAGE1_END> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb99`      b99:	48 8d 15 a0 24 20 00 	lea    0x2024a0(%rip),%rdx        # 203040 <array1> groups=`['structural_role']` kinds=`['address_component']`
- `0xba0`      ba0:	48 8b 45 f8          	mov    -0x8(%rbp),%rax groups=`['structural_role']` kinds=`['address_component']`
- `0xba4`      ba4:	48 01 d0             	add    %rdx,%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xba7`      ba7:	0f b6 00             	movzbl (%rax),%eax groups=`['structural_role']` kinds=`['address_component']`
- `0xbaa`      baa:	0f b6 c0             	movzbl %al,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbad`      bad:	c1 e0 09             	shl    $0x9,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbb0`      bb0:	48 63 d0             	movslq %eax,%rdx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbb3`      bb3:	48 8d 05 06 07 21 00 	lea    0x210706(%rip),%rax        # 2112c0 <array2> groups=`['structural_role']` kinds=`['address_component']`
- `0xbba`      bba:	0f b6 14 02          	movzbl (%rdx,%rax,1),%edx groups=`['structural_role']` kinds=`['address_component']`
- `0xbbe`      bbe:	0f b6 05 44 25 20 00 	movzbl 0x202544(%rip),%eax        # 203109 <temp> groups=`['structural_role']` kinds=`['address_component']`
- `0xbc5`      bc5:	21 d0                	and    %edx,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbc7`      bc7:	88 05 3c 25 20 00    	mov    %al,0x20253c(%rip)        # 203109 <temp> groups=`['structural_role']` kinds=`['address_component']`
- `0xbf6`      bf6:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbf9`      bf9:	48 83 ec 30          	sub    $0x30,%rsp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbfd`      bfd:	48 89 7d d8          	mov    %rdi,-0x28(%rbp) groups=`['structural_role']` kinds=`['address_component']`
- `0xc01`      c01:	c7 45 e4 1d 00 00 00 	movl   $0x1d,-0x1c(%rbp) groups=`['structural_role']` kinds=`['address_component']`
- `0xc08`      c08:	e9 9e 00 00 00       	jmpq   cab <stage1_mistrain_trigger+0xb6> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc0d`      c0d:	8b 45 e4             	mov    -0x1c(%rbp),%eax groups=`['structural_role']` kinds=`['address_component']`
- `0xc10`      c10:	99                   	cltd    groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc11`      c11:	c1 ea 1c             	shr    $0x1c,%edx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc19`      c19:	29 d0                	sub    %edx,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc1b`      c1b:	48 98                	cltq    groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc1d`      c1d:	48 89 45 e8          	mov    %rax,-0x18(%rbp) groups=`['structural_role']` kinds=`['address_component']`
- `0xc21`      c21:	48 8d 05 f8 23 20 00 	lea    0x2023f8(%rip),%rax        # 203020 <array1_size> groups=`['structural_role']` kinds=`['address_component']`
- `0xc28`      c28:	48 89 45 f8          	mov    %rax,-0x8(%rbp) groups=`['structural_role']` kinds=`['address_component']`
- `0xc2c`      c2c:	48 8b 45 f8          	mov    -0x8(%rbp),%rax groups=`['structural_role']` kinds=`['address_component']`
- `0xc30`      c30:	0f ae 38             	clflush (%rax) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc33`      c33:	c7 45 e0 00 00 00 00 	movl   $0x0,-0x20(%rbp) groups=`['structural_role']` kinds=`['address_component']`
- `0xc3a`      c3a:	eb 09                	jmp    c45 <stage1_mistrain_trigger+0x50> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc3c`      c3c:	8b 45 e0             	mov    -0x20(%rbp),%eax groups=`['structural_role']` kinds=`['address_component']`
- `0xc3f`      c3f:	83 c0 01             	add    $0x1,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc42`      c42:	89 45 e0             	mov    %eax,-0x20(%rbp) groups=`['structural_role']` kinds=`['address_component']`
- `0xc45`      c45:	8b 45 e0             	mov    -0x20(%rbp),%eax groups=`['structural_role']` kinds=`['address_component']`
- `0xc48`      c48:	3d c7 00 00 00       	cmp    $0xc7,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc4d`      c4d:	7e ed                	jle    c3c <stage1_mistrain_trigger+0x47> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc4f`      c4f:	8b 4d e4             	mov    -0x1c(%rbp),%ecx groups=`['structural_role']` kinds=`['address_component']`
- `0xc52`      c52:	ba ab aa aa 2a       	mov    $0x2aaaaaab,%edx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc57`      c57:	89 c8                	mov    %ecx,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc6a`      c6a:	29 c1                	sub    %eax,%ecx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc6c`      c6c:	89 ca                	mov    %ecx,%edx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc6e`      c6e:	8d 42 ff             	lea    -0x1(%rdx),%eax groups=`['structural_role']` kinds=`['address_component']`
- `0xc71`      c71:	66 b8 00 00          	mov    $0x0,%ax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc75`      c75:	48 98                	cltq    groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc77`      c77:	48 89 45 f0          	mov    %rax,-0x10(%rbp) groups=`['structural_role']` kinds=`['address_component']`
- `0xc7b`      c7b:	48 8b 45 f0          	mov    -0x10(%rbp),%rax groups=`['structural_role']` kinds=`['address_component']`
- `0xc7f`      c7f:	48 c1 e8 10          	shr    $0x10,%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc83`      c83:	48 09 45 f0          	or     %rax,-0x10(%rbp) groups=`['structural_role']` kinds=`['address_component']`
- `0xc87`      c87:	48 8b 45 d8          	mov    -0x28(%rbp),%rax groups=`['structural_role']` kinds=`['address_component']`
- `0xc8b`      c8b:	48 33 45 e8          	xor    -0x18(%rbp),%rax groups=`['structural_role']` kinds=`['address_component']`
- `0xc8f`      c8f:	48 23 45 f0          	and    -0x10(%rbp),%rax groups=`['structural_role']` kinds=`['address_component']`
- `0xc93`      c93:	48 33 45 e8          	xor    -0x18(%rbp),%rax groups=`['structural_role']` kinds=`['address_component']`
- `0xc97`      c97:	48 89 45 f0          	mov    %rax,-0x10(%rbp) groups=`['structural_role']` kinds=`['address_component']`
- `0xc9b`      c9b:	48 8b 45 f0          	mov    -0x10(%rbp),%rax groups=`['structural_role']` kinds=`['address_component']`
- `0xc9f`      c9f:	48 89 c7             	mov    %rax,%rdi groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xca2`      ca2:	e8 d3 fe ff ff       	callq  b7a <spectre_function> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xca7`      ca7:	83 6d e4 01          	subl   $0x1,-0x1c(%rbp) groups=`['structural_role']` kinds=`['address_component']`
- `0xcab`      cab:	83 7d e4 00          	cmpl   $0x0,-0x1c(%rbp) groups=`['structural_role']` kinds=`['address_component']`
- `0xcaf`      caf:	0f 89 58 ff ff ff    	jns    c0d <stage1_mistrain_trigger+0x18> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd3c`      d3c:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd3f`      d3f:	48 83 ec 20          	sub    $0x20,%rsp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd43`      d43:	89 7d ec             	mov    %edi,-0x14(%rbp) groups=`['structural_role']` kinds=`['address_component']`
- `0xd46`      d46:	48 89 75 e0          	mov    %rsi,-0x20(%rbp) groups=`['structural_role']` kinds=`['address_component']`
- `0xd4a`      d4a:	48 8b 05 8f 23 20 00 	mov    0x20238f(%rip),%rax        # 2030e0 <secret> groups=`['structural_role']` kinds=`['address_component']`
- `0xd51`      d51:	48 89 c2             	mov    %rax,%rdx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd54`      d54:	48 8d 05 e5 22 20 00 	lea    0x2022e5(%rip),%rax        # 203040 <array1> groups=`['structural_role']` kinds=`['address_component']`
- `0xd5b`      d5b:	48 29 c2             	sub    %rax,%rdx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd5e`      d5e:	48 89 d0             	mov    %rdx,%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd61`      d61:	48 89 45 f8          	mov    %rax,-0x8(%rbp) groups=`['structural_role']` kinds=`['address_component']`
- `0xd65`      d65:	c7 45 f0 00 00 00 00 	movl   $0x0,-0x10(%rbp) groups=`['structural_role']` kinds=`['address_component']`
- `0xd6c`      d6c:	eb 15                	jmp    d83 <main+0x48> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd6e`      d6e:	8b 45 f0             	mov    -0x10(%rbp),%eax groups=`['structural_role']` kinds=`['address_component']`
- `0xd71`      d71:	48 63 d0             	movslq %eax,%rdx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd74`      d74:	48 8d 05 45 05 21 00 	lea    0x210545(%rip),%rax        # 2112c0 <array2> groups=`['structural_role']` kinds=`['address_component']`
- `0xd7b`      d7b:	c6 04 02 01          	movb   $0x1,(%rdx,%rax,1) groups=`['structural_role']` kinds=`['address_component']`
- `0xd7f`      d7f:	83 45 f0 01          	addl   $0x1,-0x10(%rbp) groups=`['structural_role']` kinds=`['address_component']`
- `0xd83`      d83:	81 7d f0 ff ff 01 00 	cmpl   $0x1ffff,-0x10(%rbp) groups=`['structural_role']` kinds=`['address_component']`
- `0xd8a`      d8a:	7e e2                	jle    d6e <main+0x33> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd8c`      d8c:	48 8b 45 f8          	mov    -0x8(%rbp),%rax groups=`['structural_role']` kinds=`['address_component']`
- `0xd90`      d90:	48 89 c7             	mov    %rax,%rdi groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd93`      d93:	e8 5d fe ff ff       	callq  bf5 <stage1_mistrain_trigger> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd98`      d98:	e8 6f 01 00 00       	callq  f0c <pmu_stage1_get_count> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd9d`      d9d:	89 45 f4             	mov    %eax,-0xc(%rbp) groups=`['structural_role']` kinds=`['address_component']`
- `0xda0`      da0:	c7 45 f0 00 00 00 00 	movl   $0x0,-0x10(%rbp) groups=`['structural_role']` kinds=`['address_component']`
- `0xda7`      da7:	eb 27                	jmp    dd0 <main+0x95> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xdcc`      dcc:	83 45 f0 01          	addl   $0x1,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xdd0`      dd0:	8b 45 f0             	mov    -0x10(%rbp),%eax groups=`['structural_role']` kinds=`['address_component']`
- `0xdd3`      dd3:	3b 45 f4             	cmp    -0xc(%rbp),%eax groups=`['structural_role']` kinds=`['address_component']`
- `0xdd6`      dd6:	7c d1                	jl     da9 <main+0x6e> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xf0c`      f0c:	55                   	push   %rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xf0d`      f0d:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xf10`      f10:	8b 05 2a 42 20 00    	mov    0x20422a(%rip),%eax        # 205140 <stage1_count> groups=`['structural_role']` kinds=`['address_component']`
- `0xf16`      f16:	5d                   	pop    %rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xf17`      f17:	c3                   	retq    groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x150b`     150b:	55                   	push   %rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x150c`     150c:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x150f`     150f:	8b 05 6f fc 20 00    	mov    0x20fc6f(%rip),%eax        # 211184 <uops_available> groups=`['structural_role']` kinds=`['address_component']`
- `0x1515`     1515:	85 c0                	test   %eax,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1517`     1517:	74 5e                	je     1577 <pmu_uops_snap_before+0x6c> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x157b`     157b:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x157e`     157e:	48 83 ec 20          	sub    $0x20,%rsp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1582`     1582:	8b 05 fc fb 20 00    	mov    0x20fbfc(%rip),%eax        # 211184 <uops_available> groups=`['structural_role']` kinds=`['address_component']`
- `0x1588`     1588:	85 c0                	test   %eax,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x158a`     158a:	0f 84 fe 00 00 00    	je     168e <pmu_uops_snap_after+0x114> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1692`     1692:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1695`     1695:	48 83 ec 10          	sub    $0x10,%rsp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1699`     1699:	c7 45 fc 00 00 00 00 	movl   $0x0,-0x4(%rbp) groups=`['structural_role']` kinds=`['address_component']`
- `0x16a0`     16a0:	e9 8b 00 00 00       	jmpq   1730 <pmu_uops_print_results+0x9f> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x16a5`     16a5:	8b 45 fc             	mov    -0x4(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1727`     1727:	e8 74 f2 ff ff       	callq  9a0 <printf@plt> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x172c`     172c:	83 45 fc 01          	addl   $0x1,-0x4(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1730`     1730:	8b 05 4a fa 20 00    	mov    0x20fa4a(%rip),%eax        # 211180 <uops_cnt> groups=`['structural_role']` kinds=`['address_component']`
- `0x1736`     1736:	39 45 fc             	cmp    %eax,-0x4(%rbp) groups=`['structural_role']` kinds=`['address_component']`
- `0x1739`     1739:	0f 8c 66 ff ff ff    	jl     16a5 <pmu_uops_print_results+0x14> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x173f`     173f:	90                   	nop groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:58` function=`spectre_function` pcs=`['0xb7b', '0xb7e', '0xb82']` groups=`['evidence_only', 'structural_role']` kinds=`['address_component', 'evidence_only']`

```c
   56: ********************************************************************/
   57: __attribute__((noinline))
   58: void spectre_function(size_t x) {
   59: 
   60:   pmu_uops_snap_before();
```

- `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function` pcs=`['0xb8b', '0xb91', '0xb93', '0xb97']` groups=`['evidence_only', 'structural_role']` kinds=`['address_component', 'evidence_only']`

```c
   61: 
   62:   asm volatile(".globl STAGE1_BEGIN\nSTAGE1_BEGIN:");
   63:   if (x < array1_size) {
   64:     NOP_REGION_BEGIN
   65:     temp &= array2[array1[x] * 512];
```

- `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function` pcs=`['0xb99', '0xba0', '0xba4', '0xba7', '0xbaa', '0xbad', '0xbb0', '0xbb3', '0xbba', '0xbbe', '0xbc5', '0xbc7']` groups=`['evidence_only', 'structural_role']` kinds=`['address_component', 'evidence_only']`

```c
   63:   if (x < array1_size) {
   64:     NOP_REGION_BEGIN
   65:     temp &= array2[array1[x] * 512];
   66:     NOP_REGION_END
   67:   }
```

- `/root/src/spectre_stage1_2_auto.c:88` function=`stage1_mistrain_trigger` pcs=`['0xbf6', '0xbf9', '0xbfd']` groups=`['evidence_only', 'structural_role']` kinds=`['address_component', 'evidence_only']`

```c
   86: ********************************************************************/
   87: __attribute__((noinline))
   88: void stage1_mistrain_trigger(size_t malicious_x) {
   89:     int j;
   90:     size_t training_x, x;
```

- `/root/src/spectre_stage1_2_auto.c:92` function=`stage1_mistrain_trigger` pcs=`['0xc01']` groups=`['structural_role']` kinds=`['address_component']`

```c
   90:     size_t training_x, x;
   91: 
   92:     for (j = 29; j >= 0; j--) {
   93:         training_x = (size_t)(j % 16);
   94:         _mm_clflush(&array1_size);
```

- `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger` pcs=`['0xc0d', '0xc10', '0xc11', '0xc19', '0xc1b', '0xc1d', '0xc21', '0xc28']` groups=`['evidence_only', 'structural_role']` kinds=`['address_component', 'evidence_only']`

```c
   91: 
   92:     for (j = 29; j >= 0; j--) {
   93:         training_x = (size_t)(j % 16);
   94:         _mm_clflush(&array1_size);
   95:         for (volatile int z = 0; z < 200; z++) {}
```

- `/root/src/spectre_stage1_2_auto.c:95` function=`stage1_mistrain_trigger` pcs=`['0xc33']` groups=`['structural_role']` kinds=`['address_component']`

```c
   93:         training_x = (size_t)(j % 16);
   94:         _mm_clflush(&array1_size);
   95:         for (volatile int z = 0; z < 200; z++) {}
   96: 
   97:         x = ((j % 6) - 1) & ~0xFFFF;
```

- `/root/src/spectre_stage1_2_auto.c:124` function=`main` pcs=`['0xd3c', '0xd3f', '0xd46']` groups=`['evidence_only', 'structural_role']` kinds=`['address_component', 'evidence_only']`

```c
  122: ********************************************************************/
  123: #ifndef STAGE2_TEST_MAIN
  124: int main(int argc, const char **argv) {
  125:     size_t malicious_x = (size_t)(secret - (char *)array1);
  126:     int i;
```

- `/root/src/spectre_stage1_2_auto.c:125` function=`main` pcs=`['0xd4a', '0xd51', '0xd54', '0xd5b', '0xd5e', '0xd61']` groups=`['evidence_only', 'structural_role']` kinds=`['address_component', 'evidence_only']`

```c
  123: #ifndef STAGE2_TEST_MAIN
  124: int main(int argc, const char **argv) {
  125:     size_t malicious_x = (size_t)(secret - (char *)array1);
  126:     int i;
  127: 
```

- `/root/src/spectre_stage1_2_auto.c:129` function=`main` pcs=`['0xd65']` groups=`['structural_role']` kinds=`['address_component']`

```c
  127: 
  128:     /* 初始化 array2 */
  129:     for (i = 0; i < (int)sizeof(array2); i++) {
  130:         array2[i] = 1;
  131:     }
```

- `/root/src/spectre_stage1_2_auto.c:134` function=`main` pcs=`['0xd8c', '0xd90', '0xd93']` groups=`['evidence_only', 'structural_role']` kinds=`['address_component', 'evidence_only']`

```c
  132: 
  133:     /* 执行阶段1 */
  134:     stage1_mistrain_trigger(malicious_x);
  135: 
  136:     /* Stage1 BR_MISP 数据 */
```

- `/usr/lib/gcc/x86_64-linux-gnu/7/include/emmintrin.h:1486` function=`_mm_clflush` pcs=`['0xc2c']` groups=`['structural_role']` kinds=`['address_component']`

### 147. `stack:[rsp-0x8]`

- Role: `backward_leaf`
- Type: `stack`
- Label: `stack[rsp-0x8]`
- Mapping kind: `stack_slot_local_or_spill`
- Confidence: `probable`
- Object semantic tags: `[]`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Reason: 对象类型为 stack，通常对应局部变量、形参栈槽或编译器 spill 槽位。
- Candidate program elements: `['stack[rsp-0x8]']`
- direct_use_pcs: `['0xa75', '0xde2', '0xde3']`
- direct_def_pcs: `[]`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `['0xa75', '0xde2', '0xde3']`
- structural_role_pcs: `[]`
- anchor_pcs: `['0xa75', '0xde2', '0xde3']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xa70', '0xa72', '0xa76', '0xa79', '0xddd']`
- all_mapped_pcs: `['0xa70', '0xa72', '0xa75', '0xa76', '0xa79', '0xddd', '0xde2', '0xde3']`
- direct_parents: `[]`
- direct_children: `['reg:rbp', 'reg:rip', 'reg:rsi', 'reg:rsp']`

#### PC Relation Entries

- `0xa70` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xa72` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xa75` kinds=`['direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['object_detail.used_by/instruction_details.use_objects']`
- `0xa76` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xa79` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xddd` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xde2` kinds=`['direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['object_detail.used_by/instruction_details.use_objects']`
- `0xde3` kinds=`['direct_use']` groups=`['direct_operand']` primary_group=`direct_operand` sources=`['object_detail.used_by/instruction_details.use_objects']`

#### Direct Anchor Instruction Evidence

- PC `0xa75`: `pop rsi` groups=`['direct_operand']` kinds=`['direct_use']`
  - Source: `??:None` function=`_start`
  - use_objects: `['reg:rsp', 'stack:[rsp-0x8]']`
  - def_objects: `['reg:rip', 'reg:rsi', 'reg:rsp']`
- PC `0xde2`: `None` groups=`['direct_operand']` kinds=`['direct_use']`
- PC `0xde3`: `None` groups=`['direct_operand']` kinds=`['direct_use']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xa70`: `xor ebp, ebp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xa72`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xa76`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xa79`: `and rsp, 0xfffffffffffffff0` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xddd`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xa70`      a70:	31 ed                	xor    %ebp,%ebp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xa72`      a72:	49 89 d1             	mov    %rdx,%r9 groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xa75`      a75:	5e                   	pop    %rsi groups=`['direct_operand']` kinds=`['direct_use']`
- `0xa76`      a76:	48 89 e2             	mov    %rsp,%rdx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xa79`      a79:	48 83 e4 f0          	and    $0xfffffffffffffff0,%rsp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xddd`      ddd:	b8 00 00 00 00       	mov    $0x0,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xde2`      de2:	c9                   	leaveq  groups=`['direct_operand']` kinds=`['direct_use']`
- `0xde3`      de3:	c3                   	retq    groups=`['direct_operand']` kinds=`['direct_use']`

#### Source Evidence

_No source evidence found._

## Forward Sink Mappings

### 1. `reg:af`

- Role: `forward_sink`
- Type: `reg`
- Label: `af`
- Mapping kind: `execution_register_carrier`
- Confidence: `structural`
- Object semantic tags: `[]`
- Anchor instruction tags: `['prologue']`
- Scaffolding tags: `['prologue']`
- Reason: 对象类型为 reg，表示执行时承载值的寄存器，而不是稳定的 C 变量名。 检测到 ABI/脚手架标签：prologue，应更偏向解释为结构性对象，而非优先可变异语义对象。
- Candidate program elements: `['af']`
- direct_use_pcs: `[]`
- direct_def_pcs: `['0xb7e', '0xb93', '0xba4', '0xbf9', '0xc14', '0xc19', '0xc3f', '0xc48', '0xc60', '0xc64', '0xc66', '0xc68', '0xc6a', '0xca7', '0xcab', '0xd3f', '0xd5b', '0xd7f', '0xd83', '0xdd3', '0x157e', '0x1695', '0x1736']`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `[]`
- structural_role_pcs: `['0xb7e', '0xb93', '0xba4', '0xbf9', '0xc14', '0xc19', '0xc3f', '0xc48', '0xc60', '0xc64', '0xc66', '0xc68', '0xc6a', '0xca7', '0xcab', '0xd3f', '0xd5b', '0xd7f', '0xd83', '0xdd3', '0x157e', '0x1695', '0x1736']`
- anchor_pcs: `['0xb7e', '0xb93', '0xba4', '0xbf9', '0xc14', '0xc19', '0xc3f', '0xc48', '0xc60', '0xc64', '0xc66', '0xc68', '0xc6a', '0xca7', '0xcab', '0xd3f', '0xd5b', '0xd7f', '0xd83', '0xdd3', '0x157e', '0x1695', '0x1736']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xb7a', '0xb7b', '0xb82', '0xb8b', '0xb91', '0xb97', '0xb99', '0xba0', '0xba7', '0xbaa', '0xbf5', '0xbf6', '0xbfd', '0xc10', '0xc11', '0xc16', '0xc1b', '0xc1d', '0xc3a', '0xc3c', '0xc42', '0xc45', '0xc4d', '0xc5b', '0xc5d', '0xc62', '0xc6c', '0xc6e', '0xca2', '0xcaf', '0xd3b', '0xd3c', '0xd43', '0xd46', '0xd51', '0xd54', '0xd5e', '0xd61', '0xd7b', '0xd8a', '0xdcc', '0xdd0', '0xdd6', '0x157a', '0x157b', '0x1582', '0x1588', '0x1691', '0x1692', '0x1699', '0x16a0', '0x172c', '0x1730', '0x1739', '0x173f']`
- all_mapped_pcs: `['0xb7a', '0xb7b', '0xb7e', '0xb82', '0xb8b', '0xb91', '0xb93', '0xb97', '0xb99', '0xba0', '0xba4', '0xba7', '0xbaa', '0xbf5', '0xbf6', '0xbf9', '0xbfd', '0xc10', '0xc11', '0xc14', '0xc16', '0xc19', '0xc1b', '0xc1d', '0xc3a', '0xc3c', '0xc3f', '0xc42', '0xc45', '0xc48', '0xc4d', '0xc5b', '0xc5d', '0xc60', '0xc62', '0xc64', '0xc66', '0xc68', '0xc6a', '0xc6c', '0xc6e', '0xca2', '0xca7', '0xcab', '0xcaf', '0xd3b', '0xd3c', '0xd3f', '0xd43', '0xd46', '0xd51', '0xd54', '0xd5b', '0xd5e', '0xd61', '0xd7b', '0xd7f', '0xd83', '0xd8a', '0xdcc', '0xdd0', '0xdd3', '0xdd6', '0x157a', '0x157b', '0x157e', '0x1582', '0x1588', '0x1691', '0x1692', '0x1695', '0x1699', '0x16a0', '0x172c', '0x1730', '0x1736', '0x1739', '0x173f']`
- direct_parents: `['reg:cf', 'reg:of', 'reg:rax', 'reg:rbp', 'reg:rcx', 'reg:rdx', 'reg:rsp', 'reg:sf', 'reg:zf', 'stack:[rbp-0x10]', 'stack:[rbp-0x1c]', 'stack:[rbp-0x4]', 'stack:[rbp-0x8]', 'stack:[rbp-0xc]']`
- direct_children: `[]`

#### PC Relation Entries

- `0xb7a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb7b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb7e` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xb82` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb8b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb91` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb93` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xb97` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb99` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xba0` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xba4` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xba7` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbaa` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbf5` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbf6` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbf9` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xbfd` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc10` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc11` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc14` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xc16` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc19` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xc1b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc1d` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc3a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc3c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc3f` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xc42` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc45` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc48` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xc4d` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc5b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc5d` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc60` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xc62` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc64` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xc66` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xc68` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xc6a` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xc6c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc6e` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xca2` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xca7` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xcab` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xcaf` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd3b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd3c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd3f` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xd43` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd46` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd51` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd54` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd5b` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xd5e` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd61` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd7b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd7f` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xd83` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xd8a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xdcc` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xdd0` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xdd3` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xdd6` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x157a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x157b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x157e` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0x1582` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1588` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1691` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1692` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1695` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0x1699` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x16a0` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x172c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1730` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1736` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0x1739` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x173f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xb7e`: `sub rsp, 0x10` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:58` function=`spectre_function`
  - instruction_semantic_tags: `['prologue']`
  - use_objects: `['imm_occurrence:0xb7e:operand_imm:1:0x10:i64', 'reg:rsp']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xb7e:operand_imm:1:0x10:i64']`
- PC `0xb93`: `cmp qword ptr [rbp - 8], rax` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x8]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xb93:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xb93:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xb93:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xb93:mem_scale:0:0x1:i64']`
- PC `0xba4`: `add rax, rdx` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rdx']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0xbf9`: `sub rsp, 0x30` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:88` function=`stage1_mistrain_trigger`
  - instruction_semantic_tags: `['prologue']`
  - use_objects: `['imm_occurrence:0xbf9:operand_imm:1:0x30:i64', 'reg:rsp']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xbf9:operand_imm:1:0x30:i64']`
- PC `0xc14`: `add eax, edx` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rdx']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0xc19`: `sub eax, edx` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rdx']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0xc3f`: `add eax, 1` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc3f:operand_imm:1:0x1:i32', 'reg:rax']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xc3f:operand_imm:1:0x1:i32']`
- PC `0xc48`: `cmp eax, 0xc7` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc48:operand_imm:1:0xc7:i32', 'reg:rax']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xc48:operand_imm:1:0xc7:i32']`
- PC `0xc60`: `None` groups=`['structural_role']` kinds=`['store_target']`
- PC `0xc64`: `None` groups=`['structural_role']` kinds=`['store_target']`
- PC `0xc66`: `None` groups=`['structural_role']` kinds=`['store_target']`
- PC `0xc68`: `None` groups=`['structural_role']` kinds=`['store_target']`
- PC `0xc6a`: `None` groups=`['structural_role']` kinds=`['store_target']`
- PC `0xca7`: `sub dword ptr [rbp - 0x1c], 1` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xca7:operand_imm:1:0x1:i32', 'reg:rbp', 'stack:[rbp-0x1c]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf', 'stack:[rbp-0x1c]']`
  - addr_objects: `['imm_occurrence:0xca7:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xca7:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xca7:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xca7:mem_scale:0:0x1:i64', 'imm_occurrence:0xca7:operand_imm:1:0x1:i32']`
- PC `0xcab`: `cmp dword ptr [rbp - 0x1c], 0` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xcab:operand_imm:1:0x0:i32', 'reg:rbp', 'stack:[rbp-0x1c]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xcab:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xcab:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xcab:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xcab:mem_scale:0:0x1:i64', 'imm_occurrence:0xcab:operand_imm:1:0x0:i32']`
- PC `0xd3f`: `sub rsp, 0x20` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:124` function=`main`
  - instruction_semantic_tags: `['prologue']`
  - use_objects: `['imm_occurrence:0xd3f:operand_imm:1:0x20:i64', 'reg:rsp']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xd3f:operand_imm:1:0x20:i64']`
- PC `0xd5b`: `sub rdx, rax` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:125` function=`main`
  - use_objects: `['reg:rax', 'reg:rdx']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rdx', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0xd7f`: `add dword ptr [rbp - 0x10], 1` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`main`
  - use_objects: `['imm_occurrence:0xd7f:operand_imm:1:0x1:i32', 'reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf', 'stack:[rbp-0x10]']`
  - addr_objects: `['imm_occurrence:0xd7f:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd7f:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd7f:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd7f:mem_scale:0:0x1:i64', 'imm_occurrence:0xd7f:operand_imm:1:0x1:i32']`
- PC `0xd83`: `cmp dword ptr [rbp - 0x10], 0x1ffff` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`main`
  - use_objects: `['imm_occurrence:0xd83:operand_imm:1:0x1ffff:i32', 'reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xd83:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd83:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd83:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd83:mem_scale:0:0x1:i64', 'imm_occurrence:0xd83:operand_imm:1:0x1ffff:i32']`
- PC `0xdd3`: `None` groups=`['structural_role']` kinds=`['store_target']`
- PC `0x157e`: `sub rsp, 0x20` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - instruction_semantic_tags: `['prologue']`
  - use_objects: `['imm_occurrence:0x157e:operand_imm:1:0x20:i64', 'reg:rsp']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0x157e:operand_imm:1:0x20:i64']`
- PC `0x1695`: `None` groups=`['structural_role']` kinds=`['store_target']`
- PC `0x1736`: `None` groups=`['structural_role']` kinds=`['store_target']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xb7a`: `push rbp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xb7b`: `mov rbp, rsp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xb82`: `mov qword ptr [rbp - 8], rdi` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xb8b`: `mov eax, dword ptr [rip + 0x20248f]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xb91`: `mov eax, eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xb97`: `jae 0xbcd` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xb99`: `lea rdx, [rip + 0x2024a0]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xba0`: `mov rax, qword ptr [rbp - 8]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xba7`: `movzx eax, byte ptr [rax]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbaa`: `movzx eax, al` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbf5`: `push rbp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbf6`: `mov rbp, rsp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbfd`: `mov qword ptr [rbp - 0x28], rdi` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc10`: `cdq` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc11`: `shr edx, 0x1c` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc16`: `and eax, 0xf` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc1b`: `cdqe` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc1d`: `mov qword ptr [rbp - 0x18], rax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc3a`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc3c`: `mov eax, dword ptr [rbp - 0x20]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc42`: `mov dword ptr [rbp - 0x20], eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc45`: `mov eax, dword ptr [rbp - 0x20]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc4d`: `jle 0xc3c` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc5b`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc5d`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc62`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc6c`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc6e`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xca2`: `call 0xb7a` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xcaf`: `jns 0xc0d` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd3b`: `push rbp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd3c`: `mov rbp, rsp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd43`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd46`: `mov qword ptr [rbp - 0x20], rsi` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd51`: `mov rdx, rax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd54`: `lea rax, [rip + 0x2022e5]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd5e`: `mov rax, rdx` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd61`: `mov qword ptr [rbp - 8], rax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd7b`: `mov byte ptr [rdx + rax], 1` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd8a`: `jle 0xd6e` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xdcc`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xdd0`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xdd6`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x157a`: `push rbp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x157b`: `mov rbp, rsp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1582`: `mov eax, dword ptr [rip + 0x20fbfc]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1588`: `test eax, eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1691`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1692`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1699`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x16a0`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x172c`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1730`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1739`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x173f`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xb7a`      b7a:	55                   	push   %rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb7b`      b7b:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb7e`      b7e:	48 83 ec 10          	sub    $0x10,%rsp groups=`['structural_role']` kinds=`['store_target']`
- `0xb82`      b82:	48 89 7d f8          	mov    %rdi,-0x8(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb8b`      b8b:	8b 05 8f 24 20 00    	mov    0x20248f(%rip),%eax        # 203020 <array1_size> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb91`      b91:	89 c0                	mov    %eax,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb93`      b93:	48 39 45 f8          	cmp    %rax,-0x8(%rbp) groups=`['structural_role']` kinds=`['store_target']`
- `0xb97`      b97:	73 34                	jae    bcd <STAGE1_END> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb99`      b99:	48 8d 15 a0 24 20 00 	lea    0x2024a0(%rip),%rdx        # 203040 <array1> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xba0`      ba0:	48 8b 45 f8          	mov    -0x8(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xba4`      ba4:	48 01 d0             	add    %rdx,%rax groups=`['structural_role']` kinds=`['store_target']`
- `0xba7`      ba7:	0f b6 00             	movzbl (%rax),%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbaa`      baa:	0f b6 c0             	movzbl %al,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbf5`      bf5:	55                   	push   %rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbf6`      bf6:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbf9`      bf9:	48 83 ec 30          	sub    $0x30,%rsp groups=`['structural_role']` kinds=`['store_target']`
- `0xbfd`      bfd:	48 89 7d d8          	mov    %rdi,-0x28(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc10`      c10:	99                   	cltd    groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc11`      c11:	c1 ea 1c             	shr    $0x1c,%edx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc14`      c14:	01 d0                	add    %edx,%eax groups=`['structural_role']` kinds=`['store_target']`
- `0xc16`      c16:	83 e0 0f             	and    $0xf,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc19`      c19:	29 d0                	sub    %edx,%eax groups=`['structural_role']` kinds=`['store_target']`
- `0xc1b`      c1b:	48 98                	cltq    groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc1d`      c1d:	48 89 45 e8          	mov    %rax,-0x18(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc3a`      c3a:	eb 09                	jmp    c45 <stage1_mistrain_trigger+0x50> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc3c`      c3c:	8b 45 e0             	mov    -0x20(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc3f`      c3f:	83 c0 01             	add    $0x1,%eax groups=`['structural_role']` kinds=`['store_target']`
- `0xc42`      c42:	89 45 e0             	mov    %eax,-0x20(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc45`      c45:	8b 45 e0             	mov    -0x20(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc48`      c48:	3d c7 00 00 00       	cmp    $0xc7,%eax groups=`['structural_role']` kinds=`['store_target']`
- `0xc4d`      c4d:	7e ed                	jle    c3c <stage1_mistrain_trigger+0x47> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc5b`      c5b:	89 c8                	mov    %ecx,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc5d`      c5d:	c1 f8 1f             	sar    $0x1f,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc60`      c60:	29 c2                	sub    %eax,%edx groups=`['structural_role']` kinds=`['store_target']`
- `0xc62`      c62:	89 d0                	mov    %edx,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc64`      c64:	01 c0                	add    %eax,%eax groups=`['structural_role']` kinds=`['store_target']`
- `0xc66`      c66:	01 d0                	add    %edx,%eax groups=`['structural_role']` kinds=`['store_target']`
- `0xc68`      c68:	01 c0                	add    %eax,%eax groups=`['structural_role']` kinds=`['store_target']`
- `0xc6a`      c6a:	29 c1                	sub    %eax,%ecx groups=`['structural_role']` kinds=`['store_target']`
- `0xc6c`      c6c:	89 ca                	mov    %ecx,%edx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc6e`      c6e:	8d 42 ff             	lea    -0x1(%rdx),%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xca2`      ca2:	e8 d3 fe ff ff       	callq  b7a <spectre_function> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xca7`      ca7:	83 6d e4 01          	subl   $0x1,-0x1c(%rbp) groups=`['structural_role']` kinds=`['store_target']`
- `0xcab`      cab:	83 7d e4 00          	cmpl   $0x0,-0x1c(%rbp) groups=`['structural_role']` kinds=`['store_target']`
- `0xcaf`      caf:	0f 89 58 ff ff ff    	jns    c0d <stage1_mistrain_trigger+0x18> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd3b`      d3b:	55                   	push   %rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd3c`      d3c:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd3f`      d3f:	48 83 ec 20          	sub    $0x20,%rsp groups=`['structural_role']` kinds=`['store_target']`
- `0xd43`      d43:	89 7d ec             	mov    %edi,-0x14(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd46`      d46:	48 89 75 e0          	mov    %rsi,-0x20(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd51`      d51:	48 89 c2             	mov    %rax,%rdx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd54`      d54:	48 8d 05 e5 22 20 00 	lea    0x2022e5(%rip),%rax        # 203040 <array1> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd5b`      d5b:	48 29 c2             	sub    %rax,%rdx groups=`['structural_role']` kinds=`['store_target']`
- `0xd5e`      d5e:	48 89 d0             	mov    %rdx,%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd61`      d61:	48 89 45 f8          	mov    %rax,-0x8(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd7b`      d7b:	c6 04 02 01          	movb   $0x1,(%rdx,%rax,1) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd7f`      d7f:	83 45 f0 01          	addl   $0x1,-0x10(%rbp) groups=`['structural_role']` kinds=`['store_target']`
- `0xd83`      d83:	81 7d f0 ff ff 01 00 	cmpl   $0x1ffff,-0x10(%rbp) groups=`['structural_role']` kinds=`['store_target']`
- `0xd8a`      d8a:	7e e2                	jle    d6e <main+0x33> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xdcc`      dcc:	83 45 f0 01          	addl   $0x1,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xdd0`      dd0:	8b 45 f0             	mov    -0x10(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xdd3`      dd3:	3b 45 f4             	cmp    -0xc(%rbp),%eax groups=`['structural_role']` kinds=`['store_target']`
- `0xdd6`      dd6:	7c d1                	jl     da9 <main+0x6e> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x157a`     157a:	55                   	push   %rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x157b`     157b:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x157e`     157e:	48 83 ec 20          	sub    $0x20,%rsp groups=`['structural_role']` kinds=`['store_target']`
- `0x1582`     1582:	8b 05 fc fb 20 00    	mov    0x20fbfc(%rip),%eax        # 211184 <uops_available> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1588`     1588:	85 c0                	test   %eax,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1691`     1691:	55                   	push   %rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1692`     1692:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1695`     1695:	48 83 ec 10          	sub    $0x10,%rsp groups=`['structural_role']` kinds=`['store_target']`
- `0x1699`     1699:	c7 45 fc 00 00 00 00 	movl   $0x0,-0x4(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x16a0`     16a0:	e9 8b 00 00 00       	jmpq   1730 <pmu_uops_print_results+0x9f> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x172c`     172c:	83 45 fc 01          	addl   $0x1,-0x4(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1730`     1730:	8b 05 4a fa 20 00    	mov    0x20fa4a(%rip),%eax        # 211180 <uops_cnt> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1736`     1736:	39 45 fc             	cmp    %eax,-0x4(%rbp) groups=`['structural_role']` kinds=`['store_target']`
- `0x1739`     1739:	0f 8c 66 ff ff ff    	jl     16a5 <pmu_uops_print_results+0x14> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x173f`     173f:	90                   	nop groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:58` function=`spectre_function` pcs=`['0xb7a', '0xb7b', '0xb7e', '0xb82']` groups=`['evidence_only', 'structural_role']` kinds=`['evidence_only', 'store_target']`

```c
   56: ********************************************************************/
   57: __attribute__((noinline))
   58: void spectre_function(size_t x) {
   59: 
   60:   pmu_uops_snap_before();
```

- `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function` pcs=`['0xb8b', '0xb91', '0xb93', '0xb97']` groups=`['evidence_only', 'structural_role']` kinds=`['evidence_only', 'store_target']`

```c
   61: 
   62:   asm volatile(".globl STAGE1_BEGIN\nSTAGE1_BEGIN:");
   63:   if (x < array1_size) {
   64:     NOP_REGION_BEGIN
   65:     temp &= array2[array1[x] * 512];
```

- `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function` pcs=`['0xb99', '0xba0', '0xba4', '0xba7', '0xbaa']` groups=`['evidence_only', 'structural_role']` kinds=`['evidence_only', 'store_target']`

```c
   63:   if (x < array1_size) {
   64:     NOP_REGION_BEGIN
   65:     temp &= array2[array1[x] * 512];
   66:     NOP_REGION_END
   67:   }
```

- `/root/src/spectre_stage1_2_auto.c:88` function=`stage1_mistrain_trigger` pcs=`['0xbf5', '0xbf6', '0xbf9', '0xbfd']` groups=`['evidence_only', 'structural_role']` kinds=`['evidence_only', 'store_target']`

```c
   86: ********************************************************************/
   87: __attribute__((noinline))
   88: void stage1_mistrain_trigger(size_t malicious_x) {
   89:     int j;
   90:     size_t training_x, x;
```

- `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger` pcs=`['0xc10', '0xc11', '0xc14', '0xc16', '0xc19', '0xc1b', '0xc1d']` groups=`['evidence_only', 'structural_role']` kinds=`['evidence_only', 'store_target']`

```c
   91: 
   92:     for (j = 29; j >= 0; j--) {
   93:         training_x = (size_t)(j % 16);
   94:         _mm_clflush(&array1_size);
   95:         for (volatile int z = 0; z < 200; z++) {}
```

- `/root/src/spectre_stage1_2_auto.c:124` function=`main` pcs=`['0xd3b', '0xd3c', '0xd3f', '0xd46']` groups=`['evidence_only', 'structural_role']` kinds=`['evidence_only', 'store_target']`

```c
  122: ********************************************************************/
  123: #ifndef STAGE2_TEST_MAIN
  124: int main(int argc, const char **argv) {
  125:     size_t malicious_x = (size_t)(secret - (char *)array1);
  126:     int i;
```

- `/root/src/spectre_stage1_2_auto.c:125` function=`main` pcs=`['0xd51', '0xd54', '0xd5b', '0xd5e', '0xd61']` groups=`['evidence_only', 'structural_role']` kinds=`['evidence_only', 'store_target']`

```c
  123: #ifndef STAGE2_TEST_MAIN
  124: int main(int argc, const char **argv) {
  125:     size_t malicious_x = (size_t)(secret - (char *)array1);
  126:     int i;
  127: 
```

### 2. `reg:pf`

- Role: `forward_sink`
- Type: `reg`
- Label: `pf`
- Mapping kind: `execution_register_carrier`
- Confidence: `structural`
- Object semantic tags: `[]`
- Anchor instruction tags: `['prologue', 'stack_alignment']`
- Scaffolding tags: `['prologue', 'stack_alignment']`
- Reason: 对象类型为 reg，表示执行时承载值的寄存器，而不是稳定的 C 变量名。 检测到 ABI/脚手架标签：prologue, stack_alignment，应更偏向解释为结构性对象，而非优先可变异语义对象。
- Candidate program elements: `['pf']`
- direct_use_pcs: `[]`
- direct_def_pcs: `['0xa70', '0xa79', '0xb7e', '0xb93', '0xba4', '0xbad', '0xbc5', '0xbf9', '0xc11', '0xc14', '0xc16', '0xc19', '0xc3f', '0xc48', '0xc5d', '0xc60', '0xc64', '0xc66', '0xc68', '0xc6a', '0xc7f', '0xc83', '0xc8b', '0xc8f', '0xc93', '0xca7', '0xcab', '0xd3f', '0xd5b', '0xd7f', '0xd83', '0xdd3', '0x1515', '0x157e', '0x1588', '0x1695', '0x1736']`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `[]`
- structural_role_pcs: `['0xa70', '0xa79', '0xb7e', '0xb93', '0xba4', '0xbad', '0xbc5', '0xbf9', '0xc11', '0xc14', '0xc16', '0xc19', '0xc3f', '0xc48', '0xc5d', '0xc60', '0xc64', '0xc66', '0xc68', '0xc6a', '0xc7f', '0xc83', '0xc8b', '0xc8f', '0xc93', '0xca7', '0xcab', '0xd3f', '0xd5b', '0xd7f', '0xd83', '0xdd3', '0x1515', '0x157e', '0x1588', '0x1695', '0x1736']`
- anchor_pcs: `['0xa70', '0xa79', '0xb7e', '0xb93', '0xba4', '0xbad', '0xbc5', '0xbf9', '0xc11', '0xc14', '0xc16', '0xc19', '0xc3f', '0xc48', '0xc5d', '0xc60', '0xc64', '0xc66', '0xc68', '0xc6a', '0xc7f', '0xc83', '0xc8b', '0xc8f', '0xc93', '0xca7', '0xcab', '0xd3f', '0xd5b', '0xd7f', '0xd83', '0xdd3', '0x1515', '0x157e', '0x1588', '0x1695', '0x1736']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xa72', '0xa75', '0xa76', '0xa7d', '0xa7e', '0xb7a', '0xb7b', '0xb82', '0xb8b', '0xb91', '0xb97', '0xb99', '0xba0', '0xba7', '0xbaa', '0xbb0', '0xbb3', '0xbba', '0xbbe', '0xbc7', '0xbf5', '0xbf6', '0xbfd', '0xc0d', '0xc10', '0xc1b', '0xc1d', '0xc3a', '0xc3c', '0xc42', '0xc45', '0xc4d', '0xc59', '0xc5b', '0xc62', '0xc6c', '0xc6e', '0xc7b', '0xc87', '0xc97', '0xca2', '0xcaf', '0xd3b', '0xd3c', '0xd43', '0xd46', '0xd51', '0xd54', '0xd5e', '0xd61', '0xd7b', '0xd8a', '0xdcc', '0xdd0', '0xdd6', '0x150c', '0x150f', '0x1517', '0x1519', '0x157a', '0x157b', '0x1582', '0x158a', '0x1590', '0x1691', '0x1692', '0x1699', '0x16a0', '0x172c', '0x1730', '0x1739', '0x173f']`
- all_mapped_pcs: `['0xa70', '0xa72', '0xa75', '0xa76', '0xa79', '0xa7d', '0xa7e', '0xb7a', '0xb7b', '0xb7e', '0xb82', '0xb8b', '0xb91', '0xb93', '0xb97', '0xb99', '0xba0', '0xba4', '0xba7', '0xbaa', '0xbad', '0xbb0', '0xbb3', '0xbba', '0xbbe', '0xbc5', '0xbc7', '0xbf5', '0xbf6', '0xbf9', '0xbfd', '0xc0d', '0xc10', '0xc11', '0xc14', '0xc16', '0xc19', '0xc1b', '0xc1d', '0xc3a', '0xc3c', '0xc3f', '0xc42', '0xc45', '0xc48', '0xc4d', '0xc59', '0xc5b', '0xc5d', '0xc60', '0xc62', '0xc64', '0xc66', '0xc68', '0xc6a', '0xc6c', '0xc6e', '0xc7b', '0xc7f', '0xc83', '0xc87', '0xc8b', '0xc8f', '0xc93', '0xc97', '0xca2', '0xca7', '0xcab', '0xcaf', '0xd3b', '0xd3c', '0xd3f', '0xd43', '0xd46', '0xd51', '0xd54', '0xd5b', '0xd5e', '0xd61', '0xd7b', '0xd7f', '0xd83', '0xd8a', '0xdcc', '0xdd0', '0xdd3', '0xdd6', '0x150c', '0x150f', '0x1515', '0x1517', '0x1519', '0x157a', '0x157b', '0x157e', '0x1582', '0x1588', '0x158a', '0x1590', '0x1691', '0x1692', '0x1695', '0x1699', '0x16a0', '0x172c', '0x1730', '0x1736', '0x1739', '0x173f']`
- direct_parents: `['reg:cf', 'reg:of', 'reg:rax', 'reg:rbp', 'reg:rcx', 'reg:rdx', 'reg:rsp', 'reg:sf', 'reg:zf', 'stack:[rbp-0x10]', 'stack:[rbp-0x18]', 'stack:[rbp-0x1c]', 'stack:[rbp-0x4]', 'stack:[rbp-0x8]', 'stack:[rbp-0xc]']`
- direct_children: `[]`

#### PC Relation Entries

- `0xa70` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xa72` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xa75` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xa76` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xa79` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xa7d` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xa7e` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb7a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb7b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb7e` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xb82` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb8b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb91` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb93` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xb97` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xb99` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xba0` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xba4` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xba7` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbaa` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbad` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xbb0` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbb3` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbba` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbbe` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbc5` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xbc7` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbf5` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbf6` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xbf9` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xbfd` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc0d` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc10` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc11` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xc14` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xc16` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xc19` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xc1b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc1d` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc3a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc3c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc3f` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xc42` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc45` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc48` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xc4d` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc59` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc5b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc5d` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xc60` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xc62` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc64` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xc66` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xc68` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xc6a` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xc6c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc6e` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc7b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc7f` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xc83` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xc87` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xc8b` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xc8f` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xc93` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xc97` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xca2` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xca7` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xcab` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xcaf` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd3b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd3c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd3f` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xd43` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd46` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd51` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd54` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd5b` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xd5e` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd61` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd7b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd7f` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xd83` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xd8a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xdcc` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xdd0` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xdd3` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xdd6` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x150c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x150f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1515` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0x1517` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1519` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x157a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x157b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x157e` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0x1582` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1588` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0x158a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1590` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1691` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1692` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1695` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0x1699` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x16a0` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x172c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1730` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x1736` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0x1739` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0x173f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xa70`: `xor ebp, ebp` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `??:None` function=`_start`
  - use_objects: `['reg:rbp']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rbp', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0xa79`: `and rsp, 0xfffffffffffffff0` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `??:None` function=`_start`
  - instruction_semantic_tags: `['stack_alignment']`
  - use_objects: `['imm_occurrence:0xa79:operand_imm:1:0xfffffffffffffff0:i64', 'reg:rsp']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xa79:operand_imm:1:0xfffffffffffffff0:i64']`
- PC `0xb7e`: `sub rsp, 0x10` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:58` function=`spectre_function`
  - instruction_semantic_tags: `['prologue']`
  - use_objects: `['imm_occurrence:0xb7e:operand_imm:1:0x10:i64', 'reg:rsp']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xb7e:operand_imm:1:0x10:i64']`
- PC `0xb93`: `cmp qword ptr [rbp - 8], rax` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x8]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xb93:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xb93:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xb93:mem_disp:0:0xfffffffffffffff8:i64', 'imm_occurrence:0xb93:mem_scale:0:0x1:i64']`
- PC `0xba4`: `add rax, rdx` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rdx']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0xbad`: `shl eax, 9` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['imm_occurrence:0xbad:operand_imm:1:0x9:i8', 'reg:rax']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xbad:operand_imm:1:0x9:i8']`
- PC `0xbc5`: `and eax, edx` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function`
  - use_objects: `['reg:rax', 'reg:rdx']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0xbf9`: `sub rsp, 0x30` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:88` function=`stage1_mistrain_trigger`
  - instruction_semantic_tags: `['prologue']`
  - use_objects: `['imm_occurrence:0xbf9:operand_imm:1:0x30:i64', 'reg:rsp']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xbf9:operand_imm:1:0x30:i64']`
- PC `0xc11`: `shr edx, 0x1c` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc11:operand_imm:1:0x1c:i8', 'reg:rdx']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rdx', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xc11:operand_imm:1:0x1c:i8']`
- PC `0xc14`: `add eax, edx` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rdx']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0xc16`: `and eax, 0xf` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc16:operand_imm:1:0xf:i32', 'reg:rax']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xc16:operand_imm:1:0xf:i32']`
- PC `0xc19`: `sub eax, edx` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rdx']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0xc3f`: `add eax, 1` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc3f:operand_imm:1:0x1:i32', 'reg:rax']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xc3f:operand_imm:1:0x1:i32']`
- PC `0xc48`: `cmp eax, 0xc7` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc48:operand_imm:1:0xc7:i32', 'reg:rax']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xc48:operand_imm:1:0xc7:i32']`
- PC `0xc5d`: `None` groups=`['structural_role']` kinds=`['store_target']`
- PC `0xc60`: `None` groups=`['structural_role']` kinds=`['store_target']`
- PC `0xc64`: `None` groups=`['structural_role']` kinds=`['store_target']`
- PC `0xc66`: `None` groups=`['structural_role']` kinds=`['store_target']`
- PC `0xc68`: `None` groups=`['structural_role']` kinds=`['store_target']`
- PC `0xc6a`: `None` groups=`['structural_role']` kinds=`['store_target']`
- PC `0xc7f`: `shr rax, 0x10` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xc7f:operand_imm:1:0x10:i8', 'reg:rax']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xc7f:operand_imm:1:0x10:i8']`
- PC `0xc83`: `or qword ptr [rbp - 0x10], rax` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf', 'stack:[rbp-0x10]']`
  - addr_objects: `['imm_occurrence:0xc83:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc83:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc83:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xc83:mem_scale:0:0x1:i64']`
- PC `0xc8b`: `xor rax, qword ptr [rbp - 0x18]` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x18]']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xc8b:mem_disp:1:0xffffffffffffffe8:i64', 'imm_occurrence:0xc8b:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc8b:mem_disp:1:0xffffffffffffffe8:i64', 'imm_occurrence:0xc8b:mem_scale:1:0x1:i64']`
- PC `0xc8f`: `and rax, qword ptr [rbp - 0x10]` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xc8f:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc8f:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc8f:mem_disp:1:0xfffffffffffffff0:i64', 'imm_occurrence:0xc8f:mem_scale:1:0x1:i64']`
- PC `0xc93`: `xor rax, qword ptr [rbp - 0x18]` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['reg:rax', 'reg:rbp', 'stack:[rbp-0x18]']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rax', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xc93:mem_disp:1:0xffffffffffffffe8:i64', 'imm_occurrence:0xc93:mem_scale:1:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xc93:mem_disp:1:0xffffffffffffffe8:i64', 'imm_occurrence:0xc93:mem_scale:1:0x1:i64']`
- PC `0xca7`: `sub dword ptr [rbp - 0x1c], 1` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xca7:operand_imm:1:0x1:i32', 'reg:rbp', 'stack:[rbp-0x1c]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf', 'stack:[rbp-0x1c]']`
  - addr_objects: `['imm_occurrence:0xca7:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xca7:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xca7:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xca7:mem_scale:0:0x1:i64', 'imm_occurrence:0xca7:operand_imm:1:0x1:i32']`
- PC `0xcab`: `cmp dword ptr [rbp - 0x1c], 0` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`stage1_mistrain_trigger`
  - use_objects: `['imm_occurrence:0xcab:operand_imm:1:0x0:i32', 'reg:rbp', 'stack:[rbp-0x1c]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xcab:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xcab:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xcab:mem_disp:0:0xffffffffffffffe4:i64', 'imm_occurrence:0xcab:mem_scale:0:0x1:i64', 'imm_occurrence:0xcab:operand_imm:1:0x0:i32']`
- PC `0xd3f`: `sub rsp, 0x20` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:124` function=`main`
  - instruction_semantic_tags: `['prologue']`
  - use_objects: `['imm_occurrence:0xd3f:operand_imm:1:0x20:i64', 'reg:rsp']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0xd3f:operand_imm:1:0x20:i64']`
- PC `0xd5b`: `sub rdx, rax` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:125` function=`main`
  - use_objects: `['reg:rax', 'reg:rdx']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rdx', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0xd7f`: `add dword ptr [rbp - 0x10], 1` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`main`
  - use_objects: `['imm_occurrence:0xd7f:operand_imm:1:0x1:i32', 'reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf', 'stack:[rbp-0x10]']`
  - addr_objects: `['imm_occurrence:0xd7f:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd7f:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd7f:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd7f:mem_scale:0:0x1:i64', 'imm_occurrence:0xd7f:operand_imm:1:0x1:i32']`
- PC `0xd83`: `cmp dword ptr [rbp - 0x10], 0x1ffff` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:None` function=`main`
  - use_objects: `['imm_occurrence:0xd83:operand_imm:1:0x1ffff:i32', 'reg:rbp', 'stack:[rbp-0x10]']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
  - addr_objects: `['imm_occurrence:0xd83:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd83:mem_scale:0:0x1:i64', 'reg:rbp', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xd83:mem_disp:0:0xfffffffffffffff0:i64', 'imm_occurrence:0xd83:mem_scale:0:0x1:i64', 'imm_occurrence:0xd83:operand_imm:1:0x1ffff:i32']`
- PC `0xdd3`: `None` groups=`['structural_role']` kinds=`['store_target']`
- PC `0x1515`: `test eax, eax` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `??:None` function=`pmu_uops_snap_before`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0x157e`: `sub rsp, 0x20` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - instruction_semantic_tags: `['prologue']`
  - use_objects: `['imm_occurrence:0x157e:operand_imm:1:0x20:i64', 'reg:rsp']`
  - def_objects: `['reg:af', 'reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:rsp', 'reg:sf', 'reg:zf']`
  - immediates: `['imm_occurrence:0x157e:operand_imm:1:0x20:i64']`
- PC `0x1588`: `test eax, eax` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `??:None` function=`pmu_uops_snap_after`
  - use_objects: `['reg:rax']`
  - def_objects: `['reg:cf', 'reg:of', 'reg:pf', 'reg:rip', 'reg:sf', 'reg:zf']`
- PC `0x1695`: `None` groups=`['structural_role']` kinds=`['store_target']`
- PC `0x1736`: `None` groups=`['structural_role']` kinds=`['store_target']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xa72`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xa75`: `pop rsi` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xa76`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xa7d`: `push rax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xa7e`: `push rsp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xb7a`: `push rbp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xb7b`: `mov rbp, rsp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xb82`: `mov qword ptr [rbp - 8], rdi` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xb8b`: `mov eax, dword ptr [rip + 0x20248f]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xb91`: `mov eax, eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xb97`: `jae 0xbcd` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xb99`: `lea rdx, [rip + 0x2024a0]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xba0`: `mov rax, qword ptr [rbp - 8]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xba7`: `movzx eax, byte ptr [rax]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbaa`: `movzx eax, al` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbb0`: `movsxd rdx, eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbb3`: `lea rax, [rip + 0x210706]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbba`: `movzx edx, byte ptr [rdx + rax]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbbe`: `movzx eax, byte ptr [rip + 0x202544]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbc7`: `mov byte ptr [rip + 0x20253c], al` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbf5`: `push rbp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbf6`: `mov rbp, rsp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xbfd`: `mov qword ptr [rbp - 0x28], rdi` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc0d`: `mov eax, dword ptr [rbp - 0x1c]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc10`: `cdq` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc1b`: `cdqe` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc1d`: `mov qword ptr [rbp - 0x18], rax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc3a`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc3c`: `mov eax, dword ptr [rbp - 0x20]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc42`: `mov dword ptr [rbp - 0x20], eax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc45`: `mov eax, dword ptr [rbp - 0x20]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc4d`: `jle 0xc3c` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc59`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc5b`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc62`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc6c`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc6e`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc7b`: `mov rax, qword ptr [rbp - 0x10]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc87`: `mov rax, qword ptr [rbp - 0x28]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xc97`: `mov qword ptr [rbp - 0x10], rax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xca2`: `call 0xb7a` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xcaf`: `jns 0xc0d` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd3b`: `push rbp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd3c`: `mov rbp, rsp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd43`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd46`: `mov qword ptr [rbp - 0x20], rsi` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd51`: `mov rdx, rax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd54`: `lea rax, [rip + 0x2022e5]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd5e`: `mov rax, rdx` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd61`: `mov qword ptr [rbp - 8], rax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd7b`: `mov byte ptr [rdx + rax], 1` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd8a`: `jle 0xd6e` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xdcc`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xdd0`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xdd6`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x150c`: `mov rbp, rsp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x150f`: `mov eax, dword ptr [rip + 0x20fc6f]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1517`: `je 0x1577` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1519`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x157a`: `push rbp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x157b`: `mov rbp, rsp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1582`: `mov eax, dword ptr [rip + 0x20fbfc]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x158a`: `je 0x168e` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1590`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1691`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1692`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1699`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x16a0`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x172c`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1730`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x1739`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0x173f`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xa70`      a70:	31 ed                	xor    %ebp,%ebp groups=`['structural_role']` kinds=`['store_target']`
- `0xa72`      a72:	49 89 d1             	mov    %rdx,%r9 groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xa75`      a75:	5e                   	pop    %rsi groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xa76`      a76:	48 89 e2             	mov    %rsp,%rdx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xa79`      a79:	48 83 e4 f0          	and    $0xfffffffffffffff0,%rsp groups=`['structural_role']` kinds=`['store_target']`
- `0xa7d`      a7d:	50                   	push   %rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xa7e`      a7e:	54                   	push   %rsp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb7a`      b7a:	55                   	push   %rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb7b`      b7b:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb7e`      b7e:	48 83 ec 10          	sub    $0x10,%rsp groups=`['structural_role']` kinds=`['store_target']`
- `0xb82`      b82:	48 89 7d f8          	mov    %rdi,-0x8(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb8b`      b8b:	8b 05 8f 24 20 00    	mov    0x20248f(%rip),%eax        # 203020 <array1_size> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb91`      b91:	89 c0                	mov    %eax,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb93`      b93:	48 39 45 f8          	cmp    %rax,-0x8(%rbp) groups=`['structural_role']` kinds=`['store_target']`
- `0xb97`      b97:	73 34                	jae    bcd <STAGE1_END> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xb99`      b99:	48 8d 15 a0 24 20 00 	lea    0x2024a0(%rip),%rdx        # 203040 <array1> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xba0`      ba0:	48 8b 45 f8          	mov    -0x8(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xba4`      ba4:	48 01 d0             	add    %rdx,%rax groups=`['structural_role']` kinds=`['store_target']`
- `0xba7`      ba7:	0f b6 00             	movzbl (%rax),%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbaa`      baa:	0f b6 c0             	movzbl %al,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbad`      bad:	c1 e0 09             	shl    $0x9,%eax groups=`['structural_role']` kinds=`['store_target']`
- `0xbb0`      bb0:	48 63 d0             	movslq %eax,%rdx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbb3`      bb3:	48 8d 05 06 07 21 00 	lea    0x210706(%rip),%rax        # 2112c0 <array2> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbba`      bba:	0f b6 14 02          	movzbl (%rdx,%rax,1),%edx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbbe`      bbe:	0f b6 05 44 25 20 00 	movzbl 0x202544(%rip),%eax        # 203109 <temp> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbc5`      bc5:	21 d0                	and    %edx,%eax groups=`['structural_role']` kinds=`['store_target']`
- `0xbc7`      bc7:	88 05 3c 25 20 00    	mov    %al,0x20253c(%rip)        # 203109 <temp> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbf5`      bf5:	55                   	push   %rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbf6`      bf6:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xbf9`      bf9:	48 83 ec 30          	sub    $0x30,%rsp groups=`['structural_role']` kinds=`['store_target']`
- `0xbfd`      bfd:	48 89 7d d8          	mov    %rdi,-0x28(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc0d`      c0d:	8b 45 e4             	mov    -0x1c(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc10`      c10:	99                   	cltd    groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc11`      c11:	c1 ea 1c             	shr    $0x1c,%edx groups=`['structural_role']` kinds=`['store_target']`
- `0xc14`      c14:	01 d0                	add    %edx,%eax groups=`['structural_role']` kinds=`['store_target']`
- `0xc16`      c16:	83 e0 0f             	and    $0xf,%eax groups=`['structural_role']` kinds=`['store_target']`
- `0xc19`      c19:	29 d0                	sub    %edx,%eax groups=`['structural_role']` kinds=`['store_target']`
- `0xc1b`      c1b:	48 98                	cltq    groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc1d`      c1d:	48 89 45 e8          	mov    %rax,-0x18(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc3a`      c3a:	eb 09                	jmp    c45 <stage1_mistrain_trigger+0x50> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc3c`      c3c:	8b 45 e0             	mov    -0x20(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc3f`      c3f:	83 c0 01             	add    $0x1,%eax groups=`['structural_role']` kinds=`['store_target']`
- `0xc42`      c42:	89 45 e0             	mov    %eax,-0x20(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc45`      c45:	8b 45 e0             	mov    -0x20(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc48`      c48:	3d c7 00 00 00       	cmp    $0xc7,%eax groups=`['structural_role']` kinds=`['store_target']`
- `0xc4d`      c4d:	7e ed                	jle    c3c <stage1_mistrain_trigger+0x47> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc59`      c59:	f7 ea                	imul   %edx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc5b`      c5b:	89 c8                	mov    %ecx,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc5d`      c5d:	c1 f8 1f             	sar    $0x1f,%eax groups=`['structural_role']` kinds=`['store_target']`
- `0xc60`      c60:	29 c2                	sub    %eax,%edx groups=`['structural_role']` kinds=`['store_target']`
- `0xc62`      c62:	89 d0                	mov    %edx,%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc64`      c64:	01 c0                	add    %eax,%eax groups=`['structural_role']` kinds=`['store_target']`
- `0xc66`      c66:	01 d0                	add    %edx,%eax groups=`['structural_role']` kinds=`['store_target']`
- `0xc68`      c68:	01 c0                	add    %eax,%eax groups=`['structural_role']` kinds=`['store_target']`
- `0xc6a`      c6a:	29 c1                	sub    %eax,%ecx groups=`['structural_role']` kinds=`['store_target']`
- `0xc6c`      c6c:	89 ca                	mov    %ecx,%edx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc6e`      c6e:	8d 42 ff             	lea    -0x1(%rdx),%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc7b`      c7b:	48 8b 45 f0          	mov    -0x10(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc7f`      c7f:	48 c1 e8 10          	shr    $0x10,%rax groups=`['structural_role']` kinds=`['store_target']`
- `0xc83`      c83:	48 09 45 f0          	or     %rax,-0x10(%rbp) groups=`['structural_role']` kinds=`['store_target']`
- `0xc87`      c87:	48 8b 45 d8          	mov    -0x28(%rbp),%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xc8b`      c8b:	48 33 45 e8          	xor    -0x18(%rbp),%rax groups=`['structural_role']` kinds=`['store_target']`
- `0xc8f`      c8f:	48 23 45 f0          	and    -0x10(%rbp),%rax groups=`['structural_role']` kinds=`['store_target']`
- `0xc93`      c93:	48 33 45 e8          	xor    -0x18(%rbp),%rax groups=`['structural_role']` kinds=`['store_target']`
- `0xc97`      c97:	48 89 45 f0          	mov    %rax,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xca2`      ca2:	e8 d3 fe ff ff       	callq  b7a <spectre_function> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xca7`      ca7:	83 6d e4 01          	subl   $0x1,-0x1c(%rbp) groups=`['structural_role']` kinds=`['store_target']`
- `0xcab`      cab:	83 7d e4 00          	cmpl   $0x0,-0x1c(%rbp) groups=`['structural_role']` kinds=`['store_target']`
- `0xcaf`      caf:	0f 89 58 ff ff ff    	jns    c0d <stage1_mistrain_trigger+0x18> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd3b`      d3b:	55                   	push   %rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd3c`      d3c:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd3f`      d3f:	48 83 ec 20          	sub    $0x20,%rsp groups=`['structural_role']` kinds=`['store_target']`
- `0xd43`      d43:	89 7d ec             	mov    %edi,-0x14(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd46`      d46:	48 89 75 e0          	mov    %rsi,-0x20(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd51`      d51:	48 89 c2             	mov    %rax,%rdx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd54`      d54:	48 8d 05 e5 22 20 00 	lea    0x2022e5(%rip),%rax        # 203040 <array1> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd5b`      d5b:	48 29 c2             	sub    %rax,%rdx groups=`['structural_role']` kinds=`['store_target']`
- `0xd5e`      d5e:	48 89 d0             	mov    %rdx,%rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd61`      d61:	48 89 45 f8          	mov    %rax,-0x8(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd7b`      d7b:	c6 04 02 01          	movb   $0x1,(%rdx,%rax,1) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd7f`      d7f:	83 45 f0 01          	addl   $0x1,-0x10(%rbp) groups=`['structural_role']` kinds=`['store_target']`
- `0xd83`      d83:	81 7d f0 ff ff 01 00 	cmpl   $0x1ffff,-0x10(%rbp) groups=`['structural_role']` kinds=`['store_target']`
- `0xd8a`      d8a:	7e e2                	jle    d6e <main+0x33> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xdcc`      dcc:	83 45 f0 01          	addl   $0x1,-0x10(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xdd0`      dd0:	8b 45 f0             	mov    -0x10(%rbp),%eax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xdd3`      dd3:	3b 45 f4             	cmp    -0xc(%rbp),%eax groups=`['structural_role']` kinds=`['store_target']`
- `0xdd6`      dd6:	7c d1                	jl     da9 <main+0x6e> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x150c`     150c:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x150f`     150f:	8b 05 6f fc 20 00    	mov    0x20fc6f(%rip),%eax        # 211184 <uops_available> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1515`     1515:	85 c0                	test   %eax,%eax groups=`['structural_role']` kinds=`['store_target']`
- `0x1517`     1517:	74 5e                	je     1577 <pmu_uops_snap_before+0x6c> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1519`     1519:	8b 05 41 3c 20 00    	mov    0x203c41(%rip),%eax        # 205160 <use_rdpmc> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x157a`     157a:	55                   	push   %rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x157b`     157b:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x157e`     157e:	48 83 ec 20          	sub    $0x20,%rsp groups=`['structural_role']` kinds=`['store_target']`
- `0x1582`     1582:	8b 05 fc fb 20 00    	mov    0x20fbfc(%rip),%eax        # 211184 <uops_available> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1588`     1588:	85 c0                	test   %eax,%eax groups=`['structural_role']` kinds=`['store_target']`
- `0x158a`     158a:	0f 84 fe 00 00 00    	je     168e <pmu_uops_snap_after+0x114> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1590`     1590:	8b 05 ca 3b 20 00    	mov    0x203bca(%rip),%eax        # 205160 <use_rdpmc> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1691`     1691:	55                   	push   %rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1692`     1692:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1695`     1695:	48 83 ec 10          	sub    $0x10,%rsp groups=`['structural_role']` kinds=`['store_target']`
- `0x1699`     1699:	c7 45 fc 00 00 00 00 	movl   $0x0,-0x4(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x16a0`     16a0:	e9 8b 00 00 00       	jmpq   1730 <pmu_uops_print_results+0x9f> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x172c`     172c:	83 45 fc 01          	addl   $0x1,-0x4(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1730`     1730:	8b 05 4a fa 20 00    	mov    0x20fa4a(%rip),%eax        # 211180 <uops_cnt> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x1736`     1736:	39 45 fc             	cmp    %eax,-0x4(%rbp) groups=`['structural_role']` kinds=`['store_target']`
- `0x1739`     1739:	0f 8c 66 ff ff ff    	jl     16a5 <pmu_uops_print_results+0x14> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0x173f`     173f:	90                   	nop groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:58` function=`spectre_function` pcs=`['0xb7a', '0xb7b', '0xb7e', '0xb82']` groups=`['evidence_only', 'structural_role']` kinds=`['evidence_only', 'store_target']`

```c
   56: ********************************************************************/
   57: __attribute__((noinline))
   58: void spectre_function(size_t x) {
   59: 
   60:   pmu_uops_snap_before();
```

- `/root/src/spectre_stage1_2_auto.c:63` function=`spectre_function` pcs=`['0xb8b', '0xb91', '0xb93', '0xb97']` groups=`['evidence_only', 'structural_role']` kinds=`['evidence_only', 'store_target']`

```c
   61: 
   62:   asm volatile(".globl STAGE1_BEGIN\nSTAGE1_BEGIN:");
   63:   if (x < array1_size) {
   64:     NOP_REGION_BEGIN
   65:     temp &= array2[array1[x] * 512];
```

- `/root/src/spectre_stage1_2_auto.c:65` function=`spectre_function` pcs=`['0xb99', '0xba0', '0xba4', '0xba7', '0xbaa', '0xbad', '0xbb0', '0xbb3', '0xbba', '0xbbe', '0xbc5', '0xbc7']` groups=`['evidence_only', 'structural_role']` kinds=`['evidence_only', 'store_target']`

```c
   63:   if (x < array1_size) {
   64:     NOP_REGION_BEGIN
   65:     temp &= array2[array1[x] * 512];
   66:     NOP_REGION_END
   67:   }
```

- `/root/src/spectre_stage1_2_auto.c:88` function=`stage1_mistrain_trigger` pcs=`['0xbf5', '0xbf6', '0xbf9', '0xbfd']` groups=`['evidence_only', 'structural_role']` kinds=`['evidence_only', 'store_target']`

```c
   86: ********************************************************************/
   87: __attribute__((noinline))
   88: void stage1_mistrain_trigger(size_t malicious_x) {
   89:     int j;
   90:     size_t training_x, x;
```

- `/root/src/spectre_stage1_2_auto.c:93` function=`stage1_mistrain_trigger` pcs=`['0xc0d', '0xc10', '0xc11', '0xc14', '0xc16', '0xc19', '0xc1b', '0xc1d']` groups=`['evidence_only', 'structural_role']` kinds=`['evidence_only', 'store_target']`

```c
   91: 
   92:     for (j = 29; j >= 0; j--) {
   93:         training_x = (size_t)(j % 16);
   94:         _mm_clflush(&array1_size);
   95:         for (volatile int z = 0; z < 200; z++) {}
```

- `/root/src/spectre_stage1_2_auto.c:124` function=`main` pcs=`['0xd3b', '0xd3c', '0xd3f', '0xd46']` groups=`['evidence_only', 'structural_role']` kinds=`['evidence_only', 'store_target']`

```c
  122: ********************************************************************/
  123: #ifndef STAGE2_TEST_MAIN
  124: int main(int argc, const char **argv) {
  125:     size_t malicious_x = (size_t)(secret - (char *)array1);
  126:     int i;
```

- `/root/src/spectre_stage1_2_auto.c:125` function=`main` pcs=`['0xd51', '0xd54', '0xd5b', '0xd5e', '0xd61']` groups=`['evidence_only', 'structural_role']` kinds=`['evidence_only', 'store_target']`

```c
  123: #ifndef STAGE2_TEST_MAIN
  124: int main(int argc, const char **argv) {
  125:     size_t malicious_x = (size_t)(secret - (char *)array1);
  126:     int i;
  127: 
```

### 3. `reg:r8`

- Role: `forward_sink`
- Type: `reg`
- Label: `r8`
- Mapping kind: `execution_register_carrier`
- Confidence: `structural`
- Object semantic tags: `[]`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Reason: 对象类型为 reg，表示执行时承载值的寄存器，而不是稳定的 C 变量名。
- Candidate program elements: `['r8']`
- direct_use_pcs: `[]`
- direct_def_pcs: `['0xa7f']`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `[]`
- structural_role_pcs: `['0xa7f']`
- anchor_pcs: `['0xa7f']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xa7d', '0xa7e', '0xa86', '0xa8d']`
- all_mapped_pcs: `['0xa7d', '0xa7e', '0xa7f', '0xa86', '0xa8d']`
- direct_parents: `['reg:rip']`
- direct_children: `[]`

#### PC Relation Entries

- `0xa7d` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xa7e` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xa7f` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xa86` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xa8d` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xa7f`: `lea r8, [rip + 0xfaa]` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `??:None` function=`_start`
  - use_objects: `['reg:rip']`
  - def_objects: `['reg:r8', 'reg:rip']`
  - addr_objects: `['imm_occurrence:0xa7f:mem_disp:1:0xfaa:i64', 'imm_occurrence:0xa7f:mem_scale:1:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xa7f:mem_disp:1:0xfaa:i64', 'imm_occurrence:0xa7f:mem_scale:1:0x1:i64']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xa7d`: `push rax` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xa7e`: `push rsp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xa86`: `lea rcx, [rip + 0xf33]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xa8d`: `lea rdi, [rip + 0x2a7]` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xa7d`      a7d:	50                   	push   %rax groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xa7e`      a7e:	54                   	push   %rsp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xa7f`      a7f:	4c 8d 05 aa 0f 00 00 	lea    0xfaa(%rip),%r8        # 1a30 <__libc_csu_fini> groups=`['structural_role']` kinds=`['store_target']`
- `0xa86`      a86:	48 8d 0d 33 0f 00 00 	lea    0xf33(%rip),%rcx        # 19c0 <__libc_csu_init> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xa8d`      a8d:	48 8d 3d a7 02 00 00 	lea    0x2a7(%rip),%rdi        # d3b <main> groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 4. `reg:r9`

- Role: `forward_sink`
- Type: `reg`
- Label: `r9`
- Mapping kind: `execution_register_carrier`
- Confidence: `structural`
- Object semantic tags: `[]`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Reason: 对象类型为 reg，表示执行时承载值的寄存器，而不是稳定的 C 变量名。
- Candidate program elements: `['r9']`
- direct_use_pcs: `[]`
- direct_def_pcs: `['0xa72']`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `[]`
- structural_role_pcs: `['0xa72']`
- anchor_pcs: `['0xa72']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xa70', '0xa75', '0xa76']`
- all_mapped_pcs: `['0xa70', '0xa72', '0xa75', '0xa76']`
- direct_parents: `['reg:rdx']`
- direct_children: `[]`

#### PC Relation Entries

- `0xa70` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xa72` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xa75` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xa76` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xa72`: `None` groups=`['structural_role']` kinds=`['store_target']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xa70`: `xor ebp, ebp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xa75`: `pop rsi` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xa76`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xa70`      a70:	31 ed                	xor    %ebp,%ebp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xa72`      a72:	49 89 d1             	mov    %rdx,%r9 groups=`['structural_role']` kinds=`['store_target']`
- `0xa75`      a75:	5e                   	pop    %rsi groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xa76`      a76:	48 89 e2             	mov    %rsp,%rdx groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

_No source evidence found._

### 5. `stack:[rbp-0x14]`

- Role: `forward_sink`
- Type: `stack`
- Label: `stack[rbp-0x14]`
- Mapping kind: `stack_slot_local_or_spill`
- Confidence: `probable`
- Object semantic tags: `[]`
- Anchor instruction tags: `[]`
- Scaffolding tags: `[]`
- Reason: 对象类型为 stack，通常对应局部变量、形参栈槽或编译器 spill 槽位。
- Candidate program elements: `['stack[rbp-0x14]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `['0xd43']`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `[]`
- structural_role_pcs: `['0xd43']`
- anchor_pcs: `['0xd43']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xd3c', '0xd3f', '0xd46']`
- all_mapped_pcs: `['0xd3c', '0xd3f', '0xd43', '0xd46']`
- direct_parents: `['reg:rbp', 'reg:rdi']`
- direct_children: `[]`

#### PC Relation Entries

- `0xd3c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd3f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd43` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xd46` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xd43`: `None` groups=`['structural_role']` kinds=`['store_target']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xd3c`: `mov rbp, rsp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd3f`: `sub rsp, 0x20` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd46`: `mov qword ptr [rbp - 0x20], rsi` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xd3c`      d3c:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd3f`      d3f:	48 83 ec 20          	sub    $0x20,%rsp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd43`      d43:	89 7d ec             	mov    %edi,-0x14(%rbp) groups=`['structural_role']` kinds=`['store_target']`
- `0xd46`      d46:	48 89 75 e0          	mov    %rsi,-0x20(%rbp) groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:124` function=`main` pcs=`['0xd3c', '0xd3f', '0xd46']` groups=`['evidence_only']` kinds=`['evidence_only']`

```c
  122: ********************************************************************/
  123: #ifndef STAGE2_TEST_MAIN
  124: int main(int argc, const char **argv) {
  125:     size_t malicious_x = (size_t)(secret - (char *)array1);
  126:     int i;
```

### 6. `stack:[rsp+0x0]`

- Role: `forward_sink`
- Type: `stack`
- Label: `stack[rsp+0x0]`
- Mapping kind: `stack_slot_scaffold_or_spill`
- Confidence: `semantic`
- Object semantic tags: `[]`
- Anchor instruction tags: `['callee_save_spill', 'prologue']`
- Scaffolding tags: `['callee_save_spill', 'prologue']`
- Reason: 对象类型为 stack，且关联到脚手架标签，通常对应形参搬运、callee-save spill/restore 或对齐槽位。 检测到 ABI/脚手架标签：callee_save_spill, prologue，应更偏向解释为结构性对象，而非优先可变异语义对象。
- Candidate program elements: `['stack[rsp+0x0]']`
- direct_use_pcs: `[]`
- direct_def_pcs: `['0xa7d', '0xa7e', '0xa94', '0xd3b']`
- direct_addr_pcs: `[]`
- direct_ctrl_pcs: `[]`
- direct_imm_pcs: `[]`
- direct_operand_pcs: `[]`
- structural_role_pcs: `['0xa7d', '0xa7e', '0xa94', '0xd3b']`
- anchor_pcs: `['0xa7d', '0xa7e', '0xa94', '0xd3b']`
- derived_or_related_pcs: `[]`
- evidence_pcs: `['0xa76', '0xa79', '0xa7f', '0xa86', '0xa8d', '0xa9a', '0xa9b', '0xd3c', '0xd3f']`
- all_mapped_pcs: `['0xa76', '0xa79', '0xa7d', '0xa7e', '0xa7f', '0xa86', '0xa8d', '0xa94', '0xa9a', '0xa9b', '0xd3b', '0xd3c', '0xd3f']`
- direct_parents: `['mem:0x202fe0', 'reg:rax', 'reg:rbp', 'reg:rip', 'reg:rsp']`
- direct_children: `[]`

#### PC Relation Entries

- `0xa76` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xa79` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xa7d` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xa7e` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xa7f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xa86` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xa8d` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xa94` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xa9a` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xa9b` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd3b` kinds=`['store_target']` groups=`['structural_role']` primary_group=`structural_role` sources=`['object_detail.defined_by/instruction_details.def_objects']`
- `0xd3c` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`
- `0xd3f` kinds=`['evidence_only']` groups=`['evidence_only']` primary_group=`evidence_only` sources=`['asm_context']`

#### Direct Anchor Instruction Evidence

- PC `0xa7d`: `push rax` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `??:None` function=`_start`
  - use_objects: `['reg:rax', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rsp+0x0]']`
- PC `0xa7e`: `push rsp` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `??:None` function=`_start`
  - use_objects: `['reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rsp+0x0]']`
- PC `0xa94`: `call qword ptr [rip + 0x202546]` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `??:None` function=`_start`
  - call_target: `{'operand': 'qword ptr [rip + 0x202546]', 'resolved_symbol': '__libc_start_main@GLIBC_2.2.5', 'call_kind': 'indirect_call_through_memory', 'display_target': '__libc_start_main@GLIBC_2.2.5'}`
  - use_objects: `['mem:0x202fe0', 'reg:rip', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rsp+0x0]']`
  - addr_objects: `['imm_occurrence:0xa94:mem_disp:0:0x202546:i64', 'imm_occurrence:0xa94:mem_scale:0:0x1:i64', 'reg:rip', 'reg:unknown']`
  - immediates: `['imm_occurrence:0xa94:mem_disp:0:0x202546:i64', 'imm_occurrence:0xa94:mem_scale:0:0x1:i64']`
- PC `0xd3b`: `push rbp` groups=`['structural_role']` kinds=`['store_target']`
  - Source: `/root/src/spectre_stage1_2_auto.c:124` function=`main`
  - instruction_semantic_tags: `['callee_save_spill', 'prologue']`
  - use_objects: `['reg:rbp', 'reg:rsp']`
  - def_objects: `['reg:rip', 'reg:rsp', 'stack:[rsp+0x0]']`

#### Related Instruction Evidence

_No related instruction evidence._

#### Evidence-only Instruction Evidence

- PC `0xa76`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xa79`: `and rsp, 0xfffffffffffffff0` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xa7f`: `lea r8, [rip + 0xfaa]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xa86`: `lea rcx, [rip + 0xf33]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xa8d`: `lea rdi, [rip + 0x2a7]` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xa9a`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xa9b`: `None` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd3c`: `mov rbp, rsp` groups=`['evidence_only']` kinds=`['evidence_only']`
- PC `0xd3f`: `sub rsp, 0x20` groups=`['evidence_only']` kinds=`['evidence_only']`

#### Assembly References

- `0xa76`      a76:	48 89 e2             	mov    %rsp,%rdx groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xa79`      a79:	48 83 e4 f0          	and    $0xfffffffffffffff0,%rsp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xa7d`      a7d:	50                   	push   %rax groups=`['structural_role']` kinds=`['store_target']`
- `0xa7e`      a7e:	54                   	push   %rsp groups=`['structural_role']` kinds=`['store_target']`
- `0xa7f`      a7f:	4c 8d 05 aa 0f 00 00 	lea    0xfaa(%rip),%r8        # 1a30 <__libc_csu_fini> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xa86`      a86:	48 8d 0d 33 0f 00 00 	lea    0xf33(%rip),%rcx        # 19c0 <__libc_csu_init> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xa8d`      a8d:	48 8d 3d a7 02 00 00 	lea    0x2a7(%rip),%rdi        # d3b <main> groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xa94`      a94:	ff 15 46 25 20 00    	callq  *0x202546(%rip)        # 202fe0 <__libc_start_main@GLIBC_2.2.5> groups=`['structural_role']` kinds=`['store_target']`
- `0xa9a`      a9a:	f4                   	hlt     groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xa9b`      a9b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1) groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd3b`      d3b:	55                   	push   %rbp groups=`['structural_role']` kinds=`['store_target']`
- `0xd3c`      d3c:	48 89 e5             	mov    %rsp,%rbp groups=`['evidence_only']` kinds=`['evidence_only']`
- `0xd3f`      d3f:	48 83 ec 20          	sub    $0x20,%rsp groups=`['evidence_only']` kinds=`['evidence_only']`

#### Source Evidence

- `/root/src/spectre_stage1_2_auto.c:124` function=`main` pcs=`['0xd3b', '0xd3c', '0xd3f']` groups=`['evidence_only', 'structural_role']` kinds=`['evidence_only', 'store_target']`

```c
  122: ********************************************************************/
  123: #ifndef STAGE2_TEST_MAIN
  124: int main(int argc, const char **argv) {
  125:     size_t malicious_x = (size_t)(secret - (char *)array1);
  126:     int i;
```

