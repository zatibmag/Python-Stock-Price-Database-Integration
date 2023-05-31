def insert_stock_price(mydb, current_date, price):
    # Insert the stock price into the database with a new ID
    cursor = mydb.cursor()

    # Get the last ID from the table
    query = "SELECT MAX(id) FROM tesla_inc"
    cursor.execute(query)
    last_id = cursor.fetchone()[0]

    # Generate a new ID based on the last ID
    if last_id is None:
        new_id = 0
    else:
        new_id = int(last_id) + 1

    # Insert the new record into the table
    query = "INSERT INTO tesla_inc (id, date, price) VALUES (%s, %s, %s)"
    values = (new_id, current_date, price)
    cursor.execute(query, values)
    mydb.commit()
    print("Record added successfully. ID:", new_id)

    cursor.close()

