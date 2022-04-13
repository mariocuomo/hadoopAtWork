import requests

url = 'https://raw.githubusercontent.com/mariocuomo/LeetCode/main/README.md'
page = requests.get(url)

linee=page.text.split('\n')
linee=linee[12:len(linee)-10]


lst=[]

for riga in linee:
	parti = riga.split('|')
	
	nome=parti[1]
	
	velocita=parti[6]
	memoria=parti[7]

	#modifica velocita che ha la forma 'x.y %:' in 'x.y'
	velocita=velocita.replace('%','')
	velocita=velocita.strip()

	#modifica memoria che ha la forma 'x.y %:' in 'x.y'
	memoria = memoria.replace('%','')
	memoria = memoria.strip()

	#modifica nome che ha la forma '[nome sfida](link)' in 'nome sfida'
	nome = nome.strip()
	nome = nome.split('[', 1)[1].split(']')[0]


	lst.append([nome,velocita,memoria])



"""
genera un file che ha la forma
nome sfida \t velocita \t memoria
"""
with open('file.txt', 'w') as out:
	for [nome,velocita,memoria] in lst:
		out.write(nome + '\t' + velocita + '\t' + memoria +'\n')
