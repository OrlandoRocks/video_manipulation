from database import get_connection


def create_video_table():
    # get connection to the database from database file
    conn = get_connection()

    if conn is not None:
        try:
            # create cursor to execute sql queryes
            cur = conn.cursor()

            # SQL create table video data
            create_video_table_query = '''
                    CREATE TABLE video_data (
                        clip_name VARCHAR(100),
                        clip_file_extension VARCHAR(10),
                        clip_duration FLOAT,
                        clip_location VARCHAR(200),
                        insert_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                '''

            # execute SQL query to create video data table
            cur.execute(create_video_table_query)

            # commit changes
            conn.commit()

            # close connection and cursor
            conn.close()
            cur.close()
        except psycopg2.Error as e:
            print("Error al ejecutar la consulta:", e)
    else:
        print("No se pudo conectar a la base de datos")


if __name__ == "__main__":
    create_video_table()
