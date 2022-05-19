#!/usr/bin/env python3
"""reducer"""

import sys
import itertools


product_users={}


# input con forma (prodotto, listaUtenti)
# output con forma (utente1, utente2, prodotto)
for line in sys.stdin:
	line = line.strip()

	words = line.split("\t")

	prodotto=words[0]
	utenti=words[1].split(" ")


	lst = product_users.get(prodotto,[])

	if lst==[]:
		product_users[prodotto]=utenti
	else:
		product_users[prodotto]=lst+utenti




for prodotto in product_users.keys():
	lst=product_users.get(prodotto)

	for utente1, utente2 in list(itertools.combinations(lst, 2)):
		print(utente1+'\t'+utente2+'\t'+prodotto)


