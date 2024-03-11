/*
SQLyog Enterprise - MySQL GUI v6.56
MySQL - 5.5.5-10.1.13-MariaDB : Database - dermatology
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`dermatology` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `dermatology`;

/*Table structure for table `appointment` */

DROP TABLE IF EXISTS `appointment`;

CREATE TABLE `appointment` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `pname` varchar(100) DEFAULT NULL,
  `pemail` varchar(100) DEFAULT NULL,
  `age` varchar(100) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `bmi` varchar(100) DEFAULT NULL,
  `infection` varchar(100) DEFAULT NULL,
  `smoking` varchar(100) DEFAULT NULL,
  `days` varchar(100) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `disease` varchar(100) DEFAULT NULL,
  `severity` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  `hname` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `dname` varchar(100) DEFAULT NULL,
  `demail` varchar(100) DEFAULT NULL,
  `accepted_date` varchar(100) DEFAULT 'Not updated',
  `status` varchar(100) DEFAULT 'pending',
  `feedback` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Table structure for table `chatting` */

DROP TABLE IF EXISTS `chatting`;

CREATE TABLE `chatting` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `sender_email` varchar(100) DEFAULT NULL,
  `receiver_email` varchar(100) DEFAULT NULL,
  `chat_date` varchar(100) DEFAULT NULL,
  `chat_time` varchar(100) DEFAULT NULL,
  `msg` varchar(100) DEFAULT NULL,
  `patient_name` varchar(100) DEFAULT NULL,
  `patient_email` varchar(100) DEFAULT NULL,
  `doctor_email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Table structure for table `disease_info` */

DROP TABLE IF EXISTS `disease_info`;

CREATE TABLE `disease_info` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `pname` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `age` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `smoking` varchar(100) DEFAULT NULL,
  `days` varchar(100) DEFAULT NULL,
  `infection` varchar(100) DEFAULT NULL,
  `bmi` varchar(100) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `disease` varchar(100) DEFAULT NULL,
  `severity` varchar(100) DEFAULT NULL,
  `causes` text,
  `remedies` text,
  `date` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Table structure for table `doctor` */

DROP TABLE IF EXISTS `doctor`;

CREATE TABLE `doctor` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Password` varchar(100) DEFAULT NULL,
  `age` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `hospital_name` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `exp_type` varchar(100) DEFAULT NULL,
  `mobile` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `user_Name` varchar(100) DEFAULT NULL,
  `user_Email` varchar(100) DEFAULT NULL,
  `Password` varchar(100) DEFAULT NULL,
  `user_Phone` varchar(100) DEFAULT NULL,
  `user_Addr` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
