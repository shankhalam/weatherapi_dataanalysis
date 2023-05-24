from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def data(station, date):
    temparature = 23
    return {
        "Station": station,
        "Date": date,
        "Temparature": temparature
    }


if __name__ == "__main__":
    app.run(debug=True)
