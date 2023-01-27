CREATE TABLE `books` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `title` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `pages` json DEFAULT NULL,
  PRIMARY KEY (`id`)
)
