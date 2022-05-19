"""
questo script pulisce il dataset Reviews.csv e crea 3 versioni del file con dimensioni differenti

***OPERAZIONI DI PULIZIA***

- converte Time nell'anno corrispondente
- pulisce il campo Text eliminando la punteggiatura e le stop words
- separa i campi col simbolo \t
- rimuove duplicati (se un utente ha recensito due volte lo stesso prodotto)
- elimina header


***FILE CREATI***

- cardinalità N (ReviewsPulitoN.txt)
- cardinalità 2N (ReviewPulito2N.txt)
- cardinalità 3N (ReviewPulito3N.txt)

"""
import pandas as pd
from datetime import datetime
import string
import re
import random
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))


def pulisciTesto(text):
	recensione = re.findall(r'\w+', text)
	recensione = list(map(lambda x: x.lower(), recensione))
	
	filtered_sentence = []
 
	for parola in recensione:
		if parola not in stop_words:
			filtered_sentence.append(parola)

	return " ".join(str(elem) for elem in filtered_sentence)	


	

def acquisisciAnno(text):
	anno=datetime.utcfromtimestamp(int(text)).strftime("%Y")
	return anno


colonne_da_eliminare = ['Id', 'ProfileName', 'HelpfulnessNumerator', 'HelpfulnessDenominator', 'Summary']

dataframe=pd.read_csv('../datasets/Reviews.csv').dropna()
dataframe = dataframe.drop(colonne_da_eliminare, axis=1)
listaUtenti=dataframe.iloc[:, 1].unique()
listaProdotti=dataframe.iloc[:, 0].unique()

"""
ReviewsPulitoN.txt
"""

dataframe.iloc[:, 3] = dataframe.iloc[:, 3].apply(acquisisciAnno)
dataframe.iloc[:, 4] = dataframe.iloc[:, 4].apply(pulisciTesto)
dataframe = dataframe[dataframe.Text != ""]
dataframe = dataframe.drop_duplicates(subset = ['ProductId', 'UserId'],keep = 'last')
dataframe.to_csv('../datasets/ReviewsPulitoN.txt', sep = '\t', index=False, header=None)




"""
ReviewsPulito2N.txt
"""
dataframeCopy=dataframe.copy()
dataframeCopy.iloc[:, 3] = dataframeCopy.iloc[:, 3].apply(lambda x: random.randint(1999, 2012))
dataframeCopy.iloc[:, 2] = dataframeCopy.iloc[:, 2].apply(lambda x: random.randint(1, 5))
dataframeCopy.iloc[:, 1] = dataframeCopy.iloc[:, 1].apply(lambda x: listaUtenti[random.randint(0, len(listaUtenti)-1)])
dataframeCopy.iloc[:, 0] = dataframeCopy.iloc[:, 0].apply(lambda x: listaProdotti[random.randint(0, len(listaProdotti)-1)])

_dataframe = pd.concat([dataframe, dataframeCopy], ignore_index=True)
_dataframe = _dataframe.drop_duplicates(subset = ['ProductId', 'UserId'],keep = 'last')
_dataframe.to_csv('../datasets/ReviewsPulito2N.txt', sep = '\t', index=False, header=None)



"""
ReviewsPulito3N.txt
"""

dataframeCopy=dataframe.copy()
dataframeCopy.iloc[:, 3] = dataframeCopy.iloc[:, 3].apply(lambda x: random.randint(1999, 2012))
dataframeCopy.iloc[:, 2] = dataframeCopy.iloc[:, 2].apply(lambda x: random.randint(1, 5))
dataframeCopy.iloc[:, 1] = dataframeCopy.iloc[:, 1].apply(lambda x: listaUtenti[random.randint(0, len(listaUtenti)-1)])
dataframeCopy.iloc[:, 0] = dataframeCopy.iloc[:, 0].apply(lambda x: listaProdotti[random.randint(0, len(listaProdotti)-1)])

dataframe = pd.concat([_dataframe, dataframeCopy], ignore_index=True)
dataframe = dataframe.drop_duplicates(subset = ['ProductId', 'UserId'],keep = 'last')
dataframe.to_csv('../datasets/ReviewsPulito3N.txt', sep = '\t', index=False, header=None)
