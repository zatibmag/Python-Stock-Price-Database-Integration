import requests
import datetime
from database import connect_to_database, close_database_connection
from data_insertion import insert_stock_price

def main():
    # Connect to the database
    mydb = connect_to_database()

    api_key = "apidojo-yahoo-finance-v1.p.rapidapi.com"
    symbol = "TSLA"

    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"

    # Get the stock price
    response = requests.get(url)
    data = response.json()
    price = data["Global Quote"]["05. price"]
    print(f"The current price of {symbol} is {price}")

    # Get the current date
    current_date = datetime.date.today()

    # Check if a record already exists for today's date
    if record_exists(mydb, current_date):
        print("Record already exists for today.")
    else:
        # Insert the stock price into the database
        insert_stock_price(mydb, current_date, price)
        print("Record added successfully.")

    # Close the database connection
    close_database_connection(mydb)

def record_exists(mydb, current_date):
    cursor = mydb.cursor()

    # Check if a record exists for the current date
    query = "SELECT * FROM tesla_inc WHERE date = %s"
    values = (current_date,)
    cursor.execute(query, values)
    record = cursor.fetchone()

    cursor.close()

    return record is not None

if __name__ == "__main__":
    main()


