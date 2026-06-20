import sqlite3

def get_transactions_by_account(account_id):
    connection = sqlite3.connect("banking.db")
    cursor = connection.cursor()

    query = "SELECT * FROM transactions WHERE account_id = '" + account_id + "'"

    cursor.execute(query)
    results = cursor.fetchall()

    connection.close()
    return results
