from flask import Flask
from db import get_db_connection

app = Flask(__name__)

@app.route("/")
def home():
    conn = get_db_connection()
    users = conn.execute("SELECT * FROM users").fetchall()
    conn.close()

    return f"Users in DB: {len(users)}"

if __name__ == "__main__":
    app.run(debug=True)
