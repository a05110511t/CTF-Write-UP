# -*- coding:utf-8 -*-
# Server connection example file for Python 2

import socket
import sys
import random
from random import shuffle
from z3 import *
host = 'ppc1.chal.ctf.westerns.tokyo'
if len(sys.argv) > 1:
    host = sys.argv[1]
port = 31111
if len(sys.argv) > 2:
    host = int(sys.argv[2])

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

client_file = client.makefile('b')

while client_file.readline().strip() != "Let's play!":
    pass

client_file.readline()
for case in range(0, 30):
    client_file.readline()
    words = client_file.readline().split()[2:]
    # words: input
    # answer: answer
    ##  Please write some code here
    test = words
    def rotate(l,n):
        return l[n:] + l[:n]
    print len(''.join(words))
    for i in range(0, 7257601):
	#print 'random:'
	shuffle(words)
#	s = sorted(words, key=lambda x: x, reverse = True)
#	rotate(words, i)
	s = ''.join(words)
        if(len(s)%2 == 1):
            if( s[:len(s)/2:] == s[len(s)/2+1:][::-1] ):
                Found = ' '.join(s)
                print 'Found'
		break
	else:
	    if( s[:len(s)/2:] == s[(len(s))/2:][::-1] ):
                Found = ' '.join(s)
       	        print 'Found'
		break
    answer = words
    print  ' '.join(answer)

    client_file.write(' '.join(answer) + "\n")
    client_file.flush()
    ret = client_file.readline()[8:-1]
    print(ret)
    if 'Wrong Answer' in ret:
        print(client_file.readline())
        sys.exit(1)
