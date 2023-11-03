import psycopg2
from flask import Flask, render_template, request

app = Flask(__name__)

def get_data_from_database(name):
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

    # 名前に対応するデータを取得
    cursor.execute('SELECT age FROM users WHERE name = %s;', (name,))
    age = cursor.fetchone()

    # カーソルとデータベースをクローズ
    cursor.close()
    conn.close()

    return age

@app.route('/', methods=['GET', 'POST'])
def input_form():
    if request.method == 'POST':
        # フォームから送信された名前を取得
        name = request.form.get('name')

        # データベースから該当するデータを取得
        age = get_data_from_database(name)

        # 年齢が取得できた場合は表示
        if age:
            return f"{name}の年齢は{age[0]}歳です。"
        else:
            return f"{name}のデータが見つかりませんでした。"

    return render_template('input_form.html')

if __name__ == "__main__":
    app.run(debug=True)
