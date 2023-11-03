from flask import Flask, render_template 
from datetime import datetime
import jinja2

app = Flask(__name__)

# フィルターの関数定義
def format_datetime(value, format='%Y-%m-%d'):
    return value.strftime(format)

# フィルターの登録  
app.jinja_env.filters['strftime'] = format_datetime

@app.route("/")
def index():
    user = "Taro"
    items = ["Apple", "Banana", "Orange"]
    condition = True
    date = datetime.now()

    return render_template("index.html", user=user, items=items, condition=condition, date=date)

if __name__ == "__main__":
   app.run(debug=True)