Here, we're using Flask to create a web server that listens for incoming messages from WhatsApp. When a message is received, the bot function is called, which checks the message contents and sends a response using the Twilio API.

To use this chatbot, you'll need to set up a Twilio account and create a WhatsApp Sandbox. Once you have your Twilio credentials, you can run this script and configure your Twilio Sandbox to send incoming messages to the URL of your Flask app.

Note that this is just a simple example and you'll likely want to customize the bot's responses and add more functionality. Also, keep in mind that while Twilio provides a free trial, there may be fees associated with sending messages to and from WhatsApp.
