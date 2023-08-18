from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<name>")
def api(name):
    upper_word = name.upper()
    result_dictionary = {"name": name, "capital": upper_word}
    return result_dictionary


app.run(debug=True)
