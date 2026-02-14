import requests

APP_ID="app_17e2207c3b4e488f8d18080c"
API_KEY="nix_live_QY5tlaFc8FkUFsJV2AzoVKAcS0a75UfC"

headers={
"x-app-id": APP_ID,
"x-app-key": API_KEY
}

response=requests.get("https://app.100daysofpython.dev/healthz",headers=headers)
print(response.text)
print(response.json())

# exercise_input=input("Tell me which exercise you did today")
#
# parameters={
#
#   "query": exercise_input,
#   "weight_kg": 70,
#   "height_cm": 175,
#   "age": 30,
#   "gender": "male"
# }
#
#
#
# calorie_burned=requests.post("https://app.100daysofpython.dev/v1/nutrition/natural/exercise",headers=headers,json=parameters)
#
#
# print(calorie_burned.json())
# print(calorie_burned.text)
#
#
# data= calorie_burned.json()


parameters_sheety={
  "sheet1": [
    {
      "date": "21/07/2020",
      "time": "15:00:00",
      "exercise": "Running",
      "duration": 22,
      "calories": 130,
      "id": 3
    }
  ]
}


sheety_get=requests.get("https://api.sheety.co/f878894ca96eedd8055b5a328db0a5d3/workouts/sheet1")
sheety_get.raise_for_status()
print(sheety_get.json())
print(sheety_get.text)
sheety_response=requests.post("https://api.sheety.co/f878894ca96eedd8055b5a328db0a5d3/workouts/sheet1",json=parameters_sheety,headers=None)
sheety_response.raise_for_status()
print(sheety_response.text)
print(sheety_response.json())



# for i in data["exercises"]:
#     exercise=i[1]["name"]
#     exercise_activity=i[0]["user_input"]
#     with open(f"letter_templates/", "w") as f:
#         f.write(exercise)
#         f.write(exercise_activity)
#
#
# parameters={
#
#   "query": "ran 3 miles",
#   "weight_kg": 70,                  // Optional: Weight in kg (1-500)
#   "height_cm": 175,                 // Optional: Height in cm (1-300)
#   "age": 30,                        // Optional: Age (1-150)
#   "gender": "male"                  // Optional: "male" or "female"
# }