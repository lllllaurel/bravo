-- MySQL dump 10.13  Distrib 5.7.25, for macos10.14 (x86_64)
--
-- Host: localhost    Database: admin
-- ------------------------------------------------------
-- Server version	5.7.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `automata.bu_overview`
--

DROP TABLE IF EXISTS `automata.bu_overview`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `automata.bu_overview` (
  `id` int(4) NOT NULL AUTO_INCREMENT,
  `appid` varchar(100) NOT NULL,
  `user_num` int(4) NOT NULL,
  `visit_num` int(4) NOT NULL,
  `ds` varchar(50) NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `automata.bu_overview`
--

LOCK TABLES `automata.bu_overview` WRITE;
/*!40000 ALTER TABLE `automata.bu_overview` DISABLE KEYS */;
INSERT INTO `automata.bu_overview` VALUES (1,'automata',9,12,'20200202','2020-02-08 14:33:01'),(2,'automata',19,22,'20200203','2020-02-08 14:33:01'),(3,'automata',29,32,'20200204','2020-02-08 14:33:01'),(4,'automata',39,52,'20200205','2020-02-08 14:33:01'),(5,'automata',59,72,'20200206','2020-02-08 14:33:01'),(6,'automata',69,92,'20200207','2020-02-08 14:33:01'),(7,'automata',79,102,'20200208','2020-02-08 14:33:01'),(8,'automata',6,102,'20200201','2020-02-08 14:33:01');
/*!40000 ALTER TABLE `automata.bu_overview` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `automata.bu_testtb1`
--

DROP TABLE IF EXISTS `automata.bu_testtb1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `automata.bu_testtb1` (
  `id` int(4) NOT NULL AUTO_INCREMENT,
  `appid` varchar(100) NOT NULL,
  `budata1` varchar(50) NOT NULL,
  `budata2` varchar(50) NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `automata.bu_testtb1`
--

LOCK TABLES `automata.bu_testtb1` WRITE;
/*!40000 ALTER TABLE `automata.bu_testtb1` DISABLE KEYS */;
INSERT INTO `automata.bu_testtb1` VALUES (1,'automata','super_k.tb1_test','测试1data','2020-02-08 10:34:26'),(2,'automata','super_k.tb2_test','测试2data','2020-02-08 10:34:26');
/*!40000 ALTER TABLE `automata.bu_testtb1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `automata.bu_testtb2`
--

DROP TABLE IF EXISTS `automata.bu_testtb2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `automata.bu_testtb2` (
  `id` int(4) NOT NULL AUTO_INCREMENT,
  `appid` varchar(100) NOT NULL,
  `budata1` varchar(50) NOT NULL,
  `budata2` varchar(50) NOT NULL,
  `budata3` varchar(50) NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `automata.bu_testtb2`
--

LOCK TABLES `automata.bu_testtb2` WRITE;
/*!40000 ALTER TABLE `automata.bu_testtb2` DISABLE KEYS */;
INSERT INTO `automata.bu_testtb2` VALUES (1,'automata','测试1data','测试2data','测试3data','2020-02-08 10:36:49'),(2,'automata','测试1.1data','测试2.2data','测试2.2data','2020-02-08 10:36:49'),(3,'automata','测试3data','测试2data','测试3data','2020-02-08 14:33:01'),(4,'automata','测试4.1data','测试2.2data','测试2.2data','2020-02-08 14:33:01');
/*!40000 ALTER TABLE `automata.bu_testtb2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `uu_admin`
--

DROP TABLE IF EXISTS `uu_admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `uu_admin` (
  `id` int(4) NOT NULL AUTO_INCREMENT,
  `appid` varchar(50) NOT NULL,
  `uuid` varchar(20) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `last_login` varchar(20) DEFAULT NULL,
  `super_user` int(2) DEFAULT '0',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `password` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `uu_admin`
--

LOCK TABLES `uu_admin` WRITE;
/*!40000 ALTER TABLE `uu_admin` DISABLE KEYS */;
INSERT INTO `uu_admin` VALUES (5,'oasis','1581166809.2778','sdk','13555550000',NULL,0,'2020-02-08 21:00:34',NULL),(14,'oasis1','1581168607.728225','sdk','13555550000',NULL,0,'2020-02-08 21:30:07',NULL),(15,'oasis2','1581168691.389872','sdk','13555550000',NULL,0,'2020-02-08 21:31:31',NULL),(16,'oasis3','1581168710.052323','sdk','13555550000',NULL,0,'2020-02-08 21:31:50',NULL),(17,'sfsf','1581220631.264777','jdbc','13222222222',NULL,0,'2020-02-09 11:57:11','c0p5r3y5v6'),(18,'asdf','1581221607.2888598','antik','13232323232',NULL,0,'2020-02-09 12:13:27','e1k7n5b6b5'),(19,'tmodel','1581221780.1642308','antik1','13332323232',NULL,0,'2020-02-09 12:16:20','o3o2i0z3n9'),(20,'tmodel1','1581221802.0353951','antik1','13332323232',NULL,0,'2020-02-09 12:16:42','abcdef'),(21,'flask','1581222134.048165','flask','134535352323',NULL,1,'2020-02-09 12:22:14','asdfjk');
/*!40000 ALTER TABLE `uu_admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `uu_tables`
--

DROP TABLE IF EXISTS `uu_tables`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `uu_tables` (
  `id` int(4) NOT NULL AUTO_INCREMENT,
  `appid` varchar(100) NOT NULL,
  `tablename` varchar(50) NOT NULL,
  `tablecomment` varchar(50) NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `uu_tables`
--

LOCK TABLES `uu_tables` WRITE;
/*!40000 ALTER TABLE `uu_tables` DISABLE KEYS */;
INSERT INTO `uu_tables` VALUES (1,'automata','automata.bu_testtb1','测试1表','2020-02-07 13:08:59'),(2,'automata','automata.bu_testtb2','测试2表','2020-02-07 13:08:59');
/*!40000 ALTER TABLE `uu_tables` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-02-10 12:36:06
