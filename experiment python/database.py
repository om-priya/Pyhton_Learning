import sqlite3

class DatabaseConnection:
    _instance = None

    def __init__(self, database_file):
        if DatabaseConnection._instance is not None:
            raise Exception("A DatabaseConnection instance already exists. Use get_instance() to access it.")
        self._database_file = database_file
        self._connection = sqlite3.connect(database_file)
        DatabaseConnection._instance = self

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            raise Exception("No DatabaseConnection instance has been created. Use __init__ to create one.")
        return cls._instance

    def get_connection(self):
        return self._connection

    def close_connection(self):
        self._connection.close()

if __name__ == "__main__":
    # Creating a database connection using the singleton
    db_connection = DatabaseConnection('my_database.db')
    
    # Get the connection
    connection = db_connection.get_connection()

    # You can use the connection for database operations
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS example (id INTEGER PRIMARY KEY, data TEXT)")
    cursor.execute("INSERT INTO example (data) VALUES ('Sample data')")
    connection.commit()

    # Close the connection when you're done
    db_connection.close_connection()
