set hive.exec.dynamic.partition.mode=nonstrict

CREATE TABLE info (valore INT) 
PARTITIONED BY(lettera STRING) 
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY '\t'; 

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
