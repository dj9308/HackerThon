from flask import Flask, render_template, request
import requests
from decouple import config
from pprint import pprint as pp
import random
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
#https://api.telegram.org/bot911358092:AAHI3lCGez-4JssmOuotIgStnRvXExcsK4Y/setWebhook?url=https://ef6a055d.ngrok.io/911358092:AAHI3lCGez-4JssmOuotIgStnRvXExcsK4Y
@app.route(f'/{token}',methods=['POST'])
def webhook():
    #1. webhook을 통해 telegram에 보낸 요청 안에 있는 메세지를 가져옴
    url = f'{base}/bot{token}/setWebhook?url=https://ef6a055d.ngrok.io/{token}'
    requests.get(url)
    #2. 그대로 전송
    res = request.get_json()

    if res.get('message'):
        text = res.get('message').get('text')
        chat_id = res.get('message').get('chat').get('id')
        method = 'sendMessage'


        if '로또' in text:
            num = range(1,46)
            lottonum = sorted(random.sample(num,6))
            text = lottonum
        elif text[0:4] == '/번역 ':
            naver_client_id = config('NAVER_CLIENT_ID')
            naver_client_secret = config('NAVER_CLIENT_SECRET')
            url = 'https://openapi.naver.com/v1/papago/n2mt'
            text = text[4:]
            headers = {
                'X-Naver-Client-Id' : naver_client_id,
                'X-Naver-Client-Secret' : naver_client_secret
            }
            data = {
                'source' : 'ko',
                'target' : 'en',
                'text' : text
            }
            response = requests.post(url,data=data,headers=headers).json()
            text = response.get('message').get('result').get('translatedText')
        elif '비트코인' in text:
            url = 'https://api.bithumb.com/public/ticker/BTC'
            response = requests.get(url).json()
            text = response.get('data').get('opening_price')
            
        url = f'{base}/bot{token}/{method}?chat_id={chat_id}&text={text}'
        requests.get(url)
    return '', 200