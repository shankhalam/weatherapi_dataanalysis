from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
station = pd.read_csv("data/stations.txt", skiprows=17)
station = station[["STAID", "STANAME                                 "]]


@app.route("/")
def home():
    return render_template("home.html", data=station.to_html())


@app.route("/api/v1/<station>/<date>")
def data(station, date):
    filename = "data/TG_STAID" + station.zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {
        "Station": station,
        "Date": date,
        "Temperature": temperature
    }


@app.route("/api/v1/<station>")
def station_data(station):
    filename = "data/TG_STAID" + station.zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient='records')
    return result


if __name__ == "__main__":
    app.run(debug=True)
