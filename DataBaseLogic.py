import mysql.connector
from mysql.connector import Error

# Artile from free code camp was used to implement database connection
# The article can be found at https://www.freecodecamp.org/news/connect-python-with-sql/

class DatabaseCred():
    def __init__(self):
        self.host = "INSERT HOST NAME HERE"
        self.uname = "INSERT USER NAME HERE"
        self.pwd = "INSERT PASSWORD HERE"
        self.db_name = "INSERT DATABASE NAME HERE"
        self.connection = self.create_db_connection()

    def create_db_connection(self):
        connection = None
        try:
            connection = mysql.connector.connect(
                host = self.host,
                user = self.uname,
                passwd = self.pwd,
                database = self.db_name
            )
            print("Database connection sucessful")
        except Error as err:
            print(f"Error: '{err}'")            #error handling incase connection fails
        return connection

class UploadToDB():
    def __init__(self, Product):
        self.Product = Product
        self.credentials = DatabaseCred()
        self.connection = self.credentials.connection
        self.query = "INSERT INTO ProgSocTest (Name, Price, Availability) VALUES (%s, %s, %s);"
        self.data = (Product.name, Product.price, Product.availability)
        self.executeQuery()

    def executeQuery(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute(self.query, self.data)
            self.connection.commit()
            print("Query sucessful")
        except Error as err:
            print(f"Error: '{err}'")
        cursor.close()

class ReadFromDB():
    def __init__(self):
        self.credentials = DatabaseCred()
        self.connection = self.credentials.connection
        self.preSavedItems = self.executeQuery()

    def executeQuery(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM ProgSocTest")
            getAllresult = cursor.fetchall()
            print(getAllresult)
            return getAllresult
        except Err as err:
            print(f"Error: '{err}'")

def initDBLogic(Product):
    UploadToDB(Product)

if __name__ == '__main__':
    ReadFromDB()




