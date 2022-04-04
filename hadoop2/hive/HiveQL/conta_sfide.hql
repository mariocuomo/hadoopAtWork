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