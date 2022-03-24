#!/usr/bin/env python3
"""mapper"""

import sys

for line in sys.stdin:

	line = line.strip()
	words = line.split(" ")

	lettera=words[0]

	try:
		numero=int(words[1])
		print('%s %i A' % (lettera,numero))
	except ValueError:
		codice=words[1]
		print('%s %s B' % (lettera,codice))