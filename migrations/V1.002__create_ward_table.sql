CREATE TABLE electoral_unit.ward
(
    id     INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY
    ,name  TEXT NOT NULL UNIQUE
    ,constituency_id INTEGER NOT NULL REFERENCES electoral_unit.constituency(id)
);
