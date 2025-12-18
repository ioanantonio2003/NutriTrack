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

DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
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
    kcal_per_100g REAL NOT NULL
);
DROP TABLE IF EXISTS meals;

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

INSERT INTO daily_progress(user_id,date,kcal_consumed,water_consumed,activity_calories,kcal_goal,water_goal,activity_goal)
        VALUES(1,'2025-12-17',1,2,3,2300,2,60)

--TEST
INSERT INTO users (name, password, age)
VALUES ('Test User', '1234', 25);

select*from users

ALTER TABLE recipes
ADD COLUMN type TEXT;

INSERT INTO recipes (title, description, calories, type)
VALUES 
('Vegan Salad', 'A healthy mix of vegetables and tofu.', 250, 'vegan'),
('Spicy Chili', 'Hot chili with beans and spices.', 450, 'spicy');


INSERT INTO MEALS (name,kcal_per_100g) VALUES('pui', 50);
INSERT INTO MEALS (name,kcal_per_100g) VALUES('piure', 150);



INSERT INTO recipes (title, description, calories, type) VALUES
('Spicy Chili Chicken', 'A fiery chicken chili with peppers and beans', 450, 'spicy'),
('Protein Pancakes', 'Fluffy pancakes made with protein powder and oats', 300, 'protein'),
('Spicy Tofu Stir-Fry', 'Tofu and vegetables cooked in a spicy sauce', 400, 'spicy'),
('Vegan Lentil Soup', 'Comforting lentil soup with herbs and spices', 250, 'vegan'),
('Protein Smoothie', 'A smoothie with banana, peanut butter, and whey protein', 200, 'protein'),
('Spicy Shrimp Tacos', 'Tacos filled with spicy marinated shrimp and slaw', 420, 'spicy'),
('Vegan Avocado Toast', 'Whole grain toast topped with smashed avocado and seeds', 280, 'vegan'),
('Protein Chicken Salad', 'Grilled chicken with mixed greens and protein-rich dressing', 350, 'protein'),
('Spicy Veggie Curry', 'A hot curry with seasonal vegetables and coconut milk', 380, 'spicy');
