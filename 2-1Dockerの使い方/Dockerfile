# ベースイメージを指定
FROM python:3.9

# 作業ディレクトリを指定
WORKDIR /app

# ホストのファイルをコンテナにコピー
COPY . /app

# 必要なPythonパッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

# Flaskアプリを起動
CMD ["python", "app.py"]
