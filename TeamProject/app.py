from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('test')
def hello_world():
    return 'test'

@app.route('/pushTest')
def hello_world():
    return 'pushTest'

@app.route("/index")
def get_html():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
