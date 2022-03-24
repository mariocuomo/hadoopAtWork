#!/usr/bin/env python3
"""mapper"""

import sys

for line in sys.stdin:

	line = line.strip()

	words = line.split(" ")

	numero=int(words[1])
	lettera=words[0]

	print('%i %s %i' % (numero,lettera,numero))