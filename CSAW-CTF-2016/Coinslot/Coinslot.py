from pwn import *
from itertools import *

i_coins = [10000, 5000, 1000, 500, 100, 50, 20, 10, 5, 1]
d_coins = [50, 25, 10, 5, 1]

host = "misc.chal.csaw.io"
port = 8000
s = remote(host, port)
c = 0
while True:
    s.recvuntil('$')
    words = s.recvuntil('$')[:-2]
    print words 

    a, b = words.split('.')
    a = int(a)
    b = int(b)

    for i in i_coins:
        s.recvuntil('bills: ')
        nu = a // i
	a %= i
	#printi str(nu)
        s.sendline(str(nu))
    
    for i in d_coins:
        s.recvuntil('c): ')
        nu = b // i
	b = b % i
	#print str(nu)
        s.sendline(str(nu))
    
    re = s.recvline().strip()
#    print re
    c  += 1
    if c == 400:
	break
    print c
s.interactive()    