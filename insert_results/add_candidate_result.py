from sqlalchemy import Engine, text


def add_candidate_result(
    engine: Engine, candidate: str, party: str, votes: int, electorate: int, spoilt: int, ward: str, election_date: int
) -> None:
    with engine.begin() as connection:
        connection.execute(
            text(
                """
            INSERT INTO election.results
            (
                candidate_name, 
                party_id, 
                votes, 
                electorate, 
                spoilt_ballots, 
                ward_id, 
                election_date
            )
            SELECT 
                :candidate_name,
                party.id,
                :votes,
                :electorate,
                :spoilt_ballots,
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
                "candidate_name": candidate,
                "party_name": party,
                "votes": votes,
                "electorate": electorate,
                "spoilt_ballots": spoilt,
                "ward_name": ward,
                "election_date": election_date,
            },
        )
