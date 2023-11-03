import psycopg2

try:
    # データベースに接続
    conn = psycopg2.connect(
        dbname='mydb',
        user='hinata',
        password='hinata',
        host='localhost',
        port='5432'
    )
    print("データベースに接続成功")
    conn.close()
except Exception as e:
    print("データベース接続エラー:", e)
