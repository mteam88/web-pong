from flask import Flask, render_template, request
import json
import random
app = Flask(__name__)

playerskin = "static/player/whiteplayer.png"
ballskins = ["static/ball/ball1.png", "static/ball/blueball.png", "static/ball/redball.png"]

@app.route("/")
def startscreen():
    return render_template("start.html")

@app.route("/pong")
def pong():
    print(playerskin)
    return render_template("index.html", data={"playerskin": playerskin, 'ballskin': random.choice(ballskins)})

@app.route("/gameover/<winner>")
def gameover(winner):
    return render_template("gameover.html", data={"winner": winner})

@app.route("/setplayerskin", methods=['POST'])
def setplayerskin():
    global playerskin
    print(request.json)
    print(playerskin)
    playerskin = request.json['skin']
    print("playerskin: " + playerskin)
    return "Success!"

app.run(debug=True)