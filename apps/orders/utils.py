from django.db import connection


def generate_uuid_v4():
    with connection.cursor() as c:
        c.execute("SELECT uuid_generate_v4()")
        return c.fetchone()[0]