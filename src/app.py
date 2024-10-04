import openai
from flask import Flask, request, jsonify
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

app = Flask(__name__)
@app.route('/whatsapp', methods=['POST'])

client = openai.OpenAI(api_key=OPENAI_API_KEY)

def chatbot_response(message):
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
        "role": "user",
        "content": message
        }
    ],
    )
    completion = response.choices[0].message.content
    return completion

def handle_incoming_message():
    message = request.from['Body']
    response = chatbot_response(message)
    client = Client(account_sid, auth_token)
    number = request.from['From']

    to_number = number
    client.messages.create(
        to=to_number,
        from='whatsapp:+14155238886',
        body=response)
    
    return 'Return: Ok'

if __name__ == '__main__':
    app.run()