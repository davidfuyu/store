USE general;

CREATE TABLE organism (
    organism_id INT UNSIGNED NOT NULL AUTO_INCREMENT, 
    organism_name VARCHAR(64) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
    PRIMARY KEY (organism_id)
);