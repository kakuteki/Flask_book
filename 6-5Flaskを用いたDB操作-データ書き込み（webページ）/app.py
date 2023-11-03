import psycopg2
from flask import Flask, render_template, request

app = Flask(__name__)

def create_table():
    # データベースに接続
    conn = psycopg2.connect(
        dbname='mydb',
        user='hinata',
        password='hinata',
        host='localhost',
        port='5432'
    )

    # カーソルを作成
    cursor = conn.cursor()

    # テーブルがない場合は作成（最初の実行時のみ必要）
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR,
            age INTEGER
        )
    ''')

    # 変更を保存（コミット）
    conn.commit()

    # データベースとカーソルをクローズ
    cursor.close()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def input_form():
    if request.method == 'POST':
        # フォームから送信されたデータを取得
        name = request.form.get('name')
        age = int(request.form.get('age'))

        # データベースにデータを挿入
        conn = psycopg2.connect(
            dbname='mydb',
            user='hinata',
            password='hinata',
            host='localhost',
            port='5432'
        )
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, age) VALUES (%s, %s)', (name, age))
        conn.commit()
        cursor.close()
        conn.close()

        # 入力データをコマンドラインに表示
        print(f"名前：{name}、年齢：{age} のデータをデータベースに挿入しました。")

    return render_template('input_form.html')

if __name__ == "__main__":
    create_table()  # テーブルがなければ作成
    app.run(debug=True)
