from sqlalchemy import Engine, text


def add_candidate_result(
    engine: Engine,
    forename: str,
    surname: str,
    party: str,
    votes: int,
    electorate: int,
    spoilt: int,
    elected: bool,
    ward: str,
    election_date: int,
) -> None:
    with engine.begin() as connection:
        connection.execute(
            text(
                """
            INSERT INTO election.results
            (
                candidate_forename,
                candidate_surname,
                party_id, 
                votes, 
                electorate, 
                spoilt_ballots,
                elected,
                ward_id, 
                election_date
            )
            SELECT 
                :candidate_forename,
                :candidate_surname,
                party.id,
                :votes,
                :electorate,
                :spoilt_ballots,
                :elected,
                ward.id,
                :election_date
            FROM (SELECT 1) AS dummy
            LEFT JOIN election.party
                ON party.name = :party_name
            LEFT JOIN electoral_unit.ward
                ON ward.name = :ward_name
            """
            ),
            {
                "candidate_forename": forename,
                "candidate_surname": surname,
                "party_name": party,
                "votes": votes,
                "electorate": electorate,
                "spoilt_ballots": spoilt,
                "elected": elected,
                "ward_name": ward,
                "election_date": election_date,
            },
        )
