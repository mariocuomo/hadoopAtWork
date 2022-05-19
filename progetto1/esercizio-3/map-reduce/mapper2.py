#!/usr/bin/env python3
"""mapper"""

import sys


user1_user2_prodotti={}


# input con forma (utente1, utente2, prodotto)
# output con forma (utente1, utente2, listaProdotti)
for line in sys.stdin:
	line = line.strip()
	words = line.split("\t")

	user1=words[0]
	user2=words[1]

	prodotto=words[2]

	lst=user1_user2_prodotti.get((user1,user2),[])

	if lst==[]:
		user1_user2_prodotti[(user1,user2)]=[prodotto]
	else:
		lst.append(prodotto)
		user1_user2_prodotti[(user1,user2)]=lst

	


for (user1,user2) in user1_user2_prodotti.keys():
	lst=user1_user2_prodotti.get((user1,user2))	
	print(user1+'\t'+user2+'\t'+" ".join(lst))