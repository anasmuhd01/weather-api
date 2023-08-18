from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)


@app.route("/")
def home():
    stations = pd.read_csv('data_small/stations.txt',skiprows=17)
    stations = stations[["STAID", "STANAME                                 "]]
    return render_template("home.html", var= stations.to_html())


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    print(station)
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename,skiprows=20,parse_dates=["    DATE"])

    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10

    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }


app.run(debug=True)
