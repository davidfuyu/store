USE general;

CREATE TABLE status (
    status_id INT UNSIGNED NOT NULL AUTO_INCREMENT, 
    status_name VARCHAR(256) NOT NULL,
    status_order INT UNSIGNED NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
    PRIMARY KEY (status_id)
);

INSERT INTO status (status_name, status_order)
VALUES
  ('input', 1),
  ('updated', 2),
  ('verified', 3);