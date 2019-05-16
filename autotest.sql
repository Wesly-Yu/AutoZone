/*
Navicat MySQL Data Transfer

Source Server         : autotest
Source Server Version : 50717
Source Host           : 127.0.0.1:3306
Source Database       : autotest

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2019-01-09 11:42:14
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for apitest_create_product
-- ----------------------------
DROP TABLE IF EXISTS `apitest_create_product`;
CREATE TABLE `apitest_create_product` (
  `productid` int(11) NOT NULL AUTO_INCREMENT,
  `modelname` varchar(10) NOT NULL,
  `productname` varchar(200) NOT NULL,
  `tester` varchar(200) NOT NULL,
  `developer` varchar(200) NOT NULL,
  `productdesc` varchar(200) NOT NULL,
  `status` varchar(20) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  PRIMARY KEY (`productid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of apitest_create_product
-- ----------------------------

-- ----------------------------
-- Table structure for apitest_email
-- ----------------------------
DROP TABLE IF EXISTS `apitest_email`;
CREATE TABLE `apitest_email` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sender` varchar(20) NOT NULL,
  `receivers` varchar(100) NOT NULL,
  `host_dir` varchar(20) NOT NULL,
  `email_port` varchar(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `passwd` varchar(20) NOT NULL,
  `Headerfrom` varchar(20) NOT NULL,
  `Headerto` varchar(100) NOT NULL,
  `subject` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of apitest_email
-- ----------------------------

-- ----------------------------
-- Table structure for apitest_need_data_apis
-- ----------------------------
DROP TABLE IF EXISTS `apitest_need_data_apis`;
CREATE TABLE `apitest_need_data_apis` (
  `process_name` varchar(100) NOT NULL,
  `productid` int(11) NOT NULL AUTO_INCREMENT,
  `modelname` varchar(100) NOT NULL,
  `depend_Apiname` varchar(100) NOT NULL,
  `Apiurl_data` varchar(200) NOT NULL,
  `Apimethod` varchar(20) NOT NULL,
  `Apiheader` varchar(800) NOT NULL,
  `Apiformdata` varchar(800) NOT NULL,
  `Apidependdata` varchar(100) NOT NULL,
  `Apiexpectresult` varchar(200) NOT NULL,
  `Apischarger` varchar(50) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  PRIMARY KEY (`productid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of apitest_need_data_apis
-- ----------------------------

-- ----------------------------
-- Table structure for apitest_process_apis_task
-- ----------------------------
DROP TABLE IF EXISTS `apitest_process_apis_task`;
CREATE TABLE `apitest_process_apis_task` (
  `task_id` int(11) NOT NULL AUTO_INCREMENT,
  `task_process_name` varchar(100) NOT NULL,
  `task_modelname` varchar(100) NOT NULL,
  `task_depend_Apiname` varchar(100) NOT NULL,
  `task_Apiurl_data` varchar(1024) NOT NULL,
  `task_Apimethod` varchar(20) NOT NULL,
  `task_Apiheader` varchar(800) NOT NULL,
  `task_Apiformdata` varchar(800) NOT NULL,
  `task_Apidependdata` varchar(100) NOT NULL,
  `task_Apiexpectresult` varchar(200) NOT NULL,
  `task_status` varchar(200) NOT NULL,
  `task_response` varchar(500) NOT NULL,
  `task_retry` varchar(10) NOT NULL,
  `task_result` varchar(20) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  PRIMARY KEY (`task_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of apitest_process_apis_task
-- ----------------------------

-- ----------------------------
-- Table structure for apitest_singel_apis
-- ----------------------------
DROP TABLE IF EXISTS `apitest_singel_apis`;
CREATE TABLE `apitest_singel_apis` (
  `productid` int(11) NOT NULL AUTO_INCREMENT,
  `Product` varchar(100) NOT NULL,
  `Apiname` varchar(100) NOT NULL,
  `Apiurl` varchar(200) DEFAULT NULL,
  `Apiheader` varchar(800) DEFAULT NULL,
  `Apiformdata` varchar(800) NOT NULL,
  `Apimethod` varchar(20) NOT NULL,
  `Apiexpectresult` varchar(200) NOT NULL,
  `Apischarger` varchar(50) NOT NULL,
  `create_time` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`productid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of apitest_singel_apis
-- ----------------------------

-- ----------------------------
-- Table structure for apitest_singel_apis_task
-- ----------------------------
DROP TABLE IF EXISTS `apitest_singel_apis_task`;
CREATE TABLE `apitest_singel_apis_task` (
  `task_id` int(11) NOT NULL AUTO_INCREMENT,
  `task_modelname` varchar(200) NOT NULL,
  `task_casename` varchar(200) NOT NULL,
  `task_Apiurl` varchar(200) DEFAULT NULL,
  `task_Apiheader` varchar(800) DEFAULT NULL,
  `task_Apiformdata` varchar(800) NOT NULL,
  `task_Apimethod` varchar(20) NOT NULL,
  `task_Apiexpectresult` varchar(200) NOT NULL,
  `task_status` varchar(200) NOT NULL,
  `task_response` varchar(500) NOT NULL,
  `task_retry` varchar(10) NOT NULL,
  `task_result` varchar(20) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  PRIMARY KEY (`task_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of apitest_singel_apis_task
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can view log entry', '1', 'view_logentry');
INSERT INTO `auth_permission` VALUES ('5', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can view permission', '2', 'view_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('11', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('12', 'Can view group', '3', 'view_group');
INSERT INTO `auth_permission` VALUES ('13', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('14', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('16', 'Can view user', '4', 'view_user');
INSERT INTO `auth_permission` VALUES ('17', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('18', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('19', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('20', 'Can view content type', '5', 'view_contenttype');
INSERT INTO `auth_permission` VALUES ('21', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('22', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('23', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('24', 'Can view session', '6', 'view_session');
INSERT INTO `auth_permission` VALUES ('25', 'Can add create_product', '7', 'add_create_product');
INSERT INTO `auth_permission` VALUES ('26', 'Can change create_product', '7', 'change_create_product');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete create_product', '7', 'delete_create_product');
INSERT INTO `auth_permission` VALUES ('28', 'Can view create_product', '7', 'view_create_product');
INSERT INTO `auth_permission` VALUES ('29', 'Can add email', '8', 'add_email');
INSERT INTO `auth_permission` VALUES ('30', 'Can change email', '8', 'change_email');
INSERT INTO `auth_permission` VALUES ('31', 'Can delete email', '8', 'delete_email');
INSERT INTO `auth_permission` VALUES ('32', 'Can view email', '8', 'view_email');
INSERT INTO `auth_permission` VALUES ('33', 'Can add need_data_ apis', '9', 'add_need_data_apis');
INSERT INTO `auth_permission` VALUES ('34', 'Can change need_data_ apis', '9', 'change_need_data_apis');
INSERT INTO `auth_permission` VALUES ('35', 'Can delete need_data_ apis', '9', 'delete_need_data_apis');
INSERT INTO `auth_permission` VALUES ('36', 'Can view need_data_ apis', '9', 'view_need_data_apis');
INSERT INTO `auth_permission` VALUES ('37', 'Can add process_apis_task', '10', 'add_process_apis_task');
INSERT INTO `auth_permission` VALUES ('38', 'Can change process_apis_task', '10', 'change_process_apis_task');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete process_apis_task', '10', 'delete_process_apis_task');
INSERT INTO `auth_permission` VALUES ('40', 'Can view process_apis_task', '10', 'view_process_apis_task');
INSERT INTO `auth_permission` VALUES ('41', 'Can add singel_ apis', '11', 'add_singel_apis');
INSERT INTO `auth_permission` VALUES ('42', 'Can change singel_ apis', '11', 'change_singel_apis');
INSERT INTO `auth_permission` VALUES ('43', 'Can delete singel_ apis', '11', 'delete_singel_apis');
INSERT INTO `auth_permission` VALUES ('44', 'Can view singel_ apis', '11', 'view_singel_apis');
INSERT INTO `auth_permission` VALUES ('45', 'Can add singel_apis_task', '12', 'add_singel_apis_task');
INSERT INTO `auth_permission` VALUES ('46', 'Can change singel_apis_task', '12', 'change_singel_apis_task');
INSERT INTO `auth_permission` VALUES ('47', 'Can delete singel_apis_task', '12', 'delete_singel_apis_task');
INSERT INTO `auth_permission` VALUES ('48', 'Can view singel_apis_task', '12', 'view_singel_apis_task');
INSERT INTO `auth_permission` VALUES ('49', 'Can add django job', '13', 'add_djangojob');
INSERT INTO `auth_permission` VALUES ('50', 'Can change django job', '13', 'change_djangojob');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete django job', '13', 'delete_djangojob');
INSERT INTO `auth_permission` VALUES ('52', 'Can view django job', '13', 'view_djangojob');
INSERT INTO `auth_permission` VALUES ('53', 'Can add django job execution', '14', 'add_djangojobexecution');
INSERT INTO `auth_permission` VALUES ('54', 'Can change django job execution', '14', 'change_djangojobexecution');
INSERT INTO `auth_permission` VALUES ('55', 'Can delete django job execution', '14', 'delete_djangojobexecution');
INSERT INTO `auth_permission` VALUES ('56', 'Can view django job execution', '14', 'view_djangojobexecution');
INSERT INTO `auth_permission` VALUES ('57', 'Can add web测试步骤', '15', 'add_webcase');
INSERT INTO `auth_permission` VALUES ('58', 'Can change web测试步骤', '15', 'change_webcase');
INSERT INTO `auth_permission` VALUES ('59', 'Can delete web测试步骤', '15', 'delete_webcase');
INSERT INTO `auth_permission` VALUES ('60', 'Can view web测试步骤', '15', 'view_webcase');
INSERT INTO `auth_permission` VALUES ('61', 'Can add webcasestep', '16', 'add_webcasestep');
INSERT INTO `auth_permission` VALUES ('62', 'Can change webcasestep', '16', 'change_webcasestep');
INSERT INTO `auth_permission` VALUES ('63', 'Can delete webcasestep', '16', 'delete_webcasestep');
INSERT INTO `auth_permission` VALUES ('64', 'Can view webcasestep', '16', 'view_webcasestep');
INSERT INTO `auth_permission` VALUES ('65', 'Can add webcase_keywords', '17', 'add_webcase_keywords');
INSERT INTO `auth_permission` VALUES ('66', 'Can change webcase_keywords', '17', 'change_webcase_keywords');
INSERT INTO `auth_permission` VALUES ('67', 'Can delete webcase_keywords', '17', 'delete_webcase_keywords');
INSERT INTO `auth_permission` VALUES ('68', 'Can view webcase_keywords', '17', 'view_webcase_keywords');
INSERT INTO `auth_permission` VALUES ('69', 'Can add webtest_task', '18', 'add_webtest_task');
INSERT INTO `auth_permission` VALUES ('70', 'Can change webtest_task', '18', 'change_webtest_task');
INSERT INTO `auth_permission` VALUES ('71', 'Can delete webtest_task', '18', 'delete_webtest_task');
INSERT INTO `auth_permission` VALUES ('72', 'Can view webtest_task', '18', 'view_webtest_task');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$120000$YFT2by10K3Ge$ynqhW4mFVeo9qJKG03x3hYG3xRFJ1It0k2hI+GaPkIU=', '2019-01-07 01:14:19.545036', '1', 'wesley', '', '', '1633235633@qq.com', '1', '1', '2018-12-19 09:10:36.298620');
INSERT INTO `auth_user` VALUES ('2', 'pbkdf2_sha256$120000$66njrAjJksTD$dAsGoHhzmLchR3aS3fTXftD72tpx5dNXlpIyERvgeII=', null, '0', 'test', '', '', '', '0', '1', '2018-12-19 09:11:31.414994');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2018-12-19 09:11:31.514938', '2', 'test', '1', '[{\"added\": {}}]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('2', '2018-12-19 10:13:04.236934', '1', 'Webcase object (1)', '1', '[{\"added\": {}}, {\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (1)\"}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('3', '2018-12-19 10:47:30.589936', '1', 'Webcase object (1)', '3', '', '15', '1');
INSERT INTO `django_admin_log` VALUES ('4', '2018-12-19 10:47:58.588110', '2', 'Webcase object (2)', '1', '[{\"added\": {}}, {\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (2)\"}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('5', '2018-12-19 11:13:45.188692', '3', 'Webcase object (3)', '1', '[{\"added\": {}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('6', '2018-12-20 03:46:33.619241', '2', 'Webcase object (2)', '2', '[]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('7', '2018-12-20 05:57:16.662836', '2', 'Webcase object (2)', '2', '[{\"changed\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (2)\", \"fields\": [\"webcomments\"]}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('8', '2018-12-20 07:13:34.126253', '2', 'Webcase object (2)', '2', '[{\"changed\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (2)\", \"fields\": [\"webkwargestwo\"]}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('9', '2018-12-20 07:24:14.451093', '2', 'Webcase object (2)', '2', '[{\"changed\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (2)\", \"fields\": [\"webkwargestwo\"]}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('10', '2018-12-21 01:33:12.511697', '2', 'Webcase object (2)', '2', '[{\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (3)\"}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('11', '2018-12-21 01:41:40.715834', '2', 'Webcase object (2)', '2', '[{\"deleted\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (None)\"}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('12', '2018-12-21 01:42:02.517259', '2', 'Webcase object (2)', '2', '[{\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (4)\"}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('13', '2018-12-21 02:46:22.051918', '2', 'Webcase object (2)', '3', '', '15', '1');
INSERT INTO `django_admin_log` VALUES ('14', '2018-12-21 02:47:18.567353', '4', 'Webcase object (4)', '1', '[{\"added\": {}}, {\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (5)\"}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('15', '2018-12-21 02:48:17.604332', '3', 'Webcase object (3)', '3', '', '15', '1');
INSERT INTO `django_admin_log` VALUES ('16', '2018-12-24 06:42:31.788479', '4', 'Webcase object (4)', '2', '[{\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (6)\"}}, {\"changed\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (5)\", \"fields\": [\"webfindmethod\", \"webkwargesone\", \"webkwargestwo\"]}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('17', '2018-12-24 07:21:13.559356', '4', 'Webcase object (4)', '3', '', '15', '1');
INSERT INTO `django_admin_log` VALUES ('18', '2018-12-24 07:22:24.745289', '5', 'Webcase object (5)', '1', '[{\"added\": {}}, {\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (7)\"}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('19', '2018-12-24 07:28:44.053380', '5', 'Webcase object (5)', '2', '[{\"changed\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (7)\", \"fields\": [\"webfindmethod\", \"webkwargesone\", \"webkwargestwo\"]}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('20', '2018-12-24 07:47:52.549128', '5', 'Webcase object (5)', '2', '[{\"changed\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (7)\", \"fields\": [\"webkwargesone\"]}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('21', '2018-12-24 07:52:23.275404', '5', 'Webcase object (5)', '2', '[{\"changed\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (7)\", \"fields\": [\"webkwargesone\"]}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('22', '2018-12-24 07:55:55.066979', '5', 'Webcase object (5)', '2', '[{\"changed\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (7)\", \"fields\": [\"webtestlocation\"]}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('23', '2018-12-24 08:07:08.973364', '5', 'Webcase object (5)', '2', '[{\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (8)\"}}, {\"changed\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (7)\", \"fields\": [\"webfindmethod\", \"webkwargesone\", \"webkwargestwo\"]}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('24', '2018-12-25 07:36:44.908385', '5', 'Webcase object (5)', '2', '[{\"changed\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (7)\", \"fields\": [\"webkwargesone\"]}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('25', '2018-12-25 07:37:09.509474', '5', 'Webcase object (5)', '2', '[{\"changed\": {\"fields\": [\"webcasename\"]}}, {\"changed\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (7)\", \"fields\": [\"webcasename\"]}}, {\"changed\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (8)\", \"fields\": [\"webcasename\"]}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('26', '2018-12-25 07:50:23.368102', '5', 'Webcase object (5)', '2', '[]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('27', '2018-12-25 07:55:29.669814', '5', 'Webcase object (5)', '2', '[{\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (9)\"}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('28', '2018-12-25 07:56:25.842163', '5', 'Webcase object (5)', '3', '', '15', '1');
INSERT INTO `django_admin_log` VALUES ('29', '2018-12-25 08:00:55.804748', '6', 'Webcase object (6)', '1', '[{\"added\": {}}, {\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (10)\"}}, {\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (11)\"}}, {\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (12)\"}}, {\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (13)\"}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('30', '2018-12-25 08:01:11.350129', '6', 'Webcase object (6)', '2', '[{\"changed\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (13)\", \"fields\": [\"webfindmethod\"]}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('31', '2018-12-26 03:32:31.318319', '6', 'Webcase object (6)', '2', '[]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('32', '2018-12-26 05:47:12.589486', '6', 'Webcase object (6)', '2', '[{\"deleted\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (None)\"}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('33', '2018-12-26 06:24:35.223121', '6', 'Webcase object (6)', '2', '[{\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (14)\"}}, {\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (15)\"}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('34', '2018-12-26 08:06:38.832330', '6', 'Webcase object (6)', '2', '[{\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (16)\"}}, {\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (17)\"}}, {\"changed\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (15)\", \"fields\": [\"webfindmethod\"]}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('35', '2018-12-26 08:13:54.371063', '6', 'Webcase object (6)', '2', '[{\"changed\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (15)\", \"fields\": [\"webkwargesone\"]}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('36', '2018-12-26 08:24:10.100683', '6', 'Webcase object (6)', '2', '[{\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (18)\"}}, {\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (19)\"}}, {\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (20)\"}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('37', '2018-12-26 09:27:47.607492', '6', 'Webcase object (6)', '2', '[{\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (21)\"}}, {\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (22)\"}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('38', '2019-01-02 02:28:58.761277', '6', 'Webcase object (6)', '2', '[{\"changed\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (20)\", \"fields\": [\"webfindmethod\"]}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('39', '2019-01-02 03:01:27.939366', '6', 'Webcase object (6)', '2', '[{\"changed\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (21)\", \"fields\": [\"webkwargesone\"]}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('40', '2019-01-07 01:23:43.699530', '7', 'Webcase object (7)', '1', '[{\"added\": {}}, {\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (23)\"}}, {\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (24)\"}}, {\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (25)\"}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('41', '2019-01-07 01:29:20.660073', '7', 'Webcase object (7)', '2', '[{\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (26)\"}}, {\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (27)\"}}, {\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (28)\"}}, {\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (29)\"}}, {\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (30)\"}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('42', '2019-01-07 01:32:49.927317', '7', 'Webcase object (7)', '2', '[{\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (31)\"}}, {\"changed\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (29)\", \"fields\": [\"webfindmethod\", \"webkwargesone\"]}}, {\"changed\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (30)\", \"fields\": [\"webfindmethod\", \"webkwargesone\", \"webkwargestwo\"]}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('43', '2019-01-07 02:15:56.166303', '7', 'Webcase object (7)', '2', '[{\"added\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (32)\"}}, {\"changed\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (24)\", \"fields\": [\"webkwargesone\"]}}, {\"changed\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (25)\", \"fields\": [\"webfindmethod\", \"webkwargesone\"]}}, {\"changed\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (26)\", \"fields\": [\"webfindmethod\", \"webkwargesone\", \"webkwargestwo\"]}}, {\"changed\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (27)\", \"fields\": [\"webfindmethod\", \"webkwargesone\", \"webkwargestwo\"]}}, {\"changed\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (28)\", \"fields\": [\"webkwargesone\", \"webkwargestwo\"]}}, {\"changed\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (29)\", \"fields\": [\"webfindmethod\", \"webkwargesone\", \"webkwargestwo\"]}}, {\"changed\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (30)\", \"fields\": [\"webfindmethod\", \"webkwargesone\", \"webkwargestwo\"]}}, {\"changed\": {\"name\": \"webcasestep\", \"object\": \"Webcasestep object (31)\", \"fields\": [\"webcasename\", \"webfindmethod\", \"webkwargesone\"]}}]', '15', '1');

-- ----------------------------
-- Table structure for django_apscheduler_djangojob
-- ----------------------------
DROP TABLE IF EXISTS `django_apscheduler_djangojob`;
CREATE TABLE `django_apscheduler_djangojob` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `next_run_time` datetime(6) DEFAULT NULL,
  `job_state` longblob NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `django_apscheduler_djangojob_next_run_time_2f022619` (`next_run_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_apscheduler_djangojob
-- ----------------------------

-- ----------------------------
-- Table structure for django_apscheduler_djangojobexecution
-- ----------------------------
DROP TABLE IF EXISTS `django_apscheduler_djangojobexecution`;
CREATE TABLE `django_apscheduler_djangojobexecution` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` varchar(50) NOT NULL,
  `run_time` datetime(6) NOT NULL,
  `duration` decimal(15,2) DEFAULT NULL,
  `started` decimal(15,2) DEFAULT NULL,
  `finished` decimal(15,2) DEFAULT NULL,
  `exception` varchar(1000) DEFAULT NULL,
  `traceback` longtext,
  `job_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_apscheduler_d_job_id_daf5090a_fk_django_ap` (`job_id`),
  KEY `django_apscheduler_djangojobexecution_run_time_16edd96b` (`run_time`),
  CONSTRAINT `django_apscheduler_d_job_id_daf5090a_fk_django_ap` FOREIGN KEY (`job_id`) REFERENCES `django_apscheduler_djangojob` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_apscheduler_djangojobexecution
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('7', 'apitest', 'create_product');
INSERT INTO `django_content_type` VALUES ('8', 'apitest', 'email');
INSERT INTO `django_content_type` VALUES ('9', 'apitest', 'need_data_apis');
INSERT INTO `django_content_type` VALUES ('10', 'apitest', 'process_apis_task');
INSERT INTO `django_content_type` VALUES ('11', 'apitest', 'singel_apis');
INSERT INTO `django_content_type` VALUES ('12', 'apitest', 'singel_apis_task');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('13', 'django_apscheduler', 'djangojob');
INSERT INTO `django_content_type` VALUES ('14', 'django_apscheduler', 'djangojobexecution');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('15', 'webtest', 'webcase');
INSERT INTO `django_content_type` VALUES ('16', 'webtest', 'webcasestep');
INSERT INTO `django_content_type` VALUES ('17', 'webtest', 'webcase_keywords');
INSERT INTO `django_content_type` VALUES ('18', 'webtest', 'webtest_task');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2018-12-19 09:07:58.186263');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2018-12-19 09:08:03.600906');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2018-12-19 09:08:04.900349');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2018-12-19 09:08:04.954571');
INSERT INTO `django_migrations` VALUES ('5', 'admin', '0003_logentry_add_action_flag_choices', '2018-12-19 09:08:04.974560');
INSERT INTO `django_migrations` VALUES ('6', 'apitest', '0001_initial', '2018-12-19 09:08:05.981884');
INSERT INTO `django_migrations` VALUES ('7', 'contenttypes', '0002_remove_content_type_name', '2018-12-19 09:08:07.084981');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0002_alter_permission_name_max_length', '2018-12-19 09:08:07.640581');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0003_alter_user_email_max_length', '2018-12-19 09:08:08.029431');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0004_alter_user_username_opts', '2018-12-19 09:08:08.048702');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0005_alter_user_last_login_null', '2018-12-19 09:08:08.912033');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0006_require_contenttypes_0002', '2018-12-19 09:08:08.962028');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0007_alter_validators_add_error_messages', '2018-12-19 09:08:09.007999');
INSERT INTO `django_migrations` VALUES ('14', 'auth', '0008_alter_user_username_max_length', '2018-12-19 09:08:09.810071');
INSERT INTO `django_migrations` VALUES ('15', 'auth', '0009_alter_user_last_name_max_length', '2018-12-19 09:08:10.897861');
INSERT INTO `django_migrations` VALUES ('16', 'django_apscheduler', '0001_initial', '2018-12-19 09:08:12.625100');
INSERT INTO `django_migrations` VALUES ('17', 'django_apscheduler', '0002_auto_20180412_0758', '2018-12-19 09:08:13.058222');
INSERT INTO `django_migrations` VALUES ('18', 'sessions', '0001_initial', '2018-12-19 09:08:13.549207');
INSERT INTO `django_migrations` VALUES ('19', 'webtest', '0001_initial', '2018-12-19 09:08:45.589286');
INSERT INTO `django_migrations` VALUES ('20', 'webtest', '0002_auto_20181219_1805', '2018-12-19 10:06:01.354762');
INSERT INTO `django_migrations` VALUES ('21', 'webtest', '0003_auto_20181219_1807', '2018-12-19 10:07:16.453382');
INSERT INTO `django_migrations` VALUES ('22', 'webtest', '0004_remove_webcasestep_webtestlocation', '2018-12-20 08:26:20.395831');
INSERT INTO `django_migrations` VALUES ('23', 'webtest', '0005_webcasestep_webtestlocation', '2018-12-20 08:38:50.912848');
INSERT INTO `django_migrations` VALUES ('24', 'webtest', '0006_auto_20181221_0935', '2018-12-21 01:35:16.373294');
INSERT INTO `django_migrations` VALUES ('25', 'webtest', '0007_auto_20181221_0937', '2018-12-21 01:37:41.114888');
INSERT INTO `django_migrations` VALUES ('26', 'webtest', '0008_auto_20181225_1543', '2018-12-25 07:43:33.624545');
INSERT INTO `django_migrations` VALUES ('27', 'webtest', '0002_remove_webcasestep_webcasename', '2019-01-07 02:19:43.942856');
INSERT INTO `django_migrations` VALUES ('28', 'webtest', '0003_webtest_task', '2019-01-07 09:21:53.863314');
INSERT INTO `django_migrations` VALUES ('29', 'webtest', '0004_webtest_task_task_stepdesc', '2019-01-08 02:49:19.585097');
INSERT INTO `django_migrations` VALUES ('30', 'webtest', '0005_webtest_task_case_id', '2019-01-08 06:19:26.789775');
INSERT INTO `django_migrations` VALUES ('31', 'webtest', '0006_auto_20190108_1435', '2019-01-08 06:36:11.145191');
INSERT INTO `django_migrations` VALUES ('32', 'webtest', '0002_auto_20190109_1141', '2019-01-09 03:41:25.742299');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('3prhejwgdaxohn61vnm2muyk1tllenuu', 'MmM2ZjVkMzNjY2JlZTBkZjk2N2JhZjAxNjFhNmQ3ZmYzNTA5YmQ1MDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhZDQ5NjhlODNhNWQ4ZjI2YTZjYzgwNTk4MzdhZDBjMWVhN2RlZTcxIiwidXNlciI6Indlc2xleSJ9', '2019-01-05 02:38:42.702775');
INSERT INTO `django_session` VALUES ('c6t7aue5ucyrtzd1bf269pxiiohphe77', 'MmM2ZjVkMzNjY2JlZTBkZjk2N2JhZjAxNjFhNmQ3ZmYzNTA5YmQ1MDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhZDQ5NjhlODNhNWQ4ZjI2YTZjYzgwNTk4MzdhZDBjMWVhN2RlZTcxIiwidXNlciI6Indlc2xleSJ9', '2019-01-03 03:46:15.494251');
INSERT INTO `django_session` VALUES ('ybwimdsp1cutj05ollqjnphif1x3jewa', 'MmM2ZjVkMzNjY2JlZTBkZjk2N2JhZjAxNjFhNmQ3ZmYzNTA5YmQ1MDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhZDQ5NjhlODNhNWQ4ZjI2YTZjYzgwNTk4MzdhZDBjMWVhN2RlZTcxIiwidXNlciI6Indlc2xleSJ9', '2019-01-21 01:14:19.640981');
INSERT INTO `django_session` VALUES ('z9g87962vx5rloojjly50mpgaw7m92o5', 'MmM2ZjVkMzNjY2JlZTBkZjk2N2JhZjAxNjFhNmQ3ZmYzNTA5YmQ1MDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhZDQ5NjhlODNhNWQ4ZjI2YTZjYzgwNTk4MzdhZDBjMWVhN2RlZTcxIiwidXNlciI6Indlc2xleSJ9', '2019-01-02 09:12:10.765825');

-- ----------------------------
-- Table structure for webtest_webcase
-- ----------------------------
DROP TABLE IF EXISTS `webtest_webcase`;
CREATE TABLE `webtest_webcase` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `webcase_models` varchar(250) NOT NULL,
  `webcasename` varchar(50) NOT NULL,
  `webcasedesc` varchar(50) NOT NULL,
  `webteststep` varchar(200) NOT NULL,
  `webcase_charger` varchar(200) NOT NULL,
  `creat_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of webtest_webcase
-- ----------------------------
INSERT INTO `webtest_webcase` VALUES ('6', '登录', 'login', '输入正确账户密码', '输入正确账户密码', '我', '2019-01-02 03:01:27.911514');
INSERT INTO `webtest_webcase` VALUES ('7', '登录', '登录testhome', '输入正确账户密码', '输入正确账户密码', '我', '2019-01-07 02:15:56.077354');

-- ----------------------------
-- Table structure for webtest_webcasestep
-- ----------------------------
DROP TABLE IF EXISTS `webtest_webcasestep`;
CREATE TABLE `webtest_webcasestep` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `webfindmethod` varchar(200) DEFAULT NULL,
  `webkwargesone` varchar(200) DEFAULT NULL,
  `webkwargestwo` varchar(200) DEFAULT NULL,
  `webkwargesthree` varchar(200) DEFAULT NULL,
  `webassertdata` varchar(200) DEFAULT NULL,
  `webtestresult` varchar(50) DEFAULT NULL,
  `webcomments` varchar(200) DEFAULT '',
  `Webcase_id` int(11) NOT NULL,
  `webtestlocation` varchar(200) NOT NULL,
  `webkwargesfour` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `webtest_webcasestep_Webcase_id_c8229174_fk_webtest_webcase_id` (`Webcase_id`),
  CONSTRAINT `webtest_webcasestep_Webcase_id_c8229174_fk_webtest_webcase_id` FOREIGN KEY (`Webcase_id`) REFERENCES `webtest_webcase` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of webtest_webcasestep
-- ----------------------------
INSERT INTO `webtest_webcasestep` VALUES ('18', 'open browser', 'https://www.baidu.com/', 'chrome', '', '', '', '', '6', 'id', '');
INSERT INTO `webtest_webcasestep` VALUES ('19', 'sleep', '3', '', '', '', '', '', '6', 'id', '');
INSERT INTO `webtest_webcasestep` VALUES ('20', 'Selenium2Library.Input Text', 'id=kw', 'python', '', '', '', '', '6', 'id', '');
INSERT INTO `webtest_webcasestep` VALUES ('21', 'Click', '${picture_path}/baidu.png', '', '', '', '', '', '6', 'id', '');
INSERT INTO `webtest_webcasestep` VALUES ('22', 'close browser', '', '', '', '', '', '', '6', 'id', '');
INSERT INTO `webtest_webcasestep` VALUES ('23', 'open browser', 'https://testerhome.com/', 'chrome', '', '', '', '', '7', 'id', '');
INSERT INTO `webtest_webcasestep` VALUES ('24', 'sleep', '3', '', '', '', '', '', '7', 'id', '');
INSERT INTO `webtest_webcasestep` VALUES ('25', 'maximize browser window', '', '', '', '', '', '', '7', 'id', '');
INSERT INTO `webtest_webcasestep` VALUES ('26', 'click', '${picture_path}/login.png', '', '', '', '', '', '7', 'id', '');
INSERT INTO `webtest_webcasestep` VALUES ('27', 'Selenium2Library.wait until page contains element', 'id=user_login', '5', '', '', '', '', '7', 'id', '');
INSERT INTO `webtest_webcasestep` VALUES ('28', 'Selenium2Library.Input Text', 'id=user_login', '1633235633@qq.com', '', '', '', '', '7', 'id', '');
INSERT INTO `webtest_webcasestep` VALUES ('29', 'Selenium2Library.Input Text', 'id=user_password', 'yp10086', '', '', '', '', '7', 'id', '');
INSERT INTO `webtest_webcasestep` VALUES ('30', 'Selenium2Library.click button', 'name=commit', '', '', '', '', '', '7', 'id', '');
INSERT INTO `webtest_webcasestep` VALUES ('31', 'Selenium2Library.wait until page contains element', 'xpath=//*[@id=\"main-page\"]/div[1]/nav/div/ul[1]/li/a/img', '', '', '', '', '', '7', 'id', '');
INSERT INTO `webtest_webcasestep` VALUES ('32', 'close browser', '', '', '', '', '', '', '7', 'id', '');

-- ----------------------------
-- Table structure for webtest_webcase_keywords
-- ----------------------------
DROP TABLE IF EXISTS `webtest_webcase_keywords`;
CREATE TABLE `webtest_webcase_keywords` (
  `keyword_id` int(11) NOT NULL AUTO_INCREMENT,
  `library` varchar(50) NOT NULL,
  `keyword` varchar(200) NOT NULL,
  `parameter` varchar(200) NOT NULL,
  `comment` varchar(200) NOT NULL,
  PRIMARY KEY (`keyword_id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of webtest_webcase_keywords
-- ----------------------------
INSERT INTO `webtest_webcase_keywords` VALUES ('1', 'Selenium2LIbrary', 'open browser', 'URl              浏览器类型', '打开浏览器');
INSERT INTO `webtest_webcase_keywords` VALUES ('3', 'Selenium2LIbrary', 'maximize browser window', '', '最大化浏览器');
INSERT INTO `webtest_webcase_keywords` VALUES ('4', 'Selenium2LIbrary', 'click button', 'locator {id,xpath,css,name,class-name}          ', '点击按键');
INSERT INTO `webtest_webcase_keywords` VALUES ('5', 'Selenium2LIbrary', 'wait until page contains element', 'locator     times', '等待定位元素出现  等待时间 /在等时间内出现则成功 否则报错');
INSERT INTO `webtest_webcase_keywords` VALUES ('6', 'Selenium2LIbrary', 'Selenium2Library.get title', '', '通常会将获取的 title 传递给一个变量，然后与预期结果进行比较。从而判断当前脚本执行成功');
INSERT INTO `webtest_webcase_keywords` VALUES ('7', 'Selenium2LIbrary', 'Selenium2Library.get text', 'locator', '获取定位元素的text属性 给一个变量/判断变量与预期是否匹配');
INSERT INTO `webtest_webcase_keywords` VALUES ('8', 'Selenium2LIbrary', 'Selenium2LIbrary.add cookie', 'Key_name          Value_name', '添加 cookie。添加一对 cooke （key：value）');
INSERT INTO `webtest_webcase_keywords` VALUES ('9', 'Selenium2LIbrary', 'Selenium2Library.should contain', '', '判断一个变量与预期的text是否一致');
INSERT INTO `webtest_webcase_keywords` VALUES ('10', 'Selenium2LIbrary', 'Selenium2Library.select frame', 'locator', '进入定位的表单');
INSERT INTO `webtest_webcase_keywords` VALUES ('11', 'Selenium2LIbrary', 'close browser', '', '关闭浏览器');
INSERT INTO `webtest_webcase_keywords` VALUES ('12', 'Selenium2LIbrary', 'Selenium2Library.click element', 'locator', '点击定位元素');
INSERT INTO `webtest_webcase_keywords` VALUES ('13', 'Selenium2LIbrary', 'Selenium2Library.delete all cookies', '', '删除所有cookie');
INSERT INTO `webtest_webcase_keywords` VALUES ('14', 'Selenium2LIbrary', 'Selenium2Library.Set Variable', '${a}        Set Variable           text', '申明变量名称与值');
INSERT INTO `webtest_webcase_keywords` VALUES ('15', 'Selenium2LIbrary', 'Selenium2Library.Xpath Should Match X Times', 'Xpath Should Match X Times    ${xpath}    ${expected_xpath_count}    ${msg}    ${loglevel}', '根据xpath匹配数量 判断页面包含多少个相同的元素 ');
INSERT INTO `webtest_webcase_keywords` VALUES ('16', 'Selenium2LIbrary', 'Selenium2Library.reload page', '', '刷新页面');
INSERT INTO `webtest_webcase_keywords` VALUES ('17', 'Selenium2LIbrary', 'double click element', 'locator', '双击定位元素');
INSERT INTO `webtest_webcase_keywords` VALUES ('18', 'Selenium2LIbrary', 'Selenium2Library.go back', '', '回退');
INSERT INTO `webtest_webcase_keywords` VALUES ('19', 'Selenium2LIbrary', 'Selenium2Library.capture page screenshot', 'filename', '将截图保存到指定的路径');
INSERT INTO `webtest_webcase_keywords` VALUES ('20', 'Selenium2LIbrary', 'Selenium2Library.Clear Element Text', 'locator', '清除定位元素文本');
INSERT INTO `webtest_webcase_keywords` VALUES ('21', 'Selenium2LIbrary', 'Selenium2Library.get table cell', '${cell}    Get Table Cell    ${table_locator}    ${row}    ${column}    ${loglevel}', '将列表中的数据取出赋值给变量${cell}');
INSERT INTO `webtest_webcase_keywords` VALUES ('22', 'BuiltIn', 'Convert To Integer', '${res}    Convert To Integer    ${item}    ${base}', '转成int形');
INSERT INTO `webtest_webcase_keywords` VALUES ('23', 'BuiltIn', 'convert to string', '${res}    Convert To String    ${item}', '转换成string');
INSERT INTO `webtest_webcase_keywords` VALUES ('24', 'BuiltIn', 'get length', '${res}    Get Length    ${item}', '[Return]    ${res}     将获取到的  长度赋值给${res}');
INSERT INTO `webtest_webcase_keywords` VALUES ('25', 'BuiltIn', 'Should Not Be Equal', 'Should Not Be Equal    ${first}    ${second}      ${values}=True', '${first}    ${second}  两个参数应该相等');
INSERT INTO `webtest_webcase_keywords` VALUES ('26', 'SikuliLibrary', 'Click', '图片名称', 'Click image');
INSERT INTO `webtest_webcase_keywords` VALUES ('27', 'SikuliLibrary', 'Double Click', 'picture name', '双击匹配的GUI');
INSERT INTO `webtest_webcase_keywords` VALUES ('28', 'SikuliLibrary', 'Drag And Drop', 'srcImage,  targetImage', 'Drag the source image to target image. If source image is empty, drag the last match and drop at given target');
INSERT INTO `webtest_webcase_keywords` VALUES ('29', 'SikuliLibrary', 'Exists', 'image, timeout=', 'Check whether image exists in screen');
INSERT INTO `webtest_webcase_keywords` VALUES ('30', 'SikuliLibrary', 'SikuliLibrary.Input Text', 'image, text', 'Input text. Image could be empty');
INSERT INTO `webtest_webcase_keywords` VALUES ('31', 'Selenium2LIbrary', 'Press Special Key', 'keyConstant', 'Presses a special keyboard key.  For a list of possible Keys view docs for org.sikuli.script.Key .');
INSERT INTO `webtest_webcase_keywords` VALUES ('32', 'SikuliLibrary', 'Right Click', 'image', 'Right click image');
INSERT INTO `webtest_webcase_keywords` VALUES ('33', 'SikuliLibrary', 'Screen Should Contain', 'image', 'Screen should contain image');
INSERT INTO `webtest_webcase_keywords` VALUES ('34', 'SikuliLibrary', 'Wait Until Screen Contain', 'image, timeout', 'Wait until image shown in screen');
INSERT INTO `webtest_webcase_keywords` VALUES ('35', 'SikuliLibrary', 'Wait For Image', 'wantedImage, notWantedImage, timeout', 'Check wantedImage exist. If notWantedImage appear or timeout happened, throw exception');
INSERT INTO `webtest_webcase_keywords` VALUES ('36', 'SikuliLibrary', 'Wheel Down', 'steps, image=', '移动鼠标到目标图片，并向下移动给定步数滚轮');
INSERT INTO `webtest_webcase_keywords` VALUES ('37', 'SikuliLibrary', 'Wheel Up', 'steps, image=', '移动鼠标到目标图片，并向上移动给定步数滚轮');

-- ----------------------------
-- Table structure for webtest_webtest_task
-- ----------------------------
DROP TABLE IF EXISTS `webtest_webtest_task`;
CREATE TABLE `webtest_webtest_task` (
  `task_id` int(11) NOT NULL AUTO_INCREMENT,
  `task_modelname` varchar(100) NOT NULL,
  `task_casename` varchar(200) NOT NULL,
  `task_status` varchar(200) NOT NULL,
  `task_retry` varchar(10) NOT NULL,
  `task_result` varchar(20) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `task_stepdesc` varchar(100) DEFAULT NULL,
  `case_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`task_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of webtest_webtest_task
-- ----------------------------
INSERT INTO `webtest_webtest_task` VALUES ('5', '登录', 'login', 'True', '', '', '2019-01-08 06:20:25.030168', '2019-01-08 06:20:25.030168', '输入正确账户密码', '6');
INSERT INTO `webtest_webtest_task` VALUES ('6', '登录', '登录testhome', 'True', '', '', '2019-01-08 06:20:25.079137', '2019-01-08 06:20:25.080135', '输入正确账户密码', '7');
