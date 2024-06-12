from flask import Flask, request
import requests
import webbrowser
from services.summarize import summarize

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Hello World"

@app.route('/create', methods=['GET'])
def create_document():
    url = request.args.get('url')
    summarized = summarize(url)
    
    response = requests.post('https://script.google.com/macros/s/AKfycbwgYt-sqixHoaLjyqtx-NCcaVHQNZPrRyK1cspg73mQnDDuIoI8QVJxEYeNHzQHuG9Bxw/exec', json=summarized)
    
    if response.status_code == 200:
        webbrowser.open(response.text)
        return "done!"
    else:
        return (f"狀態碼：{response.status_code}")

if __name__ == '__main__':
    app.run()