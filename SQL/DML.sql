INSERT INTO major_info VALUES ('12071','����Ʈ����');
INSERT INTO major_info (major_id,major) VALUES ('12072','��ǻ�Ͱ���');
INSERT INTO major_info VALUES ('12073','������ǻ��');
COMMIT;
SELECT * FROM major_info ;


INSERT INTO student VALUES('SK001','�����',28,'12071','M','2020/07/01');
INSERT INTO student VALUES('SK002','�����',27,'12071','M','2020/07/01');
INSERT INTO student VALUES('SK003','�̸��',26,'12071','M','2020/07/01');
INSERT INTO student VALUES('SK004','�ڽ���',27,'12071','M','2020/07/01');
INSERT INTO student VALUES('SK005','�ں���',25,'12071','F','2020/07/01');
# INSERT INTO student VALUES('SK006','ȫ�浿',25,'12074','M','2020/07/01');
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
SET major='��ǻ�Ͱ���'
WHERE major_id=12072;

ROLLBACK;

DELETE FROM student
WHERE major_id=(SELECT major_id	FROM major_info WHERE major='������ǻ��');
SELECT * FROM student

INSERT INTO student VALUES ('SK006','ȫ�浿',25,'12071','M','2020/07/01');
UPDATE student SET major_id='12072' WHERE s_id='SK006';

SAVEPOINT ss;

DELETE FROM student WHERE s_id='SK006'

ROLLBACK TO ss;