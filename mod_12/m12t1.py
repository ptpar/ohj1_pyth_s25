import requests
import random

# Retrieve a list of available categories: https://api.chucknorris.io/jokes/categories
categories_response = requests.get("https://api.chucknorris.io/jokes/categories").json()
category = random.choice(categories_response)

joke_response = requests.get(f"https://api.chucknorris.io/jokes/random?category={category}").json()
print(joke_response["value"])