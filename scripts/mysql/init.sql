mysql -u root

create database apidb;
CREATE USER 'api_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON * . * TO 'api_user'@'localhost';