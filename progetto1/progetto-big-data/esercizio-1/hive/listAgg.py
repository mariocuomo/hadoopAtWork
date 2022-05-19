#!/usr/bin/env python3
import sys


annolst={}
for line in sys.stdin:
	line = line.strip()

	words=line.split("\t")

	anno=words[0]
	parola=words[1]
	occorrenze=words[2]

	lst = annolst.get(anno,[])
	lst.append([parola,occorrenze])
	annolst[anno]=lst

for anno in annolst.keys():
	lst = annolst.get(anno)
	lst = sorted(lst,key = lambda x: x[1], reverse=True)
	lst = list(map(lambda x: ":".join(x),lst))
	lst = ";".join(lst)
	print(anno+'\t'+lst)
