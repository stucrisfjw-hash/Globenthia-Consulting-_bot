from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Importar configuración
import settings

FB_PAGE_TOKEN = settings.FB_PAGE_TOKEN
VERIFY_TOKEN = settings.VERIFY_TOKEN

@app.route('/')
def home():
    return "🤖 Bot Multi-Tenant activo en Render!"

# Webhook para Facebook Messenger
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return request.args.get("hub.challenge") if token_sent == VERIFY_TOKEN else "Token inválido"
    else:
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    recipient_id = message['sender']['id']
                    if 'text' in message['message']:
                        response_sent_text = message['message']['text']
                        send_message(recipient_id, f"Recibí: {response_sent_text}")
        return "Message Processed"

def send_message(recipient_id, text):
    url = "https://graph.facebook.com/v12.0/me/messages"
    params = {"access_token": FB_PAGE_TOKEN}
    headers = {"Content-Type": "application/json"}
    data = {
        "recipient": {"id": recipient_id},
        "message": {"text": text}
    }
    requests.post(url, params=params, headers=headers, json=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
