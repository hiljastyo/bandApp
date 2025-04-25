import mariadb
import sys
class Database():
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mariadb.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("connect SUCCESS!")
        except mariadb.Error as e:
            print(f"connect FAIL: {e}")

    def fetch_data(self, query):
        if not self.cursor:
            print("NO CONNECTION TO DATABASE!")
            return None

        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            return results
        except mariadb.Error as e:
            print(f"ERROR WHILE PROCESSING: {e}")
            return None

    def insert_data(self, query, values):
        if not self.cursor:
            print("NO CONNECTION TO DATABASE!")
            return False

        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Data add SUCCESS!")
            return True
        except mariadb.Error as e:
            print(f"error while adding!!: {e}")
            return False

    def close_connection(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("connection SHUTDOWN.")

