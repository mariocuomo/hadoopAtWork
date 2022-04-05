import requests
from datetime import datetime

url = 'https://raw.githubusercontent.com/mariocuomo/LeetCode/main/README.md'
page = requests.get(url)

linee=page.text.split('\n')
linee=linee[12:len(linee)-11]


lst=[]

for riga in linee:
	parti = riga.split('|')

	nome=parti[1]
	data=parti[4]

	#pulisci il campo data
	data=data.replace(':','')
	data=data.strip()


	#modifica nome che ha la forma '[nome sfida](link)' 'nome sfida'
	nome=nome.strip()
	nome = nome.split('[', 1)[1].split(']')[0]


	lst.append([nome,data])


"""
genera un file che ha la forma
nome sfida \t data
"""
with open('file.txt', 'w') as out:
	for [nome,data] in lst:
		out.write(nome + '\t' + data+'\n')
