import psycopg2
from flask import Flask, request, redirect, render_template

#ベーシック認証
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)

#ベーシック認証
auth = HTTPBasicAuth()

#new db class
def create_table():
    # データベース接続
    conn = psycopg2.connect(
        dbname='mydb',
        user='hinata',
        password='hinata',
        host='localhost',
        port='5432'
    )
    cursor = conn.cursor()

    # テーブルを作成（初回実行時のみ必要）
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id SERIAL PRIMARY KEY,
            username VARCHAR,
            post_content TEXT
        )
    ''')

    conn.commit()
    cursor.close()
    conn.close()

# post class
@app.route('/post', methods=['GET', 'POST'])
def input_form():
    if request.method == 'POST':
        # フォームデータ取得
        username = request.form.get('username')
        post_content = request.form.get('postContent')

        # データベースに挿入
        conn = psycopg2.connect(
            dbname='mydb',
            user='hinata',
            password='hinata',
            host='localhost',
            port='5432'
        )
        cursor = conn.cursor()
        cursor.execute('INSERT INTO posts (username, post_content) VALUES (%s, %s)', (username, post_content))
        conn.commit()
        cursor.close()
        conn.close()

        # 挿入したデータをコンソールに表示
        print(f"ユーザー名：{username}、投稿内容：{post_content} のデータをデータベースに挿入しました。")

        return redirect('/timeline')
    return render_template('sns_post_form.html')

# timeline lead root class
@app.route('/timeline')
def sns_timeline():
    # データベースからタイムラインのデータを取得
    timeline_data = get_timeline_data()
    return render_template('sns_timeline.html', timeline_data=timeline_data)

# timeline lead class
def get_timeline_data():
    # データベース接続
    conn = psycopg2.connect(
        dbname='mydb',
        user='hinata',
        password='hinata',
        host='localhost',
        port='5432'
    )

    # カーソルを作成
    cursor = conn.cursor()

    # データベースから投稿データを取得
    cursor.execute('SELECT username, post_content FROM posts ORDER BY id DESC;')
    timeline_data = cursor.fetchall()

    # カーソルとデータベースをクローズ
    cursor.close()
    conn.close()
    return timeline_data

#hub class
#@app.route('/')
#def home():
#    return render_template('hub.html')

#ベーシック認証
users = {
    "testuser": "engsns"
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None
#https://engchatapp.azurewebsites.net/
@app.route('/')
@auth.login_required
def index():
    return render_template('hub.html')

if __name__ == "__main__":
    #create_table()
    app.run(debug=True)
