# User Defined Functions


L'idea di base di hive è quella di nascondere al programmatore l'utilizzo di map-reduce fornendogli un linguaggio SQL-like.

In questo esempio si mostra come utilizzare le User Defined Functions.<br>
Si ha a disposizione un file.txt che ha la seguente forma e in cui i campi sono separati dal simbolo di tabulazione.<br>
I dati sono stati acquisti da <a href="https://github.com/mariocuomo/LeetCode/blob/main/README.md">qui</a>.

| NOME SFIDA | DATA
| :---: | :---: |
| Palindrome Number | 16.03.2022
| Plus One | 16.03.2022
| Valid Anagram | 17.03.2022


Si vuole restituire in output il numero di sfide completate per per ogni giorno.<br>
L'output del sistema sarà il seguente.

| GIORNO | SFIDE COMPLETATE
| :---: | :---: |
| venerdi | 15
| domenica | 2

La conversione da data in formato stringa a nome del giono avviene in una user defined function.

--- 
```
CREATE TABLE info (nome STRING, data STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t';

LOAD DATA LOCAL INPATH '/home/mariocuomo/Desktop/hadoopAtWork/hadoop2/hive/UserDefinedFunctions/file.txt'
OVERWRITE INTO TABLE info;

SELECT * FROM info LIMIT 10;

ADD FILE /home/mariocuomo/Desktop/hadoopAtWork/hadoop2/hive/UserDefinedFunctions/date_convert.py;

CREATE TABLE days AS
SELECT TRANSFORM(info.nome, info.data)
USING 'python3 /home/mariocuomo/Desktop/hadoopAtWork/hadoop2/hive/UserDefinedFunctions/date_convert.py'
AS name, giorno
FROM info;

SELECT * FROM days LIMIT 10;

CREATE TABLE days_count AS
SELECT giorno, count(*) as sfide_completate
FROM days
GROUP BY giorno;

SELECT * FROM days_count;

DROP TABLE info;
DROP TABLE days;
DROP TABLE  days_count;
```

```python
#!/usr/bin/env python3

import sys
from datetime import datetime

for line in sys.stdin:
	line = line.strip()

	nome, data=line.split("\t")

	#estrai nome giorno dalla data
	data=data.replace(':','')
	data=data.strip()
	data=data.replace('.','-')
	data = datetime.strptime(data, '%d-%m-%Y').strftime('%A')

	print("\t".join([nome,data]))
```


