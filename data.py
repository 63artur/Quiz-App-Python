import requests
data = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
data = data.json()
question_data = data['results']