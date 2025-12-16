import requests

BASE_URL = "http://127.0.0.1:5000"

# #TEST REGISTER
# def test_register(name, password, age):
#     url = f"{BASE_URL}/register"
#     data = {
#         "name": name,
#         "password": password,
#         "age": age
#     }
#     response = requests.post(url, json=data)
#     print("REGISTER RESPONSE:", response.status_code, response.json())

# #TEST LOGIN
# def test_login(name, password):
#     url = f"{BASE_URL}/login"
#     data = {
#         "name": name,
#         "password": password
#     }
#     response = requests.post(url, json=data)
#     print("LOGIN RESPONSE:", response.status_code, response.json())

# if __name__ == "__main__":
#     test_register("ioan", "1234", 22) #inregistrare
#     test_login("ioan", "1234") #logare
#     test_login("ioan", "wrongpass")  # parola gresita




# user_id = 1  #test id

# def test_add_water(amount):
#     response = requests.post(f"{BASE_URL}/add_water", json={"user_id": user_id, "water": amount})
#     print("Adaugare apa:", response.status_code, response.json())

# def test_add_meal(kcal):
#     response = requests.post(f"{BASE_URL}/add_meal", json={"user_id": user_id, "kcal": kcal})
#     print("Adaugare masa:", response.status_code, response.json())

# def test_add_activity(activity_cal):
#     response = requests.post(f"{BASE_URL}/add_activity", json={"user_id": user_id, "activity_cal": activity_cal})
#     print("Adaugare activitarea", response.status_code, response.json())


# if __name__ == "__main__":
#     print("CREATE ROW")
#     test_add_water(0.5)
#     test_add_meal(400)
#     test_add_activity(150)

#     print("\nUPDATE")
#     test_add_water(0.3)
#     test_add_meal(200)
#     test_add_activity(100)


# def test_update_goals():
#     url = f"{BASE_URL}/update_goals"
#     data = {
#         "user_id": 1,
#         "kcal_goal": 2300,
#         "water_goal": 2.5,
#         "activity_goal": 75
#     }

#     response = requests.post(url, json=data)
#     print("UPDATE GOALS:", response.status_code, response.json())


# if __name__ == "__main__":
#     test_update_goals()

# def test_progress(days):
#     response = requests.get(
#         f"{BASE_URL}/progress",
#         params={"user_id": 1, "range": days}
#     )
#     print(response.status_code)
#     print(response.json())

# if __name__ == "__main__":
#     test_progress(7)
#     test_progress(30)

# def test_get_recipes(recipe_type=None):
#     params = {}
#     if recipe_type:
#         params["type"] = recipe_type

#     response = requests.get(f"{BASE_URL}/recipes", params=params)
#     print("STATUS:", response.status_code)
#     print("DATA:", response.json())

# if __name__ == "__main__":
#     test_get_recipes()    
#     test_get_recipes("vegan")  
#     test_get_recipes("spicy")  

def test_streak(user_id):
    url = f"{BASE_URL}/streak"
    params = {"user_id": user_id}
    response = requests.get(url, params=params)
    print("STREAK:", response.status_code, response.json())

if __name__ == "__main__":
    test_streak(1) 
