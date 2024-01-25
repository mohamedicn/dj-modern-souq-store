import psycopg2
import os
from railway.exceptions import ConnectionError
from railway.postgres import configs

try:
    conn = psycopg2.connect(
        database=configs["database"],
        user=configs["user"],
        host=configs["host"],
        password=configs["password"],
    )
except Exception as e:
    raise ConnectionError(
        e, "Connection Failed.\n Postgres unable to connect")
