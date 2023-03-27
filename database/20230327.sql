-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: social_media_network_db
-- ------------------------------------------------------
-- Server version	8.0.26

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
  `name` varchar(150) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
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
  `name` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add tag',6,'add_tag'),(22,'Can change tag',6,'change_tag'),(23,'Can delete tag',6,'delete_tag'),(24,'Can view tag',6,'view_tag'),(25,'Can add post',7,'add_post'),(26,'Can change post',7,'change_post'),(27,'Can delete post',7,'delete_post'),(28,'Can view post',7,'view_post'),(29,'Can add user',8,'add_customuser'),(30,'Can change user',8,'change_customuser'),(31,'Can delete user',8,'delete_customuser'),(32,'Can view user',8,'view_customuser'),(33,'Can add discussion',9,'add_discussion'),(34,'Can change discussion',9,'change_discussion'),(35,'Can delete discussion',9,'delete_discussion'),(36,'Can view discussion',9,'view_discussion'),(37,'Can add notification',10,'add_notification'),(38,'Can change notification',10,'change_notification'),(39,'Can delete notification',10,'delete_notification'),(40,'Can view notification',10,'view_notification'),(41,'Can add Token',11,'add_token'),(42,'Can change Token',11,'change_token'),(43,'Can delete Token',11,'delete_token'),(44,'Can view Token',11,'view_token'),(45,'Can add token',12,'add_tokenproxy'),(46,'Can change token',12,'change_tokenproxy'),(47,'Can delete token',12,'delete_tokenproxy'),(48,'Can view token',12,'view_tokenproxy'),(49,'Can add auction history',13,'add_auctionhistory'),(50,'Can change auction history',13,'change_auctionhistory'),(51,'Can delete auction history',13,'delete_auctionhistory'),(52,'Can view auction history',13,'view_auctionhistory');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authtoken_token`
--

DROP TABLE IF EXISTS `authtoken_token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_userApp_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `userapp_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authtoken_token`
--

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;
INSERT INTO `authtoken_token` VALUES ('86c4145415200a385ef18e738d06419b4472c456','2023-03-18 06:38:16.611953',6);
/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
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
  `object_id` longtext COLLATE utf8mb4_unicode_520_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_userApp_customuser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_userApp_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `userapp_customuser` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-03-10 04:34:08.826587','2','This is first post',1,'[{\"added\": {}}]',7,1),(2,'2023-03-10 07:09:25.575821','4','Medium',1,'[{\"added\": {}}]',6,1),(3,'2023-03-10 07:09:54.755498','3','This is second post',1,'[{\"added\": {}}]',7,1);
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
  `app_label` varchar(100) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(11,'authtoken','token'),(12,'authtoken','tokenproxy'),(4,'contenttypes','contenttype'),(13,'post','auctionhistory'),(9,'post','discussion'),(10,'post','notification'),(7,'post','post'),(6,'post','tag'),(5,'sessions','session'),(8,'userApp','customuser');
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
  `app` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-03-08 15:59:03.440386'),(2,'contenttypes','0002_remove_content_type_name','2023-03-08 15:59:03.839807'),(3,'auth','0001_initial','2023-03-08 15:59:04.432975'),(4,'auth','0002_alter_permission_name_max_length','2023-03-08 15:59:04.695818'),(5,'auth','0003_alter_user_email_max_length','2023-03-08 15:59:04.720590'),(6,'auth','0004_alter_user_username_opts','2023-03-08 15:59:04.747005'),(7,'auth','0005_alter_user_last_login_null','2023-03-08 15:59:04.781210'),(8,'auth','0006_require_contenttypes_0002','2023-03-08 15:59:04.785896'),(9,'auth','0007_alter_validators_add_error_messages','2023-03-08 15:59:04.818687'),(10,'auth','0008_alter_user_username_max_length','2023-03-08 15:59:04.871420'),(11,'auth','0009_alter_user_last_name_max_length','2023-03-08 15:59:04.896325'),(12,'auth','0010_alter_group_name_max_length','2023-03-08 15:59:04.946591'),(13,'auth','0011_update_proxy_permissions','2023-03-08 15:59:04.965287'),(14,'auth','0012_alter_user_first_name_max_length','2023-03-08 15:59:04.985017'),(15,'userApp','0001_initial','2023-03-08 15:59:05.588796'),(16,'admin','0001_initial','2023-03-08 15:59:05.992669'),(17,'admin','0002_logentry_remove_auto_add','2023-03-08 15:59:06.009775'),(18,'admin','0003_logentry_add_action_flag_choices','2023-03-08 15:59:06.031927'),(19,'post','0001_initial','2023-03-08 15:59:06.620387'),(20,'post','0002_initial','2023-03-08 15:59:06.787395'),(21,'sessions','0001_initial','2023-03-08 15:59:06.919676'),(22,'post','0003_alter_post_options_alter_tag_options','2023-03-08 16:11:46.270250'),(23,'post','0004_alter_tag_options','2023-03-08 16:15:44.679884'),(24,'post','0005_alter_post_options','2023-03-08 16:16:20.316583'),(25,'userApp','0002_customuser_phone_alter_customuser_email','2023-03-09 15:43:59.152503'),(26,'post','0006_discussion_notification','2023-03-10 04:19:25.383753'),(27,'post','0007_alter_post_tags','2023-03-10 04:35:40.598075'),(28,'post','0008_alter_post_link','2023-03-10 04:36:59.966875'),(29,'post','0009_alter_notification_discussion_alter_post_tags','2023-03-18 06:25:57.086898'),(30,'authtoken','0001_initial','2023-03-18 06:37:51.410964'),(31,'authtoken','0002_auto_20160226_1747','2023-03-18 06:37:51.437654'),(32,'authtoken','0003_tokenproxy','2023-03-18 06:37:51.443798'),(33,'post','0010_discussion_parent_id','2023-03-24 13:21:28.357956'),(34,'post','0011_auctionhistory','2023-03-27 14:37:34.534457');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('xm8zas3kb56ol0j2s98i6v62selep9ds','.eJxVjMsOwiAUBf-FtSGXAqV16d5vINwHtmogKe3K-O_apAvdnpk5LxXTtk5xa7LEmdVZGXX63TDRQ8oO-J7KrWqqZV1m1LuiD9r0tbI8L4f7dzClNn3rrjPIIgCW2GSwbgwZHIURSAgxW59l4JC99GRdb61HBwCchiQZR1TvD_YpOK8:1paUPO:ZgQIzKkd7n5P4MeBxNNrJXBC0uMj_87t8QmBZUZHzx8','2023-03-24 04:31:10.262626');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post_auctionhistory`
--

DROP TABLE IF EXISTS `post_auctionhistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `post_auctionhistory` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_date` datetime(6) NOT NULL,
  `modified_date` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  `price` bigint NOT NULL,
  `status` varchar(20) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `author_id` bigint NOT NULL,
  `post_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `post_auctionhistory_author_id_14484b35_fk_userApp_customuser_id` (`author_id`),
  KEY `post_auctionhistory_post_id_b3f66b50_fk_post_post_id` (`post_id`),
  CONSTRAINT `post_auctionhistory_author_id_14484b35_fk_userApp_customuser_id` FOREIGN KEY (`author_id`) REFERENCES `userapp_customuser` (`id`),
  CONSTRAINT `post_auctionhistory_post_id_b3f66b50_fk_post_post_id` FOREIGN KEY (`post_id`) REFERENCES `post_post` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post_auctionhistory`
--

LOCK TABLES `post_auctionhistory` WRITE;
/*!40000 ALTER TABLE `post_auctionhistory` DISABLE KEYS */;
/*!40000 ALTER TABLE `post_auctionhistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post_discussion`
--

DROP TABLE IF EXISTS `post_discussion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `post_discussion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_date` datetime(6) NOT NULL,
  `modified_date` datetime(6) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `type` smallint NOT NULL,
  `content` longtext COLLATE utf8mb4_unicode_520_ci,
  `post_id` bigint NOT NULL,
  `parent_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `post_discussion_post_id_fa9eeba0_fk_post_post_id` (`post_id`),
  CONSTRAINT `post_discussion_post_id_fa9eeba0_fk_post_post_id` FOREIGN KEY (`post_id`) REFERENCES `post_post` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post_discussion`
--

LOCK TABLES `post_discussion` WRITE;
/*!40000 ALTER TABLE `post_discussion` DISABLE KEYS */;
INSERT INTO `post_discussion` VALUES (4,'2023-03-24 13:35:02.460070','2023-03-24 13:35:02.460070',1,1,'string',2,NULL),(7,'2023-03-10 07:18:04.955892','2023-03-10 07:18:04.955892',1,0,'Comment',2,5);
/*!40000 ALTER TABLE `post_discussion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post_notification`
--

DROP TABLE IF EXISTS `post_notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `post_notification` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_date` datetime(6) NOT NULL,
  `modified_date` datetime(6) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `isReaded` tinyint(1) NOT NULL,
  `discussion_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `post_notification_discussion_id_cfb8747e_fk_post_discussion_id` (`discussion_id`),
  CONSTRAINT `post_notification_discussion_id_cfb8747e_fk_post_discussion_id` FOREIGN KEY (`discussion_id`) REFERENCES `post_discussion` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post_notification`
--

LOCK TABLES `post_notification` WRITE;
/*!40000 ALTER TABLE `post_notification` DISABLE KEYS */;
/*!40000 ALTER TABLE `post_notification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post_post`
--

DROP TABLE IF EXISTS `post_post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `post_post` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_date` datetime(6) NOT NULL,
  `modified_date` datetime(6) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `title` varchar(100) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `link` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `post_post_user_id_b9c97aef_fk_userApp_customuser_id` (`user_id`),
  CONSTRAINT `post_post_user_id_b9c97aef_fk_userApp_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `userapp_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post_post`
--

LOCK TABLES `post_post` WRITE;
/*!40000 ALTER TABLE `post_post` DISABLE KEYS */;
INSERT INTO `post_post` VALUES (2,'2023-03-10 04:34:08.796668','2023-03-10 07:29:16.150548',1,'This is first post','Hello\r\nProduct','string8',1),(3,'2023-03-10 07:09:54.739924','2023-03-20 14:13:49.751901',0,'title updated','string','string8',1),(4,'2023-03-18 10:41:22.176230','2023-03-18 10:41:22.176230',1,'string','string','string8',6),(5,'2023-03-18 10:45:07.202676','2023-03-18 10:45:07.202676',1,'string','string','string8',6),(6,'2023-03-18 10:45:30.370615','2023-03-18 10:45:30.370615',1,'stringadd','stringadsad','string8',6),(7,'2023-03-18 10:51:14.046645','2023-03-18 10:51:14.046645',1,'string','string','string8',6),(8,'2023-03-18 10:52:33.165397','2023-03-18 10:52:33.165397',1,'string','string','string8',6),(9,'2023-03-18 10:55:21.587577','2023-03-18 10:55:21.594470',1,'string','string','http://127.0.0.1:8000/posts/9',6),(10,'2023-03-18 10:56:18.734651','2023-03-20 14:29:28.367510',0,'string','string','http://127.0.0.1:8000/api/posts/10',6);
/*!40000 ALTER TABLE `post_post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post_post_tags`
--

DROP TABLE IF EXISTS `post_post_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `post_post_tags` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `post_id` bigint NOT NULL,
  `tag_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `post_post_tags_post_id_tag_id_15c628ee_uniq` (`post_id`,`tag_id`),
  KEY `post_post_tags_tag_id_cb551e85_fk_post_tag_id` (`tag_id`),
  CONSTRAINT `post_post_tags_post_id_6adf1c1b_fk_post_post_id` FOREIGN KEY (`post_id`) REFERENCES `post_post` (`id`),
  CONSTRAINT `post_post_tags_tag_id_cb551e85_fk_post_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `post_tag` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post_post_tags`
--

LOCK TABLES `post_post_tags` WRITE;
/*!40000 ALTER TABLE `post_post_tags` DISABLE KEYS */;
INSERT INTO `post_post_tags` VALUES (4,2,5),(9,3,12);
/*!40000 ALTER TABLE `post_post_tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post_tag`
--

DROP TABLE IF EXISTS `post_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `post_tag` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_date` datetime(6) NOT NULL,
  `modified_date` datetime(6) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `name` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post_tag`
--

LOCK TABLES `post_tag` WRITE;
/*!40000 ALTER TABLE `post_tag` DISABLE KEYS */;
INSERT INTO `post_tag` VALUES (1,'2023-03-08 16:03:38.087429','2023-03-08 16:03:38.087429',1,'HoTro'),(2,'2023-03-08 16:05:00.793425','2023-03-08 16:05:00.793425',1,'TuThien'),(4,'2023-03-10 07:09:25.555558','2023-03-10 07:09:25.555558',1,'Medium'),(5,'2023-03-10 07:28:57.883197','2023-03-10 07:28:57.883197',1,'Quoc te'),(6,'2023-03-16 13:43:03.837771','2023-03-16 13:43:03.837771',1,'Community'),(7,'2023-03-16 13:44:07.385239','2023-03-16 13:44:07.385239',1,'Xa hoi'),(8,'2023-03-18 05:01:30.293398','2023-03-18 05:01:30.294405',1,'Create'),(9,'2023-03-18 05:14:04.529711','2023-03-18 05:14:04.529711',1,'string'),(10,'2023-03-18 06:51:03.480018','2023-03-18 06:51:03.480018',1,'Khach Hang'),(11,'2023-03-20 13:24:01.465864','2023-03-20 13:24:01.465864',1,'updated1'),(12,'2023-03-20 14:01:00.344385','2023-03-20 14:01:00.344385',1,'updated2');
/*!40000 ALTER TABLE `post_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userapp_customuser`
--

DROP TABLE IF EXISTS `userapp_customuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userapp_customuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `avatar` varchar(100) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `phone` varchar(255) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `userApp_customuser_email_c237201e_uniq` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userapp_customuser`
--

LOCK TABLES `userapp_customuser` WRITE;
/*!40000 ALTER TABLE `userapp_customuser` DISABLE KEYS */;
INSERT INTO `userapp_customuser` VALUES (1,'pbkdf2_sha256$390000$nPaDLJtAlFR9P8uVsY6zfI$GXoaUjqzP13Zo520pwrt9u9aSP+QyuMfoFa4fvjU9sA=','2023-03-10 04:31:10.254626',1,'admin','','','admin@admin.com',1,1,'2023-03-10 04:29:07.977402','',NULL),(2,'pbkdf2_sha256$390000$Bi8qyIgoSITNlLavNMrtQb$YNl/GOHi8z0F5QTym+pGfzpC+gpOqRyDWa1QzllNhgk=',NULL,0,'mrsteve','','','mrsteve.bang@gmail.com',0,1,'2023-03-12 11:06:51.499832','',NULL),(3,'pbkdf2_sha256$390000$LT4BJCu1HMMXCcUgmaARA0$T2oeQRr9Yf13kL8VpCPdx85W7Ykdw+7nSNcaANejSVE=',NULL,0,'thanhsang','','','sang@gmail.com',0,1,'2023-03-16 14:49:56.712984','',NULL),(4,'pbkdf2_sha256$390000$vksQaIof9AfmrLbNGiXOCf$UPtrBvJv0BUCd0IkhCVao6UjkOLZeWLXfNRG9L/h4UA=',NULL,0,'thanhSen','','','sen@gmail.com',0,1,'2023-03-16 14:51:25.842292','',NULL),(5,'pbkdf2_sha256$390000$N37OREbphzSgZnDJIKFMTw$ZM5VgX24Cnv50Y6afwq7YtQa0YjyjI7R0OdrTZ3/T8o=',NULL,0,'thanhSena','','','san@gmail.com',0,1,'2023-03-16 14:51:45.454681','',NULL),(6,'pbkdf2_sha256$390000$PNgl1gnU56MBxRfjh7r3H0$e1lMuGjXUroFHn6qagjRM0Afa7MC0B4RAhClCaw0ieI=',NULL,0,'admin1','string','string','admin@example.com',0,1,'2023-03-18 05:23:37.577990','',NULL),(15,'pbkdf2_sha256$390000$5y9WKjrF5r2UsjuF4I3cqP$oli9Jazrmbvk0dU2tIKW5yGuTXQSp+44TOKNUdRTyp0=',NULL,0,'thanhsang1111','string','string','mrsang110501@gmail.com',0,1,'2023-03-25 03:08:12.414748','',NULL);
/*!40000 ALTER TABLE `userapp_customuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userapp_customuser_groups`
--

DROP TABLE IF EXISTS `userapp_customuser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userapp_customuser_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `userApp_customuser_groups_customuser_id_group_id_13af19f1_uniq` (`customuser_id`,`group_id`),
  KEY `userApp_customuser_groups_group_id_9ea84ae9_fk_auth_group_id` (`group_id`),
  CONSTRAINT `userApp_customuser_g_customuser_id_8509e990_fk_userApp_c` FOREIGN KEY (`customuser_id`) REFERENCES `userapp_customuser` (`id`),
  CONSTRAINT `userApp_customuser_groups_group_id_9ea84ae9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userapp_customuser_groups`
--

LOCK TABLES `userapp_customuser_groups` WRITE;
/*!40000 ALTER TABLE `userapp_customuser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `userapp_customuser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userapp_customuser_user_permissions`
--

DROP TABLE IF EXISTS `userapp_customuser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userapp_customuser_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `userApp_customuser_user__customuser_id_permission_adcdd779_uniq` (`customuser_id`,`permission_id`),
  KEY `userApp_customuser_u_permission_id_0d6201db_fk_auth_perm` (`permission_id`),
  CONSTRAINT `userApp_customuser_u_customuser_id_a7a40a81_fk_userApp_c` FOREIGN KEY (`customuser_id`) REFERENCES `userapp_customuser` (`id`),
  CONSTRAINT `userApp_customuser_u_permission_id_0d6201db_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userapp_customuser_user_permissions`
--

LOCK TABLES `userapp_customuser_user_permissions` WRITE;
/*!40000 ALTER TABLE `userapp_customuser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `userapp_customuser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-27 21:45:32
