#!/usr/bin/env python3
"""mapper"""

import sys

dictLetter_occ={}

for line in sys.stdin:
	line = line.strip()

	words = line.split(" ")

	numero=int(words[2])
	lettera=words[1]

	print('%s %i' % (lettera,numero))


