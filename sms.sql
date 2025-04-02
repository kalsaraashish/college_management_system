-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: college_management_system
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can view permission',1,'view_permission'),(5,'Can add group',2,'add_group'),(6,'Can change group',2,'change_group'),(7,'Can delete group',2,'delete_group'),(8,'Can view group',2,'view_group'),(9,'Can add content type',3,'add_contenttype'),(10,'Can change content type',3,'change_contenttype'),(11,'Can delete content type',3,'delete_contenttype'),(12,'Can view content type',3,'view_contenttype'),(13,'Can add attendance',4,'add_attendance'),(14,'Can change attendance',4,'change_attendance'),(15,'Can delete attendance',4,'delete_attendance'),(16,'Can view attendance',4,'view_attendance'),(17,'Can add courses',5,'add_courses'),(18,'Can change courses',5,'change_courses'),(19,'Can delete courses',5,'delete_courses'),(20,'Can view courses',5,'view_courses'),(21,'Can add user',6,'add_customuser'),(22,'Can change user',6,'change_customuser'),(23,'Can delete user',6,'delete_customuser'),(24,'Can view user',6,'view_customuser'),(25,'Can add admin hod',7,'add_adminhod'),(26,'Can change admin hod',7,'change_adminhod'),(27,'Can delete admin hod',7,'delete_adminhod'),(28,'Can view admin hod',7,'view_adminhod'),(29,'Can add staffs',8,'add_staffs'),(30,'Can change staffs',8,'change_staffs'),(31,'Can delete staffs',8,'delete_staffs'),(32,'Can view staffs',8,'view_staffs'),(33,'Can add notification staffs',9,'add_notificationstaffs'),(34,'Can change notification staffs',9,'change_notificationstaffs'),(35,'Can delete notification staffs',9,'delete_notificationstaffs'),(36,'Can view notification staffs',9,'view_notificationstaffs'),(37,'Can add leave report staff',10,'add_leavereportstaff'),(38,'Can change leave report staff',10,'change_leavereportstaff'),(39,'Can delete leave report staff',10,'delete_leavereportstaff'),(40,'Can view leave report staff',10,'view_leavereportstaff'),(41,'Can add feed back staffs',11,'add_feedbackstaffs'),(42,'Can change feed back staffs',11,'change_feedbackstaffs'),(43,'Can delete feed back staffs',11,'delete_feedbackstaffs'),(44,'Can view feed back staffs',11,'view_feedbackstaffs'),(45,'Can add students',12,'add_students'),(46,'Can change students',12,'change_students'),(47,'Can delete students',12,'delete_students'),(48,'Can view students',12,'view_students'),(49,'Can add notification student',13,'add_notificationstudent'),(50,'Can change notification student',13,'change_notificationstudent'),(51,'Can delete notification student',13,'delete_notificationstudent'),(52,'Can view notification student',13,'view_notificationstudent'),(53,'Can add leave report student',14,'add_leavereportstudent'),(54,'Can change leave report student',14,'change_leavereportstudent'),(55,'Can delete leave report student',14,'delete_leavereportstudent'),(56,'Can view leave report student',14,'view_leavereportstudent'),(57,'Can add feed back student',15,'add_feedbackstudent'),(58,'Can change feed back student',15,'change_feedbackstudent'),(59,'Can delete feed back student',15,'delete_feedbackstudent'),(60,'Can view feed back student',15,'view_feedbackstudent'),(61,'Can add attendance report',16,'add_attendancereport'),(62,'Can change attendance report',16,'change_attendancereport'),(63,'Can delete attendance report',16,'delete_attendancereport'),(64,'Can view attendance report',16,'view_attendancereport'),(65,'Can add subjects',17,'add_subjects'),(66,'Can change subjects',17,'change_subjects'),(67,'Can delete subjects',17,'delete_subjects'),(68,'Can view subjects',17,'view_subjects'),(69,'Can add log entry',18,'add_logentry'),(70,'Can change log entry',18,'change_logentry'),(71,'Can delete log entry',18,'delete_logentry'),(72,'Can view log entry',18,'view_logentry'),(73,'Can add session',19,'add_session'),(74,'Can change session',19,'change_session'),(75,'Can delete session',19,'delete_session'),(76,'Can view session',19,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `college_management_app_adminhod`
--

DROP TABLE IF EXISTS `college_management_app_adminhod`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `college_management_app_adminhod` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `admin_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_id` (`admin_id`),
  CONSTRAINT `college_management_a_admin_id_9e60b3e3_fk_college_m` FOREIGN KEY (`admin_id`) REFERENCES `college_management_app_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_management_app_adminhod`
--

LOCK TABLES `college_management_app_adminhod` WRITE;
/*!40000 ALTER TABLE `college_management_app_adminhod` DISABLE KEYS */;
INSERT INTO `college_management_app_adminhod` VALUES (1,'2025-02-04 08:49:06.883828','2025-02-04 08:49:06.883828',1);
/*!40000 ALTER TABLE `college_management_app_adminhod` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `college_management_app_attendance`
--

DROP TABLE IF EXISTS `college_management_app_attendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `college_management_app_attendance` (
  `id` int NOT NULL AUTO_INCREMENT,
  `attendance_date` datetime(6) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `subject_id_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `college_management_a_subject_id_id_2dce47dc_fk_college_m` (`subject_id_id`),
  CONSTRAINT `college_management_a_subject_id_id_2dce47dc_fk_college_m` FOREIGN KEY (`subject_id_id`) REFERENCES `college_management_app_subjects` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_management_app_attendance`
--

LOCK TABLES `college_management_app_attendance` WRITE;
/*!40000 ALTER TABLE `college_management_app_attendance` DISABLE KEYS */;
/*!40000 ALTER TABLE `college_management_app_attendance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `college_management_app_attendancereport`
--

DROP TABLE IF EXISTS `college_management_app_attendancereport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `college_management_app_attendancereport` (
  `id` int NOT NULL AUTO_INCREMENT,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `attendance_id_id` int NOT NULL,
  `student_id_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `college_management_a_attendance_id_id_a41a958b_fk_college_m` (`attendance_id_id`),
  KEY `college_management_a_student_id_id_d485776b_fk_college_m` (`student_id_id`),
  CONSTRAINT `college_management_a_attendance_id_id_a41a958b_fk_college_m` FOREIGN KEY (`attendance_id_id`) REFERENCES `college_management_app_attendance` (`id`),
  CONSTRAINT `college_management_a_student_id_id_d485776b_fk_college_m` FOREIGN KEY (`student_id_id`) REFERENCES `college_management_app_students` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_management_app_attendancereport`
--

LOCK TABLES `college_management_app_attendancereport` WRITE;
/*!40000 ALTER TABLE `college_management_app_attendancereport` DISABLE KEYS */;
/*!40000 ALTER TABLE `college_management_app_attendancereport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `college_management_app_courses`
--

DROP TABLE IF EXISTS `college_management_app_courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `college_management_app_courses` (
  `id` int NOT NULL AUTO_INCREMENT,
  `course_name` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_management_app_courses`
--

LOCK TABLES `college_management_app_courses` WRITE;
/*!40000 ALTER TABLE `college_management_app_courses` DISABLE KEYS */;
INSERT INTO `college_management_app_courses` VALUES (1,'BCA','2025-02-04 08:51:16.908694','2025-02-04 08:51:16.908694'),(2,'BA','2025-02-04 09:00:16.663550','2025-02-04 09:00:16.663550');
/*!40000 ALTER TABLE `college_management_app_courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `college_management_app_customuser`
--

DROP TABLE IF EXISTS `college_management_app_customuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `college_management_app_customuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `user_type` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_management_app_customuser`
--

LOCK TABLES `college_management_app_customuser` WRITE;
/*!40000 ALTER TABLE `college_management_app_customuser` DISABLE KEYS */;
INSERT INTO `college_management_app_customuser` VALUES (1,'pbkdf2_sha256$870000$ijVdHQxfotrV8lO7QthTgy$LkdMa1M//LdQImCTKnGYQSZD00OH/2xavJGL42IdxoU=','2025-02-04 13:39:49.060368',1,'admin','','','admin@gmail.com',1,1,'2025-02-04 08:49:06.176495','1'),(2,'pbkdf2_sha256$870000$To6nPLw9OahlT8nSdf24Jx$Gs3BDGyXsmSET0BERyZL9fD7EnEOjXu+ylVsetQD8fY=',NULL,0,'tea1','Teacher','one','teacher2@gmail.com',0,1,'2025-02-04 08:51:09.795104','2'),(3,'pbkdf2_sha256$870000$H0gnfCBLgDVuiaCnVDAhhl$OZmfihkYgHlrI/KMSq16/PksEaTHgeiNzpfMXBNdxjU=','2025-02-04 08:58:23.343704',0,'jay123','jay','Pandya','jaypandya341@gmail.com',0,1,'2025-02-04 08:51:47.601414','3');
/*!40000 ALTER TABLE `college_management_app_customuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `college_management_app_customuser_groups`
--

DROP TABLE IF EXISTS `college_management_app_customuser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `college_management_app_customuser_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `college_management_app_c_customuser_id_group_id_e87eaaf1_uniq` (`customuser_id`,`group_id`),
  KEY `college_management_a_group_id_378c3eb6_fk_auth_grou` (`group_id`),
  CONSTRAINT `college_management_a_customuser_id_6a8c43b8_fk_college_m` FOREIGN KEY (`customuser_id`) REFERENCES `college_management_app_customuser` (`id`),
  CONSTRAINT `college_management_a_group_id_378c3eb6_fk_auth_grou` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_management_app_customuser_groups`
--

LOCK TABLES `college_management_app_customuser_groups` WRITE;
/*!40000 ALTER TABLE `college_management_app_customuser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `college_management_app_customuser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `college_management_app_customuser_user_permissions`
--

DROP TABLE IF EXISTS `college_management_app_customuser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `college_management_app_customuser_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `college_management_app_c_customuser_id_permission_9ff3bc3d_uniq` (`customuser_id`,`permission_id`),
  KEY `college_management_a_permission_id_283da4d6_fk_auth_perm` (`permission_id`),
  CONSTRAINT `college_management_a_customuser_id_380998f3_fk_college_m` FOREIGN KEY (`customuser_id`) REFERENCES `college_management_app_customuser` (`id`),
  CONSTRAINT `college_management_a_permission_id_283da4d6_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_management_app_customuser_user_permissions`
--

LOCK TABLES `college_management_app_customuser_user_permissions` WRITE;
/*!40000 ALTER TABLE `college_management_app_customuser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `college_management_app_customuser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `college_management_app_feedbackstaffs`
--

DROP TABLE IF EXISTS `college_management_app_feedbackstaffs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `college_management_app_feedbackstaffs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `feedback` longtext NOT NULL,
  `feedback_reply` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `staff_id_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `college_management_a_staff_id_id_480e6a98_fk_college_m` (`staff_id_id`),
  CONSTRAINT `college_management_a_staff_id_id_480e6a98_fk_college_m` FOREIGN KEY (`staff_id_id`) REFERENCES `college_management_app_staffs` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_management_app_feedbackstaffs`
--

LOCK TABLES `college_management_app_feedbackstaffs` WRITE;
/*!40000 ALTER TABLE `college_management_app_feedbackstaffs` DISABLE KEYS */;
/*!40000 ALTER TABLE `college_management_app_feedbackstaffs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `college_management_app_feedbackstudent`
--

DROP TABLE IF EXISTS `college_management_app_feedbackstudent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `college_management_app_feedbackstudent` (
  `id` int NOT NULL AUTO_INCREMENT,
  `feedback` longtext NOT NULL,
  `feedback_reply` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `student_id_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `college_management_a_student_id_id_b8a724c1_fk_college_m` (`student_id_id`),
  CONSTRAINT `college_management_a_student_id_id_b8a724c1_fk_college_m` FOREIGN KEY (`student_id_id`) REFERENCES `college_management_app_students` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_management_app_feedbackstudent`
--

LOCK TABLES `college_management_app_feedbackstudent` WRITE;
/*!40000 ALTER TABLE `college_management_app_feedbackstudent` DISABLE KEYS */;
/*!40000 ALTER TABLE `college_management_app_feedbackstudent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `college_management_app_leavereportstaff`
--

DROP TABLE IF EXISTS `college_management_app_leavereportstaff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `college_management_app_leavereportstaff` (
  `id` int NOT NULL AUTO_INCREMENT,
  `leave_date` varchar(255) NOT NULL,
  `leave_message` longtext NOT NULL,
  `leave_status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `staff_id_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `college_management_a_staff_id_id_d2db00df_fk_college_m` (`staff_id_id`),
  CONSTRAINT `college_management_a_staff_id_id_d2db00df_fk_college_m` FOREIGN KEY (`staff_id_id`) REFERENCES `college_management_app_staffs` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_management_app_leavereportstaff`
--

LOCK TABLES `college_management_app_leavereportstaff` WRITE;
/*!40000 ALTER TABLE `college_management_app_leavereportstaff` DISABLE KEYS */;
/*!40000 ALTER TABLE `college_management_app_leavereportstaff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `college_management_app_leavereportstudent`
--

DROP TABLE IF EXISTS `college_management_app_leavereportstudent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `college_management_app_leavereportstudent` (
  `id` int NOT NULL AUTO_INCREMENT,
  `leave_date` varchar(255) NOT NULL,
  `leave_message` longtext NOT NULL,
  `leave_status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `student_id_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `college_management_a_student_id_id_1b900ea4_fk_college_m` (`student_id_id`),
  CONSTRAINT `college_management_a_student_id_id_1b900ea4_fk_college_m` FOREIGN KEY (`student_id_id`) REFERENCES `college_management_app_students` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_management_app_leavereportstudent`
--

LOCK TABLES `college_management_app_leavereportstudent` WRITE;
/*!40000 ALTER TABLE `college_management_app_leavereportstudent` DISABLE KEYS */;
/*!40000 ALTER TABLE `college_management_app_leavereportstudent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `college_management_app_notificationstaffs`
--

DROP TABLE IF EXISTS `college_management_app_notificationstaffs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `college_management_app_notificationstaffs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `staff_id_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `college_management_a_staff_id_id_31e1af2b_fk_college_m` (`staff_id_id`),
  CONSTRAINT `college_management_a_staff_id_id_31e1af2b_fk_college_m` FOREIGN KEY (`staff_id_id`) REFERENCES `college_management_app_staffs` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_management_app_notificationstaffs`
--

LOCK TABLES `college_management_app_notificationstaffs` WRITE;
/*!40000 ALTER TABLE `college_management_app_notificationstaffs` DISABLE KEYS */;
/*!40000 ALTER TABLE `college_management_app_notificationstaffs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `college_management_app_notificationstudent`
--

DROP TABLE IF EXISTS `college_management_app_notificationstudent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `college_management_app_notificationstudent` (
  `id` int NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `student_id_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `college_management_a_student_id_id_e0b8c7a8_fk_college_m` (`student_id_id`),
  CONSTRAINT `college_management_a_student_id_id_e0b8c7a8_fk_college_m` FOREIGN KEY (`student_id_id`) REFERENCES `college_management_app_students` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_management_app_notificationstudent`
--

LOCK TABLES `college_management_app_notificationstudent` WRITE;
/*!40000 ALTER TABLE `college_management_app_notificationstudent` DISABLE KEYS */;
/*!40000 ALTER TABLE `college_management_app_notificationstudent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `college_management_app_staffs`
--

DROP TABLE IF EXISTS `college_management_app_staffs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `college_management_app_staffs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `address` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `admin_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_id` (`admin_id`),
  CONSTRAINT `college_management_a_admin_id_a6596c20_fk_college_m` FOREIGN KEY (`admin_id`) REFERENCES `college_management_app_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_management_app_staffs`
--

LOCK TABLES `college_management_app_staffs` WRITE;
/*!40000 ALTER TABLE `college_management_app_staffs` DISABLE KEYS */;
INSERT INTO `college_management_app_staffs` VALUES (1,'amreli','2025-02-04 08:51:10.703423','2025-02-04 08:51:10.703423',2);
/*!40000 ALTER TABLE `college_management_app_staffs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `college_management_app_students`
--

DROP TABLE IF EXISTS `college_management_app_students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `college_management_app_students` (
  `id` int NOT NULL AUTO_INCREMENT,
  `gender` varchar(255) NOT NULL,
  `profile_pic` varchar(100) NOT NULL,
  `address` longtext NOT NULL,
  `session_start_year` date NOT NULL,
  `session_end_year` date NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `admin_id` bigint NOT NULL,
  `course_id_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_id` (`admin_id`),
  KEY `college_management_a_course_id_id_8389a1cf_fk_college_m` (`course_id_id`),
  CONSTRAINT `college_management_a_admin_id_b1a80a3c_fk_college_m` FOREIGN KEY (`admin_id`) REFERENCES `college_management_app_customuser` (`id`),
  CONSTRAINT `college_management_a_course_id_id_8389a1cf_fk_college_m` FOREIGN KEY (`course_id_id`) REFERENCES `college_management_app_courses` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_management_app_students`
--

LOCK TABLES `college_management_app_students` WRITE;
/*!40000 ALTER TABLE `college_management_app_students` DISABLE KEYS */;
INSERT INTO `college_management_app_students` VALUES (1,'Male','','sk','2025-02-07','2025-02-27','2025-02-04 08:51:48.423844','2025-02-04 08:51:48.423844',3,1);
/*!40000 ALTER TABLE `college_management_app_students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `college_management_app_subjects`
--

DROP TABLE IF EXISTS `college_management_app_subjects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `college_management_app_subjects` (
  `id` int NOT NULL AUTO_INCREMENT,
  `subject_name` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `course_id_id` int NOT NULL,
  `staff_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `college_management_a_course_id_id_26b1da12_fk_college_m` (`course_id_id`),
  KEY `college_management_a_staff_id_id_70fd13ad_fk_college_m` (`staff_id_id`),
  CONSTRAINT `college_management_a_course_id_id_26b1da12_fk_college_m` FOREIGN KEY (`course_id_id`) REFERENCES `college_management_app_courses` (`id`),
  CONSTRAINT `college_management_a_staff_id_id_70fd13ad_fk_college_m` FOREIGN KEY (`staff_id_id`) REFERENCES `college_management_app_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_management_app_subjects`
--

LOCK TABLES `college_management_app_subjects` WRITE;
/*!40000 ALTER TABLE `college_management_app_subjects` DISABLE KEYS */;
INSERT INTO `college_management_app_subjects` VALUES (1,'Java','2025-02-04 09:29:51.407991','2025-02-04 09:29:51.408121',1,2);
/*!40000 ALTER TABLE `college_management_app_subjects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_college_m` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_college_m` FOREIGN KEY (`user_id`) REFERENCES `college_management_app_customuser` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (18,'admin','logentry'),(2,'auth','group'),(1,'auth','permission'),(7,'college_management_app','adminhod'),(4,'college_management_app','attendance'),(16,'college_management_app','attendancereport'),(5,'college_management_app','courses'),(6,'college_management_app','customuser'),(11,'college_management_app','feedbackstaffs'),(15,'college_management_app','feedbackstudent'),(10,'college_management_app','leavereportstaff'),(14,'college_management_app','leavereportstudent'),(9,'college_management_app','notificationstaffs'),(13,'college_management_app','notificationstudent'),(8,'college_management_app','staffs'),(12,'college_management_app','students'),(17,'college_management_app','subjects'),(3,'contenttypes','contenttype'),(19,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-02-04 08:39:02.962008'),(2,'contenttypes','0002_remove_content_type_name','2025-02-04 08:39:03.058484'),(3,'auth','0001_initial','2025-02-04 08:39:03.244403'),(4,'auth','0002_alter_permission_name_max_length','2025-02-04 08:39:03.287500'),(5,'auth','0003_alter_user_email_max_length','2025-02-04 08:39:03.292605'),(6,'auth','0004_alter_user_username_opts','2025-02-04 08:39:03.296918'),(7,'auth','0005_alter_user_last_login_null','2025-02-04 08:39:03.301936'),(8,'auth','0006_require_contenttypes_0002','2025-02-04 08:39:03.304883'),(9,'auth','0007_alter_validators_add_error_messages','2025-02-04 08:39:03.311109'),(10,'auth','0008_alter_user_username_max_length','2025-02-04 08:39:03.315574'),(11,'auth','0009_alter_user_last_name_max_length','2025-02-04 08:39:03.320983'),(12,'auth','0010_alter_group_name_max_length','2025-02-04 08:39:03.332719'),(13,'auth','0011_update_proxy_permissions','2025-02-04 08:39:03.337626'),(14,'auth','0012_alter_user_first_name_max_length','2025-02-04 08:39:03.342709'),(15,'college_management_app','0001_initial','2025-02-04 08:39:04.353566'),(16,'admin','0001_initial','2025-02-04 08:48:46.103436'),(17,'admin','0002_logentry_remove_auto_add','2025-02-04 08:48:46.110482'),(18,'admin','0003_logentry_add_action_flag_choices','2025-02-04 08:48:46.117460'),(19,'sessions','0001_initial','2025-02-04 08:48:46.141883'),(20,'college_management_app','0002_alter_subjects_staff_id','2025-02-04 09:22:20.111337');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('fm9ufpy7vlz2jg5ciraamoa7emqk47uy','.eJxVjE0OwiAYBe_C2hh-A7g06TnIA76WRsDGtivj3a07u5w3L_NmAftWwr7SK8yZ3Zhgl_8tIj2o_0R61koThYaOiRr1LWBZrkPDXO_Ha-j5BOdOwVqOiFYWYlRI0nFvNHkrhbckXJZSwviYfSJExcfokhLGqaS4sdnCw0BL9vkClCQ5_g:1tfJ9Z:7Ez5PBxb_mLBC8vowozGP9HSK1N2dJlnDF3iDzfxd_g','2025-02-18 13:39:49.062365'),('rvf4joha3wxpd6x85rnqes4w511cmcyq','.eJxVjE0OwiAYBe_C2hh-A7g06TnIA76WRsDGtivj3a07u5w3L_NmAftWwr7SK8yZ3Zhgl_8tIj2o_0R61koThYaOiRr1LWBZrkPDXO_Ha-j5BOdOwVqOiFYWYlRI0nFvNHkrhbckXJZSwviYfSJExcfokhLGqaS4sdnCw0BL9vkClCQ5_g:1tfFFX:D18Lxxf5RfAT4aSuhvT5vVIhAQiGhIrcv6uqjFcs5Ak','2025-02-18 09:29:43.020145');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-02-04 20:10:35
