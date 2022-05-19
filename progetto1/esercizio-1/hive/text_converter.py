#!/usr/bin/env python3
import sys
from datetime import datetime

for line in sys.stdin:
	line = line.strip()

	words=line.split("\t")

	anno=words[0]
	recensione=words[1]

	for parola in recensione.split(" "):
		print("\t".join([anno,parola]))