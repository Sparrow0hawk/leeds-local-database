CREATE TABLE election.results
(
    id     INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY
    ,candidate_forename  TEXT
    ,candidate_surname  TEXT
    ,party_id INTEGER NOT NULL REFERENCES election.party(id)
    ,votes INTEGER NOT NULL
    ,electorate INTEGER
    ,spoilt_ballots INTEGER
    ,elected BOOLEAN NOT NULL
    ,ward_id INTEGER NOT NULL REFERENCES electoral_unit.ward(id)
    ,election_date INTEGER
);
