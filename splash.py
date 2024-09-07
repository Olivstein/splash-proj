from flask import Flask, render_template, request, send_file, jsonify


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("splash.html")


if __name__ == "__main__":
    app.run()
    #app.run(host='0.0.0', port=5000)