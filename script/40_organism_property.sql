USE general;

CREATE TABLE organism_property (
    organism_property_id INT UNSIGNED NOT NULL AUTO_INCREMENT, 
    organism_id INT UNSIGNED NOT NULL,
    property_id INT UNSIGNED NOT NULL,
    value VARCHAR(1024) NOT NULL,
    PRIMARY KEY (organism_property_id),
    FOREIGN KEY(organism_id) REFERENCES organism (organism_id), 
    FOREIGN KEY(property_id) REFERENCES property (property_id) 
);
