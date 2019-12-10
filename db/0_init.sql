CREATE DATABASE general;
USE general;

CREATE TABLE z_test(
  name VARCHAR(20),
  description VARCHAR(10)
);

INSERT INTO z_test
  (name, description)
VALUES
  ('mimi', 'dog'),
  ('wangwang', 'cat');