--TABELA USERS

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    password TEXT NOT NULL,
    age INTEGER,
    kcal_goal REAL DEFAULT 2000,
    water_goal REAL DEFAULT 2,
    activity_goal REAL DEFAULT 60
);

--TABELA MEALS

CREATE TABLE meals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    calories_per_100g REAL NOT NULL
);

--TABELA RECIPES

CREATE TABLE recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    calories REAL
);

--TABELA DAILY_PROGRESS

CREATE TABLE daily_progress (
    user_id INTEGER NOT NULL,
    date TEXT NOT NULL, -- format 'YYYY-MM-DD'
    kcal_consumed REAL DEFAULT 0,
    water_consumed REAL DEFAULT 0,
    activity_calories REAL DEFAULT 0,
    kcal_goal REAL NOT NULL,
    water_goal REAL NOT NULL,
    activity_goal REAL NOT NULL,
    PRIMARY KEY (user_id, date),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

--TEST
INSERT INTO users (name, password, age)
VALUES ('Test User', '1234', 25);

select*from users