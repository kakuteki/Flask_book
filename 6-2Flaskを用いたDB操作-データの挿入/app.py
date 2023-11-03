import psycopg2

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

# データを挿入
user_data = [('Alice', 30), ('Bob', 25), ('Charlie', 35)]
cursor.executemany('INSERT INTO users (name, age) VALUES (%s, %s)', user_data)

# 変更を保存（コミット）
conn.commit()

# データベースとカーソルをクローズ
cursor.close()
conn.close()
