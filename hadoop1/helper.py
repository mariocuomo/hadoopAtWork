import string
import random


alphabet = list(string.ascii_lowercase)

with open('file.txt', 'w') as out:
	for i in range(100000):
		letter=alphabet[random.randint(0, len(alphabet)-1)]
		number=str(random.randint(0, 100))

		out.write(letter +' '+ number+'\n')

