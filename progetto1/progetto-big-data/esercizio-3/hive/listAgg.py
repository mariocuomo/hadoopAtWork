#!/usr/bin/env python3
import sys


user1_user2_lst={}
for line in sys.stdin:
	line = line.strip()

	words=line.split("\t")

	utente1=words[0]
	utente2=words[1]
	prodotto=words[2]

	lst = user1_user2_lst.get((utente1,utente2),[])
	lst.append(prodotto)
	user1_user2_lst[(utente1,utente2)]=lst

for (utente1,utente2) in user1_user2_lst.keys():
	lst = user1_user2_lst.get((utente1,utente2))
	lst = " ".join(lst)
	print(utente1+'\t'+utente2+'\t'+lst)
