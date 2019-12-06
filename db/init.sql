CREATE DATABASE store;
use store;

CREATE TABLE favorite_colors (
  name VARCHAR(20),
  color VARCHAR(10)
);

INSERT INTO favorite_colors
  (name, color)
VALUES
  ('Lancelot', 'blue'),
  ('Galahad', 'yellow');



CREATE TABLE user(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT, 
    username VARCHAR(8)  NOT NULL,
    password VARCHAR(32) NOT NULL,
    email VARCHAR(32) NOT NULL,
    name VARCHAR(32) NOT NULL,
    redid VARCHAR(9),
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    hash VARCHAR(32) NOT NULL,
    if_activated BOOL NOT NULL DEFAULT false,
    PRIMARY KEY (id)
);

INSERT INTO user (
	username
	, password
	, email
	, name
	, hash
	, if_activated
) VALUES (
	'abc'
	, 'yellow'
	, 'abc@abc.com'
	, 'hola'
	, 'abc'
	, true
);
