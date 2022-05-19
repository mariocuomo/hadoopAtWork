#!/usr/bin/env python3
import sys


userlst={}
for line in sys.stdin:
	line = line.strip()

	words=line.split("\t")

	utente=words[0]
	score=words[1]
	prodotto=words[2]

	lst = userlst.get(utente,[])
	lst.append([prodotto,score])
	userlst[utente]=lst

for utente in userlst.keys():
	lst = userlst.get(utente)
	lst = list(map(lambda x: ":".join(x),lst))
	lst = ";".join(lst)
	print(utente+'\t'+lst)
