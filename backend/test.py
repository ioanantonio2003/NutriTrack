import requests

BASE_URL = "http://127.0.0.1:5000"

#TEST REGISTER
def test_register(name, password, age):
    url = f"{BASE_URL}/register"
    data = {
        "name": name,
        "password": password,
        "age": age
    }
    response = requests.post(url, json=data)
    print("REGISTER RESPONSE:", response.status_code, response.json())

#TEST LOGIN
def test_login(name, password):
    url = f"{BASE_URL}/login"
    data = {
        "name": name,
        "password": password
    }
    response = requests.post(url, json=data)
    print("LOGIN RESPONSE:", response.status_code, response.json())

if __name__ == "__main__":
    test_register("ioan", "1234", 22) #inregistrare
    test_login("ioan", "1234") #logare
    test_login("ioan", "wrongpass")  # parola gresita