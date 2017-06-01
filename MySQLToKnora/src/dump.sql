# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.17)
# Database: tinyTest
# Generation Time: 2017-03-29 10:13:11 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table doctor
# ------------------------------------------------------------

DROP TABLE IF EXISTS `doctor`;

CREATE TABLE `doctor` (
  `id` int(11) DEFAULT NULL,
  `patient_id` int(11) DEFAULT NULL,
  `address` varchar(200) NOT NULL DEFAULT '',
  `name` varchar(50) DEFAULT NULL,
  KEY `par_ind` (`patient_id`),
  CONSTRAINT `fk_customer` FOREIGN KEY (`patient_id`) REFERENCES `person` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `doctor` WRITE;
/*!40000 ALTER TABLE `doctor` DISABLE KEYS */;

INSERT INTO `doctor` (`id`, `patient_id`, `address`, `name`)
VALUES
	(1,1,'GoodStreet 1','Dr. Oetker'),
	(2,2,'BadStreet 2','Dr. Schiwago'),
	(3,3,'Sunny Street 3','Dr. No'),
	(4,2,'Shady Street 4','Dr. Dre'),
	(5,1,'Windy Street','Dr. Who'),
	(6,3,'Wallstreet','Dr. Mabuse');

/*!40000 ALTER TABLE `doctor` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table person
# ------------------------------------------------------------

DROP TABLE IF EXISTS `person`;

CREATE TABLE `person` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;

INSERT INTO `person` (`id`, `name`)
VALUES
	(1,'Klaus'),
	(2,'Peter'),
	(3,'Ulrike');

/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
