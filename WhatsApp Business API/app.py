import requests
import json

# Set up API endpoint and authentication headers
url = "https://api.chat-api.com/instance{instance_id}/message?token={token}"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {token}"
}

# Define a function to send messages
def send_message(phone_number, message):
    data = {
        "phone": phone_number,
        "body": message
    }
    response = requests.post(url.format(instance_id="{your_instance_id}", token="{your_token}"), headers=headers, data=json.dumps(data))
    print(response.content)

# Define a function to process incoming messages
def process_message(message):
    if "hello" in message.lower():
        send_message("whatsapp:+1234567890", "Hi there!")
    elif "help" in message.lower():
        send_message("whatsapp:+1234567890", "I'm here to help you! Just send me a message and I'll do my best to assist you.")
    else:
        send_message("whatsapp:+1234567890", "Sorry, I didn't understand your message. Type 'help' for a list of commands.")

# Set up a webhook to receive incoming messages
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    message = request.json["messages"][0]["body"]
    process_message(message)
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=True)
