import os

try:
    configs = {
        "database": os.getenv('PGDATABASE'),
        "user": os.getenv('PGUSER'),
        "host": os.getenv('PGHOST'),
        "password": os.getenv('PGPASSWORD')
    }
except Exception as e:
    raise ConnectionError(
        e, "Environment Variables Not Found.\n Is `railway run` wrapping the command?")


class Postgres:
    @property
    def conn(self):
        return self.psycopg2

    @property
    def psycopg2(self):
        import psycopg2
        try:
            conn = psycopg2.connect(
                database=configs["database"],
                user=configs["user"],
                host=configs["host"],
                password=configs["password"],
            )
            return conn
        except Exception as e:
            raise ConnectionError(
                e, "Connection Failed.\n Postgres unable to connect")


postgres = Postgres()
