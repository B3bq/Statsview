-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 24, 2025 at 08:49 PM
-- Wersja serwera: 10.4.32-MariaDB
-- Wersja PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `stats`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `league`
--

CREATE TABLE `league` (
  `id` int(11) NOT NULL,
  `name` varchar(15) NOT NULL,
  `count` int(11) NOT NULL,
  `img` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `league`
--

INSERT INTO `league` (`id`, `name`, `count`, `img`) VALUES
(1, 'pl', 9, 0),
(2, 'bundesliga', 4, 0),
(3, 'la liga', 4, 0),
(4, 'lm', 3, 0);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `leagues_teams`
--

CREATE TABLE `leagues_teams` (
  `leagues_id` int(11) NOT NULL,
  `teams_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `leagues_teams`
--

INSERT INTO `leagues_teams` (`leagues_id`, `teams_id`) VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(1, 7),
(1, 10),
(1, 13),
(2, 5);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `teams`
--

CREATE TABLE `teams` (
  `id` int(11) NOT NULL,
  `name` varchar(15) NOT NULL,
  `homeCount` int(11) NOT NULL,
  `awayCount` int(11) NOT NULL,
  `img` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `teams`
--

INSERT INTO `teams` (`id`, `name`, `homeCount`, `awayCount`, `img`) VALUES
(1, 'palace', 4, 0, 0x20),
(2, 'chelsea', 2, 4, 0x20),
(3, 'wolves', 0, 3, 0x20),
(4, 'juve', 4, 0, 0x20),
(5, 'real', 5, 0, 0x20),
(6, 'braca', 0, 1, 0x20),
(7, 'bvb', 2, 0, 0x20),
(8, 'bayer', 0, 1, 0x20),
(9, 'bayern', 0, 1, 0x20),
(10, 'atleti', 3, 1, 0x20),
(11, 'betis', 0, 2, 0x20),
(12, 'milan', 0, 2, 0x20),
(13, 'bochum', 0, 1, 0x20);

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `league`
--
ALTER TABLE `league`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `leagues_teams`
--
ALTER TABLE `leagues_teams`
  ADD PRIMARY KEY (`leagues_id`,`teams_id`),
  ADD KEY `teams_id` (`teams_id`);

--
-- Indeksy dla tabeli `teams`
--
ALTER TABLE `teams`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `league`
--
ALTER TABLE `league`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `teams`
--
ALTER TABLE `teams`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `leagues_teams`
--
ALTER TABLE `leagues_teams`
  ADD CONSTRAINT `leagues_teams_ibfk_1` FOREIGN KEY (`leagues_id`) REFERENCES `league` (`id`),
  ADD CONSTRAINT `leagues_teams_ibfk_2` FOREIGN KEY (`teams_id`) REFERENCES `teams` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
