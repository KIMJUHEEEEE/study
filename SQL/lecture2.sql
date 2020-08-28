CREATE TABLE CahngeCols(
year INTEGER NOT NULL PRIMARY KEY,
col_1 INTEGER NOT NULL,
col_2 INTEGER NOT NULL);

DESC CahngeCols;

INSERT INTO CahngeCols VALUES(2011,10,7);
INSERT INTO CahngeCols VALUES(2012,20,6);
INSERT INTO CahngeCols VALUES(2013,30,5);
INSERT INTO CahngeCols VALUES(2014,40,4);
INSERT INTO CahngeCols VALUES(2015,50,3);

SELECT * FROM CahngeCols;

SELECT year,
CASE WHEN year <= 2013 THEN col_1
WHEN year>=2014 THEN col_2
ELSE NULL END AS col_3
FROM CahngeCols;

SELECT YEAR FROM CahngeCols 
WHERE 4<= CASE WHEN year <= 2013 THEN col_1
WHEN year >= 2014 THEN col_2
ELSE NULL END;

CREATE TABLE Perm2
(cust_id CHAR(3) PRIMARY KEY,
item_1 VARCHAR(32) NOT NULL,
item_2 VARCHAR(32) NOT NULL);

DESC Perm2;

INSERT INTO Perm2 VALUES('001','시계','정수기');
INSERT INTO Perm2 VALUES('002','휴대전화','휴대전화');
INSERT INTO Perm2 VALUES('003','정수기','시계');
INSERT INTO Perm2 VALUES('004','휴대전화','휴대전화');
INSERT INTO Perm2 VALUES('005','잉크','안경');
SELECT * FROM Perm2;

SELECT CASE WHEN item_1 < item_2 THEN item_1
ELSE item_2 END AS c1,
CASE WHEN item_1<item_2 THEN item_2
ELSE item_1 END AS c2
FROM Perm2;

SELECT DISTINCT 
CASE WHEN item_1<item_2 THEN item_1
ELSE item_2 END AS c1,
CASE WHEN item_1<item_2 THEN item_2
ELSE item_1 END AS c2
FROM Perm2;

CREATE TABLE Perm3
(cust_id CHAR(3) PRIMARY KEY,
item_1 VARCHAR(32) NOT NULL,
item_2 VARCHAR(32) NOT NULL,
item_3 VARCHAR(32) NOT NULL);

INSERT INTO Perm3 VALUES('001','시계','정수기','티슈');
INSERT INTO Perm3 VALUES('002','티슈','정수기','시계');
INSERT INTO Perm3 VALUES('003','달력','노트','시계');
INSERT INTO Perm3 VALUES('004','달력','노트','잉크');
INSERT INTO Perm3 VALUES('005','문고판 책','게임 소프트','안경');
INSERT INTO Perm3 VALUES('006','문고판 책','안경','게임 소프트');

SELECT * FROM Perm3;

DROP VIEW CustItems;

CREATE VIEW CustItems (cust_id,item) AS
SELECT cust_id,item_1
FROM Perm3
UNION ALL
SELECT cust_id,item_2 
FROM Perm3
UNION ALL
SELECT cust_id,item_3
FROM Perm3;

SELECT MAX(CI1.item) AS c1,
MAX(CI2.item) AS c2,
MAX(CI3.item) AS c3
FROM CustItems CI1
INNER JOIN CustItems CI2
ON CI1.cust_id=CI2.cust_id 
AND CI1.item <CI2.item 
INNER JOIN CustItems CI3
ON CI2.cust_id =CI3.cust_id
AND CI2.item <CI3.item
GROUP BY CI1.cust_id;

CREATE TABLE Employees
(emp_id CHAR(3) NOT NULL PRIMARY KEY,
dept VARCHAR(8) NOT NULL,
sex CHAR(2) NOT NULL,
age INTEGER NOT NULL,
salary INTEGER NOT NULL);

DESC Employees ;

INSERT INTO Employees VALUES('001',	'제조',	'남',	32,	30);
INSERT INTO Employees VALUES('002',	'제조',	'남',	30,	29);
INSERT INTO Employees VALUES('003',	'제조',	'여',	23,	19);
INSERT INTO Employees VALUES('004',	'회계',	'남',	45,	35);
INSERT INTO Employees VALUES('005',	'회계',	'남',	50,	45);
INSERT INTO Employees VALUES('006',	'영업',	'여',	40,	50);
INSERT INTO Employees VALUES('007',	'영업',	'여',	42,	40);
INSERT INTO Employees VALUES('008',	'영업',	'남',	52,	38);
INSERT INTO Employees VALUES('009',	'영업',	'남',	34,	28);
INSERT INTO Employees VALUES('010',	'영업',	'여',	41,	25);
INSERT INTO Employees VALUES('011',	'인사',	'남',	29,	25);
INSERT INTO Employees VALUES('012',	'인사',	'여',	36,	29);

SELECT * FROM Employees;

SELECT dept,
SUM(CASE WHEN age <= 30 AND sex='남' THEN 1 ELSE 0 END) AS "신입 (남)",
SUM(CASE WHEN age <= 30 AND sex='여' THEN 1 ELSE 0 END) AS "신입 (여)",
SUM(CASE WHEN age >= 31 AND sex='남' THEN 1 ELSE 0 END) AS "신입 (남)",
SUM(CASE WHEN age >= 31 AND sex='여' THEN 1 ELSE 0 END) AS "신입 (여)"
FROM Employees 
GROUP BY dept;

SELECT dept,
       COUNT(*),
       SUM(CASE WHEN age <= 30 THEN 1 ELSE 0 END) AS "신입(합계)",
       SUM(CASE WHEN age <= 30 AND sex = '남' THEN 1 ELSE 0 END) AS "신입（남）",
       SUM(CASE WHEN age <= 30 AND sex = '여' THEN 1 ELSE 0 END) AS "신입（여）",
       SUM(CASE WHEN age >= 31 THEN 1 ELSE 0 END) AS "전문가(합계)",
       SUM(CASE WHEN age >= 31 AND sex = '남' THEN 1 ELSE 0 END) AS "전문가（남）",
       SUM(CASE WHEN age >= 31 AND sex = '여' THEN 1 ELSE 0 END) AS "전문가（여）"
  FROM Employees
 GROUP BY dept;
 
SELECT dept,
       COUNT(*),
       COUNT(CASE WHEN age <= 30 THEN 1 ELSE NULL END) AS "신입(합계)",
       COUNT(CASE WHEN age <= 30 AND sex = '남' THEN 1 ELSE NULL END) AS "신입（남）",
       COUNT(CASE WHEN age <= 30 AND sex = '여' THEN 1 ELSE NULL END) AS "신입（여）",
       COUNT(CASE WHEN age >= 31 THEN 1 ELSE NULL END) AS "전문가(합계)",
       COUNT(CASE WHEN age >= 31 AND sex = '남' THEN 1 ELSE NULL END) AS "전문가（남）",
       COUNT(CASE WHEN age >= 31 AND sex = '여' THEN 1 ELSE NULL END) AS "전문가（여）"
  FROM Employees
 GROUP BY dept;

SELECT dept,
       COUNT(*) AS cnt
  FROM Employees
 GROUP BY dept;

SELECT dept,
       CASE WHEN COUNT(*) <= 2 THEN '2명 이하'
            ELSE '3명 이상' END AS cnt
  FROM Employees
 GROUP BY dept;



CREATE TABLE LoadSample
(sample_date DATE NOT NULL , 
 load_amt    INTEGER NOT NULL , 
   PRIMARY KEY (sample_date) ) ;
  
  INSERT INTO LoadSample VALUES('2014-02-01', 1024);
INSERT INTO LoadSample VALUES('2014-02-02', 2366);
INSERT INTO LoadSample VALUES('2014-02-05', 2366);
INSERT INTO LoadSample VALUES('2014-02-07',  985);
INSERT INTO LoadSample VALUES('2014-02-08',  780);
INSERT INTO LoadSample VALUES('2014-02-12', 1000);

SELECT * FROm LoadSample;

SELECT MIN(sample_date)
FROM LoadSample;

SELECT LS0.sample_date,
(SELECT MAX(sample_date)
FROM LoadSample LS1
WHERE LS1.sample_date<LS0.sample_date)AS latest
FROM LoadSample LS0;

SELECT LS0.sample_date AS cur_date,
MAX(LS1.sample_date) AS latest
FROM LoadSample LS0
LEFT OUTER JOIN LoadSample LS1
ON LS1.sample_date < LS0.sample_date
GROUP BY LS0.sample_date;

SELECT LS0.sample_date AS cur_date,
LS1.sample_date AS latest
FROM LoadSample LS0
LEFT OUTER JOIN LoadSample LS1
ON LS1.sample_date < LS0.sample_date;

SELECT LS0.sample_date AS cur_date,
       LS0.load_amt AS cur_load_amt,
       MAX(LS1.sample_date) AS latest,
       (SELECT MAX(load_amt)
          FROM LoadSample
         WHERE sample_date = MAX(LS1.sample_date)) AS latest_load_amt
  FROM LoadSample LS0
       LEFT OUTER JOIN LoadSample LS1
         ON LS1.sample_date < LS0.sample_date
 GROUP BY LS0.sample_date;

SELECT LS0.sample_date AS cur_date,
       LS0.load_amt AS cur_load,
       LS1.sample_date AS latest,
       LS1.load_amt AS latest_load
  FROM LoadSample LS0
       LEFT OUTER JOIN LoadSample LS1
         ON LS1.sample_date = (SELECT MAX(sample_date)
                                 FROM LoadSample
                                WHERE sample_date < LS0.sample_date);
                                
SELECT LS0.sample_date AS sample_date,
       MAX(LS1.sample_date) AS latest_1,
       MAX(LS2.sample_date) AS latest_2,
       MAX(LS3.sample_date) AS latest_3
  FROM LoadSample LS0
           LEFT OUTER JOIN LoadSample LS1
             ON LS1.sample_date < LS0.sample_date
             LEFT OUTER JOIN LoadSample LS2
               ON LS2.sample_date < LS1.sample_date
               LEFT OUTER JOIN LoadSample LS3
                 ON LS3.sample_date < LS2.sample_date
 GROUP BY LS0.sample_date;
 
SELECT MAX(LS1.sample_date) AS past,
       LS.sample_date AS sample_date,
       MIN(LS2.sample_date) AS future
  FROM LoadSample LS
       LEFT OUTER JOIN LoadSample LS1
         ON LS1.sample_date < LS.sample_date
         LEFT OUTER JOIN LoadSample LS2
           ON LS2.sample_date > LS.sample_date
 GROUP BY LS.sample_date;

CREATE TABLE LoadSample2
(machine     CHAR(3) NOT NULL,
 sample_date DATE NOT NULL , 
 load_amt    INTEGER NOT NULL , 
   PRIMARY KEY (machine, sample_date) ) ;
  
  INSERT INTO LoadSample2 VALUES('PC1',  '2014-02-01', 1024);
INSERT INTO LoadSample2 VALUES('PC1',  '2014-02-02', 2366);
INSERT INTO LoadSample2 VALUES('PC1',  '2014-02-05', 2366);
INSERT INTO LoadSample2 VALUES('PC1',  '2014-02-07',  985);
INSERT INTO LoadSample2 VALUES('PC1',  '2014-02-08',  780);
INSERT INTO LoadSample2 VALUES('PC1',  '2014-02-12', 1000);
INSERT INTO LoadSample2 VALUES('PC2',  '2014-02-01',  999);
INSERT INTO LoadSample2 VALUES('PC2',  '2014-02-02',   50);
INSERT INTO LoadSample2 VALUES('PC2',  '2014-02-05',  328);
INSERT INTO LoadSample2 VALUES('PC2',  '2014-02-07',  913);
INSERT INTO LoadSample2 VALUES('PC3',  '2014-02-01', 2000);
INSERT INTO LoadSample2 VALUES('PC3',  '2014-02-02', 1000);

SELECT * FROM LoadSample2;

SELECT LS0.sample_date AS cur_date,
       MAX(LS1.sample_date) AS latest_1,
       MAX(LS2.sample_date) AS latest_2,
       MAX(LS3.sample_date) AS latest_3
  FROM LoadSample2 LS0
           LEFT OUTER JOIN LoadSample2 LS1
             ON LS1.sample_date < LS0.sample_date
             LEFT OUTER JOIN LoadSample2 LS2
               ON LS2.sample_date < LS1.sample_date
               LEFT OUTER JOIN LoadSample2 LS3
                 ON LS3.sample_date < LS2.sample_date
 GROUP BY LS0.sample_date;
 
SELECT LS0.machine AS machine, 
       LS0.sample_date AS sample_date,
       MAX(LS1.sample_date) AS latest_1,
       MAX(LS2.sample_date) AS latest_2,
       MAX(LS3.sample_date) AS latest_3
  FROM LoadSample2 LS0
           LEFT OUTER JOIN LoadSample2 LS1
             ON LS1.sample_date < LS0.sample_date
             LEFT OUTER JOIN LoadSample2 LS2
               ON LS2.sample_date < LS1.sample_date
               LEFT OUTER JOIN LoadSample2 LS3
                 ON LS3.sample_date < LS2.sample_date
 GROUP BY LS0.machine, LS0.sample_date
 ORDER BY machine, sample_date;
 
DROP TABLE NonAggTbl;
CREATE TABLE NonAggTbl
(id VARCHAR(32) NOT NULL,
 data_type CHAR(1) NOT NULL,
 data_1 INTEGER,
 data_2 INTEGER,
 data_3 INTEGER,
 data_4 INTEGER,
 data_5 INTEGER,
 data_6 INTEGER);
 DELETE FROM NonAggTbl;
INSERT INTO NonAggTbl VALUES('Jim',    'A',  100,  10,     34,  346,   54,  NULL);
INSERT INTO NonAggTbl VALUES('Jim',    'B',  45,    2,    167,   77,   90,   157);
INSERT INTO NonAggTbl VALUES('Jim',    'C',  NULL,  3,    687, 1355,  324,   457);
INSERT INTO NonAggTbl VALUES('Ken',    'A',  78,    5,    724,  457, NULL,     1);
INSERT INTO NonAggTbl VALUES('Ken',    'B',  123,  12,    178,  346,   85,   235);
INSERT INTO NonAggTbl VALUES('Ken',    'C',  45, NULL,     23,   46,  687,    33);
INSERT INTO NonAggTbl VALUES('Beth',   'A',  75,    0,    190,   25,  356,  NULL);
INSERT INTO NonAggTbl VALUES('Beth',   'B',  435,   0,    183, NULL,    4,   325);
INSERT INTO NonAggTbl VALUES('Beth',   'C',  96,  128,   NULL,    0,    0,    12);

SELECT * FROM NonAggTbl;

SELECT id, data_1, data_2
  FROM NonAggTbl
 WHERE id = 'Jim'
   AND data_type = 'A';
   
  SELECT id, data_3, data_4, data_5
  FROM NonAggTbl
 WHERE id = 'Jim'
   AND data_type = 'B';
  
  SELECT id, data_6
  FROM NonAggTbl
 WHERE id = 'Jim'
   AND data_type = 'C';

  SELECT id,
        MAX(CASE WHEN data_type = 'A' THEN data_1 ELSE NULL END) AS data_1,
        MAX(CASE WHEN data_type = 'A' THEN data_2 ELSE NULL END) AS data_2,
        MAX(CASE WHEN data_type = 'B' THEN data_3 ELSE NULL END) AS data_3,
        MAX(CASE WHEN data_type = 'B' THEN data_4 ELSE NULL END) AS data_4,
        MAX(CASE WHEN data_type = 'B' THEN data_5 ELSE NULL END) AS data_5,
        MAX(CASE WHEN data_type = 'C' THEN data_6 ELSE NULL END) AS data_6
  FROM NonAggTbl
 GROUP BY id;
 
CREATE TABLE PriceByAge
(product_id VARCHAR(32) NOT NULL,
 low_age    INTEGER NOT NULL,
 high_age   INTEGER NOT NULL,
 price      INTEGER NOT NULL,
 PRIMARY KEY (product_id, low_age),
   CHECK (low_age < high_age));
   
  
INSERT INTO PriceByAge VALUES('제품1',  0  ,  50  ,  2000);
INSERT INTO PriceByAge VALUES('제품1',  51  ,  100  ,  3000);
INSERT INTO PriceByAge VALUES('제품2',  0  ,  100  ,  4200);
INSERT INTO PriceByAge VALUES('제품3',  0  ,  20  ,  500);
INSERT INTO PriceByAge VALUES('제품3',  31  ,  70  ,  800);
INSERT INTO PriceByAge VALUES('제품3',  71  ,  100  ,  1000);
INSERT INTO PriceByAge VALUES('제품4',  0  ,  99  ,  8900);

SELECT * FROM PriceByAge ;

SELECT product_id
FROM PriceByAge
GROUP BY product_id
HAVING SUM(high_age - low_age + 1) = 101;

CREATE TABLE Persons
(name   VARCHAR(8) NOT NULL,
 age    INTEGER NOT NULL,
 height FLOAT NOT NULL,
 weight FLOAT NOT NULL,
 PRIMARY KEY (name));
 
INSERT INTO Persons VALUES('Anderson',  30,  188,  90);
INSERT INTO Persons VALUES('Adela',    21,  167,  55);
INSERT INTO Persons VALUES('Bates',    87,  158,  48);
INSERT INTO Persons VALUES('Becky',    54,  187,  70);
INSERT INTO Persons VALUES('Bill',    39,  177,  120);
INSERT INTO Persons VALUES('Chris',    90,  175,  48);
INSERT INTO Persons VALUES('Darwin',  12,  160,  55);
INSERT INTO Persons VALUES('Dawson',  25,  182,  90);
INSERT INTO Persons VALUES('Donald',  30,  176,  53);

SELECT * FROM Persons;

SELECT SUBSTRING(name, 1, 1) AS label,
       COUNT(*)
  FROM Persons
 GROUP BY SUBSTRING(name, 1, 1);
 
SELECT CASE WHEN age < 20 THEN '미성년자'
            WHEN age BETWEEN 21 AND 69 THEN '성인'
            WHEN age > 70 THEN '노인'
            ELSE NULL END AS age_class,
  COUNT(*)
  FROM Persons
 GROUP BY CASE WHEN age < 20 THEN '미성년자'
               WHEN age BETWEEN 21 AND 69 THEN '성인'
               WHEN age > 70 THEN '노인'
               ELSE NULL END;
               
SELECT CASE WHEN weight / POWER(height /100, 2) < 18.5     THEN '저체중'
            WHEN 18.5 <= weight / POWER(height /100, 2) 
                   AND weight / POWER(height /100, 2) < 25 THEN '표준'
            WHEN 25 <= weight / POWER(height /100, 2)      THEN '비만'
            ELSE NULL END AS bmi,
       COUNT(*)
  FROM Persons
 GROUP BY CASE WHEN weight / POWER(height /100, 2) < 18.5     THEN '저체중'
               WHEN 18.5 <= weight / POWER(height /100, 2) 
                      AND weight / POWER(height /100, 2) < 25 THEN '표준'
               WHEN 25 <= weight / POWER(height /100, 2)      THEN '비만'
               ELSE NULL END;
               
SELECT CASE WHEN age < 20 THEN '미성년자'
            WHEN age BETWEEN 21 AND 69 THEN '성인'
            WHEN age > 70 THEN '노인'
       ELSE NULL END AS age_class,
       COUNT(*)
  FROM Persons
 GROUP BY CASE WHEN age < 20 THEN '미성년자'
               WHEN age BETWEEN 21 AND 69 THEN '성인'
               WHEN age > 70 THEN '노인'
          ELSE NULL END
          HAVING COUNT(*) = SUM(CASE WHEN weight / POWER(height /100, 2) < 25 THEN 1
                      ELSE 0 END);
                      
SELECT CASE WHEN age < 20 THEN '미성년자'
            WHEN age BETWEEN 21 AND 69 THEN '성인'
            WHEN age > 70 THEN '노인'
       ELSE NULL END AS age_class,
       COUNT(*) AS all_cnt,
       SUM(CASE WHEN weight / POWER(height /100, 2) < 25 THEN 1
           ELSE 0 END) AS not_fat_cnt
  FROM Persons
 GROUP BY CASE WHEN age < 20 THEN '미성년자'
               WHEN age BETWEEN 21 AND 69 THEN '성인'
               WHEN age > 70 THEN '노인'
          ELSE NULL END;
          
SELECT name,
       age,
       CASE WHEN age < 20 THEN '미성년자'
            WHEN age BETWEEN 21 AND 69 THEN '성인'
            WHEN age > 70 THEN '노인'
            ELSE NULL END AS age_class,
       RANK() OVER(PARTITION BY CASE WHEN age < 20 THEN '미성년자'
                                     WHEN age BETWEEN 21 AND 69 THEN '성인'
                                     WHEN age > 70 THEN '노인'
                                     ELSE NULL END
                   ORDER BY age) AS age_rank_in_class
  FROM Persons
 ORDER BY age_class, age_rank_in_class;