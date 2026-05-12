from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "secret_key"

# leaderboard list
leaders = []


@app.route('/')
def index():

    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['attempts'] = 0

    return render_template("index.html")


@app.route('/guess', methods=['POST'])
def guess():

    # prevent guessing after game ended
    if session.get('game_over'):
        return redirect('/')

    user_guess = int(request.form['guess'])
    session['attempts'] += 1

    # correct
    if user_guess == session['number']:
        session['result'] = "Correct!"
        session['correct_number'] = user_guess
        session['game_over'] = True

    # too low
    elif user_guess < session['number']:
        session['result'] = "Too Low!"

    # too high
    else:
        session['result'] = "Too High!"

    # lose after 5 attempts
    if session['attempts'] >= 5 and user_guess != session['number']:
        session['result'] = "You Lose!"
        session['game_over'] = True

    return redirect('/')


@app.route('/save', methods=['POST'])
def save():

    name = request.form['name']

    leaders.append({
        'name': name,
        'attempts': session['attempts']
    })

    return redirect('/leaderboard')


@app.route('/leaderboard')
def leaderboard():

    return render_template("leaderboard.html", leaders=leaders)


@app.route('/reset')
def reset():

    session.clear()

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)