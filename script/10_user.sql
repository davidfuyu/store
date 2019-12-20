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