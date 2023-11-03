from flask import Flask

app = Flask(__name__)

# ルートURLへのGETリクエストに応答
@app.route('/', methods=['GET'])
def hello():
    return 'Hello, GET Request!'

if __name__ == '__main__':
    app.run()
