import mysql.connector

def connect_to_database():
    # Connect to the database
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='25565',
        port="3306",
        database='tesla_price'
    )
    return mydb

def close_database_connection(mydb):
    # Close the database connection
    mydb.close()
