USE general;

CREATE TABLE organism_property (
    organism_property_id INT UNSIGNED NOT NULL AUTO_INCREMENT, 
    organism_id INT UNSIGNED NOT NULL,
    property_id INT UNSIGNED NOT NULL,
    value VARCHAR(1024) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
    PRIMARY KEY (organism_property_id),
    FOREIGN KEY(organism_id) REFERENCES organism (organism_id), 
    FOREIGN KEY(property_id) REFERENCES property (property_id) 
);


CREATE TABLE organism_property_log (
    organism_property_log_id INT UNSIGNED NOT NULL AUTO_INCREMENT, 
    organism_property_id INT UNSIGNED NOT NULL, 
    user_id INT UNSIGNED NOT NULL,
    status_id INT UNSIGNED NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    PRIMARY KEY (organism_property_log_id),
    FOREIGN KEY(organism_property_id) REFERENCES organism_property (organism_property_id), 
    FOREIGN KEY(user_id) REFERENCES user (user_id), 
    FOREIGN KEY(status_id) REFERENCES status (status_id) 
);
