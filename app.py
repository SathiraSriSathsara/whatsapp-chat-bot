from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/bot", methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()

    if 'hello' in incoming_msg:
        resp.message("Hi there! How can I help you?")
    elif 'help' in incoming_msg:
        resp.message("You can ask me questions or give me commands and I will do my best to help you.")
    else:
        resp.message("Sorry, I didn't understand your message. Type 'help' for a list of commands.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
