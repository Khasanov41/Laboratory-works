""" Öèêëû for èñïîëüçóþòñÿ äëÿ ïðîõîæäåíèÿ ïî çàäàííîé ïîñëåäîâàòåëüíîñòè. 
Íà êàæäîé èòåðàöèè ïåðåìåííîé, îïðåäåëåííîé â öèêëå for, áóäåò ïðèñâàèâàòüñÿ ñëåäóþùåå çíà÷åíèå â ñïèñêå 
""" 

# Ôóíêöèÿ range (n) âîçâðàùàåò ñïèñîê [0, 1, 2, 3, ..., n-1] 

for i in range(5):    	# äëÿ êàæäîãî ÷èñëà i â äèàïàçîíå 0-4 
    print(i)         	# ýòà ñòðîêà âûïîëíÿåòñÿ 5 ðàç. Ïåðâûé ðàç i ðàâíî 0, çàòåì 1, çàòåì 2, çàòåì 3, çàòåì 4 
  

primes = [2, 3, 5, 7]   # ñîçäàíèå íîâîãî ñïèñêà 

# Âûâåäèòå íà ýêðàí êàæäûé ýëåìåíò èç primes, èñïîëüçóÿ öèêë for ïî i

for ?? in ???
    print(primes[i]) 

# Ïåðåáîð ýëåìåíòîâ ñïèñêà âîçìîæåí è áåç èñïîëüçîâàíèÿ èíäåêñà ýëåìåíòà
for prime in primes 
    print(prime) 

  

#--------------------------------------# 

  

""" Ñòðîêè î÷åíü ïîõîæè íà ñïèñêè â Python. Âû ìîæåòå èñïîëüçîâàòü äðóãóþ ñòðîêó, ÷òîáû ïåðåáðàòü åå. 
""" 

hello_world = "Hello, World!" 

for ch in hello_world:    # ïå÷àòü êàæäîãî ñèìâîëà ñòðîêè 
    print(ch) 
  


length = 0     		# ïåðåìåííàÿ length 

# Èñïîëüçóéòå öèêë, ÷òîáû ïîäñ÷èòàòü, ñêîëüêî ñèìâîëîâ ñîäåðæèò hello_world. Ñîõðàíèòå ýòî ÷èñëî â ïåðåìåííîé length 

for ... in hello_world: 
    length += 1    	# óâåëè÷èòü ïåðåìåííóþ íà 1 ïðè êàæäîì ïðîõîäå öèêëà 
  

print(len(hello_world) == length) 
