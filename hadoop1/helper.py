import string
import random


alphabet = list(string.ascii_lowercase)




"""
genera un file che ha la forma
CARATTERE | NUMERO INTERO 
"""
with open('fileA.txt', 'w') as out:
	for i in range(100000):
		letter=alphabet[random.randint(0, len(alphabet)-1)]
		number=str(random.randint(0, 100))

		out.write(letter + ' ' + number+'\n')


"""
genera un file che ha la forma
CARATTERE | CODICE ALFANUMERICO 
"""
with open('fileB.txt', 'w') as out:
	for carattere in alphabet:
		codice = str(random.randint(0, 100))+carattere+str(random.randint(0, 100))
		out.write(carattere + ' ' + codice+'\n')

