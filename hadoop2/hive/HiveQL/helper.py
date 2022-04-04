import requests

url = 'https://raw.githubusercontent.com/mariocuomo/LeetCode/main/README.md'
page = requests.get(url)

linee=page.text.split('\n')
linee=linee[12:len(linee)-10]


lst=[]

for riga in linee:
	parti = riga.split('|')
	
	nome=parti[1]
	colore=parti[3]

	#modifica colore che ha la forma ':colore_circle:' in 'colore'
	colore=colore.replace('_circle:','')
	colore=colore.replace(':','')
	colore=colore.strip()

	#modifica nome che ha la forma '[nome sfida](link)' 'nome sfida'
	nome=nome.strip()
	nome = nome.split('[', 1)[1].split(']')[0]


	lst.append([nome,colore])



"""
genera un file che ha la forma
nome sfida \t colore
"""
with open('file.txt', 'w') as out:
	for [nome,colore] in lst:
		out.write(nome + '\t' + colore+'\n')
