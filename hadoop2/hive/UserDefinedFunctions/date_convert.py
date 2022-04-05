#!/usr/bin/env python3

import sys
from datetime import datetime

for line in sys.stdin:
	line = line.strip()

	nome, data=line.split("\t")

	#estrai nome giorno dalla data
	data=data.replace(':','')
	data=data.strip()
	data=data.replace('.','-')
	data = datetime.strptime(data, '%d-%m-%Y').strftime('%A')

	print("\t".join([nome,data]))

