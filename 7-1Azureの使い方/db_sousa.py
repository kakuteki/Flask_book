from flask import Flask
import psycopg2

app = Flask(__name__)

# Azure Cosmos DB for PostgreSQLの接続文字列を取得
conn_string = "postgres://citus:password03!@c-posts.m3nbrkb7vfz6ge.postgres.cosmos.azure.com:5432/citus?sslmode=require"

@app.route('/')
def index():
    try:
        # PostgreSQLに接続
        conn = psycopg2.connect(conn_string)
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

        username = 'username'
        post_content = 'postContent'

        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO posts (username, post_content) VALUES (%s, %s)', (username, post_content))
        conn.commit()
        cursor.close()
        conn.close()


        conn = psycopg2.connect(conn_string)

        # データベースクエリの実行例
        cur = conn.cursor()
        cur.execute('SELECT * FROM posts;')
        data = cur.fetchall()

        # クエリ結果を表示
        result = '<br>'.join([str(row) for row in data])

        # コネクションをクローズ
        cur.close()
        conn.close()

        return result
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run()
