INSERT INTO major_info VALUES ('12071','소프트웨어');
INSERT INTO major_info (major_id,major) VALUES ('12072','컴퓨터공학');
INSERT INTO major_info VALUES ('12073','응용컴퓨팅');
COMMIT;
SELECT * FROM major_info ;


INSERT INTO student VALUES('SK001','유용민',28,'12071','M','2020/07/01');
INSERT INTO student VALUES('SK002','이재원',27,'12071','M','2020/07/01');
INSERT INTO student VALUES('SK003','이명우',26,'12071','M','2020/07/01');
INSERT INTO student VALUES('SK004','박시형',27,'12071','M','2020/07/01');
INSERT INTO student VALUES('SK005','박보람',25,'12071','F','2020/07/01');
# INSERT INTO student VALUES('SK006','홍길동',25,'12074','M','2020/07/01');
COMMIT;
SELECT * FROM student;

UPDATE student
SET major_id ='12072'
WHERE s_id='SK005';
COMMIT;
SELECT * FROM student;

UPDATE student
SET major_id ='12073'
WHERE s_id='SK005';
ROLLBACK;
SELECT * FROM student;

UPDATE major_info 
SET major='컴퓨터공학'
WHERE major_id=12072;

ROLLBACK;

DELETE FROM student
WHERE major_id=(SELECT major_id	FROM major_info WHERE major='응용컴퓨팅');
SELECT * FROM student

INSERT INTO student VALUES ('SK006','홍길동',25,'12071','M','2020/07/01');
UPDATE student SET major_id='12072' WHERE s_id='SK006';

SAVEPOINT ss;

DELETE FROM student WHERE s_id='SK006'

ROLLBACK TO ss;