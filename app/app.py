from flask import Flask

app = Flask(__name__)


@app.route('/')
def welcome():
    return 'root'


@app.route('/api/v1/hello-world-3')
def hello_world():
    return 'Hello World 3'


if __name__ == '__main__':
    print(1)
    app.run(host='0.0.0.0', port=81)
