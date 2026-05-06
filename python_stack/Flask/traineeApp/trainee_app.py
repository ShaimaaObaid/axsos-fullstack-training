from flask import Flask,render_template,request,redirect,session
app = Flask(__name__)
app.secret_key = "$ecREtK3y"

@app.route('/')
def hello_world():
    return"Hello World!"
@app.route("/trainees")
def trainees():
    return render_template("index.html")
@app.route("/trainees/<id>")
def trainees_profile(id):
    return f"{id}'s profile"
@app.route("/login")
def login():
    return render_template("form.html")
@app.route("/process-login",methods=["post"])
def process_login():
    name=request.form["name"]
    email=request.form["email"]
    session["name"]=name
    session["email"]=email
    return redirect("/trainees")

#run the code
if __name__ == "__main__":
    app.run(debug=True)