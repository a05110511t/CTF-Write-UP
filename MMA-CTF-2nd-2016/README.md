#README.md

Make a Palindrome! 

Problem
======================================================================================
Your task is to make a palindrome string by rearranging and concatenating given words.

Input Format: N <Word_1> <Word_2> ... <Word_N>
Answer Format: Rearranged words separated by space.
Each words contain only lower case alphabet characters.

Example Input: 3 ab cba c
Example Answer: ab c cba

You have to connect to ppc1.chal.ctf.westerns.tokyo:31111(TCP) to answer the problem.

$ nc ppc1.chal.ctf.westerns.tokyo 31111

    Time limit is 3 minutes.
    The maximum number of words is 10.
    There are 30 cases. You can get flag 1 on case 1. You can get flag 2 on case 30.
    samples.7z Server connection examples.
-------------------------------------------------------------------------------------

一開始還不知道題目有提供語Server 互動的範例，
所以立馬就nc連過去：
'''
ais@ais-VirtualBox:~/Desktop/samples/samples$ nc ppc1.chal.ctf.westerns.tokyo 31111
Your task is to make a palindrome string by rearranging and concatenating given words.

Input Format: N <Word_1> <Word_2> ... <Word_N>
Answer Format: Rearranged words separated by space.
Each words contain only lower case alphabet characters.

Example Input: 3 ab cba c
Example Answer: ab c cba


Let's play!

Case: #1
Input: 5 gujvxfqoujod ojuoqfxvjug dd si is
'''

