CREATE TABLE IF NOT EXISTS problems(
    id INTEGER PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    acceptance FLOAT DEFAULT 0.0 NOT NULL,
    difficulty VARCHAR(10) NOT NULL
)
:)
INSERT INTO problems(id,title,acceptance,difficulty) VALUES(1,"bababoe",0.3,"cringe")