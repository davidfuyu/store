USE general;

CREATE TABLE organism (
    organism_id INT UNSIGNED NOT NULL AUTO_INCREMENT, 
    name VARCHAR(64) NOT NULL,
    PRIMARY KEY (organism_id)
);