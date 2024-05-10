import csv
import os
import sys

from sqlalchemy import create_engine

from insert_results.add_candidate_result import add_candidate_result


def main(file_path: str, election_year: str) -> None:
    database_uri = os.environ["SQLALCHEMY_DATABASE_URI"]
    engine = create_engine(database_uri)
    election_year = int(election_year)

    with open(file_path) as open_file:
        data = list(csv.DictReader(open_file, dialect='unix'))

    for row in data:
        add_candidate_result(engine=engine,
                             forename=row["Forename"],
                             surname=row["Surname"],
                             party=row["Partyname"],
                             votes=row["Votes"],
                             electorate=row["Electorate"] if row.get("Electorate") else None,
                             spoilt=row["SpoiltPapers"] if row.get("SpoiltPapers") else None,
                             elected=True if row["Elected"] == "TRUE" else False,
                             ward=row["Wardname"].replace("and", "&"),
                             election_date=election_year)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
