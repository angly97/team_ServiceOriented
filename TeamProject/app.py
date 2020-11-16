#https://www.fun-coding.org/mysql_basic6.html -- pymysql 사용

from flask import Flask, render_template
from DB import mysql

app = Flask(__name__)

db = mysql.testdb()

@app.route("/")
def hello():
    result = db.select_all()
    return str(result)


@app.route("/abc") #url과 맵핑되는 x
def hello2():
    return "<h1>Hello World2222!</h1>"

#파라미터 input
@app.route("/univ/<username>")
def get_profile(username):
    return "profile: " + username

@app.route("/first/<username>")
def get_first(username):
    return "<h3>Hello " + username + "!</h3>"

#html
#get_html이라는 함수를 만들고 test로 라우트
#render_template -> view.html을 찾아가서 전달데이터를 넘겨라
@app.route("/test")
def get_html1():
    return render_template('view.html', aa = '전달데이터')

@app.route("/index")
def get_html():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()

