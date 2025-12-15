from flask import Flask, request, jsonify
from db import get_db_connection

app = Flask(__name__)

@app.route("/")
def home():
    return "NutriTrack backend is running"

#functia de inregistrare a unui user
@app.route("/register", methods=["POST"])
def register():

    #preluam informatiile despre clientul care doreste inregistrearea
    name = request.json.get("name")
    password = request.json.get("password")
    age = request.json.get("age")

    conn = get_db_connection()

    existing_user = conn.execute(
        "SELECT * FROM users WHERE name = ?", (name,)
    ).fetchone()

    #daca utilizatorul este gasit in baza de date(dupa nume) , esueaza
    if existing_user:
        conn.close()
        return jsonify({"error": "Utilizator deja existent"}), 400

    #daca nu exista, il introducem in baza de date
    conn.execute(
        "INSERT INTO users (name, password, age) VALUES (?, ?, ?)",
        (name, password, age)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Utilizator inregistrat cu succes"})



#functia de logare a unui user
@app.route("/login", methods=["POST"])
def login():
    #preluam informatiile 
    name = request.json.get("name")
    password = request.json.get("password")

    conn = get_db_connection()
    user = conn.execute(
        "SELECT * FROM users WHERE name = ? AND password = ?",
        (name, password)
    ).fetchone()
    conn.close()

    #daca nu exista utilizatorul in baza de date , esueaza
    if user is None:
        return jsonify({"error": "Email sau parola gresita!"}), 401

    #daca il gasim , conectarea este cu succes
    return jsonify({
        "message": "Logare cu succes",
        "user_id": user["id"]
    })


if __name__ == "__main__":
    app.run(debug=True)
