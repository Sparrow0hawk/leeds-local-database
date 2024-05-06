CREATE TABLE election.results
(
    id     INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY
    ,candidate_name  TEXT
    ,party_id INTEGER NOT NULL REFERENCES election.party(id)
    ,votes INTEGER NOT NULL
    ,electorate INTEGER NOT NULL
    ,spoilt_ballots INTEGER NOT NULL
    ,ward_id INTEGER NOT NULL REFERENCES electoral_unit.ward(id)
    ,election_date INTEGER
);
