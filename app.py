from flask import Flask, request
import requests
from crawler import fetch_article

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Hello World"

@app.route('/create', methods=['POST'])
def create_document():
    url = request.args.get('url')
    article = fetch_article(url=url)
    
    response = requests.post('https://script.google.com/macros/s/AKfycby6LfysEkt2vAr_ztIfMuZ736PyKNXz1iJDjiw5ZrFpLkp3gojEKsfLk1jVtq0JZgR71w/exec', json=article)
    
    if response.status_code == 200:
        return response.text
    else:
        return (f"狀態碼：{response.status_code}")

if __name__ == '__main__':
    app.run()