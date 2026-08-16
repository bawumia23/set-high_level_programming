# 0x0F. Python - Object-relational mapping

## Description

This project connects Python to a MySQL database in two ways:

1. **Raw SQL with `MySQLdb`** (tasks 0-5): connecting to MySQL, writing
   SQL queries by hand, and fetching results with cursors. This section
   also covers SQL injection - how it happens when user input is
   concatenated directly into a query, and how to prevent it using
   parameterized queries.
2. **Object-Relational Mapping with `SQLAlchemy`** (tasks 6-17): mapping
   Python classes to MySQL tables, and interacting with the database
   entirely through objects and ORM query methods instead of writing
   SQL. This section also covers relationships between models
   (`State` <-> `City`), cascading deletes, and eager loading with
   `joinedload` to avoid extra queries.

## Environment

- Ubuntu 24.04 LTS (WSL), Python 3.12
- MySQL 8.0.46
- `MySQLdb` (mysqlclient) 2.2.8
- `SQLAlchemy` 1.4.22
- pycodestyle 2.8.x

## Files

| File | Task | Description |
| --- | --- | --- |
| `0-select_states.py` | 0 | List all states, sorted by id |
| `1-filter_states.py` | 1 | List states starting with uppercase N |
| `2-my_filter_states.py` | 2 | Filter states by name (unsafe, built with `.format()`) |
| `3-my_safe_filter_states.py` | 3 | Filter states by name (safe, parameterized query) |
| `4-cities_by_state.py` | 4 | List all cities with their state name (one query) |
| `5-filter_cities.py` | 5 | List cities of a given state (safe, one query) |
| `model_state.py` | 6 | `State` model class (SQLAlchemy) |
| `6-model_state.py` | 6 | Create the `states` table |
| `7-model_state_fetch_all.py` | 7 | List all `State` objects |
| `8-model_state_fetch_first.py` | 8 | Print the first `State` object without fetching all |
| `9-model_state_filter_a.py` | 9 | List `State` objects containing the letter "a" |
| `10-model_state_my_get.py` | 10 | Get a `State` id by name |
| `11-model_state_insert.py` | 11 | Insert a new `State` ("Louisiana") |
| `12-model_state_update_id_2.py` | 12 | Update the name of the `State` with id 2 |
| `13-model_state_delete_a.py` | 13 | Delete all `State` objects containing "a" |
| `model_city.py` | 14 | `City` model class, linked to `states` by foreign key |
| `14-model_city_fetch_by_state.py` | 14 | List all cities grouped by state (manual join) |
| `relationship_state.py` | 15 | `State` model with a `cities` relationship (cascade delete) |
| `relationship_city.py` | 15 | `City` model with a `state` backref |
| `100-relationship_states_cities.py` | 15 | Create a `State` and `City` together via the relationship |
| `101-relationship_states_cities_list.py` | 16 | List all states and their cities (single query, `joinedload`) |
| `102-relationship_cities_states_list.py` | 17 | List all cities and their state (single query, `joinedload`) |

## Usage

Each script takes MySQL credentials as arguments:

```
./script.py <mysql username> <mysql password> <database name> [extra arg]
```

Example:

```
./0-select_states.py root root hbtn_0e_0_usa
```

## Author

Tajudeen
