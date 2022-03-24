#!/usr/bin/env python3
"""reducer"""

import sys

dict_co={}

for line in sys.stdin:
	line = line.strip()

	words = line.split(" ")


	lettera=words[0]
	tmp=words[1]
	fl=words[2]


	lst=dict_co.get(lettera,None)
	if lst==None:
		lst=[]
	lst.append((fl,tmp))

	dict_co[lettera]=lst


for chiave in dict_co.keys():
	lst_associata_a_chiave=dict_co.get(chiave,[])
	
	lst_record_A=list(filter(lambda x: x[0]=='A' , lst_associata_a_chiave))
	lst_record_B=list(filter(lambda x: x[0]=='B' , lst_associata_a_chiave))

	for elA in lst_record_A:
		for elB in lst_record_B:
			print('%s %s %s' % (chiave,elA[1],elB[1]))


