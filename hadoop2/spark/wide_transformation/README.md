# Trasformazione wide


Spark - a differenza di Hadoop1.0 - mette a disposizione un nuovo modello di programmazione che si basa sul savataggio in memoria principale dei risultati intermedi e nuovi paradigmi: questo permette di realizzare analisi utilizzando strumenti diversi dal classico Map Reduce.

In questo esempio si ha a disposizione un file.txt che ha la seguente forma e in cui i campi sono separati dal simbolo di tabulazione.<br>
I dati sono stati acquisti da <a href="https://github.com/mariocuomo/LeetCode/blob/main/README.md">qui</a>.

| NOME SFIDA | VELOCITA | MEMORIA 
| :---: | :---: |
| Palindrome Number | 38 | 92
| Plus One | 23 | 82
| Valid Anagram | 71 | 43


Si vuole restituire in output le migliori k sfide in termini di memoria e le migliori k sfide in termini di memoria<br>
L'output del sistema sarà il seguente.

```
MIGLIORI SFIDA PER VELOCITA
Number Complement, velocita:  99.49
Rotate Array, velocita:  98.04
Add Two Numbers, velocita:  97.66


MIGLIORI SFIDA PER MEMORIA
Peak Index in a Mountain Array, memoria:  99.13
Missing Number, memoria:  98.85
Maximum Depth of Binary Tree, memoria:  97.53
```


Durante l'esecuzione i dati sono salvati in strutture di dati particolari distribuite - i **Resilient Distributed Datasets (RDDs)** - e si utilizzano **trasformazioni wide**.<br>
Una trasformazione wide necessita di acquisire partizioni dell'RDD, effettuare operazioni di shuffle e sort per l'esecuzione.

--- 
```Python
sfida_speed_memory_RDD = input_RDD.map(f=lambda line: line.split("\t"))


sorted_speed_RDD = sfida_speed_memory_RDD.sortBy(
    keyfunc=lambda sfida_speed_memory : sfida_speed_memory[1],
    ascending=False)

sorted_memory_RDD = sfida_speed_memory_RDD.sortBy(
    keyfunc=lambda sfida_speed_memory : sfida_speed_memory[2],
    ascending=False)


top_speed = sorted_speed_RDD.take(3)
top_memory = sorted_memory_RDD.take(3)
```
