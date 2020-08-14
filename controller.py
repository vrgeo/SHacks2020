from nlp import witprocess
import json 
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

with open('definitions.json') as fr:    
    definitions = json.load(fr)

@app.route('/')
def home():
    return '<h1>Online</h1>'

@app.route('/process', methods=['GET'])
def process():
    input = request.args.get('input')
    response = witprocess.recievemessage(input)
    return jsonify(response)

if __name__ == "__main__":
  app.run()