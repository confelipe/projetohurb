CREATE USER 'product'@'%' IDENTIFIED BY 'product';
GRANT ALL PRIVILEGES ON *.* TO 'product'@'%';
FLUSH PRIVILEGES;

CREATE DATABASE hurb_test_assignment;
USE hurb_test_assignment

DROP TABLE IF EXISTS `product`;
CREATE TABLE `product` (
  `product_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(32) NOT NULL,
  `sku` varchar(32) NOT NULL,
  `description` varchar(1024) DEFAULT NULL,
  `price` decimal(12,2) NOT NULL DEFAULT '0.00',
  `created` datetime NOT NULL,
  `last_updated` datetime DEFAULT NULL,
  PRIMARY KEY (`product_id`),
  UNIQUE KEY `sku` (`sku`),
  KEY `created` (`created`),
  KEY `last_updated` (`last_updated`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;

LOCK TABLES `product` WRITE;
INSERT INTO `product` VALUES (7,'Awesome Socks','SCK-4513','Varias coisas sobre o item.....',89.99,'2021-05-30 22:56:33','2021-05-31 16:40:04'),(8,'Awesome Socks','SCK-4514',NULL,89.99,'2021-05-30 23:27:31','2021-05-30 23:27:31'),(9,'Awesome Socks','SCK-4515',NULL,89.99,'2021-05-30 23:28:35','2021-05-30 23:28:35'),(10,'Awesome Socks','SCK-4516',NULL,89.99,'2021-05-30 23:29:41','2021-05-30 23:29:41'),(11,'Meias cinzas','SCK-5517','Um par de meias cinza',99.99,'2021-05-30 23:31:43','2021-05-31 16:48:02'),(12,'Awesome Socks','SCK-4518',NULL,89.99,'2021-05-30 23:38:21','2021-05-30 23:38:21'),(13,'Awesome Socks','SCK-4519',NULL,89.99,'2021-05-30 23:39:10','2021-05-30 23:39:10'),(14,'Awesome Socks','SCK-4520',NULL,89.99,'2021-05-30 23:39:40','2021-05-30 23:39:40'),(15,'Awesome Socks','SCK-4521',NULL,89.99,'2021-05-30 23:40:12','2021-05-30 23:40:12'),(16,'Awesome Socks','SCK-4522',NULL,89.99,'2021-05-30 23:43:34','2021-05-30 23:43:34'),(17,'Awesome Socks','SCK-4523',NULL,89.99,'2021-05-30 23:44:38','2021-05-30 23:44:38'),(19,'Awesome Socks','SCK-4525',NULL,89.99,'2021-05-31 00:01:22','2021-05-31 00:01:22'),(20,'Awesome Socks','SCK-4526',NULL,89.99,'2021-05-31 00:02:22','2021-05-31 00:02:22'),(21,'Awesome Socks','SCK-4527',NULL,89.99,'2021-05-31 00:07:50','2021-05-31 00:07:50'),(24,'Awesome Socks','SCK-4532','Varias coisas sobre o item.....',89.99,'2021-05-31 01:18:02','2021-05-31 16:25:49'),(25,'Awesome Socks','SCK-4533','Varias coisas sobre o item.....',89.99,'2021-05-31 15:31:02','2021-05-31 15:31:02'),(26,'Awesome Socks','SCK-4517','Varias coisas sobre o item.....',89.99,'2021-06-04 04:23:33','2021-06-04 04:23:33');
UNLOCK TABLES;

DROP TABLE IF EXISTS `product_attribute`;
CREATE TABLE `product_attribute` (
  `product_id` int(10) unsigned NOT NULL,
  `name` varchar(16) NOT NULL,
  `value` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `product_attribute` WRITE;
INSERT INTO `product_attribute` VALUES (24,'color','red'),(24,'size','39-41'),(7,'color','blue'),(7,'size','39-43'),(11,'color','gray'),(11,'size','31-37'),(26,'color','red'),(26,'size','37-42');
UNLOCK TABLES;

DROP TABLE IF EXISTS `product_barcode`;
CREATE TABLE `product_barcode` (
  `product_id` int(10) unsigned NOT NULL,
  `barcode` varchar(32) NOT NULL,
  PRIMARY KEY (`product_id`),
  UNIQUE KEY `barcode` (`barcode`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `product_barcode` WRITE;
INSERT INTO `product_barcode` VALUES (19,'7410852096308'),(21,'7410852096310'),(24,'7410852096320'),(7,'7410852096321'),(26,'7410852096327'),(11,'7410852096330');
UNLOCK TABLES;