
import oracledb

def get_connection():
    try:
        connection = oracledb.connect(
            user="SYSTEM",
            password="College123",
            dsn="localhost:1521/XEPDB1"
        )

        print("Oracle Database Connected Successfully!")
        return connection

    except oracledb.Error as error:
        print("Database Connection Failed:", error)
        return None
