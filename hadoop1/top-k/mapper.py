#!/usr/bin/env python3
"""mapper"""

import sys

lst=[]

for line in sys.stdin:

	line = line.strip()

	words = line.split(" ")

	lettera=words[0]
	numero=int(words[1])

	lst.append((lettera, numero))


lst.sort(key = lambda x: x[1], reverse=True)

for t in lst[:10]:
	print('%s %i' % (t[0],t[1]))