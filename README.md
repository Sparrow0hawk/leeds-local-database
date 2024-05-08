# Leeds Local Election Database

## Setup

To use this repository you will need:
- Docker

1. Start containers and run migrations
   ```bash
   docker compose up 
   ```
2. Stop containers running by interrupting with CTRL+C
3. Teardown containers and destroy all data
   ```bash
   docker compose down 
   ```

### Generating result migrations

To bootstrap initial migrations for the actual election results data the following process was followed:

- Spin up a local instance of Postgres
- Download CSV file for a years results from Data Mill North
- Run the `main.py` script passing the file path as the first argument and the year of the election as the second
- Deal with any database errors e.g. insert new party names
- Once loaded use PyCharm database to export the `election.results` table as SQL-insert-multirow

1. Install Python3
2. Create a virtual environment
   ```bash
   python3.12 -m venv --prompt . --upgrade-deps .venv
   ```
3. Install dependencies 
   ```bash
   source .venv/bin/activate
   
   pip install .[dev]
   ```
4. Spin up local compose
   ```bash
   docker compose up
   ```
5. Run `main.py`
   ```bash
   export SQLALCHEMY_DATABASE_URI=postgresql+pg8000://elections:password@localhost/local-elections
   
   python main.py Results_05May2022.csv 2022
   ```
6. Run tests
   ```bash
   pytest
   ```
