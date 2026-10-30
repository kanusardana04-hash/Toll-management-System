
from database import get_connection

connection = get_connection()

if connection:
    cursor = connection.cursor()

    cursor.execute("SELECT USER FROM DUAL")

    result = cursor.fetchone()

    print("Connected User:", result[0])

    cursor.close()
    connection.close()
