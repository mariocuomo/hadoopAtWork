#!/usr/bin/env python3
"""reducer"""

import sys

for line in sys.stdin:
	line = line.strip()

	words = line.split(" ")

	lettera=words[0]
	numero=int(words[1])

	for word in words:
		print('%s\t%i' % (lettera,numero))
