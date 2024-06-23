import requests
from datetime import datetime as dt

GENDER = 
WEIGHT_KG = 
HEIGHT_CM = 
AGE = 

APP_ID = 
APP_KEY = 

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = 

user_input = input("What workout you did buddy: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}


parameters = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

exercise_result = requests.post(url=exercise_endpoint, json=parameters, headers=headers).json()

today_date = dt.now().strftime("%d.%m.%Y")
now_time = dt.now().strftime("%X")

# Now update data in google sheets
for exercise in exercise_result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs)
    print(sheet_response.text)