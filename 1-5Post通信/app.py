from flask import Flask, request

app = Flask(__name__)

# ルートURLへのPOSTリクエストに応答
@app.route('/', methods=['POST'])
def receive_post_data():
    if request.method == 'POST':
        data = request.form['data']
        return f'Received POST data: {data}'

if __name__ == '__main__':
    app.run()
