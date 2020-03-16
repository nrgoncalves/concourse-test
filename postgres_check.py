import psycopg2


def test_postgres():
    conn = psycopg2.connect(dbname="test", user="postgres", host="database")
    cur = conn.cursor()

    print("PostgreSQL database version:")
    cur.execute("SELECT version();")

    # display the PostgreSQL database server version
    db_version = cur.fetchone()
    print(db_version)

    # another query
    cur.execute("SELECT 1;")

    # close the communication with the PostgreSQL
    cur.close()


test_postgres()
