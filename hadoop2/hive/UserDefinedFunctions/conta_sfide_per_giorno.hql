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