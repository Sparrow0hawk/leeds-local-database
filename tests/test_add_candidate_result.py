from typing import Sequence, NamedTuple

from sqlalchemy import Engine, text, Row

from insert_results.add_candidate_result import add_candidate_result


def test_add_candidate_result(engine: Engine) -> None:
    add_candidate_result(engine, "John", "Smith", "Conservative Party", 100, 300, 20, False, "Wetherby", 2024)

    (candidate_result_row1,) = select_results(engine=engine, election=2024)

    assert (
        candidate_result_row1.candidate_forename == "John"
        and candidate_result_row1.candidate_surname == "Smith"
        and candidate_result_row1.party_name == "Conservative Party"
        and candidate_result_row1.votes == 100
        and candidate_result_row1.electorate == 300
        and candidate_result_row1.spoilt_ballots == 20
        and candidate_result_row1.elected is False
        and candidate_result_row1.ward_name == "Wetherby"
    )


def select_results(engine: Engine, election: int) -> Sequence[Row[NamedTuple]]:
    with engine.connect() as connection:
        result = connection.execute(
            text(
                """
                SELECT 
                    candidate_forename,
                    candidate_surname,
                    party.name as party_name,
                    votes,
                    electorate,
                    spoilt_ballots,
                    elected,
                    ward.name as ward_name
                FROM election.results
                LEFT JOIN electoral_unit.ward
                    ON results.ward_id = ward.id
                LEFT JOIN election.party
                    ON results.party_id = party.id
                WHERE results.election_date = :election_date
                """
            ),
            {"election_date": election},
        )
        return result.all()
