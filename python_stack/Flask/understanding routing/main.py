from flask import Flask

app = Flask(__name__)

# 1
@app.route("/")
def hello():
    return "Hello World!"

# 2
@app.route("/Champion")
def champion():
    return "Champion!"

# 3
@app.route("/say/<name>")
def say_hi(name):
    return f"Hi {name}!"

# 4 (NINJA BONUS → int converter)
@app.route("/repeat/<int:num>/<word>")
def repeat(num, word):
    return (word + " ") * num

# 5 (SENSEI BONUS → catch any route other than the specified)
@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again.", 404

if __name__ == "__main__":
    app.run(debug=True)