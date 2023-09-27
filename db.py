import mysql.connector
from mysql.connector import Error

# Artile from free code camp was used to implement database connection
# The article can be found at https://www.freecodecamp.org/news/connect-python-with-sql/

host = "DB name name"    #define variables for database credentials
uname = "User name"
pwd = "DB password"
db_name = "DB name"

def create_db_connection(host_name, user_name, user_password, db_name):     #function to connect to database
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
        )
        print("Database connection sucessful")
    except Error as err:
        print(f"Error: '{err}'")            #error handling incase connection fails
    return connection

if __name__ == "__main__":
    create_db_connection(host, uname, pwd, db_name) 