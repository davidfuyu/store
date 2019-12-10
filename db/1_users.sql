CREATE TABLE store.users (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT, 
    username VARCHAR(32)  NOT NULL,
    password VARCHAR(32) NOT NULL,
    email VARCHAR(32) NOT NULL,
    name VARCHAR(32) NOT NULL,
    redid VARCHAR(32),
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    PRIMARY KEY (id)
);
INSERT INTO store.users(username, password, email, name) VALUES (
  'username_test', 'password_test', 'email_test', 'name_test'
)