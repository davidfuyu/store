USE general;

-- CREATE TABLE taxonomy_kingdom(
--     taxonomy_kingdom_id INT UNSIGNED NOT NULL AUTO_INCREMENT, 
--     name VARCHAR(1024) NOT NULL,
--     PRIMARY KEY (taxonomy_kingdom_id)
-- );

-- CREATE TABLE taxonomy_phylum(
--     taxonomy_phylum_id INT UNSIGNED NOT NULL AUTO_INCREMENT, 
--     name VARCHAR(1024) NOT NULL,
--     parent_id INT UNSIGNED,
--     PRIMARY KEY (taxonomy_phylum_id)
--     FOREIGN KEY(parent_id) REFERENCES taxonomy_kingdom(taxonomy_kingdom_id)
-- );

-- CREATE TABLE taxonomy_class(
--     taxonomy_class_id INT UNSIGNED NOT NULL AUTO_INCREMENT, 
--     name VARCHAR(1024) NOT NULL,
--     parent_id INT UNSIGNED,
--     PRIMARY KEY (taxonomy_class_id)
--     FOREIGN KEY(parent_id) REFERENCES taxonomy_phylum(taxonomy_phylum_id)
-- );

-- CREATE TABLE taxonomy_order(
--     taxonomy_order_id INT UNSIGNED NOT NULL AUTO_INCREMENT, 
--     name VARCHAR(1024) NOT NULL,
--     parent_id INT UNSIGNED,
--     PRIMARY KEY (taxonomy_order_id)
--     FOREIGN KEY(parent_id) REFERENCES taxonomy_class(taxonomy_class_id)
-- );

-- CREATE TABLE taxonomy_family(
--     taxonomy_family_id INT UNSIGNED NOT NULL AUTO_INCREMENT, 
--     name VARCHAR(1024) NOT NULL,
--     parent_id INT UNSIGNED,
--     PRIMARY KEY (taxonomy_family_id)
--     FOREIGN KEY(parent_id) REFERENCES taxonomy_order(taxonomy_order_id)
-- );

-- CREATE TABLE taxonomy_genus(
--     taxonomy_genus_id INT UNSIGNED NOT NULL AUTO_INCREMENT, 
--     name VARCHAR(1024) NOT NULL,
--     parent_id INT UNSIGNED,
--     PRIMARY KEY (taxonomy_genus_id)
--     FOREIGN KEY(parent_id) REFERENCES taxonomy_family(taxonomy_family_id)
-- );

-- CREATE TABLE taxonomy_species(
--     taxonomy_species_id INT UNSIGNED NOT NULL AUTO_INCREMENT, 
--     name VARCHAR(1024) NOT NULL,
--     parent_id INT UNSIGNED,
--     PRIMARY KEY (taxonomy_species_id)
--     FOREIGN KEY(parent_id) REFERENCES taxonomy_genus(taxonomy_genus_id)
-- );

CREATE TABLE taxonomy_level(
    taxonomy_level_id INT UNSIGNED NOT NULL AUTO_INCREMENT, 
    name VARCHAR(1024) NOT NULL,
    taxonomy_level_order INT UNSIGNED NOT NULL, 
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    PRIMARY KEY (taxonomy_level_id)
);

CREATE TABLE taxonomy(
    taxonomy_id INT UNSIGNED NOT NULL AUTO_INCREMENT, 
    name VARCHAR(1024) NOT NULL,
    taxonomy_level_id INT UNSIGNED, 
    parent_id INT UNSIGNED,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    PRIMARY KEY (taxonomy_id),
    FOREIGN KEY(taxonomy_level_id) REFERENCES taxonomy_level(taxonomy_level_id),
    FOREIGN KEY(parent_id) REFERENCES taxonomy(taxonomy_id),
    CONSTRAINT unique_taxonomy UNIQUE (name, taxonomy_level_id)
);

INSERT INTO taxonomy_level(name, taxonomy_level_order)
VALUES
    ('domain', 0),
    ('kingdom', 1),
    ('phylum', 2),
    ('class', 3),
    ('order', 4),
    ('family', 5),
    ('genus', 6),
    ('species', 7);