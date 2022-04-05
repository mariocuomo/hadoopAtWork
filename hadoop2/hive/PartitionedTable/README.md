# Partitioned Table


L'idea di base di hive è quella di nascondere al programmatore l'utilizzo di map-reduce fornendogli un linguaggio SQL-like.

In questo esempio si mostra come utilizzare le Partitioned Table.<br>
Si ha a disposizione un file.txt che ha la seguente forma e in cui i campi sono separati dal simbolo di tabulazione.<br>

| NUMERO | LETTERA
| :---: | :---: |
| 24 | a
| 33 | s
| 6 | r


Si vuole restituire in output la somma dei numeri associati a ogni lettera.<br>
L'output del sistema sarà il seguente.

| LETTERA | SOMMA
| :---: | :---: |
| a | 1221
| b | 325


Si utilizza una Partitioned Table partizionata sul valore della lettera.<br>
I record relativi alla stessa lettera sono salvati in stessi file.<br>
Questo permette in fase di aggregazione di velocizzare il meccanismo di somma.<br>


SENZA PARTITION: 6.074 seconds<br>
CON PARTITION: **4.695** seconds


--- 
```HQL
CREATE TABLE info_tmp (valore INT, lettera STRING) 
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY '\t'; 

LOAD DATA LOCAL INPATH '/home/mariocuomo/Desktop/hadoopAtWork/hadoop2/hive/PartitionedTable/file.txt' INTO TABLE info_tmp;

INSERT OVERWRITE TABLE info PARTITION(lettera) SELECT valore,lettera from info_tmp;

SELECT * FROM info LIMIT 10;

CREATE TABLE lettere_somma AS
SELECT lettera, sum(valore) as somma_valori
FROM info
GROUP BY lettera;

SELECT * FROM lettere_somma LIMIT 10;

DROP TABLE info_tmp;
DROP TABLE info;
DROP TABLE lettere_somma;

```


