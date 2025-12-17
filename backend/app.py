from flask import Flask, request, jsonify
from db import get_db_connection
from datetime import datetime,timedelta
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "NutriTrack backend is running"


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
@app.route("/add_water", methods=["POST"])
def add_water():
    data = request.json
    user_id = data.get("user_id")
    water = data.get("water")  #in litri

    conn = get_db_connection()
    cur = conn.cursor()

    #verificam daca s-au introdus date astazi
    row = cur.execute(
        "SELECT * FROM daily_progress WHERE user_id = ? AND date = DATE('now')",
        (user_id,)
    ).fetchone()

    #daca s-au introdus doar acutalizam apa bautaa
    if row:
        new_water = row["water_consumed"] + water
        cur.execute(
            "UPDATE daily_progress SET water_consumed = ? WHERE user_id = ? AND date = DATE('now')",
            (new_water, user_id)
        )
    else:
        #daca nu, luam goalurile generale din USERS
        user = cur.execute(
            "SELECT kcal_goal, water_goal, activity_goal FROM users WHERE id = ?",
            (user_id,)
        ).fetchone()

        #si creem un nou obiect in tabela
        cur.execute(
            "INSERT INTO daily_progress (user_id, date, water_consumed, kcal_consumed, activity_calories, kcal_goal, water_goal, activity_goal) "
            "VALUES (?, DATE('now'), ?, 0, 0, ?, ?, ?)",
            (user_id, water, user["kcal_goal"], user["water_goal"], user["activity_goal"])
        )

    conn.commit()
    conn.close()
    return jsonify({"message": "Apa introdusa cu succes"})


#functie adaugare de activitate
@app.route("/add_activity", methods=["POST"])
def add_activity():
    data = request.json
    user_id = data.get("user_id")
    activity_cal = data.get("activity_cal")  #calorii arse

    conn = get_db_connection()
    cur = conn.cursor()
    
    #verificam daca s-au itnrodus date azi
    row = cur.execute(
        "SELECT * FROM daily_progress WHERE user_id = ? AND date = DATE('now')",
        (user_id,)
    ).fetchone()

    #daca da, actualizam kcal arse deja
    if row:
        new_activity = row["activity_calories"] + activity_cal
        cur.execute(
            "UPDATE daily_progress SET activity_calories = ? WHERE user_id = ? AND date = DATE('now')",
            (new_activity, user_id)
        )
    else:#daca nu luam goalurile generale din USERS
        user = cur.execute(
            "SELECT kcal_goal, water_goal, activity_goal FROM users WHERE id = ?",
            (user_id,)
        ).fetchone()

    #si introducem un nou obiect in tabela
        cur.execute(
            "INSERT INTO daily_progress (user_id, date, water_consumed, kcal_consumed, activity_calories, kcal_goal, water_goal, activity_goal) "
            "VALUES (?, DATE('now'), 0, 0, ?, ?, ?, ?)",
            (user_id, activity_cal, user["kcal_goal"], user["water_goal"], user["activity_goal"])
        )

    conn.commit()
    conn.close()
    return jsonify({"message": "Activitiate introdusa cu succes"})


#functie pentru editarea goal-urilor
@app.route("/update_goals", methods=["POST"])
def update_goals():
    user_id = request.json.get("user_id")
    kcal_goal = request.json.get("kcal_goal")
    water_goal = request.json.get("water_goal")
    activity_goal = request.json.get("activity_goal")

    #daca lipseste un parametru nu poti schimba
    if not all([user_id, kcal_goal, water_goal, activity_goal]):
        return jsonify({"error": "Lipsesc date"}), 400

    conn = get_db_connection()
    cur = conn.cursor()

    #Schimbam obiectivele generale
    cur.execute("""
        UPDATE users
        SET kcal_goal = ?, water_goal = ?, activity_goal = ?
        WHERE id = ?
    """, (kcal_goal, water_goal, activity_goal, user_id))

    #Schimbam obiectivele din daily de azi daca exista
    cur.execute("""
        UPDATE daily_progress
        SET kcal_goal = ?, water_goal = ?, activity_goal = ?
        WHERE user_id = ?
          AND date = DATE('now')
    """, (kcal_goal, water_goal, activity_goal, user_id))

    conn.commit()
    conn.close()

    return jsonify({"message": "Goal-uri actualizate cu succes"})


#functia pentru aflarea progresului
@app.route("/progress", methods=["GET"])
def get_progress():
    user_id = request.args.get("user_id")
    days = int(request.args.get("range", 7))

    #luam toate datele in functie de range ul trimis
    conn = get_db_connection()
    rows = conn.execute("""
        SELECT *
        FROM daily_progress
        WHERE user_id = ?
        ORDER BY date DESC
        LIMIT ?
    """, (user_id, days)).fetchall()
    conn.close()

    result = []

    #luam fiecare linie si verificam daca obiectivul a fost atins
    for row in rows:
        kcal_ok = row["kcal_consumed"] <= row["kcal_goal"]
        water_ok = row["water_consumed"] >= row["water_goal"]
        activity_ok = row["activity_calories"] >= row["activity_goal"]

        day_ok = kcal_ok and water_ok and activity_ok

        result.append({
            "date": row["date"],
            "kcal": {
                "value": row["kcal_consumed"],
                "goal": row["kcal_goal"],
                "ok": kcal_ok
            },
            "water": {
                "value": row["water_consumed"],
                "goal": row["water_goal"],
                "ok": water_ok
            },
            "activity": {
                "value": row["activity_calories"],
                "goal": row["activity_goal"],
                "ok": activity_ok
            },
            "day_ok": day_ok
        })

    return jsonify(result)

#functie pentru colectarea retetelor
@app.route("/recipes", methods=["GET"])
def get_recipes():
    recipe_type = request.args.get("type")  #type daca exista

    conn = get_db_connection()

    #daca exista un type , filtram doar acele retete
    if recipe_type:  
        rows = conn.execute(
            "SELECT * FROM recipes WHERE type = ?", (recipe_type,)
        ).fetchall()
    else:#daca nu , le lua, pe toate
        rows = conn.execute("SELECT * FROM recipes").fetchall()

    conn.close()

    result = []
    for row in rows:
        result.append({
            "id": row["id"],
            "title": row["title"],
            "description": row["description"],
            "calories": row["calories"],
            "type": row["type"]
        })

    return jsonify(result)


#functie pentru streak incepand din ziua de ieri
@app.route("/streak", methods=["GET"])
def get_streak():
    user_id = request.args.get("user_id")

    conn = get_db_connection()

    rows = conn.execute("""
        SELECT date
        FROM daily_progress
        WHERE user_id = ?
        ORDER BY date DESC
    """, (user_id,)).fetchall()

    conn.close()

    dates = [
        datetime.strptime(row["date"], "%Y-%m-%d").date()
        for row in rows
    ]

    today = datetime.now().date()
    yesterday = today - timedelta(days=1)

    streak = 0
    current_day = yesterday

    # clcularea streakului incepand de ieri
    while current_day in dates:
        streak += 1
        current_day -= timedelta(days=1)

    # daca s a introdus azi adaugam si ziua de azi
    if today in dates:
        streak += 1

    return jsonify({"streak": streak})


#functie pentru a verifica daca exista date introduse in ziua respectiva
@app.route("/reminder", methods=["GET"])
def check_daily_reminder():
    user_id = request.args.get("user_id")

    
    conn = get_db_connection()
    row = conn.execute("""
        SELECT *
        FROM daily_progress
        WHERE user_id = ? AND date = ?
    """, (user_id, datetime.now().strftime("%Y-%m-%d"))).fetchone()
    conn.close()

    if row:
        # s-au introdus deja date
        return jsonify({"reminder": False})
    else:
        # nu s-au introdus date
        return jsonify({"reminder": True})
    
#functie pt preluarea goal urilor generale
@app.route("/goals", methods=["GET"])
def get_goals():
    user_id = request.args.get("user_id") 


    conn = get_db_connection()
    user = conn.execute(
        "SELECT kcal_goal, water_goal, activity_goal FROM users WHERE id = ?",
        (user_id,)
    ).fetchone()
    conn.close()

    if user is None:
        return jsonify({"error": "EROARE"}), 404

    return jsonify({
        "kcal_goal": user["kcal_goal"],
        "water_goal": user["water_goal"],
        "activity_goal": user["activity_goal"]
    })

#functie pentru preluarea tuturor akimentelor
@app.route("/meals", methods=["GET"])
def get_meals():
    conn = get_db_connection()
    rows = conn.execute("SELECT name, kcal_per_100g FROM meals").fetchall()
    conn.close()
    meals = [{"name": row["name"], "kcal_per_100g": row["kcal_per_100g"]} for row in rows]
    return jsonify({"meals": meals})


#functie pentru adaugarea unei mese 
@app.route("/add_meal", methods=["POST"])
def add_meal():
    data = request.json
    user_id = data.get("user_id")
    meal_name = data.get("name")
    amount = float(data.get("amount", 0)) #gramele de mancarea

    conn = get_db_connection()
    meal = conn.execute("SELECT kcal_per_100g FROM meals WHERE name = ?", (meal_name,)).fetchone()
    if not meal:
        conn.close()
        return jsonify({"error": "Aliment inexistent"}), 404

    kcal_added = (meal["kcal_per_100g"] * amount) / 100

    # Verificam daca s a introdus azi vreo data
    today = datetime.now().strftime("%Y-%m-%d")
    existing = conn.execute(
        "SELECT * FROM daily_progress WHERE user_id = ? AND date = ?",
        (user_id, today)
    ).fetchone()

    if existing:
        #daca da actualizam kcal consumate
        conn.execute(
            "UPDATE daily_progress SET kcal_consumed = kcal_consumed + ? WHERE user_id = ? AND date = ?",
            (kcal_added, user_id, today)
        )
    else:
        # daca nu creem un nou obiect
        conn.execute(
            "INSERT INTO daily_progress (user_id, date, kcal_consumed, water_consumed, activity_calories) VALUES (?, ?, ?, 0, 0)",
            (user_id, today, kcal_added)
        )

    conn.commit()
    conn.close()
    return jsonify({"message": "Masa adaugata cu succes"})



if __name__ == "__main__":
    app.run(debug=True)

