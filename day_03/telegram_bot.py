from flask import Flask, render_template, request
import requests
from decouple import config
from pprint import pprint as pp
app = Flask(__name__)

base = 'https://api.telegram.org'
token = config('TOKEN')


@app.route('/')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    method = 'getUpdates'
    url = f'{base}/bot{token}/{method}'
    res = requests.get(url).json()
    # pp(res)

    chat_id = res['result'][0]['message']['chat']['id']

    method = 'sendMessage'
    text = request.args.get('msg')
    url = f'{base}/bot{token}/{method}?chat_id={chat_id}&text={text}'

    requests.get(url)
    return '전송완료'