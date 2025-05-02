-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 23, 2025 at 04:35 PM
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
-- Database: `statsview`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `basketball_broker`
--

CREATE TABLE `basketball_broker` (
  `id_league` int(11) NOT NULL,
  `id_teams` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `basketball_leagues`
--

CREATE TABLE `basketball_leagues` (
  `id` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `count` int(11) NOT NULL,
  `img` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `basketball_teams`
--

CREATE TABLE `basketball_teams` (
  `id` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `homeCount` int(11) NOT NULL,
  `awayCount` int(11) NOT NULL,
  `img` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `cs_broker`
--

CREATE TABLE `cs_broker` (
  `id_league` int(11) NOT NULL,
  `id_teams` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `cs_leagues`
--

CREATE TABLE `cs_leagues` (
  `id` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `count` int(11) NOT NULL,
  `img` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `cs_teams`
--

CREATE TABLE `cs_teams` (
  `id` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `homeCount` int(11) NOT NULL,
  `awayCount` int(11) NOT NULL,
  `img` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `football_broker`
--

CREATE TABLE `football_broker` (
  `id_league` int(11) NOT NULL,
  `id_teams` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `football_leagues`
--

CREATE TABLE `football_leagues` (
  `id` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `count` int(11) NOT NULL,
  `img` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `football_teams`
--

CREATE TABLE `football_teams` (
  `id` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `homeCount` int(11) NOT NULL,
  `awayCount` int(11) NOT NULL,
  `img` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `lol_broker`
--

CREATE TABLE `lol_broker` (
  `id_league` int(11) NOT NULL,
  `id_teams` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `lol_leagues`
--

CREATE TABLE `lol_leagues` (
  `id` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `count` int(11) NOT NULL,
  `img` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `lol_teams`
--

CREATE TABLE `lol_teams` (
  `id` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `homeCount` int(11) NOT NULL,
  `awayCount` int(11) NOT NULL,
  `img` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `login` varchar(15) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `basketball_broker`
--
ALTER TABLE `basketball_broker`
  ADD PRIMARY KEY (`id_league`,`id_teams`),
  ADD KEY `fk_bteam` (`id_teams`);

--
-- Indeksy dla tabeli `basketball_leagues`
--
ALTER TABLE `basketball_leagues`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_basketl_user` (`id_user`);

--
-- Indeksy dla tabeli `basketball_teams`
--
ALTER TABLE `basketball_teams`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_baskett_user` (`id_user`);

--
-- Indeksy dla tabeli `cs_broker`
--
ALTER TABLE `cs_broker`
  ADD PRIMARY KEY (`id_teams`,`id_league`),
  ADD KEY `fk_league_cs` (`id_league`);

--
-- Indeksy dla tabeli `cs_leagues`
--
ALTER TABLE `cs_leagues`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_csleague_user` (`id_user`);

--
-- Indeksy dla tabeli `cs_teams`
--
ALTER TABLE `cs_teams`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_csteam_user` (`id_user`);

--
-- Indeksy dla tabeli `football_broker`
--
ALTER TABLE `football_broker`
  ADD PRIMARY KEY (`id_teams`),
  ADD KEY `fk_footabll_league` (`id_league`);

--
-- Indeksy dla tabeli `football_leagues`
--
ALTER TABLE `football_leagues`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_footabll_user` (`id_user`);

--
-- Indeksy dla tabeli `football_teams`
--
ALTER TABLE `football_teams`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_footabllt_user` (`id_user`);

--
-- Indeksy dla tabeli `lol_broker`
--
ALTER TABLE `lol_broker`
  ADD PRIMARY KEY (`id_league`,`id_teams`),
  ADD KEY `fk_team_lol` (`id_teams`);

--
-- Indeksy dla tabeli `lol_leagues`
--
ALTER TABLE `lol_leagues`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_lolleague_user` (`id_user`);

--
-- Indeksy dla tabeli `lol_teams`
--
ALTER TABLE `lol_teams`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_lolteam_user` (`id_user`);

--
-- Indeksy dla tabeli `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `basketball_leagues`
--
ALTER TABLE `basketball_leagues`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `basketball_teams`
--
ALTER TABLE `basketball_teams`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cs_leagues`
--
ALTER TABLE `cs_leagues`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cs_teams`
--
ALTER TABLE `cs_teams`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `football_leagues`
--
ALTER TABLE `football_leagues`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `football_teams`
--
ALTER TABLE `football_teams`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `lol_leagues`
--
ALTER TABLE `lol_leagues`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `lol_teams`
--
ALTER TABLE `lol_teams`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `basketball_broker`
--
ALTER TABLE `basketball_broker`
  ADD CONSTRAINT `fk_bleague` FOREIGN KEY (`id_league`) REFERENCES `basketball_leagues` (`id`),
  ADD CONSTRAINT `fk_bteam` FOREIGN KEY (`id_teams`) REFERENCES `basketball_teams` (`id`);

--
-- Constraints for table `basketball_leagues`
--
ALTER TABLE `basketball_leagues`
  ADD CONSTRAINT `fk_basketl_user` FOREIGN KEY (`id_user`) REFERENCES `users` (`id`);

--
-- Constraints for table `basketball_teams`
--
ALTER TABLE `basketball_teams`
  ADD CONSTRAINT `fk_baskett_user` FOREIGN KEY (`id_user`) REFERENCES `users` (`id`);

--
-- Constraints for table `cs_broker`
--
ALTER TABLE `cs_broker`
  ADD CONSTRAINT `fk_league_cs` FOREIGN KEY (`id_league`) REFERENCES `cs_leagues` (`id`),
  ADD CONSTRAINT `fk_team_cs` FOREIGN KEY (`id_teams`) REFERENCES `cs_teams` (`id`);

--
-- Constraints for table `cs_leagues`
--
ALTER TABLE `cs_leagues`
  ADD CONSTRAINT `fk_csleague_user` FOREIGN KEY (`id_user`) REFERENCES `users` (`id`);

--
-- Constraints for table `cs_teams`
--
ALTER TABLE `cs_teams`
  ADD CONSTRAINT `fk_csteam_user` FOREIGN KEY (`id_user`) REFERENCES `users` (`id`);

--
-- Constraints for table `football_broker`
--
ALTER TABLE `football_broker`
  ADD CONSTRAINT `fk_footabll_league` FOREIGN KEY (`id_league`) REFERENCES `football_leagues` (`id`),
  ADD CONSTRAINT `fk_footabll_team` FOREIGN KEY (`id_teams`) REFERENCES `football_teams` (`id`);

--
-- Constraints for table `football_leagues`
--
ALTER TABLE `football_leagues`
  ADD CONSTRAINT `fk_footabll_user` FOREIGN KEY (`id_user`) REFERENCES `users` (`id`);

--
-- Constraints for table `football_teams`
--
ALTER TABLE `football_teams`
  ADD CONSTRAINT `fk_footabllt_user` FOREIGN KEY (`id_user`) REFERENCES `users` (`id`);

--
-- Constraints for table `lol_broker`
--
ALTER TABLE `lol_broker`
  ADD CONSTRAINT `fk_league_lol` FOREIGN KEY (`id_league`) REFERENCES `lol_leagues` (`id`),
  ADD CONSTRAINT `fk_team_lol` FOREIGN KEY (`id_teams`) REFERENCES `lol_teams` (`id`);

--
-- Constraints for table `lol_leagues`
--
ALTER TABLE `lol_leagues`
  ADD CONSTRAINT `fk_lolleague_user` FOREIGN KEY (`id_user`) REFERENCES `users` (`id`);

--
-- Constraints for table `lol_teams`
--
ALTER TABLE `lol_teams`
  ADD CONSTRAINT `fk_lolteam_user` FOREIGN KEY (`id_user`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
