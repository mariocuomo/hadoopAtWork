#!/usr/bin/env python3
"""mapper"""

import sys

# input con forma (ProductId, UserId, Score, Time, Text)
# output con forma (anno, parola, occorrenze)
for line in sys.stdin:
	line = line.strip()
	words = line.split("\t")

	anno=int(words[3])
	recensione = words[4].split(" ")

	parole2occorrenze={}
	for parola in recensione:
		occorrenze=parole2occorrenze.get(parola,0)
		if occorrenze==0:
			parole2occorrenze[parola]=1
		else:
			parole2occorrenze[parola]=occorrenze+1

	
	for parola,occorrenze in parole2occorrenze.items():
		print('%s %s %d' % (anno,parola,occorrenze))