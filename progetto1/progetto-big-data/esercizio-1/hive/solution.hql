CREATE TABLE info (ProductId STRING, UserId STRING, Score STRING, Timee STRING, Textt STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t';


LOAD DATA LOCAL INPATH '/home/mariocuomo/Desktop/progetto-big-data/datasets/ReviewsPulitoN.txt'
OVERWRITE INTO TABLE info;


ADD FILE /home/mariocuomo/Desktop/progetto-big-data/esercizio-1/hive/text_converter.py;
ADD FILE /home/mariocuomo/Desktop/progetto-big-data/esercizio-1/hive/listAgg.py;

CREATE TABLE annoParole AS
SELECT TRANSFORM(info.Timee, info.Textt)
USING 'python3 /home/mariocuomo/Desktop/progetto-big-data/esercizio-1/hive/text_converter.py'
AS anno, parola
FROM info;


CREATE TABLE annoParoleOccorrenze AS
SELECT anno, parola,Count(*) as occorrenze
FROM annoParole
GROUP BY anno, parola;



CREATE TABLE result AS
WITH cte AS (
SELECT anno, parola, occorrenze, ROW_NUMBER() OVER (PARTITION BY anno ORDER BY occorrenze DESC) AS rn
FROM annoParoleOccorrenze
)
SELECT anno,parola,occorrenze
FROM cte
WHERE rn <= 10
ORDER BY occorrenze DESC;


CREATE TABLE resultList AS
SELECT TRANSFORM(result.anno, result.parola, result.occorrenze)
USING 'python3 /home/mariocuomo/Desktop/progetto-big-data/esercizio-1/hive/listAgg.py'
FROM result;

DROP TABLE info;
DROP TABLE annoParole;
DROP TABLE annoParoleOccorrenze;
DROP TABLE result;

INSERT OVERWRITE LOCAL DIRECTORY '/home/mariocuomo/Desktop/progetto-big-data/esercizio-1/hive/output' ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' SELECT * FROM resultList;

DROP TABLE resultList;
