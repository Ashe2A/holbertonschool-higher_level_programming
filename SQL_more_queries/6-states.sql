-- states (should not fail)

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states
(
    id INT UNIQUE AUTO NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
