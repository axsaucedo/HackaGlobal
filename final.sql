SET sql_mode='NO_BACKSLASH_ESCAPES';
CREATE TABLE `django_admin_log` (
    `id` integer NOT NULL PRIMARY KEY,
    `action_time` datetime NOT NULL,
    `user_id` integer NOT NULL,
    `content_type_id` integer,
    `object_id` text,
    `object_repr` varchar(200) NOT NULL,
    `action_flag` smallint unsigned NOT NULL,
    `change_message` text NOT NULL
);
INSERT INTO `django_admin_log` VALUES(1,'2014-04-06 08:22:26.413980',1,8,'4','Event object',2,'Changed country and tags.');
INSERT INTO `django_admin_log` VALUES(2,'2014-04-06 08:34:26.576916',1,8,'6','Event object',2,'Changed country and tags.');
INSERT INTO `django_admin_log` VALUES(3,'2014-04-06 08:40:59.162000',1,8,'8','Event object',2,'Changed creator, address, country and tags.');
INSERT INTO `django_admin_log` VALUES(4,'2014-04-06 08:42:58.478322',1,8,'3','Event object',2,'Changed creator, name, website, start, end and tags.');
INSERT INTO `django_admin_log` VALUES(5,'2014-04-06 08:45:48.110808',1,8,'10','Event object',2,'Changed creator and tags.');
INSERT INTO `django_admin_log` VALUES(6,'2014-04-06 08:46:01.707242',1,8,'1','Event object',2,'Changed creator and tags.');
INSERT INTO `django_admin_log` VALUES(7,'2014-04-06 08:46:20.317875',1,8,'2','Event object',2,'Changed creator and tags.');
INSERT INTO `django_admin_log` VALUES(8,'2014-04-06 10:03:10.732220',1,8,'17','Event object',2,'Changed country and tags.');
INSERT INTO `django_admin_log` VALUES(9,'2014-04-06 10:03:30.055349',1,8,'17','Event object',2,'Changed creator and tags.');
INSERT INTO `django_admin_log` VALUES(10,'2014-04-06 10:08:14.188509',1,8,'19','Event object',2,'Changed city and tags.');
INSERT INTO `django_admin_log` VALUES(11,'2014-04-06 10:08:55.927274',1,8,'16','Event object',2,'Changed city and tags.');
INSERT INTO `django_admin_log` VALUES(12,'2014-04-06 10:09:00.321493',1,8,'13','Event object',2,'Changed city and tags.');
INSERT INTO `django_admin_log` VALUES(13,'2014-04-06 10:09:04.248700',1,8,'4','Event object',2,'Changed city and tags.');
INSERT INTO `django_admin_log` VALUES(14,'2014-04-06 16:03:56.591538',1,4,'8','SWJudges@gmail.com',1,'');
INSERT INTO `django_admin_log` VALUES(15,'2014-04-09 12:35:29.256853',1,8,'29','Event object',2,'Changed city and tags.');
INSERT INTO `django_admin_log` VALUES(16,'2014-04-09 12:35:52.065255',1,8,'22','Event object',2,'Changed tags.');
INSERT INTO `django_admin_log` VALUES(17,'2014-04-09 12:36:00.047055',1,8,'26','Event object',2,'Changed tags.');
INSERT INTO `django_admin_log` VALUES(18,'2014-04-09 12:36:28.384958',1,8,'20','Event object',2,'Changed tags.');
INSERT INTO `django_admin_log` VALUES(19,'2014-04-09 12:37:23.134640',1,8,'16','Event object',2,'Changed tags.');
INSERT INTO `django_admin_log` VALUES(20,'2014-04-09 12:37:48.572159',1,8,'17','Event object',2,'Changed tags.');
INSERT INTO `django_admin_log` VALUES(21,'2014-04-09 12:38:13.176323',1,8,'14','Event object',2,'Changed tags.');
INSERT INTO `django_admin_log` VALUES(22,'2014-04-09 12:38:35.023495',1,8,'9','Event object',2,'Changed tags.');
INSERT INTO `django_admin_log` VALUES(23,'2014-04-09 12:38:47.832765',1,8,'7','Event object',2,'Changed tags.');
INSERT INTO `django_admin_log` VALUES(24,'2014-04-09 16:57:52.156288',1,8,'11','Event object',2,'Changed country, city and tags.');
INSERT INTO `django_admin_log` VALUES(25,'2014-04-09 16:58:12.833987',1,8,'3','Event object',2,'Changed country, city, website and tags.');
INSERT INTO `django_admin_log` VALUES(26,'2014-04-10 10:07:31.058381',1,8,'31','Event object',2,'Changed country, city and tags.');
INSERT INTO `django_admin_log` VALUES(27,'2014-04-10 10:08:01.774735',1,8,'31','Event object',2,'Changed country and tags.');
INSERT INTO `django_admin_log` VALUES(28,'2014-04-10 10:08:11.173407',1,8,'30','Event object',2,'Changed country and tags.');
INSERT INTO `django_admin_log` VALUES(29,'2014-04-10 10:08:28.963161',1,8,'11','Event object',2,'Changed country and tags.');
INSERT INTO `django_admin_log` VALUES(30,'2014-04-10 10:08:39.560419',1,8,'3','Event object',2,'Changed country and tags.');
INSERT INTO `django_admin_log` VALUES(31,'2014-04-10 13:08:32.102744',1,8,'17','Event object',2,'Changed country and tags.');
INSERT INTO `django_admin_log` VALUES(32,'2014-04-10 13:09:08.057778',1,8,'12','Event object',2,'Changed country and tags.');
CREATE TABLE `auth_permission` (
    `id` integer NOT NULL PRIMARY KEY,
    `name` varchar(50) NOT NULL,
    `content_type_id` integer NOT NULL,
    `codename` varchar(100) NOT NULL,
    UNIQUE (`content_type_id`, `codename`)
);
INSERT INTO `auth_permission` VALUES(1,'Can add log entry',1,'add_logentry');
INSERT INTO `auth_permission` VALUES(2,'Can change log entry',1,'change_logentry');
INSERT INTO `auth_permission` VALUES(3,'Can delete log entry',1,'delete_logentry');
INSERT INTO `auth_permission` VALUES(4,'Can add permission',2,'add_permission');
INSERT INTO `auth_permission` VALUES(5,'Can change permission',2,'change_permission');
INSERT INTO `auth_permission` VALUES(6,'Can delete permission',2,'delete_permission');
INSERT INTO `auth_permission` VALUES(7,'Can add group',3,'add_group');
INSERT INTO `auth_permission` VALUES(8,'Can change group',3,'change_group');
INSERT INTO `auth_permission` VALUES(9,'Can delete group',3,'delete_group');
INSERT INTO `auth_permission` VALUES(10,'Can add user',4,'add_user');
INSERT INTO `auth_permission` VALUES(11,'Can change user',4,'change_user');
INSERT INTO `auth_permission` VALUES(12,'Can delete user',4,'delete_user');
INSERT INTO `auth_permission` VALUES(13,'Can add content type',5,'add_contenttype');
INSERT INTO `auth_permission` VALUES(14,'Can change content type',5,'change_contenttype');
INSERT INTO `auth_permission` VALUES(15,'Can delete content type',5,'delete_contenttype');
INSERT INTO `auth_permission` VALUES(16,'Can add session',6,'add_session');
INSERT INTO `auth_permission` VALUES(17,'Can change session',6,'change_session');
INSERT INTO `auth_permission` VALUES(18,'Can delete session',6,'delete_session');
INSERT INTO `auth_permission` VALUES(19,'Can add site',7,'add_site');
INSERT INTO `auth_permission` VALUES(20,'Can change site',7,'change_site');
INSERT INTO `auth_permission` VALUES(21,'Can delete site',7,'delete_site');
INSERT INTO `auth_permission` VALUES(22,'Can add event',8,'add_event');
INSERT INTO `auth_permission` VALUES(23,'Can change event',8,'change_event');
INSERT INTO `auth_permission` VALUES(24,'Can delete event',8,'delete_event');
INSERT INTO `auth_permission` VALUES(25,'Can add attendee',9,'add_attendee');
INSERT INTO `auth_permission` VALUES(26,'Can change attendee',9,'change_attendee');
INSERT INTO `auth_permission` VALUES(27,'Can delete attendee',9,'delete_attendee');
INSERT INTO `auth_permission` VALUES(28,'Can add staff',10,'add_staff');
INSERT INTO `auth_permission` VALUES(29,'Can change staff',10,'change_staff');
INSERT INTO `auth_permission` VALUES(30,'Can delete staff',10,'delete_staff');
INSERT INTO `auth_permission` VALUES(31,'Can add user social auth',11,'add_usersocialauth');
INSERT INTO `auth_permission` VALUES(32,'Can change user social auth',11,'change_usersocialauth');
INSERT INTO `auth_permission` VALUES(33,'Can delete user social auth',11,'delete_usersocialauth');
INSERT INTO `auth_permission` VALUES(34,'Can add nonce',12,'add_nonce');
INSERT INTO `auth_permission` VALUES(35,'Can change nonce',12,'change_nonce');
INSERT INTO `auth_permission` VALUES(36,'Can delete nonce',12,'delete_nonce');
INSERT INTO `auth_permission` VALUES(37,'Can add association',13,'add_association');
INSERT INTO `auth_permission` VALUES(38,'Can change association',13,'change_association');
INSERT INTO `auth_permission` VALUES(39,'Can delete association',13,'delete_association');
INSERT INTO `auth_permission` VALUES(40,'Can add code',14,'add_code');
INSERT INTO `auth_permission` VALUES(41,'Can change code',14,'change_code');
INSERT INTO `auth_permission` VALUES(42,'Can delete code',14,'delete_code');
INSERT INTO `auth_permission` VALUES(43,'Can add migration history',15,'add_migrationhistory');
INSERT INTO `auth_permission` VALUES(44,'Can change migration history',15,'change_migrationhistory');
INSERT INTO `auth_permission` VALUES(45,'Can delete migration history',15,'delete_migrationhistory');
INSERT INTO `auth_permission` VALUES(46,'Can add Tag',16,'add_tag');
INSERT INTO `auth_permission` VALUES(47,'Can change Tag',16,'change_tag');
INSERT INTO `auth_permission` VALUES(48,'Can delete Tag',16,'delete_tag');
INSERT INTO `auth_permission` VALUES(49,'Can add Tagged Item',17,'add_taggeditem');
INSERT INTO `auth_permission` VALUES(50,'Can change Tagged Item',17,'change_taggeditem');
INSERT INTO `auth_permission` VALUES(51,'Can delete Tagged Item',17,'delete_taggeditem');
CREATE TABLE `auth_group_permissions` (
    `id` integer NOT NULL PRIMARY KEY,
    `group_id` integer NOT NULL,
    `permission_id` integer NOT NULL REFERENCES `auth_permission` (`id`),
    UNIQUE (`group_id`, `permission_id`)
);
CREATE TABLE `auth_group` (
    `id` integer NOT NULL PRIMARY KEY,
    `name` varchar(80) NOT NULL UNIQUE
);
CREATE TABLE `auth_user_groups` (
    `id` integer NOT NULL PRIMARY KEY,
    `user_id` integer NOT NULL,
    `group_id` integer NOT NULL REFERENCES `auth_group` (`id`),
    UNIQUE (`user_id`, `group_id`)
);
CREATE TABLE `auth_user_user_permissions` (
    `id` integer NOT NULL PRIMARY KEY,
    `user_id` integer NOT NULL,
    `permission_id` integer NOT NULL REFERENCES `auth_permission` (`id`),
    UNIQUE (`user_id`, `permission_id`)
);
CREATE TABLE `auth_user` (
    `id` integer NOT NULL PRIMARY KEY,
    `password` varchar(128) NOT NULL,
    `last_login` datetime NOT NULL,
    `is_superuser` bool NOT NULL,
    `username` varchar(30) NOT NULL UNIQUE,
    `first_name` varchar(30) NOT NULL,
    `last_name` varchar(30) NOT NULL,
    `email` varchar(75) NOT NULL,
    `is_staff` bool NOT NULL,
    `is_active` bool NOT NULL,
    `date_joined` datetime NOT NULL
);
INSERT INTO `auth_user` VALUES(1,'pbkdf2_sha256$10000$ZyOaB2ULE4NP$RAaHsrAEPvXcnQI91HiDcgWKR4Z9EXwlLdnvEQe9eDk=','2014-04-09 12:35:04.121044',1,'axsauze','','','axsauze@gmail.com',1,1,'2014-04-06 04:57:04.252261');
INSERT INTO `auth_user` VALUES(2,'pbkdf2_sha256$10000$R8v7j1QiwDug$LrSBc05+BmgW2lwieP6nANJks0K5nVZwcrd/ucniwM4=','2014-04-09 12:34:31.546460',0,'hackatimis@gmail.com','Hacka','Timis','',0,1,'2014-04-06 07:58:45.952380');
INSERT INTO `auth_user` VALUES(3,'pbkdf2_sha256$10000$O4Bruye49WXX$7SF2szPQcLssojsotcIT46WIsXX+lDq9PfL62ka+ZYQ=','2014-04-10 09:59:27.490269',0,'hackamoscow@gmail.com','Hacka','Moscow','',0,1,'2014-04-06 08:05:18.134284');
INSERT INTO `auth_user` VALUES(4,'pbkdf2_sha256$10000$aO5NIL8NG1iV$2fSTtgBiscZs7BUzYtVput8HbR7rbB9J8OCOFa/FjkM=','2014-04-08 13:09:46.415724',0,'hackashanghai@gmail.com','Hacka','Shanghai','',0,1,'2014-04-06 08:07:05.804994');
INSERT INTO `auth_user` VALUES(5,'pbkdf2_sha256$10000$RTmRt9o5kzBP$9zIS4OXtchULFUbfURM9Iz7DC+LQ1mxTYCkW7pq3LSk=','2014-04-09 12:32:56.403463',0,'hackadf@gmail.com','Hacka','DF','',0,1,'2014-04-06 08:24:46.197461');
INSERT INTO `auth_user` VALUES(6,'pbkdf2_sha256$10000$HeYXcQQAvHPq$ew4fheCgujegUXvr7/CMGL96DYaMdz0+1k/YAbQCGC0=','2014-04-06 08:48:11.630496',0,'hackasaopaulo@gmail.com','Hacka','SaoPaulo','',0,1,'2014-04-06 08:48:11.320490');
INSERT INTO `auth_user` VALUES(7,'pbkdf2_sha256$10000$P5iPDXrRQm2Z$5WGvN3z8tTyTYa/alu8pM8C0pasWOE7zbgZHjqMRlkU=','2014-04-06 10:03:02.226832',0,'hackasoton@gmail.com','Hacka','Soton','',0,1,'2014-04-06 08:54:04.922590');
INSERT INTO `auth_user` VALUES(8,'pbkdf2_sha256$10000$9YBZdaNJA2Tq$9hyR2GE/hO+hA9WOGRC+OkbPPFqPbHEQcYI0bPorUkQ=','2014-04-06 16:03:56.074758',0,'SWJudges@gmail.com','','','',0,1,'2014-04-06 16:03:56.074808');
CREATE TABLE `django_content_type` (
    `id` integer NOT NULL PRIMARY KEY,
    `name` varchar(100) NOT NULL,
    `app_label` varchar(100) NOT NULL,
    `model` varchar(100) NOT NULL,
    UNIQUE (`app_label`, `model`)
);
INSERT INTO `django_content_type` VALUES(1,'log entry','admin','logentry');
INSERT INTO `django_content_type` VALUES(2,'permission','auth','permission');
INSERT INTO `django_content_type` VALUES(3,'group','auth','group');
INSERT INTO `django_content_type` VALUES(4,'user','auth','user');
INSERT INTO `django_content_type` VALUES(5,'content type','contenttypes','contenttype');
INSERT INTO `django_content_type` VALUES(6,'session','sessions','session');
INSERT INTO `django_content_type` VALUES(7,'site','sites','site');
INSERT INTO `django_content_type` VALUES(8,'event','hackaglobal','event');
INSERT INTO `django_content_type` VALUES(9,'attendee','hackaglobal','attendee');
INSERT INTO `django_content_type` VALUES(10,'staff','hackaglobal','staff');
INSERT INTO `django_content_type` VALUES(11,'user social auth','default','usersocialauth');
INSERT INTO `django_content_type` VALUES(12,'nonce','default','nonce');
INSERT INTO `django_content_type` VALUES(13,'association','default','association');
INSERT INTO `django_content_type` VALUES(14,'code','default','code');
INSERT INTO `django_content_type` VALUES(15,'migration history','south','migrationhistory');
INSERT INTO `django_content_type` VALUES(16,'Tag','taggit','tag');
INSERT INTO `django_content_type` VALUES(17,'Tagged Item','taggit','taggeditem');
CREATE TABLE `django_session` (
    `session_key` varchar(40) NOT NULL PRIMARY KEY,
    `session_data` text NOT NULL,
    `expire_date` datetime NOT NULL
);
INSERT INTO `django_session` VALUES('59de1tpeebg4gbqcnaljfihltskj5dcr','ZTk5ZjMzN2ZlM2EwZGUyNGY3ODBkYmNkNGZlODlmM2Q0YmUyN2UyOTqAAn1xAVgKAAAAdGVzdGNvb2tpZVgGAAAAd29ya2VkcQJzLg==','2014-04-20 08:02:13.646437');
INSERT INTO `django_session` VALUES('m5vxl52svl03rszl8qtfww2z26ssxfvm','NGRhM2UyMDY2OGJjNTg3Y2YxMjFiNGMwOWM1OGZjMWRhM2U2MWM0YTqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu','2014-04-20 07:57:21.830862');
INSERT INTO `django_session` VALUES('8ssbtju8iif6v6hw0my5bbwzl3uxcbn3','NGRhM2UyMDY2OGJjNTg3Y2YxMjFiNGMwOWM1OGZjMWRhM2U2MWM0YTqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu','2014-04-20 07:57:23.195517');
INSERT INTO `django_session` VALUES('saimz0spkb7eqhh8sl3fd0w3rrlpcrla','NGRhM2UyMDY2OGJjNTg3Y2YxMjFiNGMwOWM1OGZjMWRhM2U2MWM0YTqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu','2014-04-20 08:48:31.736065');
INSERT INTO `django_session` VALUES('obwikbgm5qrmpzcqwmovuxzap3ndgct0','MjRjNDQ3NjVlMWM2MThjZWE2ZGFjZGQ0YzUzYTBkMTk4ODc4Njc3ZDqAAn1xAShYCgAAAHRlc3Rjb29raWVxAlgGAAAAd29ya2VkcQNVDV9hdXRoX3VzZXJfaWRLAlUSX2F1dGhfdXNlcl9iYWNrZW5kVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHUu','2014-04-20 09:53:35.774932');
INSERT INTO `django_session` VALUES('cu3sbxre2ev23manqogsnugho1uara0h','MjRjNDQ3NjVlMWM2MThjZWE2ZGFjZGQ0YzUzYTBkMTk4ODc4Njc3ZDqAAn1xAShYCgAAAHRlc3Rjb29raWVxAlgGAAAAd29ya2VkcQNVDV9hdXRoX3VzZXJfaWRLAlUSX2F1dGhfdXNlcl9iYWNrZW5kVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHUu','2014-04-20 10:57:40.216446');
INSERT INTO `django_session` VALUES('jv4uz9hhcm7yrktj59cgmmgaaiezg1f0','ZTk5ZjMzN2ZlM2EwZGUyNGY3ODBkYmNkNGZlODlmM2Q0YmUyN2UyOTqAAn1xAVgKAAAAdGVzdGNvb2tpZVgGAAAAd29ya2VkcQJzLg==','2014-04-20 13:05:51.801749');
INSERT INTO `django_session` VALUES('lg5cev979qbowpkuphvyrw5n02qt4pl9','NGRhM2UyMDY2OGJjNTg3Y2YxMjFiNGMwOWM1OGZjMWRhM2U2MWM0YTqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu','2014-04-20 11:09:58.053380');
INSERT INTO `django_session` VALUES('hmm3wzvco1cu07vgfxi1p5q5p0h47vgp','NGRhM2UyMDY2OGJjNTg3Y2YxMjFiNGMwOWM1OGZjMWRhM2U2MWM0YTqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu','2014-04-20 11:18:25.177950');
INSERT INTO `django_session` VALUES('mdyzzl0ec8uiqwdk2v8mr8stqts7my83','NGRhM2UyMDY2OGJjNTg3Y2YxMjFiNGMwOWM1OGZjMWRhM2U2MWM0YTqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu','2014-04-20 12:00:04.209971');
INSERT INTO `django_session` VALUES('8ajwt5ccmawckxwgwxnozkhdwu4bj34y','NGRhM2UyMDY2OGJjNTg3Y2YxMjFiNGMwOWM1OGZjMWRhM2U2MWM0YTqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu','2014-04-20 12:33:11.959519');
INSERT INTO `django_session` VALUES('rf77p4p88yxomuyeervj426wr7y6prrj','ZTk5ZjMzN2ZlM2EwZGUyNGY3ODBkYmNkNGZlODlmM2Q0YmUyN2UyOTqAAn1xAVgKAAAAdGVzdGNvb2tpZVgGAAAAd29ya2VkcQJzLg==','2014-04-20 14:09:43.725860');
INSERT INTO `django_session` VALUES('xlht9r8fr2v3809vsm6i6mk5d05y57hm','ODlhYjNlNDMyYzgxYjJmM2VkZDk3ODU2NTQxNmRlOGQ4NWM2MmZhNTqAAn1xAS4=','2014-04-20 13:14:06.684082');
INSERT INTO `django_session` VALUES('2roo7i1m1ay77uozscmh60vd7ddhem77','ZTk5ZjMzN2ZlM2EwZGUyNGY3ODBkYmNkNGZlODlmM2Q0YmUyN2UyOTqAAn1xAVgKAAAAdGVzdGNvb2tpZVgGAAAAd29ya2VkcQJzLg==','2014-04-20 16:12:47.899101');
INSERT INTO `django_session` VALUES('gpdw4rufdbygul05958bt7q6bfc8o97f','NGRhM2UyMDY2OGJjNTg3Y2YxMjFiNGMwOWM1OGZjMWRhM2U2MWM0YTqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu','2014-04-20 21:26:07.162694');
INSERT INTO `django_session` VALUES('4rwza3asyhq5tziueiwsqdqgsro89q3f','NGRhM2UyMDY2OGJjNTg3Y2YxMjFiNGMwOWM1OGZjMWRhM2U2MWM0YTqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu','2014-04-20 22:02:28.610644');
INSERT INTO `django_session` VALUES('6oy5h80xfsnstsu55nwicgxto3u50sfk','NGRhM2UyMDY2OGJjNTg3Y2YxMjFiNGMwOWM1OGZjMWRhM2U2MWM0YTqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu','2014-04-21 13:21:30.898077');
INSERT INTO `django_session` VALUES('ts6iw8pdfzaf66lpu1alm5tb4gcj9d0g','NGRhM2UyMDY2OGJjNTg3Y2YxMjFiNGMwOWM1OGZjMWRhM2U2MWM0YTqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu','2014-04-21 14:00:36.686355');
INSERT INTO `django_session` VALUES('81anq46f74rnl4f7mwvhi5678ginl5h6','NGRhM2UyMDY2OGJjNTg3Y2YxMjFiNGMwOWM1OGZjMWRhM2U2MWM0YTqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu','2014-04-22 03:06:23.848968');
INSERT INTO `django_session` VALUES('f64038nwown93excggbn1ckhsl6w8fgq','NGRhM2UyMDY2OGJjNTg3Y2YxMjFiNGMwOWM1OGZjMWRhM2U2MWM0YTqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu','2014-04-22 07:26:10.846664');
INSERT INTO `django_session` VALUES('bx5p2a19zpe05pzaef0t0if8qhqws5w4','ZTk5ZjMzN2ZlM2EwZGUyNGY3ODBkYmNkNGZlODlmM2Q0YmUyN2UyOTqAAn1xAVgKAAAAdGVzdGNvb2tpZVgGAAAAd29ya2VkcQJzLg==','2014-04-23 16:45:12.411032');
INSERT INTO `django_session` VALUES('1jzrxqgq0wzpgv78rjnbykb5wm471g5q','NGRhM2UyMDY2OGJjNTg3Y2YxMjFiNGMwOWM1OGZjMWRhM2U2MWM0YTqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu','2014-04-22 10:31:44.260554');
INSERT INTO `django_session` VALUES('rcrbixpm6e8c6vx5jkzdn3xtjzs42xwm','NGRhM2UyMDY2OGJjNTg3Y2YxMjFiNGMwOWM1OGZjMWRhM2U2MWM0YTqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu','2014-04-22 11:00:42.512317');
INSERT INTO `django_session` VALUES('jwzbh3e1t1iexf5p4bso4ney5mfxl3vx','NTg0NGMyODFjNDhiOGQ1MmYzZDYyMDhiZTVhZTdlYTY2YWNlNmUyNzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLBHUu','2014-04-22 13:09:46.455319');
INSERT INTO `django_session` VALUES('oq849tf1t9oh7hl5midfqclz9rcsd96k','NGRhM2UyMDY2OGJjNTg3Y2YxMjFiNGMwOWM1OGZjMWRhM2U2MWM0YTqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu','2014-04-22 15:25:34.841543');
INSERT INTO `django_session` VALUES('44di8x4u03ueewap6kgwzkuhymsobodc','NGRhM2UyMDY2OGJjNTg3Y2YxMjFiNGMwOWM1OGZjMWRhM2U2MWM0YTqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu','2014-04-22 17:29:56.524772');
INSERT INTO `django_session` VALUES('tmzw1ddbudhih49iod98b6omvhv3o1tm','NGRhM2UyMDY2OGJjNTg3Y2YxMjFiNGMwOWM1OGZjMWRhM2U2MWM0YTqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu','2014-04-22 19:16:19.390796');
INSERT INTO `django_session` VALUES('s4jwhv5m8xl9m36c5e35fy9338x2tidw','NGRhM2UyMDY2OGJjNTg3Y2YxMjFiNGMwOWM1OGZjMWRhM2U2MWM0YTqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu','2014-04-22 20:26:16.980044');
INSERT INTO `django_session` VALUES('n25cypqgi0y4q4z4cvf88pkrso31zjeb','ZTk5ZjMzN2ZlM2EwZGUyNGY3ODBkYmNkNGZlODlmM2Q0YmUyN2UyOTqAAn1xAVgKAAAAdGVzdGNvb2tpZVgGAAAAd29ya2VkcQJzLg==','2014-04-23 09:43:04.240561');
INSERT INTO `django_session` VALUES('kc2e34s8ed920g4t6t43t5mtliiazblm','NjgyMDNhZjNlMmFiOGY2ZDFhNmI3ZWZkN2QwY2Y3ZDA2OWQwZTkxODqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLAnUu','2014-04-23 09:57:05.998122');
INSERT INTO `django_session` VALUES('vlg165epfuihoti71c4j20v5flvi826z','NzQzMDY3ZjE1MWE3ZmRkZWYxODY4NWI1ZDg0NjNhMDA4Mjc3M2EwODqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZFUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmRYCgAAAHRlc3Rjb29raWVxAlgGAAAAd29ya2VkcQNVDV9hdXRoX3VzZXJfaWRLAVUJX21lc3NhZ2VzVAQEAABbWyJfX2pzb25fbWVzc2FnZSIsMCwyMCwiVGhlIGV2ZW50IFwiRXZlbnQgb2JqZWN0XCIgd2FzIGNoYW5nZWQgc3VjY2Vzc2Z1bGx5LiJdLFsiX19qc29uX21lc3NhZ2UiLDAsMjAsIlRoZSBldmVudCBcIkV2ZW50IG9iamVjdFwiIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS4iXSxbIl9fanNvbl9tZXNzYWdlIiwwLDIwLCJUaGUgZXZlbnQgXCJFdmVudCBvYmplY3RcIiB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuIl0sWyJfX2pzb25fbWVzc2FnZSIsMCwyMCwiVGhlIGV2ZW50IFwiRXZlbnQgb2JqZWN0XCIgd2FzIGNoYW5nZWQgc3VjY2Vzc2Z1bGx5LiJdLFsiX19qc29uX21lc3NhZ2UiLDAsMjAsIlRoZSBldmVudCBcIkV2ZW50IG9iamVjdFwiIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS4iXSxbIl9fanNvbl9tZXNzYWdlIiwwLDIwLCJUaGUgZXZlbnQgXCJFdmVudCBvYmplY3RcIiB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuIl0sWyJfX2pzb25fbWVzc2FnZSIsMCwyMCwiVGhlIGV2ZW50IFwiRXZlbnQgb2JqZWN0XCIgd2FzIGNoYW5nZWQgc3VjY2Vzc2Z1bGx5LiJdLFsiX19qc29uX21lc3NhZ2UiLDAsMjAsIlRoZSBldmVudCBcIkV2ZW50IG9iamVjdFwiIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS4iXSxbIl9fanNvbl9tZXNzYWdlIiwwLDIwLCJUaGUgZXZlbnQgXCJFdmVudCBvYmplY3RcIiB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuIl0sWyJfX2pzb25fbWVzc2FnZSIsMCwyMCwiVGhlIGV2ZW50IFwiRXZlbnQgb2JqZWN0XCIgd2FzIGNoYW5nZWQgc3VjY2Vzc2Z1bGx5LiJdLFsiX19qc29uX21lc3NhZ2UiLDAsMjAsIlRoZSBldmVudCBcIkV2ZW50IG9iamVjdFwiIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS4iXSxbIl9fanNvbl9tZXNzYWdlIiwwLDIwLCJUaGUgZXZlbnQgXCJFdmVudCBvYmplY3RcIiB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuIl0sWyJfX2pzb25fbWVzc2FnZSIsMCwyMCwiVGhlIGV2ZW50IFwiRXZlbnQgb2JqZWN0XCIgd2FzIGNoYW5nZWQgc3VjY2Vzc2Z1bGx5LiJdXXUu','2014-04-24 14:08:38.103862');
INSERT INTO `django_session` VALUES('o4ls7de7zxgjxnadq9wnggcwgvm1jyy7','ODlhYjNlNDMyYzgxYjJmM2VkZDk3ODU2NTQxNmRlOGQ4NWM2MmZhNTqAAn1xAS4=','2014-04-23 14:00:44.256399');
INSERT INTO `django_session` VALUES('gjgb7tpiink381gdjxr79dzzghj78xv3','ZTk5ZjMzN2ZlM2EwZGUyNGY3ODBkYmNkNGZlODlmM2Q0YmUyN2UyOTqAAn1xAVgKAAAAdGVzdGNvb2tpZVgGAAAAd29ya2VkcQJzLg==','2014-04-23 16:31:22.717352');
INSERT INTO `django_session` VALUES('1qi775vjmtbvs4u9cahthbyoxzax83vz','NGRhM2UyMDY2OGJjNTg3Y2YxMjFiNGMwOWM1OGZjMWRhM2U2MWM0YTqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu','2014-04-23 23:41:58.369674');
INSERT INTO `django_session` VALUES('deabnz8o1bmjnrjh2yd26w7msl7trtds','NGRhM2UyMDY2OGJjNTg3Y2YxMjFiNGMwOWM1OGZjMWRhM2U2MWM0YTqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu','2014-04-24 01:33:25.900557');
INSERT INTO `django_session` VALUES('08b4c2jar31ra3mhezfu1j7exif7flh2','NGRhM2UyMDY2OGJjNTg3Y2YxMjFiNGMwOWM1OGZjMWRhM2U2MWM0YTqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu','2014-04-24 04:33:21.166773');
INSERT INTO `django_session` VALUES('eik8y3oacbohd38wauhwov5zepnb1sgd','ZjQ3YzdhZWRlNDkwNzNjZjViYTg4NGEyMTU5N2ExYjRkNjM4MzA0OTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLA3Uu','2014-04-24 09:59:27.534364');
INSERT INTO `django_session` VALUES('a7164p62kex5d6d5o4rssnjjsh991ewc','NGRhM2UyMDY2OGJjNTg3Y2YxMjFiNGMwOWM1OGZjMWRhM2U2MWM0YTqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu','2014-04-24 11:41:36.416062');
INSERT INTO `django_session` VALUES('3niovfl5j6xezocu4xnvau74et6lj9p0','NGRhM2UyMDY2OGJjNTg3Y2YxMjFiNGMwOWM1OGZjMWRhM2U2MWM0YTqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu','2014-04-24 18:36:21.420550');
CREATE TABLE `django_site` (
    `id` integer NOT NULL PRIMARY KEY,
    `domain` varchar(100) NOT NULL,
    `name` varchar(50) NOT NULL
);
INSERT INTO `django_site` VALUES(1,'example.com','example.com');
CREATE TABLE `hackaglobal_attendee` (
    `id` integer NOT NULL PRIMARY KEY,
    `attendee_id` integer NOT NULL REFERENCES `auth_user` (`id`),
    `type` varchar(1) NOT NULL,
    `event_id` integer NOT NULL REFERENCES `hackaglobal_event` (`id`)
);
INSERT INTO `hackaglobal_attendee` VALUES(1,2,'T',2);
CREATE TABLE `hackaglobal_staff` (
    `id` integer NOT NULL PRIMARY KEY,
    `staff_id` integer REFERENCES `auth_user` (`id`),
    `name` varchar(50) NOT NULL,
    `description` text NOT NULL,
    `url` varchar(200),
    `imgurl` varchar(200),
    `type` varchar(1) NOT NULL,
    `event_id` integer NOT NULL REFERENCES `hackaglobal_event` (`id`)
);
CREATE TABLE `social_auth_usersocialauth` (
    `id` integer NOT NULL PRIMARY KEY,
    `user_id` integer NOT NULL REFERENCES `auth_user` (`id`),
    `provider` varchar(32) NOT NULL,
    `uid` varchar(255) NOT NULL,
    `extra_data` text NOT NULL,
    UNIQUE (`provider`, `uid`)
);
CREATE TABLE `social_auth_nonce` (
    `id` integer NOT NULL PRIMARY KEY,
    `server_url` varchar(255) NOT NULL,
    `timestamp` integer NOT NULL,
    `salt` varchar(65) NOT NULL
);
CREATE TABLE `social_auth_association` (
    `id` integer NOT NULL PRIMARY KEY,
    `server_url` varchar(255) NOT NULL,
    `handle` varchar(255) NOT NULL,
    `secret` varchar(255) NOT NULL,
    `issued` integer NOT NULL,
    `lifetime` integer NOT NULL,
    `assoc_type` varchar(64) NOT NULL
);
CREATE TABLE `social_auth_code` (
    `id` integer NOT NULL PRIMARY KEY,
    `email` varchar(75) NOT NULL,
    `code` varchar(32) NOT NULL,
    `verified` bool NOT NULL,
    UNIQUE (`email`, `code`)
);
CREATE TABLE `south_migrationhistory` (
    `id` integer NOT NULL PRIMARY KEY,
    `app_name` varchar(255) NOT NULL,
    `migration` varchar(255) NOT NULL,
    `applied` datetime NOT NULL
);
INSERT INTO `south_migrationhistory` VALUES(1,'taggit','0001_initial','2014-04-09 12:25:47.188696');
INSERT INTO `south_migrationhistory` VALUES(2,'taggit','0002_unique_tagnames','2014-04-09 12:25:47.307610');
INSERT INTO `south_migrationhistory` VALUES(3,'hackaglobal','0001_initial','2014-04-09 12:29:07.611728');
INSERT INTO `south_migrationhistory` VALUES(4,'hackaglobal','0002_auto__del_field_event_tags','2014-04-09 12:29:07.895451');
CREATE TABLE `taggit_tag` (`id` integer NOT NULL PRIMARY KEY, `name` varchar(100) NOT NULL, `slug` varchar(100) NOT NULL UNIQUE);
INSERT INTO `taggit_tag` VALUES(1,'playa','playa');
INSERT INTO `taggit_tag` VALUES(2,'cancun','cancun');
INSERT INTO `taggit_tag` VALUES(3,'startup','startup');
INSERT INTO `taggit_tag` VALUES(4,'loco','loco');
INSERT INTO `taggit_tag` VALUES(5,'hackathon','hackathon');
INSERT INTO `taggit_tag` VALUES(6,'party','party');
INSERT INTO `taggit_tag` VALUES(7,'weekend','weekend');
INSERT INTO `taggit_tag` VALUES(8,'town','town');
INSERT INTO `taggit_tag` VALUES(9,'cristobal','cristobal');
INSERT INTO `taggit_tag` VALUES(10,'san','san');
INSERT INTO `taggit_tag` VALUES(11,'mexico','mexico');
INSERT INTO `taggit_tag` VALUES(12,'df','df');
INSERT INTO `taggit_tag` VALUES(13,'city','city');
INSERT INTO `taggit_tag` VALUES(14,'angelhack','angelhack');
INSERT INTO `taggit_tag` VALUES(15,'angel','angel');
INSERT INTO `taggit_tag` VALUES(16,'hack','hack');
INSERT INTO `taggit_tag` VALUES(17,'targu','targu');
INSERT INTO `taggit_tag` VALUES(18,'mures','mures');
INSERT INTO `taggit_tag` VALUES(19,'meetup','meetup');
INSERT INTO `taggit_tag` VALUES(20,'discussion','discussion');
INSERT INTO `taggit_tag` VALUES(21,'iasi','iasi');
INSERT INTO `taggit_tag` VALUES(22,'cluj','cluj');
INSERT INTO `taggit_tag` VALUES(23,'conference','conference');
INSERT INTO `taggit_tag` VALUES(24,'tomania','tomania');
INSERT INTO `taggit_tag` VALUES(25,'tech','tech');
INSERT INTO `taggit_tag` VALUES(26,'techsilvania','techsilvania');
INSERT INTO `taggit_tag` VALUES(27,'timisoara','timisoara');
INSERT INTO `taggit_tag` VALUES(28,'c','c');
INSERT INTO `taggit_tag` VALUES(29,'code','code');
INSERT INTO `taggit_tag` VALUES(30,'java','java');
INSERT INTO `taggit_tag` VALUES(31,'hackers','hackers');
INSERT INTO `taggit_tag` VALUES(32,'programmers','programmers');
INSERT INTO `taggit_tag` VALUES(33,'timis','timis');
INSERT INTO `taggit_tag` VALUES(34,'romania','romania');
INSERT INTO `taggit_tag` VALUES(35,'wars','wars');
INSERT INTO `taggit_tag` VALUES(36,'python','python');
INSERT INTO `taggit_tag` VALUES(37,'kingdom','kingdom');
INSERT INTO `taggit_tag` VALUES(38,'birmingham','birmingham');
INSERT INTO `taggit_tag` VALUES(39,'united','united');
INSERT INTO `taggit_tag` VALUES(40,'hackference','hackference');
INSERT INTO `taggit_tag` VALUES(41,'uk','uk');
INSERT INTO `taggit_tag` VALUES(42,'development','development');
INSERT INTO `taggit_tag` VALUES(43,'game','game');
INSERT INTO `taggit_tag` VALUES(44,'shanghai','shanghai');
INSERT INTO `taggit_tag` VALUES(45,'china','china');
INSERT INTO `taggit_tag` VALUES(46,'asia','asia');
INSERT INTO `taggit_tag` VALUES(47,'beijing','beijing');
INSERT INTO `taggit_tag` VALUES(48,'cleanweb','cleanweb');
INSERT INTO `taggit_tag` VALUES(49,'bucharest','bucharest');
INSERT INTO `taggit_tag` VALUES(50,'dreamhack','dreamhack');
INSERT INTO `taggit_tag` VALUES(51,'dream','dream');
INSERT INTO `taggit_tag` VALUES(52,'moscow','moscow');
INSERT INTO `taggit_tag` VALUES(53,'village','village');
INSERT INTO `taggit_tag` VALUES(54,'droidcon','droidcon');
INSERT INTO `taggit_tag` VALUES(55,'october','october');
INSERT INTO `taggit_tag` VALUES(56,'russia','russia');
INSERT INTO `taggit_tag` VALUES(57,'digital','digital');
INSERT INTO `taggit_tag` VALUES(58,'southampton','southampton');
INSERT INTO `taggit_tag` VALUES(59,'dojo','dojo');
INSERT INTO `taggit_tag` VALUES(60,'coding','coding');
INSERT INTO `taggit_tag` VALUES(61,'programming','programming');
INSERT INTO `taggit_tag` VALUES(62,'competition','competition');
CREATE TABLE `taggit_taggeditem` (`id` integer NOT NULL PRIMARY KEY, `tag_id` integer NOT NULL, `object_id` integer NOT NULL, `content_type_id` integer NOT NULL);
INSERT INTO `taggit_taggeditem` VALUES(1,1,1,8);
INSERT INTO `taggit_taggeditem` VALUES(2,2,1,8);
INSERT INTO `taggit_taggeditem` VALUES(3,3,1,8);
INSERT INTO `taggit_taggeditem` VALUES(4,4,1,8);
INSERT INTO `taggit_taggeditem` VALUES(5,5,1,8);
INSERT INTO `taggit_taggeditem` VALUES(6,6,1,8);
INSERT INTO `taggit_taggeditem` VALUES(7,7,1,8);
INSERT INTO `taggit_taggeditem` VALUES(8,3,8,8);
INSERT INTO `taggit_taggeditem` VALUES(9,7,8,8);
INSERT INTO `taggit_taggeditem` VALUES(10,8,8,8);
INSERT INTO `taggit_taggeditem` VALUES(11,9,8,8);
INSERT INTO `taggit_taggeditem` VALUES(12,10,8,8);
INSERT INTO `taggit_taggeditem` VALUES(13,11,8,8);
INSERT INTO `taggit_taggeditem` VALUES(14,3,10,8);
INSERT INTO `taggit_taggeditem` VALUES(15,5,10,8);
INSERT INTO `taggit_taggeditem` VALUES(16,7,10,8);
INSERT INTO `taggit_taggeditem` VALUES(17,11,10,8);
INSERT INTO `taggit_taggeditem` VALUES(18,12,10,8);
INSERT INTO `taggit_taggeditem` VALUES(19,13,10,8);
INSERT INTO `taggit_taggeditem` VALUES(20,14,10,8);
INSERT INTO `taggit_taggeditem` VALUES(21,15,10,8);
INSERT INTO `taggit_taggeditem` VALUES(22,16,10,8);
INSERT INTO `taggit_taggeditem` VALUES(23,17,29,8);
INSERT INTO `taggit_taggeditem` VALUES(24,18,29,8);
INSERT INTO `taggit_taggeditem` VALUES(25,3,29,8);
INSERT INTO `taggit_taggeditem` VALUES(26,7,29,8);
INSERT INTO `taggit_taggeditem` VALUES(27,19,22,8);
INSERT INTO `taggit_taggeditem` VALUES(28,20,22,8);
INSERT INTO `taggit_taggeditem` VALUES(29,3,26,8);
INSERT INTO `taggit_taggeditem` VALUES(30,21,26,8);
INSERT INTO `taggit_taggeditem` VALUES(31,7,26,8);
INSERT INTO `taggit_taggeditem` VALUES(32,24,20,8);
INSERT INTO `taggit_taggeditem` VALUES(33,25,20,8);
INSERT INTO `taggit_taggeditem` VALUES(34,26,20,8);
INSERT INTO `taggit_taggeditem` VALUES(35,22,20,8);
INSERT INTO `taggit_taggeditem` VALUES(36,23,20,8);
INSERT INTO `taggit_taggeditem` VALUES(37,32,16,8);
INSERT INTO `taggit_taggeditem` VALUES(38,33,16,8);
INSERT INTO `taggit_taggeditem` VALUES(39,34,16,8);
INSERT INTO `taggit_taggeditem` VALUES(40,35,16,8);
INSERT INTO `taggit_taggeditem` VALUES(41,36,16,8);
INSERT INTO `taggit_taggeditem` VALUES(42,5,16,8);
INSERT INTO `taggit_taggeditem` VALUES(43,7,16,8);
INSERT INTO `taggit_taggeditem` VALUES(44,22,16,8);
INSERT INTO `taggit_taggeditem` VALUES(45,27,16,8);
INSERT INTO `taggit_taggeditem` VALUES(46,28,16,8);
INSERT INTO `taggit_taggeditem` VALUES(47,29,16,8);
INSERT INTO `taggit_taggeditem` VALUES(48,30,16,8);
INSERT INTO `taggit_taggeditem` VALUES(49,31,16,8);
INSERT INTO `taggit_taggeditem` VALUES(56,42,14,8);
INSERT INTO `taggit_taggeditem` VALUES(57,43,14,8);
INSERT INTO `taggit_taggeditem` VALUES(58,44,14,8);
INSERT INTO `taggit_taggeditem` VALUES(59,45,14,8);
INSERT INTO `taggit_taggeditem` VALUES(60,46,14,8);
INSERT INTO `taggit_taggeditem` VALUES(61,23,14,8);
INSERT INTO `taggit_taggeditem` VALUES(62,48,9,8);
INSERT INTO `taggit_taggeditem` VALUES(63,47,9,8);
INSERT INTO `taggit_taggeditem` VALUES(64,45,9,8);
INSERT INTO `taggit_taggeditem` VALUES(65,5,9,8);
INSERT INTO `taggit_taggeditem` VALUES(66,34,7,8);
INSERT INTO `taggit_taggeditem` VALUES(67,5,7,8);
INSERT INTO `taggit_taggeditem` VALUES(68,16,7,8);
INSERT INTO `taggit_taggeditem` VALUES(69,49,7,8);
INSERT INTO `taggit_taggeditem` VALUES(70,50,7,8);
INSERT INTO `taggit_taggeditem` VALUES(71,51,7,8);
INSERT INTO `taggit_taggeditem` VALUES(87,56,31,8);
INSERT INTO `taggit_taggeditem` VALUES(88,52,31,8);
INSERT INTO `taggit_taggeditem` VALUES(89,5,31,8);
INSERT INTO `taggit_taggeditem` VALUES(90,54,31,8);
INSERT INTO `taggit_taggeditem` VALUES(91,23,31,8);
INSERT INTO `taggit_taggeditem` VALUES(92,5,30,8);
INSERT INTO `taggit_taggeditem` VALUES(93,23,30,8);
INSERT INTO `taggit_taggeditem` VALUES(94,52,30,8);
INSERT INTO `taggit_taggeditem` VALUES(95,54,30,8);
INSERT INTO `taggit_taggeditem` VALUES(96,55,30,8);
INSERT INTO `taggit_taggeditem` VALUES(97,56,30,8);
INSERT INTO `taggit_taggeditem` VALUES(98,57,30,8);
INSERT INTO `taggit_taggeditem` VALUES(99,3,11,8);
INSERT INTO `taggit_taggeditem` VALUES(100,52,11,8);
INSERT INTO `taggit_taggeditem` VALUES(101,5,11,8);
INSERT INTO `taggit_taggeditem` VALUES(102,53,11,8);
INSERT INTO `taggit_taggeditem` VALUES(103,3,3,8);
INSERT INTO `taggit_taggeditem` VALUES(104,52,3,8);
INSERT INTO `taggit_taggeditem` VALUES(105,5,3,8);
INSERT INTO `taggit_taggeditem` VALUES(106,7,3,8);
INSERT INTO `taggit_taggeditem` VALUES(107,37,17,8);
INSERT INTO `taggit_taggeditem` VALUES(108,38,17,8);
INSERT INTO `taggit_taggeditem` VALUES(109,39,17,8);
INSERT INTO `taggit_taggeditem` VALUES(110,40,17,8);
INSERT INTO `taggit_taggeditem` VALUES(111,41,17,8);
INSERT INTO `taggit_taggeditem` VALUES(112,23,17,8);
INSERT INTO `taggit_taggeditem` VALUES(113,5,12,8);
INSERT INTO `taggit_taggeditem` VALUES(114,39,12,8);
INSERT INTO `taggit_taggeditem` VALUES(115,41,12,8);
INSERT INTO `taggit_taggeditem` VALUES(116,58,12,8);
INSERT INTO `taggit_taggeditem` VALUES(117,59,12,8);
INSERT INTO `taggit_taggeditem` VALUES(118,60,12,8);
INSERT INTO `taggit_taggeditem` VALUES(119,61,12,8);
INSERT INTO `taggit_taggeditem` VALUES(120,62,12,8);
INSERT INTO `taggit_taggeditem` VALUES(121,37,12,8);
CREATE TABLE `hackaglobal_event` (`website` varchar(100), `city` varchar(50) NOT NULL, `end` datetime, `description` text, `zip` varchar(10) NOT NULL, `country` varchar(50) NOT NULL, `longitude` real NOT NULL, `start` datetime NOT NULL, `creator_id` integer NOT NULL, `address` varchar(100) NOT NULL, `latitude` real NOT NULL, `id` integer PRIMARY KEY, `name` varchar(50) NOT NULL);
INSERT INTO `hackaglobal_event` VALUES('http://swplaya.org/','cancun','2014-04-13 20:00:00','Startup Weekend in Playa del Carmen - An insane day of hacking in the beach',' ','mexico',-87.0738851,'2014-04-11 18:00:00',5,'Playa del Carmen, Quintana Roo, Mexico',20.6295586,1,' Playa del Carmen Startup Weekend');
INSERT INTO `hackaglobal_event` VALUES('http://timisoara.startupweekend.org/','timisoara','2014-04-06 20:01:06','Startup Weekend Timisoara 2014',' ','romania',21.237499,'2014-04-06 18:01:06',2,'Timișoara, Romania',45.755539,2,'SWTimisoara');
INSERT INTO `hackaglobal_event` VALUES('http://startupweekend.org','moscow','2014-08-24 20:00:00','HackDay Moscow - Craziest weekend!',' 107031','russia',37.626285553,'2014-08-22 18:00:00',3,'Lubyanka Square, Moscow, Russia, 101000',55.7593357381,3,'Startup Weekend Moscow');
INSERT INTO `hackaglobal_event` VALUES('http://www.summerhacks.org/#home','timisoara','2014-08-25 01:00:02','Free food, Vader and Stormtrooper masks, a ping-pong table ,teams of very good programmers varying in age from high-school students to professionals, what else could you want ? So i guess we''ll see you guys here ',' ','romania',21.2217779,'2014-08-23 01:00:02',2,'City Business Centre - B, Timișoara, Romania',45.7575132,4,'Summerhacks');
INSERT INTO `hackaglobal_event` VALUES('http://www.meetup.com/TiMoDev/events/170460272/','timișoara','2014-04-27 01:17:00','Timisoara Mobile Development Group, Timisoara Google Developer Group and Timisoara Startup Hub are building an unique opportunity for mobile technology passionates!',' ','romania',21.2217361,'2014-04-25 01:17:00',2,'City Business Centre - A, Strada Coriolan Brediceanu, Timișoara, Romania',45.7569408,5,'1st ever Project Tango Hackathon Timisoara');
INSERT INTO `hackaglobal_event` VALUES('https://docs.google.com/forms/d/1vPSe_Zanejk3UzCd3ghKJHBS6A4qQHxfUI34ks2x_9Y/viewform','shanghai','2014-05-02 15:00:00','PROGRAMME RUNDOWN
Opening
Presentation by Microsoft 
Presentation by Cyberport
Panel discussion on Emerging Technology and Fundraising from Global Perspective 
Pitching competition
To register: http://bit.ly/1mtQp1a
IMPORTANT NOTES: 
Those who are interested in pitching must be ICT-related.  Each company should submit a company profile and presentation deck via email to sindykwan@cyberport.hk [subject: Microsoft x Cyberport Pitching Competition - entry] no later than 11 April 2014 (Friday) for pre-screening.  Late submission will not be considered. We will separately inform those who are shortlisted. 
Enquiry:  Sindy Kwan (Tel: 3166 3872 / Email: sindykwan@cyberport.hk)',' ','china',121.473701,'2014-05-02 13:30:00',4,'Young Entrepreneur Lounge, Hall 1E, HKCEC, Shanghai, China',31.230416,6,'Cyberport x Microsoft ');
INSERT INTO `hackaglobal_event` VALUES('http://dreamhack.ro/2014/','bucharest','2014-04-27 01:25:52','Insane meeting in Bucuresti with Cosplay,League of Lgends, Dota 2,Fifa 14 and other gameinggoodies comming to Bucuresti',' ','romania',26.0694439,'2014-04-26 01:25:52',2,'Sala Titulescu, Bucharest, Romania',44.4781964,7,'DreamHack');
INSERT INTO `hackaglobal_event` VALUES('http://sancristobalmx.startupweekend.org/','san cristobal','2014-04-13 20:00:00','The most amazing Startup Weekend in San Cristobal - one of the most beautiful and historical cities in Mexico!',' ','mexico',-72.226061,'2014-04-11 18:00:00',5,'San Cristobal, Mexico',7.764951,8,'Startup Weekend San Cristobal');
INSERT INTO `hackaglobal_event` VALUES('http://cleanweb.co/','beijing','2014-07-28 01:38:31','The Beijing Energy Network is working with the Cleanweb Initiative to organize the first Cleanweb hackathon in Asia!  We’re looking for computer programmers, product designers, business gurus, and folks simply interested in energy and environment to come out and make this an awesome event!

Cleanweb hackathons demonstrate the impact of applying information technology to resource constraints in transportation, energy, waste, water, agriculture, etc. We will bring together developers, designers and business professionals dedicated to optimizing resource use and accelerating cleantech development. Participants are tasked with building applications leveraging web, mobile social technology coupled with available open data sets and APIs',' 100080','china',116.3111024,'2014-07-27 01:38:31',2,'Danling Street, Haidian, Beijing, China, 100080',39.9787867,9,'Cleanweb Hackathon');
INSERT INTO `hackaglobal_event` VALUES('http://www.angelhack.com/event/angelhack-mexico-city-spring-2014/','mexico city','2014-06-01 20:00:00','',' ','mx',-99.133208,'2014-05-31 18:00:00',5,'Mexico City, Federal District, Mexico',19.4326077,10,'AngelHack Mexico City');
INSERT INTO `hackaglobal_event` VALUES('http://startupvillage.ru/','moscow','2014-06-03 10:55:23','The best start-up event of the year! 
Innovation `Woodstock` in the start-up village, at Гиперкуб `Сколково`','107207','russia',37.6173,'2014-06-02 10:55:23',3,'Moscow, Russia',55.755826,11,'Startup Village');
INSERT INTO `hackaglobal_event` VALUES('https://www.facebook.com/groups/SouthamptonCodeDojo/?fref=ts','southampton','2014-04-11 21:00:00','Come along to the first edition of the Coding Dojo Southampton! An awesome opportunity to relax, enjoy some free pizza and beer, and meet some awesome people!',' SO17 1TW','united-kingdom',-1.398216,'2014-04-11 19:00:00',7,'University of Southampton, Building 33',50.9378159,12,'Southampton Coding Dojo');
INSERT INTO `hackaglobal_event` VALUES('','timisoara','2014-04-12 13:00:00','A Timisoara implementation of a concept developed by an Irish-led global movement of coding clubs for kids. Bring your kids to learn to code, hack, develop websites, apps, games and more or come yourself to teach. Fun and inspiration guaranteed!

CoderDojo is a global collaboration providing free and open learning to young people, especially in programming technology.',' 300011','ro',21.2212836742,'2014-04-12 10:00:00',2,'Timisoara Startup Hub, Colorianu Bratianu St.,  Timișoara 300011, Romania',45.7571265387,13,'CodorDojo');
INSERT INTO `hackaglobal_event` VALUES('http://www.gdcchina.com/','shanghai','2014-10-21 00:00:00','The Game Developers Conference® (GDC) is the world''s largest professionals-only game industry event. Presented every spring in San Francisco, it is the essential forum for learning, inspiration, and networking for the creators of computer, console, handheld, mobile, and online games. GDC attracts over 23,000 attendees, and is the primary forum where programmers, artists, producers, game designers, audio professionals, business decision-makers and others involved in the development of interactive games gather to exchange ideas and shape the future of the industry. GDC is produced by the UBM Tech Game Network.',' 200033','china',121.3909227,'2014-10-19 00:00:00',4,'500 Zhennan Road,  200033',31.2689443,14,'Game Developers Conference China');
INSERT INTO `hackaglobal_event` VALUES('','bucharest','2014-04-07 11:42:18','27 hours of adrenaline filled, jam packed game making, or in other words a game creating marathon. Starting on 5th April and all through April 6th, you’ll take part in an intense and open-minded atmosphere at Tech Hub Bucharest.

If you love making games, the Ubisoft Bucharest Game Jam is the perfect opportunity to join a team and spend 27 awesome filled hours to create a new game, from scratch.',' ','romania',26.1038889,'2014-04-06 11:42:18',2,'Blvd Expozitiei nr.2',44.4325,15,'Ubisoft Bucharest Game Jam');
INSERT INTO `hackaglobal_event` VALUES('https://www.facebook.com/events/449064168557364/','cluj','2014-05-10 22:00:00','This competition is open to students currently enrolled at Cluj universities with good knowledge of programming languages (Java, Python and C) and familiar with virtualization tools. An eligible team is made of 2 students and has completed the first 3 steps mentioned below by the end of April. Solving the Code Wars weekly puzzles will get you closer to finals, so bring your knowledge to battle and enroll today!

Step 1: Pair up with a friend (.. or with a colleague)

Step 2: Pick a name for your team (…or a funky mascot)

Step 3: Enroll your team at CodeWarsCluj@hp.com (.. and solve our weekly challenges to get a feeling of what is coming)

Step 4: Meet us on May 10th, 2014 (@ HP Office in Maestro Business Center, 104, 21 Dec 1989 Blvd)

Step 5: Have fun solving the trials … and win cool prizes! (Laptops, LED Monitors, Backpacks)',' 400124','romania',23.602197,'2014-05-10 09:00:00',2,'Maestro Business Center, Bulevardul 21 Decembrie 1989, Cluj-Napoca 400124, Romania',46.7745684,16,'Code Wars Cluj');
INSERT INTO `hackaglobal_event` VALUES('http://2014.hackference.co.uk/information','birmingham','2014-09-21 11:53:41','Three days of talks and panels from the best in the world, with a full weekend hackathon to top it. Aimed totally at bringing more technology to those that love developing with it, giving you more to hack with than before.',' ','united-kingdom',-1.8834676,'2014-09-19 11:53:41',7,'Fazeley Street, Birmingham, West Midlands, UK',52.4788483,17,'Hackference 2.0.14');
INSERT INTO `hackaglobal_event` VALUES('http://sh.openco.asia/','shanghai','2014-04-17 23:59:59','OpenCompany Shanghai features a unique mix/blend of presentations and company visits in just 2-days. Hear first-hand from entrepreneurs and innovators how they are gaining an edge and help to transform the way we do business in Asia.',' ','china',121.473701,'2014-04-16 09:00:00',4,'All Around Town',31.230416,18,'OpenCompany Shanghai');
INSERT INTO `hackaglobal_event` VALUES('','cluj','2014-04-07 20:00:00','Computer driven cars will change the face of global transportation, with features like self-fuelling and 360 degrees vision, auto experts say.

The driver-less cars will be safer, causing fewer accidents and less congestion and will be more energy efficient, reducing the driving time and would let land currently used for parking to be used for parks and green spaces.

Adrian GROZA from UTCN will present a few projects the University is involved in and which are related to intelligent cars of the future. He will also expose his vision on the subject.',' 400000','romania',23.5998899,'2014-04-07 18:00:00',2,'Cluj-Napoca 400000, Romania',46.777248,19,'Intelligent Cars');
INSERT INTO `hackaglobal_event` VALUES('http://techsylvania.co/','cluj','2014-06-02 22:00:00','Techsylvania has invited the region’s foremost creative minds, technologists and innovators to participate in our event, where inspiration, ideas and knowledge is shared directly between individuals leading to projects and collaborations.

Listen to disruptive technology speakers deliver insights into what the future may actually be like, be inspired by successful entrepreneurs that usually got where they are by making tons of mistakes, have coffee with investors, a beer with marketing professionals, or simply recharge your battery by socializing with your peers!

The first two days (May 31st and June 1st) of the event will be a hackathon, focused on connected devices, where teams of talented people come together to hack a solution on some of the most interesting devices out there . More information and registration details will be available soon.

The third day (June 2nd) will be the main event day consisting of presentations and discussions with key influencers and exceptional international people from around the world.  The top 3 teams that come out of the Hackathon will also present on stage what they have accomplished.

This is your chance to get that extra edge and connect with people that can really make a difference!',' 400000','romania',23.5998899,'2014-05-31 09:00:00',2,'Cluj-Napoca 400000, Romania',46.777248,20,'Techsylvania');
INSERT INTO `hackaglobal_event` VALUES('http://www.itfest.hk/14/en/event_0414_MoDev_HK_2014.php','hongkong','2014-04-17 16:30:00','An international meet-up for leading mobile application developers, designers, and marketing professionals to bounce ideas and exchange views on the future of mobile computing.

MoDev Hong Kong Forum & Disruptathon 2014 (12 April; pre-registration required)
- An international forum in the morning and a Disruptathon in the afternoon.

Hong Kong International Hackathon 2014 (13 April, by invitation only)
- A hackathon for Apps teams from the US, China and Hong Kong.',' ','china',114.1302139,'2014-04-12 09:00:00',4,'Cyberport, 100 Cyberport Road',22.2618056,21,'MoDev Hong Kong');
INSERT INTO `hackaglobal_event` VALUES('','timișoara','2014-05-01 21:00:00','Once a month we have an open discussion about interesting and useful topics regarding PHP, Programming techniques, Frameworks, Databases, Patterns and so on.

There are no rules, we just talk on the selected subject. Regardless of you being an apprentice, a journeyman or a master, you are most welcome. Attendance is free.

Each time we will propose and vote for a topic. Topics and the Poll will be published at the beginning of the meetups week. Voting ends at 3PM on the event’s day.',' 300011','romania',21.2211227417,'2014-05-01 19:00:00',2,'City Business Center, Timișoara 300011, Romania',45.7570067702,22,'PHP Community Timișoara Open Discussion');
INSERT INTO `hackaglobal_event` VALUES('http://www.squirrly.co/12th-of-april-squirrly-hackathon-in-cluj-napoca-startupers-devs-invited','cluj-napoca','2014-04-13 08:00:00','You don’t have to build your own high growth tech startup to be part of one.

Join the Squirrly Hackathon and see what’s up with growing a startup.

Be part of a startup environment of building awesome things for the web for 24 hours, on the 12th of April.

Location :: Cluj Hub, in Cluj-Napoca, the heart of Transylvania.',' 400000','romania',23.5998899,'2014-04-12 08:00:00',2,'Cluj-Napoca 400000, Romania',46.777248,23,'Squirrly Hackathon');
INSERT INTO `hackaglobal_event` VALUES('http://rotechcourses.com/portfolio/python-for-programmers/','cluj-napoca','2014-05-09 17:00:00','This course is designed for developers with experience of other languages who need to get up to speed on Python. At the end of this course the students will know the essentials of the Python language, how to use Python’s module system to structure code, and how to approach the development of Python programs. The class will focus on Python 3, unless Python 2 is specifically requested.

The course topics cover:

Built-in types and object model
Flow control and exceptions
Class definition, inheritance, and common usage patterns
Program organisation with modules and packages
The Python standard library
Obtaining and installing Python packages
Comprehensions, generators, and iteration
Serialization, unit testing, and filesystem interaction
Debugging
We believe that students learn best by doing, so they will start coding very early in this course. Testing is integral to to our approach, and we start immediately with working programs.',' 400000','romania',23.5998899,'2014-05-07 09:00:00',2,'Cluj-Napoca 400000, Romania',46.777248,24,'Python for Programmers');
INSERT INTO `hackaglobal_event` VALUES('http://iasi.codecamp.ro/','iași','2014-05-10 18:00:00','CodeCamp is your local IT community & conference, here in Iasi, aiming for better communication among the IT people.
We started in 2009 and along the way we had different conference formats, from 3 days 30 people hands-on lab & coding sessions on various technologies and disciplines; trying to fulfill the continuous demand from the community we''re now doing conferences with several parallel tracks and 500+ participants.

Interested in Java, .NET, Mobile, Agile, PHP, Ruby, Project Management, Business Analysis and many others? Join CodeCamp and meet smart people sharing from their own real life experiences.

','700054','romania',27.5902778,'2014-05-10 08:00:00',2,'Iași, Romania',47.1569444,25,'CodeCamp Iasi');
INSERT INTO `hackaglobal_event` VALUES('http://iasi.codecamp.ro/','iași','2014-05-18 18:30:00','At Startup Weekend Iasi you can bring that idea to life.  For just one weekend, you will team up with a mix of fantastic people (developers, business people, marketers). Together you will work on a business idea. We have planned to bring you the best mentors that share your appetite to change the world. They are going to support your entrepreneurial steps throughout the 54 hours of the event.  You will walk away from here with more contacts, with more ideas and with more energy. You can also bring all you learn here back to your day job or you can convey the know-how into a new startup. It’s a win-win. ',' 700054','romania',27.5902778,'2014-05-16 18:30:00',2,'Iași, Romania',47.1569444,26,'Startup Weekend Iasi');
INSERT INTO `hackaglobal_event` VALUES('http://itcamp.ro/','iași','2014-05-23 00:00:00','ITCamp is the largest premium conference focusing on Microsoft technologies in Romania, now at it’s 4th edition. You’ll spend two great days among well-known speakers who will be covering 4 separate tracks of high-quality content.

ITCamp is back with yet another edition: 2 days, 4 tracks, over 30 speakers, 40+ hours of content and open panels, pre-conference workshops and lots of networking opportunities.

DON’T MISS ITCAMP IF:

You want to be up to date with the latest IT technologies
You appreciate the chance to interact with highly skilled professionals in your area of expertise
You are an IT manager, team lead, programmer, database or systems administrator and you work with the Microsoft Application Platform
You want to find out more about useful stuff meant to improve your existing skillset
You enjoy presentations held by experienced speakers, who are well known across the country or even across the world
You wish to attend trainings that are both cost-efficient and packed with useful info
You intend to expand your customer or collaborator/partner portfolio
If any of the rows above rings a bell, we’d like to invite you at ITCamp: a premium conference, where the latest technology and a lot of amazing people will meet under the same roof.','700054','romania',27.5902778,'2014-05-22 00:00:00',2,'Iași, Romania',47.1569444,27,'ITCamp 2014');
INSERT INTO `hackaglobal_event` VALUES('http://itcamp.ro/','iași','2014-05-23 00:00:00','ITCamp is the largest premium conference focusing on Microsoft technologies in Romania, now at it’s 4th edition. You’ll spend two great days among well-known speakers who will be covering 4 separate tracks of high-quality content.

ITCamp is back with yet another edition: 2 days, 4 tracks, over 30 speakers, 40+ hours of content and open panels, pre-conference workshops and lots of networking opportunities.

DON’T MISS ITCAMP IF:

You want to be up to date with the latest IT technologies
You appreciate the chance to interact with highly skilled professionals in your area of expertise
You are an IT manager, team lead, programmer, database or systems administrator and you work with the Microsoft Application Platform
You want to find out more about useful stuff meant to improve your existing skillset
You enjoy presentations held by experienced speakers, who are well known across the country or even across the world
You wish to attend trainings that are both cost-efficient and packed with useful info
You intend to expand your customer or collaborator/partner portfolio
If any of the rows above rings a bell, we’d like to invite you at ITCamp: a premium conference, where the latest technology and a lot of amazing people will meet under the same roof.','700054','romania',27.5902778,'2014-05-22 00:00:00',2,'Iași, Romania',47.1569444,28,'ITCamp 2014');
INSERT INTO `hackaglobal_event` VALUES('','targu-mures','2014-05-25 23:00:00','Startup Weekends are weekend-long, hands-on experiences where entrepreneurs and aspiring entrepreneurs can find out if startup ideas are viable.  On average, half of Startup Weekend’s attendees have technical or design backgrounds, the other half have business backgrounds.

Beginning with open mic pitches on Friday, attendees bring their best ideas and inspire others to join their team. Over Saturday and Sunday teams focus on customer development, validating their ideas, practicing LEAN Startup Methodologies and building a minimal viable product. On Sunday evening teams demo their prototypes and receive valuable feedback from a panel of experts.','540304','romania',24.5625,'2014-05-23 00:00:00',2,'Târgu Mureș, Romania',46.5455556,29,'Startup Weekend Targu Mures');
INSERT INTO `hackaglobal_event` VALUES('http://droidcon.com/','moscow','2014-04-12 18:00:00','Biggest Android Developers Conference! First to be held in Moscow on 11-12 April 2014 at the Digital October center.','119072','russia',37.6173,'2014-04-11 09:00:00',3,'Digital October',55.755826,30,'DroidCon Moscow');
INSERT INTO `hackaglobal_event` VALUES('http://ru.droidcon.com/2014/xakaton/','moscow','2014-04-12 19:00:00','An event during which experts from different areas of software development (programmers, designers, managers) are working together to create web service or mobile application. 

The DroidCon is one of the biggest Android conferences around the world - this will be the first one taking place in Moscow','119072','russia',37.6173,'2014-04-11 09:00:00',3,'Moscow, Russia',55.755826,31,'DroidCon Hackathon Moscow');
CREATE INDEX `django_admin_log_6340c63c` ON `django_admin_log` (`user_id`);
CREATE INDEX `django_admin_log_37ef4eb4` ON `django_admin_log` (`content_type_id`);
CREATE INDEX `auth_permission_37ef4eb4` ON `auth_permission` (`content_type_id`);
CREATE INDEX `auth_group_permissions_5f412f9a` ON `auth_group_permissions` (`group_id`);
CREATE INDEX `auth_group_permissions_83d7f98b` ON `auth_group_permissions` (`permission_id`);
CREATE INDEX `auth_user_groups_6340c63c` ON `auth_user_groups` (`user_id`);
CREATE INDEX `auth_user_groups_5f412f9a` ON `auth_user_groups` (`group_id`);
CREATE INDEX `auth_user_user_permissions_6340c63c` ON `auth_user_user_permissions` (`user_id`);
CREATE INDEX `auth_user_user_permissions_83d7f98b` ON `auth_user_user_permissions` (`permission_id`);
CREATE INDEX `django_session_b7b81f0c` ON `django_session` (`expire_date`);
CREATE INDEX `hackaglobal_attendee_7c5d9048` ON `hackaglobal_attendee` (`attendee_id`);
CREATE INDEX `hackaglobal_attendee_a41e20fe` ON `hackaglobal_attendee` (`event_id`);
CREATE INDEX `hackaglobal_staff_f0a7d083` ON `hackaglobal_staff` (`staff_id`);
CREATE INDEX `hackaglobal_staff_a41e20fe` ON `hackaglobal_staff` (`event_id`);
CREATE INDEX `social_auth_usersocialauth_6340c63c` ON `social_auth_usersocialauth` (`user_id`);
CREATE INDEX `social_auth_code_09bb5fb3` ON `social_auth_code` (`code`);
CREATE INDEX `taggit_taggeditem_5659cca2` ON `taggit_taggeditem` (`tag_id`);
CREATE INDEX `taggit_taggeditem_846f0221` ON `taggit_taggeditem` (`object_id`);
CREATE INDEX `taggit_taggeditem_37ef4eb4` ON `taggit_taggeditem` (`content_type_id`);
CREATE UNIQUE INDEX `taggit_tag_name` ON `taggit_tag`(`name`);
