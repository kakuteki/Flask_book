from flask import Flask
import psycopg2

app = Flask(__name__)

# Azure Cosmos DB for PostgreSQLの接続文字列を取得
conn_string = "postgresql://your_username:your_password@your_postgres_server_name.postgres.database.azure.com:5432/your_database_name?sslmode=require"

@app.route('/')
def index():
    try:
        # PostgreSQLに接続
        conn = psycopg2.connect(conn_string)

        # データベースクエリの実行例
        cur = conn.cursor()
        cur.execute('SELECT * FROM your_table_name;')
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
