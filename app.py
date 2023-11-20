from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello DevOps Team Welcome to Python Flask Application"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5100))
    app.run(debug=True,host='0.0.0.0',port=port)
