#!/usr/bin/env python3
"""reducer"""

import sys

for line in sys.stdin:
	line = line.strip()

	words = line.split(" ")

	numero=int(words[2])
	lettera=words[1]

	print('%s %i' % (lettera,numero))


