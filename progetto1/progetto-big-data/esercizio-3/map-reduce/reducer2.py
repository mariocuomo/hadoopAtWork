#!/usr/bin/env python3
"""reducer"""

import sys
import itertools


user1_user2_prodotti={}


# input con forma (utente1, utente2, listaProdotti)
for line in sys.stdin:
	line = line.strip()

	words = line.split("\t")

	user1 = words[0]
	user2 = words[1]

	prodotti = words[2].split(" ")

	lst=user1_user2_prodotti.get((user1,user2),[])

	if lst==[]:
		user1_user2_prodotti[(user1,user2)]=prodotti
	else:
		user1_user2_prodotti[(user1,user2)]=lst+prodotti




for (user1,user2) in user1_user2_prodotti.keys():
	lst=user1_user2_prodotti.get((user1,user2))
	if len(lst)>=3:		
		print(user1+'\t'+user2+'\n'+" ".join(lst)+'\n')


