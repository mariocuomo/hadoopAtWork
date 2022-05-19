#!/usr/bin/env python3
"""mapper"""

import sys

# input con forma (ProductId, UserId, Score, Time, Text)
# output con forma (idUtente, voto, idProdotto)
for line in sys.stdin:
	line = line.strip()
	words = line.split("\t")


	idUtente=words[1]
	voto=words[2]
	idProdotto=words[0]

	
	print('%s %s %s' % (idUtente,voto,idProdotto))