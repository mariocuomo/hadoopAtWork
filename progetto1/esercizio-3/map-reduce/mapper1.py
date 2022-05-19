#!/usr/bin/env python3
"""mapper"""

import sys


product_users={}


# input con forma (ProductId, UserId, Score, Time, Text)
# output con forma (prodotto, listaUtenti)
for line in sys.stdin:
	line = line.strip()
	words = line.split("\t")

	user=words[1]
	prodotto=words[0]
	voto=int(words[2])

	if voto>=4:
		lst = product_users.get(prodotto,[])

		if lst==[]:
			product_users[prodotto]=[user]
		else:
			lst.append(user)
			product_users[prodotto]=lst


for prodotto in product_users.keys():
	lst=product_users.get(prodotto)
	s=""
	for utente in lst:
		s=s+utente+" "
	print(prodotto+'\t'+s)