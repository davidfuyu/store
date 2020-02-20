USE general;

CREATE TABLE reference (
    reference_id INT UNSIGNED NOT NULL AUTO_INCREMENT, 
    value VARCHAR(1024) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    PRIMARY KEY (reference_id)
);


CREATE TABLE organism_property_reference (
    organism_property_reference_id INT UNSIGNED NOT NULL AUTO_INCREMENT, 
    organism_property_id INT UNSIGNED NOT NULL, 
    reference_id INT UNSIGNED NOT NULL, 
    user_id INT UNSIGNED NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    PRIMARY KEY (organism_property_reference_id),
    FOREIGN KEY(organism_property_id) REFERENCES organism_property (organism_property_id), 
    FOREIGN KEY(reference_id) REFERENCES reference(reference_id),
    FOREIGN KEY(user_id) REFERENCES user (user_id)
);

INSERT INTO reference (value) VALUES ('Bergey''s manual of determinative bacteriology');
