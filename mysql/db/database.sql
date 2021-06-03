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
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `product_attribute`;
CREATE TABLE `product_attribute` (
  `product_id` int(10) unsigned NOT NULL,
  `name` varchar(16) NOT NULL,
  `value` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `product_barcode`;
CREATE TABLE `product_barcode` (
  `product_id` int(10) unsigned NOT NULL,
  `barcode` varchar(32) NOT NULL,
  PRIMARY KEY (`product_id`),
  UNIQUE KEY `barcode` (`barcode`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;