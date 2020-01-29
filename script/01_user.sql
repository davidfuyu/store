USE general;

CREATE TABLE user (
    user_id INT UNSIGNED NOT NULL AUTO_INCREMENT, 
    email VARCHAR(256) NOT NULL,
    password VARCHAR(256) NOT NULL,
    name VARCHAR(256) NOT NULL,
    redid VARCHAR(32),
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
    PRIMARY KEY (user_id)
);

INSERT INTO user(email, password, name) VALUES ('a@b.c', '$2b$12$zzx8rKAxKe8zlmWfuxqcZeTA4cR5c3Z4e6cEgfSDgVGeJT5kEtFKS', 'a@b.c');