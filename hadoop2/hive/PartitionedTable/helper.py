import requests
import string
import random


alphabet = list(string.ascii_lowercase)

"""
genera un file che ha la forma
NUMERO INTERO | CARATTERE
"""
with open('file.txt', 'w') as out:
	for i in range(100000):
		letter=alphabet[random.randint(0, len(alphabet)-1)]
		number=str(random.randint(0, 100))

		out.write(number + '\t' + letter+'\n')
