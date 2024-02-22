import mysql.connector
from mysql.connector import Error

# Artile from free code camp was used to implement database connection
# The article can be found at https://www.freecodecamp.org/news/connect-python-with-sql/

class DatabaseCred():
    def __init__(self):
        self.host = "172.18.0.2"
        self.uname = "ProgSoc"
        self.pwd = "ProgSoc"
        self.db_name = "ProgSocTest"
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
        self.now = datetime.now()
        self.formattedDate = self.now.strftime('%Y-%m-%d %H:%M:%S')
        self.Product = Product
        self.credentials = DatabaseCred()
        self.connection = self.credentials.connection
        self.query = self.getQuery()
        self.data = self.getData()
        self.executeQuery()

    def getQuery(self):
        return "INSERT INTO ProgSocTest (Name, Price, Availability, LastChecked) VALUES (%s, %s, %s, %s);"
    def getData(self):
        return (self.Product.name, self.Product.price, self.Product.availability, self.formattedDate)

    def executeQuery(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute(self.query, self.data)
            self.connection.commit()
            print("Query sucessful")
        except Error as err:
            print(f"Error: '{err}'")
        cursor.close()

class UpdateToDB(UploadToDB):
    def __init__(self, Product):
        super().__init__(Product)
    def getQuery(self):
        return "UPDATE ProgSocTest SET Price = %s, Availability = %s, LastChecked = %s WHERE Name = %s"
    def getData(self):
        return(self.Product.price, self.Product.availability, self.formattedDate,self.Product.name)

class ReadFromDB():
    def __init__(self):
        self.credentials = DatabaseCred()
        self.connection = self.credentials.connection
        self.preSavedItems = self.executeQuery()

    def executeQuery(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT Name FROM ProgSocTest")
            getAllresult = cursor.fetchall()
            print(getAllresult)
            return getAllresult
        except Err as err:
            print(f"Error: '{err}'")

def initDBLogic(Product):
    UploadToDB(Product)

def UpdateProduct(Product):
    UpdateToDB(Product)

if __name__ == '__main__':
    ReadFromDB()





