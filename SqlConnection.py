import mysql.connector

def create_db_connection():
    try:
        # Replace with your database configuration
        db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'ennterpassword', 
            'database': 'pacemaker',
        }

        # Establish and return the connection
        connection = mysql.connector.connect(**db_config)
        print("Connected")
        return connection

    except mysql.connector.Error as err:
        print(f"Error: {err}")