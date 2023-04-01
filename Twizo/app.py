import requests
import json

TWIZO_API_KEY = 'your_twizo_api_key_here'

def send_message(to, body):
    url = 'https://api.twizo.com/2.0/whatsapp/messages'
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'X-Twizo-Access-Token': TWIZO_API_KEY}
    data = {
        'to': to,
        'content': {
            'text': body
        }
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return True
    else:
        return False

def receive_message():
    url = 'https://api.twizo.com/2.0/whatsapp/messages'
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'X-Twizo-Access-Token': TWIZO_API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        messages = json.loads(response.content)
        return messages
    else:
        return None
