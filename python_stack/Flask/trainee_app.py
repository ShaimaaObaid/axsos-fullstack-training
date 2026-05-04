from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return"Hello World!"
@app.route("/trainees")
def trainees():
    return render_template("index.html")
@app.route("/trainees/<id>")
def trainees_profile(id):
    return f"{id}'s profile"

#run the code
if __name__ == "__main__":
    app.run(debug=True)