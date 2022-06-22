from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def startscreen():
    return render_template("start.html")

@app.route("/pong")
def pong():
    return render_template("index.html")

@app.route("/gameover/<winner>")
def gameover(winner):
    return render_template("gameover.html", data={"winner": winner})

app.run(debug=True)