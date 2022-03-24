#!/usr/bin/env python3
"""mapper"""

import sys

for line in sys.stdin:

	line = line.strip()

	words = line.split(" ")

	lettera=words[0]
	numero=int(words[1])

	print('%s %i' % (lettera,numero))