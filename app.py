import os
import json
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# load setting
load_dotenv()
with open('./config.json', 'r') as f:
    CONFIG = json.load(f)

SERVICE_KEY = os.getenv('SERVICE_KEY')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Hello World"

if __name__ == '__main__':
    app.run(CONFIG['HOST'], CONFIG['PORT'], debug=True)