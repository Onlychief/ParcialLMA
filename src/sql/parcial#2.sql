/*
SQLyog Ultimate v11.33 (64 bit)
MySQL - 8.0.17 : Database - parcial2
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`parcial2` /*!40100 DEFAULT CHARACTER SET latin1 */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `parcial2`;

/*Table structure for table `estudiante` */

DROP TABLE IF EXISTS `estudiante`;

CREATE TABLE `estudiante` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cc` varchar(45) DEFAULT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `apellido` varchar(45) DEFAULT NULL,
  `celular` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `semestre` int(11) DEFAULT NULL,
  `materia` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=latin1;

/*Data for the table `estudiante` */

insert  into `estudiante`(`id`,`cc`,`nombre`,`apellido`,`celular`,`email`,`semestre`,`materia`) values (41,'69006755','Janet','Diaz Rodriguez','3116238396','janet@gmail.com',7,NULL),(43,'12345567','Nicolas','Ledesma','12345','nico@gmail.com',10,NULL),(44,'1234567','Prueba2','mora','3105996767','prueba2@gmail.com',9,NULL),(45,'1088988','Nancy','Castillo','1234','nancy_ce0226@hotmail.com',8,NULL);

/*Table structure for table `materias` */

DROP TABLE IF EXISTS `materias`;

CREATE TABLE `materias` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `semester` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `materias` */

insert  into `materias`(`id`,`name`,`semester`) values (7,'Redes I','3'),(8,'Bases de Datos 2','5'),(10,'Inteligencia Artificial','7');

/*Table structure for table `materias_estudiante` */

DROP TABLE IF EXISTS `materias_estudiante`;

CREATE TABLE `materias_estudiante` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_materias` int(11) DEFAULT NULL,
  `id_estudiante` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `materias_estudiante` */

/*Table structure for table `session` */

DROP TABLE IF EXISTS `session`;

CREATE TABLE `session` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `materia` varchar(45) CHARACTER SET latin1 DEFAULT NULL,
  `fecha` varchar(45) CHARACTER SET latin1 DEFAULT NULL,
  `hora_ini` varchar(45) CHARACTER SET latin1 DEFAULT NULL,
  `hora_fin` varchar(45) CHARACTER SET latin1 DEFAULT NULL,
  `asistencia` varchar(4) CHARACTER SET latin1 DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

/*Data for the table `session` */

insert  into `session`(`id`,`materia`,`fecha`,`hora_ini`,`hora_fin`,`asistencia`) values (8,NULL,'2021-04-30','20:36','21:36',NULL),(9,NULL,NULL,NULL,NULL,NULL),(10,NULL,NULL,NULL,NULL,NULL),(11,'0','','','',NULL),(12,'0','2021-05-01','12:44','12:45',NULL),(13,'Bases de Datos 2','2021-05-01','21:09','22:10',NULL),(14,'Inteligencia Artificial','2021-05-22','21:50','22:50',NULL);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
