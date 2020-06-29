USE general;

CREATE TABLE organism (
    organism_id INT UNSIGNED NOT NULL AUTO_INCREMENT, 
    organism_name VARCHAR(1024) NOT NULL,
    taxonomy_id INT UNSIGNED,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
    PRIMARY KEY (organism_id),
    FOREIGN KEY(taxonomy_id) REFERENCES taxonomy(taxonomy_id),
    CONSTRAINT unique_organism_taxonomy UNIQUE (organism_name, taxonomy_id)
);