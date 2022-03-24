#!/usr/bin/env python3
"""mapper"""

import sys

dictLetter_occ={}

for line in sys.stdin:
	line = line.strip()

	words = line.split(" ")

	lettera=words[0]

	occ = dictLetter_occ.get(lettera,0)
	dictLetter_occ[lettera]=occ+1

for lettera in dictLetter_occ.keys():
	print('%s %i' % (lettera,dictLetter_occ.get(lettera,0)))
