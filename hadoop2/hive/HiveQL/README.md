# Linguaggio HQL


L'idea di base di hive è quella di nascondere al programmatore l'utilizzo di map-reduce fornendogli un linguaggio SQL-like.

In questo esempio si ha a disposizione un file.txt che ha la seguente forma e in cui i campi sono separati dal simbolo di tabulazione.
 
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

--- 
```
CREATE TABLE info (nome STRING, colore STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t';

LOAD DATA LOCAL INPATH '/home/mariocuomo/Desktop/hadoopAtWork/hadoop2/hive/HiveQL/file.txt'
OVERWRITE INTO TABLE info;

SELECT * FROM info LIMIT 10;

CREATE TABLE color_counts AS
SELECT colore, count(*) as sfide_completate
FROM info
GROUP BY colore;


SELECT * FROM color_counts ORDER BY sfide_completate;

DROP TABLE info;
DROP TABLE color_counts;
```
