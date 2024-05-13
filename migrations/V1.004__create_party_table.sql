CREATE TABLE election.party
(
    id     INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY
    ,name  TEXT NOT NULL UNIQUE
    ,parent_party INTEGER NOT NULL REFERENCES election.parent_party(id)
);
