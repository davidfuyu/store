CREATE TABLE store.users (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT, 
    email VARCHAR(256) NOT NULL,
    password VARCHAR(256) NOT NULL,
    name VARCHAR(256) NOT NULL,
    redid VARCHAR(32),
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    PRIMARY KEY (id)
);
INSERT INTO store.users(email, password, name) VALUES (
  'email_test', 'password_test', 'name_test'
)