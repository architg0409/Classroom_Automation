-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 08, 2018 at 05:14 PM
-- Server version: 5.7.22-log
-- PHP Version: 5.6.35

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `timeslotsdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `time`
--

DROP TABLE IF EXISTS `time`;
CREATE TABLE IF NOT EXISTS `time` (
  `SNo.` int(5) NOT NULL,
  `timeslot` time NOT NULL,
  `Monday` int(1) NOT NULL,
  `Tuesday` int(1) NOT NULL,
  `Wednesday` int(1) NOT NULL,
  `Thursday` int(1) NOT NULL,
  `Friday` int(1) NOT NULL,
  `Saturday` int(1) NOT NULL,
  PRIMARY KEY (`SNo.`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `time`
--

INSERT INTO `time` (`SNo.`, `timeslot`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`) VALUES
(1, '10:00:00', 1, 1, 1, 1, 1, 1),
(2, '10:01:00', 0, 1, 0, 1, 1, 0),
(3, '10:02:00', 1, 1, 1, 1, 1, 1),
(4, '10:03:00', 0, 1, 0, 1, 1, 0),
(5, '10:04:00', 1, 0, 1, 0, 0, 0),
(6, '10:05:00', 1, 1, 0, 1, 0, 1),
(7, '10:06:00', 0, 1, 1, 0, 1, 0),
(8, '10:07:00', 1, 1, 1, 1, 1, 1),
(9, '10:08:00', 0, 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `time1`
--

DROP TABLE IF EXISTS `time1`;
CREATE TABLE IF NOT EXISTS `time1` (
  `SNo.` int(5) NOT NULL,
  `timeslot` time NOT NULL,
  `Monday` int(1) NOT NULL,
  `Tuesday` int(1) NOT NULL,
  `Wednesday` int(1) NOT NULL,
  `Thursday` int(1) NOT NULL,
  `Friday` int(1) NOT NULL,
  `Saturday` int(1) NOT NULL,
  PRIMARY KEY (`SNo.`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `time1`
--

INSERT INTO `time1` (`SNo.`, `timeslot`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`) VALUES
(1, '10:10:00', 1, 1, 1, 1, 1, 1),
(2, '10:11:00', 0, 1, 0, 1, 1, 0),
(3, '10:12:00', 1, 1, 1, 1, 1, 1),
(4, '10:13:00', 0, 1, 0, 1, 1, 0),
(5, '10:14:00', 1, 0, 1, 0, 0, 0),
(6, '10:15:00', 1, 1, 0, 1, 0, 1),
(7, '10:16:00', 0, 1, 1, 0, 1, 0),
(8, '10:17:00', 1, 1, 1, 1, 1, 1),
(9, '10:18:00', 0, 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `time2`
--

DROP TABLE IF EXISTS `time2`;
CREATE TABLE IF NOT EXISTS `time2` (
  `SNo.` int(5) NOT NULL,
  `timeslot` time NOT NULL,
  `Monday` int(1) NOT NULL,
  `Tuesday` int(1) NOT NULL,
  `Wednesday` int(1) NOT NULL,
  `Thursday` int(1) NOT NULL,
  `Friday` int(1) NOT NULL,
  `Saturday` int(1) NOT NULL,
  PRIMARY KEY (`SNo.`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `time2`
--

INSERT INTO `time2` (`SNo.`, `timeslot`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`) VALUES
(1, '10:20:00', 1, 1, 1, 1, 1, 1),
(2, '10:21:00', 0, 1, 1, 1, 1, 0),
(3, '10:22:00', 1, 1, 1, 1, 1, 1),
(4, '10:23:00', 0, 1, 1, 1, 1, 0),
(5, '10:24:00', 1, 0, 0, 0, 0, 0),
(6, '10:25:00', 1, 1, 0, 1, 0, 1),
(7, '10:26:00', 0, 1, 1, 0, 1, 0),
(8, '10:27:00', 1, 1, 1, 1, 1, 1),
(9, '10:28:00', 0, 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `time3`
--

DROP TABLE IF EXISTS `time3`;
CREATE TABLE IF NOT EXISTS `time3` (
  `SNo.` int(5) NOT NULL,
  `timeslot` time NOT NULL,
  `Monday` int(1) NOT NULL,
  `Tuesday` int(1) NOT NULL,
  `Wednesday` int(1) NOT NULL,
  `Thursday` int(1) NOT NULL,
  `Friday` int(1) NOT NULL,
  `Saturday` int(1) NOT NULL,
  PRIMARY KEY (`SNo.`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `time3`
--

INSERT INTO `time3` (`SNo.`, `timeslot`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`) VALUES
(1, '09:30:00', 1, 1, 1, 1, 1, 1),
(2, '09:31:00', 0, 1, 1, 1, 1, 0),
(3, '09:32:00', 1, 1, 1, 1, 1, 1),
(4, '09:33:00', 0, 1, 1, 1, 1, 0),
(5, '09:34:00', 1, 0, 0, 0, 0, 0),
(6, '09:35:00', 1, 1, 0, 1, 0, 1),
(7, '09:36:00', 0, 1, 1, 0, 1, 0),
(8, '09:37:00', 1, 1, 1, 1, 1, 1),
(9, '09:38:00', 0, 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `time4`
--

DROP TABLE IF EXISTS `time4`;
CREATE TABLE IF NOT EXISTS `time4` (
  `SNo.` int(5) NOT NULL,
  `timeslot` time NOT NULL,
  `Monday` int(1) NOT NULL,
  `Tuesday` int(1) NOT NULL,
  `Wednesday` int(1) NOT NULL,
  `Thursday` int(1) NOT NULL,
  `Friday` int(1) NOT NULL,
  `Saturday` int(1) NOT NULL,
  PRIMARY KEY (`SNo.`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `time4`
--

INSERT INTO `time4` (`SNo.`, `timeslot`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`) VALUES
(1, '09:40:00', 1, 1, 1, 1, 1, 1),
(2, '09:41:00', 0, 1, 1, 1, 1, 0),
(3, '09:42:00', 1, 1, 1, 1, 1, 1),
(4, '09:43:00', 0, 1, 1, 1, 1, 0),
(5, '09:44:00', 1, 0, 0, 0, 0, 0),
(6, '09:45:00', 1, 1, 0, 1, 0, 1),
(7, '09:46:00', 0, 1, 1, 0, 1, 0),
(8, '09:47:00', 1, 1, 1, 1, 1, 1),
(9, '09:48:00', 0, 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `time5`
--

DROP TABLE IF EXISTS `time5`;
CREATE TABLE IF NOT EXISTS `time5` (
  `SNo.` int(5) NOT NULL,
  `timeslot` time NOT NULL,
  `Monday` int(1) NOT NULL,
  `Tuesday` int(1) NOT NULL,
  `Wednesday` int(1) NOT NULL,
  `Thursday` int(1) NOT NULL,
  `Friday` int(1) NOT NULL,
  `Saturday` int(1) NOT NULL,
  PRIMARY KEY (`SNo.`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `time5`
--

INSERT INTO `time5` (`SNo.`, `timeslot`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`) VALUES
(1, '09:50:00', 1, 1, 1, 1, 1, 1),
(2, '09:51:00', 0, 1, 1, 1, 1, 0),
(3, '09:52:00', 1, 1, 1, 1, 1, 1),
(4, '09:53:00', 0, 1, 1, 1, 1, 0),
(5, '09:54:00', 1, 0, 0, 0, 0, 0),
(6, '09:55:00', 1, 1, 0, 1, 0, 1),
(7, '09:56:00', 0, 1, 1, 0, 1, 0),
(8, '09:57:00', 1, 1, 1, 1, 1, 1),
(9, '09:58:00', 0, 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `timetable`
--

DROP TABLE IF EXISTS `timetable`;
CREATE TABLE IF NOT EXISTS `timetable` (
  `SNo.` int(5) NOT NULL,
  `timeslot` time NOT NULL,
  `Monday` int(1) NOT NULL,
  `Tuesday` int(1) NOT NULL,
  `Wednesday` int(1) NOT NULL,
  `Thursday` int(1) NOT NULL,
  `Friday` int(1) NOT NULL,
  `Saturday` int(1) NOT NULL,
  PRIMARY KEY (`timeslot`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `timetable`
--

INSERT INTO `timetable` (`SNo.`, `timeslot`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`) VALUES
(1, '08:00:00', 1, 1, 1, 1, 1, 1),
(2, '09:00:00', 1, 1, 1, 1, 1, 1),
(3, '10:00:00', 1, 1, 1, 1, 1, 1),
(4, '11:00:00', 1, 1, 1, 1, 1, 1),
(5, '12:00:00', 0, 0, 0, 0, 0, 0),
(6, '13:00:00', 1, 1, 0, 1, 0, 1),
(7, '14:00:00', 1, 1, 1, 0, 1, 1),
(8, '15:00:00', 1, 1, 1, 1, 1, 1),
(9, '16:05:00', 0, 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `UserID` int(11) NOT NULL,
  `UserName` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL,
  PRIMARY KEY (`UserID`),
  UNIQUE KEY `UserName` (`UserName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`UserID`, `UserName`, `Password`) VALUES
(1, 'Ayush01', 'Ayush');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
