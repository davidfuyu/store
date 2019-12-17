USE general;

CREATE TABLE property_category (
    property_category_id INT UNSIGNED NOT NULL AUTO_INCREMENT, 
    property_category_name VARCHAR(64) NOT NULL,
    PRIMARY KEY (property_category_id)
);

CREATE TABLE property_type (
    property_type_id INT UNSIGNED NOT NULL AUTO_INCREMENT, 
    property_type_name VARCHAR(64) NOT NULL,
    PRIMARY KEY (property_type_id)
);

CREATE TABLE property (
    property_id INT UNSIGNED NOT NULL AUTO_INCREMENT, 
    property_name VARCHAR(128) NOT NULL, 
    property_desc VARCHAR(1024), 
    property_category_id INT UNSIGNED NOT NULL, 
    property_type_id INT UNSIGNED NOT NULL, 
    PRIMARY KEY (property_id),
    FOREIGN KEY(property_type_id) REFERENCES property_type (property_type_id), 
    FOREIGN KEY(property_category_id) REFERENCES property_category (property_category_id) 
);

INSERT INTO property_category (property_category_name) VALUES 
('General characteristics'), 
('Enzyme activity'), 
('Growth with different C/N sources'), 
('Fermentation');

INSERT INTO property_type (property_type_name) VALUES 
('positive/negative'),
('yes/no'),
('float'),
('text')