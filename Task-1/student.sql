-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 19, 2021 at 03:22 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `practise`
--

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `NAME` varchar(20) DEFAULT NULL,
  `ID` int(11) NOT NULL,
  `COLLEGE` varchar(20) DEFAULT NULL,
  `DEPARTMENT` varchar(20) DEFAULT NULL,
  `c_marks` varchar(20) DEFAULT NULL,
  `dse_marks` varchar(20) DEFAULT NULL,
  `python_marks` varchar(20) DEFAULT NULL,
  `java_marks` varchar(20) DEFAULT NULL,
  `php_marks` varchar(20) DEFAULT NULL,
  `TOTAL` int(11) DEFAULT NULL,
  `AVERAGE` int(11) DEFAULT NULL,
  `GRADE` char(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`NAME`, `ID`, `COLLEGE`, `DEPARTMENT`, `c_marks`, `dse_marks`, `python_marks`, `java_marks`, `php_marks`, `TOTAL`, `AVERAGE`, `GRADE`) VALUES
('Naveen', 1, 'RGM', 'CSE', '90', '98', '100', '95', '99', 482, 96, 'A'),
('Kiran', 7, 'MIT', 'EEE', '90', '99', '100', '76', '67', 432, 86, 'A');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
