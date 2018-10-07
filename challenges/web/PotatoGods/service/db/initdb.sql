CREATE DATABASE  IF NOT EXISTS `potatodb` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `potatodb`;
-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: gctfstuff
-- ------------------------------------------------------
-- Server version	5.7.21-log

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
-- Table structure for table `flaggyflagflagnotgonnaspotthis`
--

DROP TABLE IF EXISTS `flaggyflagflagnotgonnaspotthis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `flaggyflagflagnotgonnaspotthis` (
  `flagid` varchar(50) NOT NULL,
  `flag` varchar(80) DEFAULT NULL,
  `troll` varchar(45) DEFAULT 'you can''t select all now haha',
  PRIMARY KEY (`flagid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flaggyflagflagnotgonnaspotthis`
--

LOCK TABLES `flaggyflagflagnotgonnaspotthis` WRITE;
/*!40000 ALTER TABLE `flaggyflagflagnotgonnaspotthis` DISABLE KEYS */;
INSERT INTO `flaggyflagflagnotgonnaspotthis` VALUES ('1','GCTF{N0T_Flag','make this so you can\'t describe'),('2','GCTF}f1ag_1sh3r3}','make this so you can\'t describe'),('3','GCTF{SQ1_15_5uP3R_53cUR3}','make this so you can\'t describe');
/*!40000 ALTER TABLE `flaggyflagflagnotgonnaspotthis` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `potatos`
--

DROP TABLE IF EXISTS `potatos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `potatos` (
  `potato` varchar(100) NOT NULL,
  `potatoimage` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`potato`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `potatos`
--

LOCK TABLES `potatos` WRITE;
/*!40000 ALTER TABLE `potatos` DISABLE KEYS */;
INSERT INTO `potatos` VALUES ('Adirondack Blue','adirondackblue.jpg'),('Adirondack Red','adirondackred.jpg'),('Carola','carola.jpg'),('Desiree Potato','desireepotato.jpg'),('Dutch Cream','dutchcream.jpg'),('Fingerling','fingerling.jpg'),('Idaho Russet','idahorusset.jpg'),('Inca Gold','incagold.jpg'),('Katahdin','katahdin.jpg'),('Purple Peru','purpleperu.jpg'),('Purple Viking','purpleviking.jpg'),('Ratte Potato','rattepotato.jpg'),('Rose Gold','rosegold.jpg'),('Royal Blue','royalblue.jpg'),('Russet Burbank','russetburbank.jpg'),('Sweet Potato','sweetpotato.jpg'),('White Potato','whitepotato.jpg'),('Yukon Gold','yukon.jpg');
/*!40000 ALTER TABLE `potatos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test`
--

DROP TABLE IF EXISTS `test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `test` (
  `sa` int(11) NOT NULL,
  PRIMARY KEY (`sa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test`
--

LOCK TABLES `test` WRITE;
/*!40000 ALTER TABLE `test` DISABLE KEYS */;
/*!40000 ALTER TABLE `test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `username`
--

DROP TABLE IF EXISTS `username`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `username` (
  `username` varchar(50) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `username`
--

LOCK TABLES `username` WRITE;
/*!40000 ALTER TABLE `username` DISABLE KEYS */;
INSERT INTO `username` VALUES ('!mpor+an+'),('1010realuser'),('1eg!+'),('griffith'),('gryph0n5-dism'),('h3r3'),('n0th!ng'),('p1ngp0ng'),('wh0@m1');
/*!40000 ALTER TABLE `username` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-06 22:09:14

CREATE USER 'gctfuser' IDENTIFIED BY 'gctf2018supersecurepassw0rd';
GRANT SELECT ON potatodb.* TO 'gctfuser'@'%';
FLUSH PRIVILEGES;
