import psycopg2

def display_table_contents():
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

    # データを表示
    for row in rows:
        print(row)

    # カーソルとデータベースをクローズ
    cursor.close()
    conn.close()

if __name__ == '__main__':
    display_table_contents()
