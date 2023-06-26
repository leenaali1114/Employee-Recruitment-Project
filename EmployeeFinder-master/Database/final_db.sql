/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.7.9 : Database - employee_finder
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`employee_finder` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `employee_finder`;

/*Table structure for table `employee` */

DROP TABLE IF EXISTS `employee`;

CREATE TABLE `employee` (
  `employee_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `emp_name` varchar(50) DEFAULT NULL,
  `emp_email` varchar(50) DEFAULT NULL,
  `emp_details` varchar(200) DEFAULT NULL,
  `emp_phone` varchar(50) DEFAULT NULL,
  `emp_address` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `employee` */

insert  into `employee`(`employee_id`,`login_id`,`emp_name`,`emp_email`,`emp_details`,`emp_phone`,`emp_address`) values (4,10,'Baby Daniel','baby@gmail.com','Finding New Oppertunities','9656323072','assa');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `feedback` varchar(500) DEFAULT NULL,
  `reply` varchar(500) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`user_id`,`feedback`,`reply`,`date`) values (3,3,'Good Service..','Thank You','2023-03-25'),(4,5,'Good Service','Pending','2023-03-26');

/*Table structure for table `job_offer` */

DROP TABLE IF EXISTS `job_offer`;

CREATE TABLE `job_offer` (
  `job_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `skill_id` int(11) DEFAULT NULL,
  `job_title` varchar(50) DEFAULT NULL,
  `job_des` varchar(500) DEFAULT NULL,
  `job_type` varchar(50) DEFAULT NULL,
  `job_status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`job_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `job_offer` */

insert  into `job_offer`(`job_id`,`user_id`,`skill_id`,`job_title`,`job_des`,`job_type`,`job_status`) values (1,5,6,'Project Manager','Project Developemnt','Permanent','Offer Accepted');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `usertype` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(10,'baby','baby1','Employee'),(11,'bless','bless','User');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `job_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `no_days` varchar(50) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  `total_amount` varchar(50) DEFAULT NULL,
  `payment_status` varchar(50) DEFAULT NULL,
  `payment_date` date DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`job_id`,`user_id`,`no_days`,`amount`,`total_amount`,`payment_status`,`payment_date`) values (3,1,5,'30','500','15000','Paid','2023-03-27');

/*Table structure for table `rating` */

DROP TABLE IF EXISTS `rating`;

CREATE TABLE `rating` (
  `rating_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `employee_id` int(11) DEFAULT NULL,
  `rate` varchar(300) DEFAULT NULL,
  `review` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `reply` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`rating_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `rating` */

insert  into `rating`(`rating_id`,`user_id`,`employee_id`,`rate`,`review`,`date`,`reply`) values (1,5,4,'5','Good Work..Thank You For Your Services','2023-03-27','Thank You');

/*Table structure for table `reference` */

DROP TABLE IF EXISTS `reference`;

CREATE TABLE `reference` (
  `ref_id` int(11) NOT NULL AUTO_INCREMENT,
  `employee_id` int(11) DEFAULT NULL,
  `previous_company` varchar(50) DEFAULT NULL,
  `current_exp` varchar(50) DEFAULT NULL,
  `relevant_position` varchar(50) DEFAULT NULL,
  `job_location` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ref_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `reference` */

insert  into `reference`(`ref_id`,`employee_id`,`previous_company`,`current_exp`,`relevant_position`,`job_location`) values (2,4,'Techwingsys','3','Team Leader','Kochi');

/*Table structure for table `skill` */

DROP TABLE IF EXISTS `skill`;

CREATE TABLE `skill` (
  `skill_id` int(11) NOT NULL AUTO_INCREMENT,
  `employee_id` int(11) DEFAULT NULL,
  `skill_name` varchar(50) DEFAULT NULL,
  `skill_des` varchar(500) DEFAULT NULL,
  `skill_experience` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`skill_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `skill` */

insert  into `skill`(`skill_id`,`employee_id`,`skill_name`,`skill_des`,`skill_experience`) values (1,2,'Programming','Python,Java,C++','2-3Years'),(3,2,'Front End Design','HTML,CSS,JAVASCRIPT,BOOTSTRAP','2-3Years'),(4,3,'Programming','Python,Java','2-3Years'),(6,4,'Programming','Java','2-3Years');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`first_name`,`last_name`,`gender`,`address`,`phone`,`email`,`place`) values (5,11,'Blesson','Baby','Male','Modiyil\r\n\r\n                    \r\n\r\n               ','9556323072','bless@gmail.com','Kollakadavu');

/*Table structure for table `work_duration` */

DROP TABLE IF EXISTS `work_duration`;

CREATE TABLE `work_duration` (
  `work_id` int(11) NOT NULL AUTO_INCREMENT,
  `job_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `work_des` varchar(200) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `work_location` varchar(50) DEFAULT NULL,
  `work_status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`work_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `work_duration` */

insert  into `work_duration`(`work_id`,`job_id`,`user_id`,`work_des`,`start_date`,`end_date`,`work_location`,`work_status`) values (4,1,5,'as','2023-03-27','2023-03-27','Kochi','Work Accepted');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
