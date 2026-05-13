from flask import Flask, render_template, request, redirect, session
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = "ninja_gold_key"

# buildings ranges (WITHOUT if/elif)
buildings = {
    "farm": (10, 20),
    "cave": (5, 10),
    "house": (2, 5),
    "casino": (-50, 50)
}


@app.route("/")
def index():

    if "gold" not in session:
        session["gold"] = 0
        session["activities"] = []
        session["moves"] = 0
        session["game_over"] = False
        session["result"] = ""

    return render_template(
        "index.html",
        gold=session["gold"],
        activities=session["activities"],
        result=session["result"],
        game_over=session["game_over"]
    )


@app.route("/process_money", methods=["POST"])
def process_money():

    building = request.form["building"]

    # RESET GAME
    if building == "reset":
        session.clear()
        return redirect("/")

    # stop game if ended
    if session["game_over"]:
        return redirect("/")

    low, high = buildings[building]

    earned = random.randint(low, high)

    session["gold"] += earned
    session["moves"] += 1

    current_time = datetime.now().strftime("%Y/%m/%d %I:%M %p")

    if earned >= 0:
        message = f"Earned {earned} golds from the {building}! ({current_time})"
        color = "green"
    else:
        message = f"Entered a casino and lost {abs(earned)} golds... Ouch. ({current_time})"
        color = "red"

    # newest first
    session["activities"].insert(0, {
        "message": message,
        "color": color
    })

    # WIN / LOSE CONDITIONS
    if session["gold"] >= 500 and session["moves"] <= 15:
        session["game_over"] = True
        session["result"] = "You Win!"

    elif session["moves"] >= 15 and session["gold"] < 500:
        session["game_over"] = True
        session["result"] = "You Lost!"

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)