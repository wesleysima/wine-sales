import requests, json

def get_clients():
    response = requests.get('http://www.mocky.io/v2/598b16291100004705515ec5', headers={'content-type': 'application/json'}, timeout=10)

    if response.status_code == 200:
        return json.loads(response.content)

def get_history_and_purchases():
    response = requests.get('http://www.mocky.io/v2/598b16861100004905515ec7', headers={'content-type': 'application/json'}, timeout=10)

    if response.status_code == 200:
        return json.loads(response.content)

    