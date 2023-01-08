CREATE DATABASE db;
USE db;

CREATE TABLE time (
    current_time DATETIME NOT NULL
);

INSERT INTO time (current_time) VALUES (NOW());