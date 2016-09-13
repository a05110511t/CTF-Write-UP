#Make a Palindrome! 

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

題目有兩小題共30個例子：

1. You can get flag 1 on case 1. 

2. You can get flag 2 on case 30.

```
ais@ais-VirtualBox:~/Desktop/samples/samples$ nc ppc1.chal.ctf.westerns.tokyo 31111
Your task is to make a palindrome string by rearranging and concatenating given words.

Input Format: N <Word_1> <Word_2> ... <Word_N>
Answer Format: Rearranged words separated by space.
Each words contain only lower case alphabet characters.

Example Input: 3 ab cba c
Example Answer: ab c cba


Let's play!

Case: #1
Input: 5 sffsc b xut bskqtuxbc qksb
```

觀察一陣子後發現是回文，需要照著題目格式，重新排列組合為可回文的順序後，即可過關。

像是這題：

5 表示有5個 strings ，於是答案為："bskqtuxbc sffsc b xut qksb"
![img](1.jpg)

Flag 1:```TWCTF{Charisma_School_Captain}```

![img](2.jpg)

Flag 2:```TWCTF{Hiyokko_Tsuppari}```

code內有註解。

將收到的字串先以```''.join(words)```不考慮空白給擠在一起，好讓程式去判斷，

曾經卡了一陣子解了幾題就失敗，才想到可能會有奇數個字元，於是分別做判斷，

最後則是卡在shuffle()次數不夠多，拉高後即可過關。

\*36行 for i in range(0, 7257601):

題目最多給10個strings，照理來說約只要算10!次，但很奇怪10!的次數有時候會不夠，

所以我就將次數提高2倍再加幾次，當時是用```for i in range(0, 8000000):```過關的。\*
