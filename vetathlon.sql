-- phpMyAdmin SQL Dump
-- version 3.3.7deb7
-- http://www.phpmyadmin.net
--
-- Serveur: localhost
-- Généré le : Dim 23 Septembre 2012 à 14:38
-- Version du serveur: 5.1.63
-- Version de PHP: 5.3.3-7+squeeze13

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données: `vetathlon`
--

-- --------------------------------------------------------

--
-- Structure de la table `config`
--

CREATE TABLE IF NOT EXISTS `config` (
  `age_junior` int(3) NOT NULL COMMENT 'Age en dessous duquel on est junior et au dessus ou égale duquel on est majeus',
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `config`
--

INSERT INTO `config` (`age_junior`, `date`) VALUES
(14, '2012-06-17');

-- --------------------------------------------------------

--
-- Structure de la table `departement`
--

CREATE TABLE IF NOT EXISTS `departement` (
  `code` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `nom` varchar(60) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Contenu de la table `departement`
--

INSERT INTO `departement` (`code`, `nom`) VALUES
('01', 'AIN'),
('02', 'AISNE'),
('03', 'ALLIER'),
('04', 'ALPES DE HAUTES PROVENCE'),
('05', 'HAUTES ALPES'),
('06', 'ALPES MARITIMES'),
('07', 'ARDECHE'),
('08', 'ARDENNES'),
('09', 'ARIEGE'),
('10', 'AUBE'),
('11', 'AUDE'),
('12', 'AVEYRON'),
('13', 'BOUCHES DU RHONE'),
('14', 'CALVADOS'),
('15', 'CANTAL'),
('16', 'CHARENTE'),
('17', 'CHARENTE MARITIME'),
('18', 'CHER'),
('19', 'CORREZE'),
('21', 'COTE D''OR'),
('22', 'COTES D''ARMOR'),
('23', 'CREUSE'),
('24', 'DORDOGNE'),
('25', 'DOUBS'),
('26', 'DROME'),
('27', 'EURE'),
('28', 'EURE ET LOIR'),
('29', 'FINISTERE'),
('2A', 'CORSE DU SUD'),
('2B', 'HAUTE CORSE'),
('30', 'GARD'),
('31', 'HAUTE GARONNE'),
('32', 'GERS'),
('33', 'GIRONDE'),
('34', 'HERAULT'),
('35', 'ILLE ET VILAINE'),
('36', 'INDRE'),
('37', 'INDRE ET LOIRE'),
('38', 'ISERE'),
('39', 'JURA'),
('40', 'LANDES'),
('41', 'LOIR ET CHER'),
('42', 'LOIRE'),
('43', 'HAUTE LOIRE'),
('44', 'LOIRE ATLANTIQUE'),
('45', 'LOIRET'),
('46', 'LOT'),
('47', 'LOT ET GARONNE'),
('48', 'LOZERE'),
('49', 'MAINE ET LOIRE'),
('50', 'MANCHE'),
('51', 'MARNE'),
('52', 'HAUTE MARNE'),
('53', 'MAYENNE'),
('54', 'MEURTHE ET MOSELLE'),
('55', 'MEUSE'),
('56', 'MORBIHAN'),
('57', 'MOSELLE'),
('58', 'NIEVRE'),
('59', 'NORD'),
('60', 'OISE'),
('61', 'ORNE'),
('62', 'PAS DE CALAIS'),
('63', 'PUY DE DOME'),
('64', 'PYRENEES ATLANTIQUES'),
('65', 'HAUTE PYRENEES'),
('66', 'PYRENEES ORIENTALES'),
('67', 'BAS RHIN'),
('68', 'HAUT RHIN'),
('69', 'RHONE'),
('70', 'HAUTE SAONE'),
('71', 'SAONE ET LOIRE'),
('72', 'SARTHE'),
('73', 'SAVOIE'),
('74', 'HAUTE SAVOIE'),
('75', 'PARIS'),
('76', 'SEINE MARITIME'),
('77', 'SEINE ET MARNE'),
('78', 'YVELINES'),
('79', 'DEUX SEVRES'),
('80', 'SOMME'),
('81', 'TARN'),
('82', 'TARN ET GARONNE'),
('83', 'VAR'),
('84', 'VAUCLUSE'),
('85', 'VENDEE'),
('86', 'VIENNE'),
('87', 'HAUTE VIENNE'),
('88', 'VOSGES'),
('89', 'YONNE'),
('90', 'TERITOIRE DE BELFORT'),
('91', 'ESSONNE'),
('92', 'HAUTS DE SEINE'),
('93', 'SEINE SAINT DENIS'),
('94', 'VAL DE MARNE'),
('95', 'VAL D''OISE'),
('971', 'GUADELOUPE'),
('972', 'MARTINIQUE'),
('973', 'GUYANNE'),
('974', 'REUNION'),
('975', 'SAINT PIERRE ET MIQUELON'),
('976', 'MAYOTTE'),
('984', 'ILES EPARSES DE L''OCEAN INDIEN ET T.A.A.F.'),
('985', 'MAYOTTE'),
('986', 'WALLIS ET FUTUNA'),
('987', 'POLYNESIE FRANCAISE'),
('988', 'NOUVELLE CALEDONIE');

-- --------------------------------------------------------

--
-- Structure de la table `dossards`
--

CREATE TABLE IF NOT EXISTS `dossards` (
  `numero` int(10) unsigned NOT NULL,
  `pieton` int(10) unsigned NOT NULL,
  `vtt` int(10) unsigned NOT NULL,
  `payer` tinyint(1) unsigned NOT NULL,
  `etat` tinyint(1) unsigned NOT NULL,
  `tmp_pieton` time NOT NULL,
  `tmp_vtt` time NOT NULL,
  `tmp_total` time NOT NULL,
  PRIMARY KEY (`numero`),
  KEY `vtt` (`vtt`),
  KEY `pieton` (`pieton`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Contenu de la table `dossards`
--

INSERT INTO `dossards` (`numero`, `pieton`, `vtt`, `payer`, `etat`, `tmp_pieton`, `tmp_vtt`, `tmp_total`) VALUES
(1, 1, 1, 1, 0, '00:37:40', '01:24:17', '02:01:57'),
(2, 2, 2, 0, 2, '00:00:00', '00:00:00', '00:00:00'),
(3, 3, 3, 1, 0, '00:35:49', '01:17:54', '01:53:43'),
(4, 4, 5, 1, 0, '00:31:43', '01:09:30', '01:41:13'),
(5, 6, 7, 1, 0, '00:45:19', '01:20:48', '02:06:07'),
(6, 8, 9, 1, 0, '00:33:51', '01:08:04', '01:41:55'),
(7, 11, 12, 1, 0, '00:35:29', '01:31:38', '02:07:07'),
(8, 13, 13, 1, 0, '00:34:06', '01:19:48', '01:53:54'),
(9, 14, 14, 1, 0, '00:39:38', '01:38:14', '02:17:52'),
(10, 15, 16, 1, 0, '00:41:23', '01:26:14', '02:07:37'),
(11, 17, 18, 1, 0, '00:40:47', '01:20:22', '02:01:09'),
(12, 19, 19, 1, 0, '00:31:37', '01:13:19', '01:44:56'),
(13, 20, 21, 1, 0, '00:34:14', '01:28:32', '02:02:46'),
(14, 37, 37, 1, 0, '00:35:13', '01:17:37', '01:52:50'),
(15, 23, 24, 1, 0, '00:39:46', '01:25:14', '02:05:00'),
(16, 25, 26, 1, 0, '00:48:22', '02:09:37', '02:57:59'),
(17, 27, 28, 1, 0, '00:41:55', '01:32:02', '02:13:57'),
(18, 29, 30, 0, 2, '00:00:00', '00:00:00', '00:00:00'),
(19, 31, 32, 0, 2, '00:00:00', '00:00:00', '00:00:00'),
(20, 33, 33, 1, 0, '00:40:21', '01:31:54', '02:12:15'),
(21, 34, 35, 1, 0, '00:55:55', '01:23:12', '02:19:07'),
(22, 38, 39, 1, 0, '00:39:07', '01:19:15', '01:58:22'),
(23, 41, 42, 1, 0, '00:30:00', '01:19:30', '01:49:30'),
(24, 44, 44, 1, 0, '00:32:09', '01:14:06', '01:46:15'),
(25, 45, 45, 1, 0, '00:35:27', '01:25:13', '02:00:40'),
(26, 46, 47, 1, 0, '00:35:45', '01:29:25', '02:05:10'),
(27, 48, 49, 1, 0, '00:32:34', '01:00:28', '01:33:02'),
(28, 50, 51, 0, 2, '00:00:00', '00:00:00', '00:00:00'),
(29, 54, 54, 1, 0, '00:47:43', '01:32:51', '02:20:34'),
(30, 56, 56, 1, 0, '00:36:20', '01:23:45', '02:00:05'),
(31, 57, 57, 1, 0, '00:47:56', '01:44:56', '02:32:52'),
(32, 58, 59, 1, 0, '00:38:40', '01:30:35', '02:09:15'),
(33, 60, 60, 1, 0, '00:36:22', '01:14:59', '01:51:21'),
(34, 61, 62, 1, 0, '00:41:44', '01:15:23', '01:57:07'),
(35, 63, 63, 1, 0, '00:33:07', '01:08:26', '01:41:33'),
(36, 64, 64, 1, 0, '00:41:35', '01:42:57', '02:24:32'),
(37, 65, 65, 1, 0, '00:38:47', '01:26:21', '02:05:08'),
(38, 66, 66, 1, 0, '00:42:56', '01:45:43', '02:28:39'),
(39, 67, 67, 1, 0, '00:35:57', '01:29:00', '02:04:57'),
(40, 68, 68, 1, 0, '00:37:41', '01:44:24', '02:22:05'),
(41, 69, 70, 1, 0, '00:44:41', '01:51:35', '02:36:16'),
(42, 71, 72, 1, 0, '00:45:16', '01:35:26', '02:20:42'),
(43, 73, 74, 1, 0, '00:39:59', '01:13:29', '01:53:28'),
(44, 75, 75, 1, 0, '00:43:33', '01:29:46', '02:13:19'),
(45, 78, 79, 1, 0, '00:32:25', '01:16:42', '01:49:07'),
(46, 80, 81, 1, 0, '00:40:51', '01:20:37', '02:01:28'),
(47, 82, 83, 1, 0, '00:33:22', '01:13:48', '01:47:10'),
(48, 84, 85, 1, 0, '00:29:59', '01:07:50', '01:37:49'),
(49, 86, 87, 1, 0, '00:41:42', '02:14:54', '02:56:36'),
(50, 90, 90, 1, 0, '00:40:11', '01:23:51', '02:04:02'),
(51, 91, 92, 1, 0, '00:40:36', '01:37:03', '02:17:39'),
(52, 95, 95, 1, 0, '00:43:01', '01:44:17', '02:27:18'),
(53, 98, 99, 1, 0, '00:37:31', '00:00:00', '00:00:00'),
(54, 101, 101, 0, 0, '00:00:00', '00:00:00', '00:00:00'),
(55, 103, 103, 1, 0, '00:00:00', '00:00:00', '00:00:00'),
(201, 10, 10, 1, 0, '00:14:22', '00:34:23', '00:48:45'),
(202, 36, 36, 1, 0, '00:13:19', '00:24:44', '00:38:03'),
(203, 40, 40, 1, 0, '00:13:40', '00:31:31', '00:45:11'),
(204, 43, 43, 1, 0, '00:15:19', '00:37:52', '00:53:11'),
(205, 52, 53, 0, 2, '00:00:00', '00:00:00', '00:00:00'),
(206, 55, 55, 1, 0, '00:12:34', '00:32:46', '00:45:20'),
(207, 76, 77, 1, 0, '00:14:50', '00:29:54', '00:44:44'),
(208, 88, 89, 1, 0, '00:14:28', '00:43:40', '00:58:08'),
(209, 93, 94, 1, 0, '00:15:37', '00:29:32', '00:45:09'),
(210, 97, 97, 0, 0, '00:14:18', '00:30:47', '00:45:05'),
(211, 100, 100, 1, 0, '00:12:26', '00:26:46', '00:39:12'),
(212, 102, 102, 1, 0, '00:12:05', '00:21:07', '00:33:12');

-- --------------------------------------------------------

--
-- Structure de la table `minichat`
--

CREATE TABLE IF NOT EXISTS `minichat` (
  `nick` varchar(20) DEFAULT NULL,
  `texte` varchar(255) NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Contenu de la table `minichat`
--


-- --------------------------------------------------------

--
-- Structure de la table `participants`
--

CREATE TABLE IF NOT EXISTS `participants` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `prenom` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `date_nais` date NOT NULL,
  `sexe` tinyint(1) unsigned NOT NULL,
  `certif` tinyint(1) unsigned DEFAULT NULL,
  `commune` int(10) unsigned DEFAULT NULL,
  `departement` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `mail` varchar(70) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `commune` (`commune`,`departement`),
  KEY `departement` (`departement`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=104 ;

--
-- Contenu de la table `participants`
--

INSERT INTO `participants` (`id`, `nom`, `prenom`, `date_nais`, `sexe`, `certif`, `commune`, `departement`, `mail`) VALUES
(1, 'lagrange', 'benjamin', '1978-03-31', 2, 1, 42, '35', 'benjamin.lagrange2@wanadoo.fr'),
(2, 'marchand', 'jÃ©rome', '1976-08-04', 2, 0, 44, '35', ''),
(3, 'chassat', 'dider', '1971-10-20', 2, 1, 45, '35', 'tigatina@hotmail.fr'),
(4, 'hamon', 'anthony', '1987-07-06', 2, 1, 46, '22', 'pierre.mordrelle@gmail.com'),
(5, 'mordrelle', 'pierre', '1987-07-13', 2, 1, 47, '22', ''),
(6, 'poulain', 'stÃ©phanie', '1977-01-14', 1, 1, 1, '35', 'speedy.poulain@free.fr'),
(7, 'cotonnec', 'cedric', '1982-12-29', 2, 1, 48, '35', 'cotonnec@gmail.com'),
(8, 'foucher', 'anthony', '1984-10-02', 2, 1, 50, '53', ''),
(9, 'chevreul', 'fred', '1977-06-25', 2, 1, 51, '35', 'frederic.chevreul@sfr.fr'),
(10, 'gernigon', 'oceane', '1999-07-20', 1, 1, 1, '35', 'vincent.gernigon@orange.fr'),
(11, 'leclere', 'anthony', '1976-08-19', 2, 1, 1, '35', 'anthonyleclere@free.fr'),
(12, 'mazurais', 'franÃ§ois', '1962-02-14', 2, 1, 48, '35', ''),
(13, 'paquet', 'xavier', '1976-05-03', 2, 1, 52, '35', 'paquet.xavier@orange.fr'),
(14, 'aubert', 'anne marie', '1965-06-27', 1, 1, 53, '35', 'annemarie.aubert29@sfr.fr'),
(15, 'dauguet', 'antoine', '1970-03-01', 2, 1, 54, '35', ''),
(16, 'goby', 'antoine', '1970-06-25', 2, 1, 54, '35', ''),
(17, 'gauthier', 'fabrice', '1967-10-30', 2, 1, 1, '35', 'gauthieranne3993@neuf.fr'),
(18, 'cosmao', 'michel', '1966-09-23', 2, 1, 18, '35', 'miki.co@infonie.fr'),
(19, 'prodhomme', 'sylvain', '1972-12-05', 2, 1, 43, '53', ''),
(20, 'benard', 'christian', '1959-06-06', 2, 1, 1, '35', ''),
(21, 'deniard', 'cedric', '1980-05-21', 2, 1, 1, '35', ''),
(23, 'gazengel', 'jean marie', '1994-05-11', 2, 1, 55, '50', 'jeanmarc.gazengel@wanadoo.fr'),
(24, 'gazengel', 'jean marc', '1971-04-07', 2, 1, 55, '50', ''),
(25, 'colas', 'celine', '1977-03-28', 1, 1, 1, '35', 'jcollas@aliceadsl.fr'),
(26, 'laurent', 'isabelle', '1965-08-24', 1, 1, 56, '35', ''),
(27, 'sabin', 'francois', '1976-04-07', 2, 1, 57, '35', 'francoissabin@orange.fr'),
(28, 'sabin', 'daniel', '1952-09-15', 2, 1, 58, '85', ''),
(29, 'le gall', 'charles', '1992-06-23', 2, 0, 59, '35', 'c.legall134@la poste.net'),
(30, 'tondoux', 'antoine', '1993-09-18', 2, 0, 52, '35', 'antoine.tondoux@hotmail.fr'),
(31, 'le pouliquen', 'efflammig', '1979-01-01', 2, 1, 60, '22', ''),
(32, 'clolus', 'pierre yves', '1982-01-01', 2, 1, 61, '22', ''),
(33, 'bobet', 'patrick', '1975-04-17', 2, 1, 62, '35', 'patrennes@hotmail.fr'),
(34, 'coquemont', 'sandrine', '1974-12-11', 1, 1, 1, '35', ''),
(35, 'coquemont', 'philippe', '1972-12-01', 2, 1, 1, '35', 'filip.coquemont@gmail.com'),
(36, 'gazengel', 'pierre', '2001-05-02', 2, 1, 55, '50', 'jean.marc.gazengel@wanadoo.fr'),
(37, 'berdat', 'david', '1976-06-23', 2, 1, 63, '35', ''),
(38, 'gieu', 'valentin', '1995-08-08', 2, 1, 64, '35', ''),
(39, 'granger', 'basile', '1993-12-09', 2, 1, 64, '35', ''),
(40, 'gilet', 'paul', '2001-01-06', 2, 1, 29, '35', ''),
(41, 'vigner', 'ronald', '1978-04-30', 2, 1, 73, '35', ''),
(42, 'le strat', 'philippe', '1971-09-08', 2, 1, 11, '35', ''),
(43, 'jouault', 'clÃ©ment', '1999-10-14', 2, 1, 1, '35', ''),
(44, 'havard', 'alain', '1968-11-02', 2, 1, 66, '56', 'alin.avard830@orange.fr'),
(45, 'jeuland', 'mickael', '1976-06-21', 2, 1, 67, '35', 'jeulandmi@wanadoo.fr'),
(46, 'page', 'jean robert', '1973-12-22', 2, 1, 37, '35', ''),
(47, 'le mÃ©nes', 'goulven', '1974-04-21', 2, 1, 68, '35', ''),
(48, 'despas', 'sebastien', '1980-05-05', 2, 1, 69, '50', ''),
(49, 'despas', 'rÃ©gis', '1988-01-06', 2, 1, 69, '50', 'regispam@orange.fr'),
(50, 'collas', 'francois', '1996-01-01', 2, 0, 4, '35', ''),
(51, 'poras', 'florent', '1996-01-01', 2, 0, 70, '35', ''),
(52, 'devernois', 'corentin', '2000-08-14', 2, 0, 1, '35', ''),
(53, 'thomas', 'pierre', '1999-04-06', 2, 0, 1, '35', 'jft@cegetel.net'),
(54, 'massot', 'lionel', '1974-02-22', 0, 1, 41, '35', 'fienel@sfr.fr'),
(55, 'compain', 'quentin', '2000-05-18', 2, 1, 1, '35', ''),
(56, 'jain', 'arnaud', '1977-12-13', 2, 1, 71, '35', 'jain_arnaud@yaou.fr'),
(57, 'hurault', 'christophe', '1969-08-14', 2, 1, 72, '35', ''),
(58, 'piel', 'catherine', '1963-02-23', 1, 1, 18, '35', 'piel.hubert@wanadoo.fr'),
(59, 'piel', 'hubert', '1962-08-13', 2, 1, 18, '35', ''),
(60, 'Fougeray', 'Geoffrey', '1981-01-21', 2, 1, 37, '35', ''),
(61, 'Souvest', 'Romzin', '1981-02-19', 2, 1, 29, '35', ''),
(62, 'Herve', 'Peter', '1978-10-13', 2, 1, 29, '35', ''),
(63, 'Guerin', 'Stephane', '1971-10-01', 2, 1, 74, '35', ''),
(64, 'Fougeray', 'Andre', '1954-01-06', 2, 1, 27, '53', ''),
(65, 'Lenouvel', 'Jerome', '1983-09-15', 2, 1, 3, '35', ''),
(66, 'Blin', 'Stephane', '1972-11-26', 2, 1, 75, '35', ''),
(67, 'Liminier', 'Bruno', '1983-03-02', 2, 1, 3, '35', ''),
(68, 'beaudoin', 'jerome', '1975-03-12', 2, 1, 76, '35', ''),
(69, 'Bigot', 'Adrien', '1990-11-20', 2, 1, 48, '35', ''),
(70, 'Froc', 'Didier', '1965-07-08', 2, 1, 15, '35', ''),
(71, 'bigot', 'catherine', '1967-10-08', 1, 1, 15, '35', ''),
(72, 'bigot', 'vincent', '1964-09-29', 2, 1, 15, '35', ''),
(73, 'Martin', 'Vincent', '1980-07-07', 2, 1, 30, '35', ''),
(74, 'Thoin', 'Frederic', '1979-11-05', 2, 1, 30, '35', ''),
(75, 'colomb', 'alexendre', '1972-09-18', 2, 1, 77, '35', ''),
(76, 'Devernois', 'Corentin', '2000-08-14', 2, 1, 1, '35', ''),
(77, 'Thomas', 'Pierre', '1999-04-06', 2, 1, 1, '35', ''),
(78, 'Thichaut', 'Jean christoph', '1970-11-01', 2, 1, 25, '35', ''),
(79, 'Rimasson', 'Addy', '1975-06-18', 2, 1, 78, '35', ''),
(80, 'parichi', 'lionel', '1967-10-30', 2, 1, 79, '35', ''),
(81, 'petit', 'guillaume', '1996-12-05', 2, 1, 79, '35', ''),
(82, 'Colas', 'Pierre', '1963-09-25', 2, 1, 25, '35', ''),
(83, 'Lecoursonnais', 'Rommualde', '1971-11-20', 2, 1, 1, '35', ''),
(84, 'Descourmiers', 'Sebastien', '1968-11-24', 2, 1, 80, '35', ''),
(85, 'Marchand', 'Dominique', '1973-07-26', 2, 1, 56, '35', ''),
(86, 'trevidic', 'henry', '1961-08-24', 2, 1, 81, '35', ''),
(87, 'petit', 'laurent', '1963-12-23', 2, 1, 82, '35', ''),
(88, 'Boixere', 'Lucas', '2002-08-09', 2, 1, 1, '35', ''),
(89, 'Thomas', 'Yann', '2002-10-24', 2, 1, 1, '35', ''),
(90, 'Hamon', 'Jean francois', '1967-07-31', 2, 1, 18, '35', ''),
(91, 'javaudin', 'patrick', '1966-03-23', 2, 1, 83, '35', ''),
(92, 'raffray', 'aurelin', '1996-04-14', 2, 1, 84, '35', ''),
(93, 'Guillochet', 'Julien', '2000-03-17', 2, 1, 1, '35', ''),
(94, 'Goby', 'Theo', '2000-03-10', 2, 1, 1, '35', ''),
(95, 'emery', 'anthony', '1980-03-13', 2, 1, 1, '35', ''),
(97, 'Gougeon', 'Sylveun', '1999-04-13', 2, 0, 1, '35', ''),
(98, 'Paquet', 'Ange', '1966-02-17', 2, 1, 85, '35', ''),
(99, 'Cochet', 'Serge', '1965-04-02', 2, 1, 1, '35', ''),
(100, 'lefeuvre', 'pierre', '2002-07-20', 2, 1, 86, '35', ''),
(101, 'Havard', 'Daniet', '1952-09-11', 2, 1, 7, '35', ''),
(102, 'lefeuvre', 'victor', '1999-10-28', 2, 1, 87, '35', ''),
(103, 'Sourdrille', 'jean christoph', '1958-12-02', 2, 1, 7, '35', '');

-- --------------------------------------------------------

--
-- Structure de la table `villes`
--

CREATE TABLE IF NOT EXISTS `villes` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=88 ;

--
-- Contenu de la table `villes`
--

INSERT INTO `villes` (`id`, `nom`) VALUES
(1, 'Dourdain'),
(3, 'Rennes'),
(4, 'Val d''IzÃ©'),
(5, 'Nantes'),
(6, 'VitrÃ©'),
(7, 'CHATEAUBOURG'),
(8, 'L''HOPITAL CAMFROUT'),
(9, 'BOURG BLANC'),
(10, 'MELESSE'),
(11, 'MORDELLES'),
(12, 'LE VERGER'),
(13, 'BALAZE'),
(14, 'GUIGNEN'),
(15, 'LA BOUÃ‹XIERE'),
(16, 'ST AUBIN DU CORMIER'),
(17, 'VERN SUR SEICHE'),
(18, 'LIFFRE'),
(19, 'CRANCHEVRIER'),
(20, 'BREAL / VITRE'),
(21, 'CHAILLAND'),
(22, 'VERN / SEICHE'),
(23, 'PONTORSON'),
(24, 'CARNAC'),
(25, 'SERVON/VILAINE'),
(26, 'POULIGUEN'),
(27, 'ST DENIS DE GASTINES'),
(28, 'ST BRICE EN COGLES'),
(29, 'VITRE'),
(30, 'CHATILLION EN VENDELAIS'),
(31, 'NONTREIL DES LANDS'),
(32, 'LAILLE'),
(33, 'TREMBLET'),
(34, 'St CRISTOPHE DES BOIS'),
(35, 'LA FONTELEL'),
(36, 'LA BARONNIERE'),
(37, 'ST AUBIN D''AUBIGNE'),
(38, 'THORIGNE'),
(39, 'TREVRON'),
(40, 'LA CELLE EN LUITRE'),
(41, 'VAL D''IZE'),
(42, 'bruc sur aff'),
(43, 'laubriÃ¨re'),
(44, 'la lande'),
(45, 'st jaques de la lande'),
(46, 'pleslin trigavou'),
(47, 'dinan'),
(48, 'la bouexiÃ¨re'),
(49, 'laubriere'),
(50, 'laval'),
(51, 'brÃ©al/s vitre'),
(52, 'pocÃ© les bois'),
(53, 'amanlis'),
(54, 'javenÃ©'),
(55, 'vessey'),
(56, 'doudain'),
(57, 'st ouen'),
(58, 'le fenouillet'),
(59, 'la mÃ©ziere'),
(60, 'st samson sur rance'),
(61, 'lanvallay'),
(62, 'goven'),
(63, 'st armel'),
(64, 'montreuil sous perouse'),
(65, 'st benoit des ondes'),
(66, 'ploermel'),
(67, 'monteuil des landes'),
(68, 'le rheu'),
(69, 'juilley'),
(70, 'balazÃ©'),
(71, 'chantepie'),
(72, 'landavran'),
(73, 'brece'),
(74, 'AcÃ©lent le vitre'),
(75, 'Chateaugiron'),
(76, 'pire sur seiche'),
(77, 'betton'),
(78, 'Le petit corsee'),
(79, 'ossÃ©'),
(80, 'Bresson'),
(81, 'corp nuds'),
(82, 'osse'),
(83, 'marpire'),
(84, 'val d ize'),
(85, 'Domagne'),
(86, 'gosne'),
(87, 'gosnÃ©');

--
-- Contraintes pour les tables exportées
--

--
-- Contraintes pour la table `dossards`
--
ALTER TABLE `dossards`
  ADD CONSTRAINT `dossards_ibfk_1` FOREIGN KEY (`pieton`) REFERENCES `participants` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `dossards_ibfk_2` FOREIGN KEY (`vtt`) REFERENCES `participants` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `participants`
--
ALTER TABLE `participants`
  ADD CONSTRAINT `participants_ibfk_1` FOREIGN KEY (`commune`) REFERENCES `villes` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `participants_ibfk_2` FOREIGN KEY (`departement`) REFERENCES `departement` (`code`) ON DELETE NO ACTION ON UPDATE NO ACTION;
