from flask import Flask, render_template
from dotenv import load_dotenv
import os

load_dotenv()
# __name__ には動かしているファイル名が自動で入る
app = Flask(__name__)

@app.route("/")
def index():
    api_key = os.getenv("GMP_API_KEY")
    return render_template("index.html", api_key=api_key)

if __name__ == "__main__":
    app.run(debug=True)