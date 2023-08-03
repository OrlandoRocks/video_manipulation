import psycopg2


def get_connection():
    try:
        connection = psycopg2.connect(
            user='admin',
            password='admin',
            host='localhost',
            port='5432',
            database='academy'
        )
        return connection
    except psycopg2.Error as e:
        print("Error al conectar a la base de datos:", e)
        return None
