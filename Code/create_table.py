import psycopg2


#connect to postgres
def connect_to_postgres():
    try:
        connection = psycopg2.connect(
            database="crypto",
            user="postgres",
            password="postgres123",
            host="localhost",
            port="5432"
        )
        cas_session=connection
        cursor = connection.cursor()
        print("Connected to PostgreSQL database")
        return cas_session
    except Exception as e:
        print(f"Error: {e}")
        return None


#Create table
def create_table():
    try:
        connection = psycopg2.connect(
            database="crypto",
            user="postgres",
            password="postgres123",
            host="localhost",
            port="5432"
        )
        cursor = connection.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS bitcoin (
            id INT PRIMARY KEY,
            Timestamp VARCHAR(100), 
            Symbol VARCHAR(100),
            Open FLOAT,
            High FLOAT,
            Low FLOAT,
            Close FLOAT,
            Volume FLOAT
        );
        """
        cursor.execute(create_table_query)
        connection.commit()
        print("Table created successfully")
    except Exception as e:
        print(f"Error: {e}")

session=connect_to_postgres()
table=create_table()
