---
title: 汇编new
date: 2021-07-11 08:40:43
typora-root-url: 汇编new
---
# 汇编new

关于输入字符串到buf：

[https://stackoverflow.com/questions/47379024/how-buffered-input-works/47379025#47379025?newreg=cee901d6491242d79e03a10a192d3684](https://stackoverflow.com/questions/47379024/how-buffered-input-works/47379025#47379025?newreg=cee901d6491242d79e03a10a192d3684)

- Buffered STDIN input.

    ```wasm
    ; -------------------
            ORG     256                     ;Create .COM program
            cld
            mov     si, msg1
            call    WriteStringDOS
            mov     dx, buf
            mov     ah, 0Ah                 ;DOS.BufferedInput
            int     21h
            mov     si, msg2
            call    WriteStringDOS
            mov     si, buf+2
            movzx   bx, [si-1]              ;Get character count
            mov     word [si+bx+1], 10      ;Keep CR, append LF and 0
            call    WriteStringDOS
            mov     ax, 4C00h               ;DOS.TerminateWithExitcode
            int     21h
    ; --------------------------------------
    ; IN (ds:si) OUT ()
    WriteStringDOS:
            pusha
            jmps    .b
    .a:     mov     dl, al
            mov     ah, 02h                 ;DOS.DisplayCharacter
            int     21h                     ; -> AL
    .b:     lodsb
            test    al, al
            jnz     .a
            popa
            ret
    ; --------------------------------------
    buf:    db      255, 16, "I'm the template", 13, 255-16-1+2 dup (0)
    msg1:   db      'Choose color ? ', 0
    msg2:   db      10, 'You chose ', 0
    ; --------------------------------------
    ```

mul:

(16位)

AX*16位reg或内存字单元 → 高位DX 低位AX 

mov ax,a

mov bx,b

mul bx

→dx,ax=a*b

div:

和16位除法类似，如果是大数，则放在EDX:EAX中，一般除以EBX(ECX)，结果是：商放在EAX中，余数放在EDX中。

除数为16位的时候，余数在DX中

eax / reg = eax ...... edx

Question:

- [ ]  far near是啥
- [ ]  prob是啥
- [ ]  buffer为什么要加数字 in lab3

- [ ]  整理出进制转换 以及十进制输出函数 from lab3

Tricks:

```c
;拼接dx:ax为eax:
shl edx, 16
and eax, 0000FFFFh
add eax, edx
```

中断重新绑定：

![Untitled.png](Untitled.png)

前面是偏移地址 后面是段地址

小数计算：

![Untitled%201.png](Untitled%201.png)

fild ：load整数

memcpy：

![Untitled%202.png](Untitled%202.png)

左右两列对应两个方向

尽可能用movsd的方法：

![Untitled%203.png](Untitled%203.png)

防止cx=0还进入循环：

![Untitled%204.png](Untitled%204.png)

naked 防止自动的汇编代码

![Untitled%205.png](Untitled%205.png)

读硬盘的方式：

![Untitled%206.png](Untitled%206.png)

![Untitled%207.png](Untitled%207.png)

逻辑的从零开始

13/42中断

![Untitled%208.png](Untitled%208.png)

bochs相关指令

![Untitled%209.png](Untitled%209.png)

![Untitled%2010.png](Untitled%2010.png)

如何看任意教室直播：第三步 记得切换一个日期

![Untitled%2011.png](Untitled%2011.png)

6.15号的回放：

![Untitled%2012.png](Untitled%2012.png)

多位计算用：

```c
减法：
sub ax, 256
sbb dx, 0  ;(dx:ax) = filesize - 256 ;上次运算可能进位所以用sbb
```

汇编Old：

[汇编lab1](https://www.notion.so/lab1-05bca2c4f2d74b4db1152fc058c3ec12)

[]()