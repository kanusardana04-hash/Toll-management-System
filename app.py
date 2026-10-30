
from flask import Flask, jsonify, send_from_directory
from database import get_connection
from pathlib import Path

# Locate the frontend folder
frontend_folder = Path(__file__).resolve().parent.parent / "frontend"

# Flask application
app = Flask(
    __name__,
    static_folder=str(frontend_folder),
    static_url_path=""
)

# Display frontend dashboard
@app.route("/")
def home():
    return send_from_directory(frontend_folder, "index.html")


# Dashboard statistics from Oracle Database
@app.route("/api/dashboard")
def dashboard():

    connection = get_connection()

    if connection is None:
        return jsonify({"error": "Database connection failed"}), 500

    cursor = None

    try:
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM VEHICLES")
        total_vehicles = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM TOLL_TRANSACTIONS")
        total_transactions = cursor.fetchone()[0]

        cursor.execute("""
            SELECT NVL(SUM(TOLL_AMOUNT), 0)
            FROM TOLL_TRANSACTIONS
        """)
        total_revenue = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM TOLL_BOOTH")
        total_booths = cursor.fetchone()[0]

        return jsonify({
            "total_vehicles": total_vehicles,
            "total_transactions": total_transactions,
            "total_revenue": float(total_revenue),
            "total_booths": total_booths
        })

    except Exception as error:
        return jsonify({"error": str(error)}), 500

    finally:
        if cursor:
            cursor.close()
        connection.close()


if __name__ == "__main__":
    app.run(debug=True, port=5000)

