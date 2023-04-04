from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")

def firstpage():
    suhan = "student"

    return render_template("index.html",index_variable=suhan)

app.run(debug=True)