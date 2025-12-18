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


INSERT INTO daily_progress(user_id,date,kcal_consumed,water_consumed,activity_calories,kcal_goal,water_goal,activity_goal)
        VALUES(2,'2025-12-17',1,2,3,2300,2,60)

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



INSERT INTO daily_progress(user_id, date, kcal_consumed, water_consumed, activity_calories, kcal_goal, water_goal, activity_goal)
VALUES
(2, '2025-12-16', 1800, 1.5, 200, 2300, 2, 60),
(2, '2025-12-15', 1750, 1.8, 250, 2300, 2, 60),
(2, '2025-12-14', 1900, 2, 180, 2300, 2, 60),
(2, '2025-12-13', 2000, 2.2, 220, 2300, 2, 60),
(2, '2025-12-12', 1850, 1.9, 210, 2300, 2, 60),
(2, '2025-12-11', 1700, 1.7, 190, 2300, 2, 60),
(2, '2025-12-10', 1950, 2.1, 230, 2300, 2, 60),
(2, '2025-12-09', 1800, 1.6, 200, 2300, 2, 60),
(2, '2025-12-08', 1750, 1.5, 180, 2300, 2, 60),
(2, '2025-12-07', 1900, 1.8, 210, 2300, 2, 60);


DELETE FROM recipes;


INSERT INTO recipes (title, description, calories, type) VALUES
('Supă picantă de legume', 'Fierbe legumele și adaugă condimente picante', 150, 'spicy'),
('Salată vegană cu quinoa', 'Amestecă quinoa cu legume proaspete și dressing', 200, 'vegan'),
('Piept de pui la grătar', 'Gătește pieptul de pui pe grătar', 250, 'protein'),
('Chili con carne', 'Fierbe carnea cu fasole și condimente picante', 300, 'spicy'),
('Smoothie verde vegan', 'Mixează spanac, banană și lapte vegetal', 180, 'vegan'),
('Ouă fierte cu avocado', 'Fierbe ouăle și servește cu avocado', 220, 'protein'),
('Tocăniță picantă de linte', 'Fierbe lintea cu legume și condimente', 210, 'spicy'),
('Paste cu legume vegan', 'Fierbe pastele și amestecă cu legume', 230, 'vegan'),
('Somon la cuptor', 'Coace somonul cu lămâie și ierburi', 280, 'protein'),
('Ardei umpluți picant', 'Umple ardeii cu orez și condimente', 240, 'spicy');


INSERT INTO MEALS (name, kcal_per_100g) VALUES
('ceafa', 290),
('paste', 350),
('orez', 130),
('fasole', 340),
('mazare', 80),
('morcovi', 41),
('cartofi', 77),
('rosii', 18),
('castraveti', 16),
('spanac', 23),
('broccoli', 34),
('varza', 25),
('ardei', 31),
('ceapa', 40),
('usturoi', 149),
('salata', 15),
('vinete', 25),
('ciuperci', 22),
('avocado', 160),
('nuci', 650),
('migdale', 575),
('seminte', 580),
('lapte', 60),
('branza', 350),
('iaurt', 60),
('oua', 155),
('somon', 208),
('ton', 132),
('carne', 250),
('vita', 250),
('porc', 290),
('curcan', 135),
('cereale', 370),
('miere', 304),
('ciocolata', 546),
('marmelada', 250),
('pâine', 265),
('covrigi', 340),
('ovaz', 389),
('quinoa', 120);