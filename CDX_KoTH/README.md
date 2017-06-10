CDX網站攻防Write Up
共100台server散落在x.x.x.1~200
觀察大概有20種題目，每種都有5題
拿分方式：把自己對五flag寫進首頁index.html
主辦輪巡15秒一次->1台1分鐘1分
隊名：90CM (4th)
共打下11台server
1. Vul mail題： *5
解：https://github.com/opsxcq/exploit-CVE-2016-10033 
2. b374k題： *1
解：弱密碼，有客製化過沒改密功能，要自己改source code，
速解->進去後趕快寫首頁然後把b374k砍掉XDDD
3. Bobby Blog題： *4
解：普通帳戶試了超久就是沒辦法寫檔，最後用FTP爆Administrator密碼(當時還跟第一名搶主機，很刺激的!!!)
第一名解法：普通user進FTP上asp碼
4. rdp題： *1
解：利用3.爆出的管理員權限密碼可登admin，然後要把資料夾權限打開即可進xampp改首頁
--
5. Try it題：應該是Honeypot，FTP隨意帳密可進，但我還是用前面爆的admin密碼進去，這時可以寫檔，pwd在/目錄，然後找不到首頁放在哪，ls -la /底下都空的= =....於是自己創wwwroot/寫index，最後flag是出現在https首頁，不過主辦沒掃https首頁所以沒分Q_Q
--
個人心得感想：
滿好玩的，第一次參加koth，一開始還不知道要幹嘛，後來漸入佳境，但是前面隊伍一開始站領太久刷太多分最後追不上了，從屁股能追到第4滿感動的XDD
分工合作滿重要的，我狂找突破點，有突破點後丟給隊友解，必要時幫忙搶。
經驗、運氣和手速和熟練度很關鍵，
聽Lionbug說在搶rdp主機時他在改密碼有人一直把它控制台關掉XDD
--
-----------------------------------------------------------------------------------
以下是打聽到的解法：
6. phpinfo題：FTP爆破用洩漏的帳號爆破
7. docker題：用docker expolit 打忘了哪個port
8. 俄文題：FTP爆user密碼
9. cgi-bin題：shellshock
10. xvwa題：command inj /tmp可寫，但是是最新的linux kernal無法提權，除非握有0day
11. 留言板honeypot題：刷flag
12. Samba題：metaspolit刷smb漏洞
13. Strust2題：刷Strust2
14. Wannacry那個SMB：metaspolit打的
15. kali題：不知道怎打但聽說弱密碼：root / toor
16. Apache首頁：缺
17. 未知
18. 未知
19. 未知
20. 未知