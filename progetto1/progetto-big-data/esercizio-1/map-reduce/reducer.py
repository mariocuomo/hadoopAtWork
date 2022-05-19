#!/usr/bin/env python3
"""reducer"""

import sys


#dict di dict
#la chiave del primo dict è l'anno, la chiave del secondo dict è la parola
anno2parole2ccorrenze={}


# input con forma (anno, parola, occorrenze)
for line in sys.stdin:
	line = line.strip()

	words = line.split(" ")

	anno=words[0]
	parola=words[1]
	occorrenze=int(words[2])


	parole2occorrenze = anno2parole2ccorrenze.get(anno,{})
	
	if parole2occorrenze=={}:
		anno2parole2ccorrenze[anno]={parola:occorrenze}
	else:
		_occorrenze = parole2occorrenze.get(parola,0)
		if _occorrenze==0:
			anno2parole2ccorrenze[anno][parola]=occorrenze
		else:
			anno2parole2ccorrenze[anno][parola]=occorrenze+_occorrenze



for anno in anno2parole2ccorrenze.keys():
	parole2occorrenze = anno2parole2ccorrenze.get(anno)

	s = anno+'\n'
	for parola,occorrenze in sorted(parole2occorrenze.items(), key=lambda x: x[1], reverse=True)[0:10]:
		s=s+parola+'\t'+str(occorrenze)+'\n'
	s=s+'\n'
	print(s)