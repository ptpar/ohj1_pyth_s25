import requests

try:
    response = requests.get('https://api.chucknorris.io/jokes/random')
    if response.status_code == 200:
        joke = response.json()
        print(joke['value'])
    else:
        print('Tapahtui odottamaton virhe: statuskoodi ei ole 200')
except requests.exceptions.RequestException as e:
    print('Hakua ei voitu suorittaa')
except Exception as e:
    print('Tapahtui odottamaton virhe:', e)