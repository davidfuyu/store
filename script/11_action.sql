USE general;

CREATE TABLE action (
    action_id INT UNSIGNED NOT NULL AUTO_INCREMENT, 
    action_name VARCHAR(256) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
    PRIMARY KEY (action_id)
);