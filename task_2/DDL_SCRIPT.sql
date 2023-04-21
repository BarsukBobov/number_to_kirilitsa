CREATE DATABASE  IF NOT EXISTS university
USE university;


DROP TABLE IF EXISTS address;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE address (
  id_address int NOT NULL,
  city varchar(45) NOT NULL,
  street varchar(45) NOT NULL,
  house int NOT NULL,
  flat int NOT NULL,
  PRIMARY KEY (id_address)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


DROP TABLE IF EXISTS academic_vacation;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE academic_vacation (
  id_academic_vacation int NOT NULL,
  id_student int NOT NULL,
  date_of_vacation date NOT NULL,
  PRIMARY KEY (id_academic_vacation),
  CONSTRAINT student_f_key FOREIGN KEY (id_student) REFERENCES student (id_student)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


DROP TABLE IF EXISTS group;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE group (
  id_group int NOT NULL,
  group_number int NOT NULL,
  speciality int NOT NULL,
  year_of_studing int NOT NULL,
  quantity_of_students int NOT NULL,
  study_form int NOT NULL,
  PRIMARY KEY (id_group),
  UNIQUE KEY group_number_UNIQUE (group_number),
  CONSTRAINT speciality FOREIGN KEY (speciality) REFERENCES speciality (id_speciality) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT study_form FOREIGN KEY (study_form) REFERENCES study_form_group (id_study_form_group) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


DROP TABLE IF EXISTS day_of_the_week;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE day_of_the_week (
  id_day_of_the_week int NOT NULL AUTO_INCREMENT,
  day_of_the_week varchar(45) NOT NULL,
  PRIMARY KEY (id_day_of_the_week)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

DROP TABLE IF EXISTS discipline;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE discipline (
  id_discipline int NOT NULL,
  name varchar(150) NOT NULL,
  PRIMARY KEY (id_discipline),
  UNIQUE KEY name_UNIQUE (name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

DROP TABLE IF EXISTS class_numbers;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE class_numbers (
  id_class_numbers int NOT NULL AUTO_INCREMENT,
  class_time varchar(45) NOT NULL,
  PRIMARY KEY (id_class_numbers)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

DROP TABLE IF EXISTS expelled;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE expelled (
  id_expelled int NOT NULL,
  id_student int NOT NULL,
  date_of_expelled date NOT NULL,
  PRIMARY KEY (id_expelled),
  CONSTRAINT student_expelled_fk FOREIGN KEY (id_student) REFERENCES student (id_student)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

DROP TABLE IF EXISTS teacher;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE teacher (
  id_teacher int NOT NULL,
  sec_name varchar(45) NOT NULL,
  name varchar(45) NOT NULL,
  midname varchar(45) DEFAULT NULL,
  birth_date date NOT NULL,
  address int NOT NULL,
  series_of_the_passport int NOT NULL,
  passport_number int NOT NULL,
  phone varchar(45) DEFAULT NULL,
  email varchar(45) DEFAULT NULL,
  login varchar(45) NOT NULL,
  password varchar(45) NOT NULL,
  PRIMARY KEY (id_teacher),
  UNIQUE KEY phone_UNIQUE (phone),
  UNIQUE KEY email_UNIQUE (email),
  CONSTRAINT address FOREIGN KEY (address) REFERENCES address (id_address) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


DROP TABLE IF EXISTS schedule;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE schedule (
  id_schedule int NOT NULL,
  day_of_the_week int NOT NULL,
  group int NOT NULL,
  class_numbers int NOT NULL,
  discipline int NOT NULL,
  teacher int NOT NULL,
  classroom varchar(45) NOT NULL,
  PRIMARY KEY (id_schedule),
  CONSTRAINT group_fk FOREIGN KEY (group) REFERENCES group (id_group) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT day_of_the_week FOREIGN KEY (day_of_the_week) REFERENCES day_of_the_week (id_day_of_the_week),
  CONSTRAINT discipline_fk FOREIGN KEY (discipline) REFERENCES discipline (id_discipline) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT class_numbers FOREIGN KEY (class_numbers) REFERENCES class_numbers (id_class_numbers) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT teacher FOREIGN KEY (teacher) REFERENCES teacher (id_teacher) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


DROP TABLE IF EXISTS speciality;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE speciality (
  id_speciality int NOT NULL,
  specialty_number varchar(45) NOT NULL,
  name varchar(90) NOT NULL,
  cost_of_education int NOT NULL,
  amount_of_budget_places int NOT NULL,
  PRIMARY KEY (id_speciality),
  UNIQUE KEY name_UNIQUE (name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

DROP TABLE IF EXISTS student_stipend;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE student_stipend (
  id int NOT NULL,
  id_student int NOT NULL,
  id_stipend int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT student_f_key FOREIGN KEY (id_student) REFERENCES student (id_student),
  CONSTRAINT stipend_f_key FOREIGN KEY (id_stipend) REFERENCES stipend (id_stipend)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

DROP TABLE IF EXISTS stipend;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE stipend (
  id_stipend int NOT NULL,
  name_of_stipend varchar(45) NOT NULL,
  amount_of_stipend int NOT NULL,
  PRIMARY KEY (id_stipend)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


DROP TABLE IF EXISTS student;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE student (
  id_student int NOT NULL AUTO_INCREMENT,
  group int NOT NULL,
  sec_name varchar(45) NOT NULL,
  name varchar(45) NOT NULL,
  midname varchar(45) DEFAULT NULL,
  address int NOT NULL,
  birth_date date NOT NULL,
  rec_book_number int NOT NULL,
  series_of_the_passport int NOT NULL,
  passport_number int NOT NULL,
  speciality int NOT NULL,
  year_of_admission int NOT NULL,
  study_form int NOT NULL,
  login varchar(45) NOT NULL,
  password varchar(45) NOT NULL,
  PRIMARY KEY (id_student),
  UNIQUE KEY rec_book_number_UNIQUE (rec_book_number),
  CONSTRAINT group FOREIGN KEY (group) REFERENCES group (id_group) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT speciality_student FOREIGN KEY (speciality) REFERENCES speciality (id_speciality),
  CONSTRAINT study_form_student FOREIGN KEY (study_form) REFERENCES study_form_student (id_study_form_student) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT address FOREIGN KEY (address) REFERENCES address (id_address) ON DELETE CASCADE ON UPDATE CASCADE

) ENGINE=InnoDB AUTO_INCREMENT=583 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

DROP TABLE IF EXISTS performance;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE performance (
  id_performance int NOT NULL,
  id_student int NOT NULL,
  discipline int NOT NULL,
  grade varchar(7) NOT NULL,
  PRIMARY KEY (id_performance),
  CONSTRAINT discipline FOREIGN KEY (discipline) REFERENCES discipline (id_discipline) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT student FOREIGN KEY (id_student) REFERENCES student (id_student) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


DROP TABLE IF EXISTS study_form_group;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE study_form_group (
  id_study_form_group int NOT NULL,
  study_form varchar(45) NOT NULL,
  PRIMARY KEY (id_study_form_group)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


DROP TABLE IF EXISTS study_form_student;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE study_form_student (
  id_study_form_student int NOT NULL,
  study_form_student varchar(45) NOT NULL,
  PRIMARY KEY (id_study_form_student)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


