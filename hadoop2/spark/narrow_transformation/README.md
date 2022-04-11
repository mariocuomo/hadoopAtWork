# Trasformazione narrow


Spark - a differenza di Hadoop1.0 - mette a disposizione un nuovo modello di programmazione che si basa sul savataggio in memoria principale dei risultati intermedi e nuovi paradigmi: questo permette di realizzare analisi utilizzando strumenti diversi dal classico Map Reduce.

In questo esempio si ha a disposizione un file.txt che ha la seguente forma e in cui i campi sono separati dal simbolo di tabulazione.<br>
I dati sono stati acquisti da <a href="https://github.com/mariocuomo/LeetCode/blob/main/README.md">qui</a>.

| NOME SFIDA | COLORE
| :---: | :---: |
| Palindrome Number | green
| Plus One | green
| Valid Anagram | orange


Si vuole restituire in output il numero di sfide per ogni colore.<br>
L'output del sistema sarà il seguente.

| COLORE | SFIDE COMPLETATE
| :---: | :---: |
| green | 15
| orange | 21


Durante l'esecuzione i dati sono salvati in strutture di dati particolari distribuite - i **Resilient Distributed Datasets (RDDs)** - e si utilizzano **trasformazioni narrow**.<br>
Una trasformazione narrow permette di acquisire una partizione dell'RDD e di lavorarla indipendentemente dalle altre.

--- 
```Python
input_RDD.filter(lambda line: 'green' in line).count()
```
