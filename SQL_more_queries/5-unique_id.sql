-- Unique ID:
CREATE TABLE IF NOT EXISTS unique_id (
    id int DEFAULT 1 UNIQUE,
    name varchar(256) NOT NULL
);
