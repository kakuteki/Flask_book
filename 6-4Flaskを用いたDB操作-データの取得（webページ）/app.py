import psycopg2
from flask import Flask

app = Flask(__name__)

# データベースからデータを取得して表示する関数
def get_data_from_database():
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

    # テーブルの内容を取得
    table_name = 'users'  # 取得するテーブルの名前を指定
    cursor.execute(f'SELECT * FROM {table_name};')
    rows = cursor.fetchall()

    # カーソルとデータベースをクローズ
    cursor.close()
    conn.close()

    return rows

@app.route('/database')
def display_database_contents():
    # データベースからデータを取得
    data = get_data_from_database()

    # データを文字列として整形
    data_str = "\n".join([str(row) for row in data])
    return data_str

if __name__ == "__main__":
    app.run(debug=True)
