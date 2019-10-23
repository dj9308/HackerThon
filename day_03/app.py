from flask import Flask, render_template, request
import random
import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world!"

@app.route("/html")
def html():
    return "<h1> This is HTML h1 tag! </h1>"

@app.route("/d_day")
def d_day():
    today = datetime.datetime.now()
    finish = datetime.datetime(2019,11,27)
    remain = finish -today
    return f'우리가 같이 있을 수 있는 시간이 이제 {remain}남음'

@app.route("/naver")
def naver():
    return render_template("naver.html")

    
@app.route("/google")
def google():
    return render_template("google.html")

@app.route("/myday")
def myday():
    today = datetime.datetime.now()
    return render_template("myday.html", today = today)

@app.route("/ping")
def ping():
    return render_template("ping.html")

@app.route("/pong")
def pong():
    name = request.args.get('name')
    age = request.args.get('age')
    return render_template("pong.html", name = name, age = age)

@app.route("/god")
def god():
    return render_template("god.html")

@app.route("/godAnswer")
def godAnswer():
    name = request.args.get('name')
    words = ['사랑을 적당히~','노안도 적당.. 엌ㅋ.. 쏟았넿ㅎㅎ', '성욕은 언제 넣었는지 모르지만 충분하군!','운을 실수한 척하고 다 털어넣자 ㅎㅎ']
    random = random.sample(words,3)
    return render_template("godAnswer.html", name = name, random = random)
