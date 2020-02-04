USE general;

CREATE TABLE audit (
    audit_id INT UNSIGNED NOT NULL AUTO_INCREMENT, 
    table_name VARCHAR(256) NOT NULL,
    column_name VARCHAR(256) NOT NULL,
    operation VARCHAR(256) NOT NULL,
    primary_key_value VARCHAR(256) NOT NULL,
    old_value VARCHAR(256) NOT NULL,
    new_value VARCHAR(256) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    PRIMARY KEY (audit_id)
);