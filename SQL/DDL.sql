CREATE TABLE student(
s_id VARCHAR(10) PRIMARY KEY,
s_name VARCHAR(20) NOT NULL,
s_age INT(3) UNSIGNED,
major VARCHAR(30) NOT NULL,
gender CHAR(1) CHECK(gender IN('F','M')),
entry_date DATE NOT NULL
);

CREATE TABLE major_info(
major_id INT(5) PRIMARY KEY,
major VARCHAR(30) NOT NULL
);

show columns from student;
show columns from major_info;

SELECT *FROM Information_schema.table_constraints WHERE TABLE_NAME='student'
SELECT *FROM information_schema.table_constraints WHERE TABLE_NAME ='major_info'

ALTER TABLE student CHANGE COLUMN major major_id VARCHAR(30) NOT NULL;

ALTER TABLE student MODIFY COLUMN major_id INT(5);

ALTER TABLE student ADD CONSTRAINT student_fk_majorId
FOREIGN KEY(major_id) REFERENCES major_info(major_id) ON DELETE CASCADE;

SELECT *FROM information_schema.TABLE_CONSTRAINTS WHERE TABLE_NAME='student';


show columns from student;
show columns from major_info;


SELECT *FROM information_schema.TABLE_CONSTRAINTS WHERE TABLE_NAME='student';

desc student;