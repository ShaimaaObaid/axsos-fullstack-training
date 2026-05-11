from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

app.secret_key = "secretkey"


@app.route('/')
def index():

    # visits counter
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1

    # actual counter
    if 'count' not in session:
        session['count'] = 0

    return render_template("index.html")


@app.route('/destroy_session')
def destroy_session():

    session.clear()

    return redirect('/')


@app.route('/add_two')
def add_two():

    session['count'] += 2

    return redirect('/')


@app.route('/reset')
def reset():

    session['count'] = 0

    return redirect('/')


@app.route('/increment', methods=['POST'])
def increment():

    number = int(request.form['number'])

    session['count'] += number

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)