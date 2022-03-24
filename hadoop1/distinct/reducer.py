#!/usr/bin/env python3
"""reducer"""

import sys

key_occ=set()

for line in sys.stdin:
	line = line.strip()
	words = line.split(" ")

	lettera=words[0]
	numero=int(words[1])

	t = (lettera, numero)

	if not t in key_occ:
		key_occ.add(t)
		print('%s %i' % (lettera,numero))


