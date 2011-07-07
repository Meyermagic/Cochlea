-- phpMyAdmin SQL Dump
-- version 3.4.3.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jul 07, 2011 at 12:51 AM
-- Server version: 5.5.14
-- PHP Version: 5.3.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `cochlea`
--

-- --------------------------------------------------------

--
-- Table structure for table `listeners`
--

CREATE TABLE IF NOT EXISTS `listeners` (
  `listener_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `listener_name` varchar(20) NOT NULL,
  `room_id` int(10) unsigned NOT NULL,
  `last_contact` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`listener_id`),
  KEY `room_id` (`room_id`,`last_contact`,`listener_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `messages`
--

CREATE TABLE IF NOT EXISTS `messages` (
  `sender_id` int(10) unsigned NOT NULL,
  `room_id` int(10) unsigned NOT NULL,
  `message` int(11) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  KEY `sender_id` (`sender_id`,`room_id`,`timestamp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `rooms`
--

CREATE TABLE IF NOT EXISTS `rooms` (
  `room_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `room_name` varchar(20) NOT NULL,
  PRIMARY KEY (`room_id`),
  UNIQUE KEY `room_name` (`room_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `songs`
--

CREATE TABLE IF NOT EXISTS `songs` (
  `song_id` char(23) NOT NULL,
  `room_id` int(10) unsigned NOT NULL,
  `votes` int(10) unsigned NOT NULL,
  `metadata` text NOT NULL,
  `state` tinyint(3) unsigned NOT NULL DEFAULT '0',
  `time_uploaded` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`song_id`),
  KEY `room_id` (`room_id`,`votes`,`time_uploaded`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
