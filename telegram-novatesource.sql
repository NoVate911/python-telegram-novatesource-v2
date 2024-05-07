-- --------------------------------------------------------
-- Хост:                         127.0.0.1
-- Версия сервера:               10.4.32-MariaDB - mariadb.org binary distribution
-- Операционная система:         Win64
-- HeidiSQL Версия:              12.6.0.6765
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Дамп структуры базы данных telegram-novatesource
CREATE DATABASE IF NOT EXISTS `telegram-novatesource` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci */;
USE `telegram-novatesource`;

-- Дамп структуры для таблица telegram-novatesource.channels
CREATE TABLE IF NOT EXISTS `channels` (
  `username` varchar(32) DEFAULT 'novatesource',
  `status` int(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- Экспортируемые данные не выделены.

-- Дамп структуры для таблица telegram-novatesource.logs
CREATE TABLE IF NOT EXISTS `logs` (
  `datetime` varchar(16) DEFAULT '2024-01-01 00:00',
  `action` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- Экспортируемые данные не выделены.

-- Дамп структуры для таблица telegram-novatesource.permissions
CREATE TABLE IF NOT EXISTS `permissions` (
  `tid` bigint(16) DEFAULT NULL,
  `permission` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT '{"administrator": 0}'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- Экспортируемые данные не выделены.

-- Дамп структуры для таблица telegram-novatesource.users
CREATE TABLE IF NOT EXISTS `users` (
  `tid` bigint(16) DEFAULT NULL,
  `language_code` varchar(3) DEFAULT 'ru'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- Экспортируемые данные не выделены.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
