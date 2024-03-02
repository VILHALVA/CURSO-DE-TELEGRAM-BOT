SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE DATABASE IF NOT EXISTS `upload` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `upload`;

CREATE TABLE `media` (
  `id` int(11) NOT NULL,
  `filename` varchar(255) NOT NULL,
  `directory` varchar(255) NOT NULL,
  `file_ext` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `media` (`id`, `filename`, `directory`, `file_ext`) VALUES
(1, 'photo_20240302144739.jpg', './MIDIAS', 'jpg');

ALTER TABLE `media`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `media`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

