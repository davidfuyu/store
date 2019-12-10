CREATE DATABASE store;
use store;

CREATE TABLE colors (
  name VARCHAR(20),
  color VARCHAR(10)
);

INSERT INTO colors
  (name, color)
VALUES
  ('Lancelot', 'blue'),
  ('Galahad', 'yellow');