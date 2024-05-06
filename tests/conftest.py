from pathlib import Path
from typing import Generator

import pytest
from sqlalchemy import create_engine, Engine, text
from testcontainers.postgres import PostgresContainer


@pytest.fixture(scope="session")
def connection_url() -> Generator[str, None, None]:
    with PostgresContainer("postgres:15") as postgres:
        yield postgres.get_connection_url(driver="pg8000")


@pytest.fixture(scope="session")
def engine(connection_url: str) -> Engine:
    return create_engine(connection_url)


@pytest.fixture(scope="session", autouse=True)
def create_schema(engine: Engine) -> None:
    schemas = ["electoral_unit", "election"]
    migrations_path = Path(__file__).parents[1] / "migrations"
    migrations = (path for path in migrations_path.glob("V[12].*.sql") if path.is_file())

    with engine.begin() as connection:
        for schema in schemas:
            connection.execute(text(f"CREATE SCHEMA {schema}"))

        for migration in sorted(migrations):
            with open(migration, "r") as file:
                connection.execute(text(file.read()))
