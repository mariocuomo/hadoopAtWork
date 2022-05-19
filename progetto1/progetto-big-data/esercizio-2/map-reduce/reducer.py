#!/usr/bin/env python3
"""reducer"""

import sys


user2products={}


# input con forma (idUtente, voto, idProdotto)
for line in sys.stdin:
	line = line.strip()

	words = line.split(" ")

	idUtente=words[0]
	voto=words[1]
	idProdotto=words[2]

	lstProdotti = user2products.get(idUtente,[])
	lstProdotti.append([idProdotto,voto])
	user2products[idUtente]=lstProdotti


for utente in sorted(list(user2products.keys())):
	lstProdotti = user2products.get(utente)
	lstProdotti = sorted(lstProdotti, key = lambda x: x[1], reverse=True)
	

	s=utente+'\n'
	for i in range(len(lstProdotti)):
		if i==5:
			break
		else:
			s=s+lstProdotti[i][0]+'\t'+lstProdotti[i][1]+'\n'
	s=s+'\n'

	print(s)	