DROP TABLE IF EXISTS artist;
DROP TABLE IF EXISTS albums;

CREATE TABLE albums (
    id SERIAL PRIMARY KEY   ,
    title VARCHAR(255),
    genre VARCHAR(255)
    );

CREATE TABLE artist (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);    