from flask import Flask,render_template,request,session,redirect
my_app =Flask(__name__)
my_app.secret_key = "Shaymaa's secret"
@my_app.route("/")
def login():
    return render_template("login.html")
@my_app.route("/process_login",methods=["POST"])
def handel_login():
    session["username"]=request.form["username"]
    session['is_logged']=True
    print(request.form["type"])
    return redirect("/home")
@my_app.route("/home")
def home():
    print(session["username"])
    print(session["is_logged"])
    return render_template("show.html")

if __name__ == "__main__":
    my_app.run(debug=True)