from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    print(request.form)  
    name = request.form["name"]
    location = request.form["location"]
    language = request.form["language"]
    comment = request.form["comment"]

    # BONUS
    gender = request.form["gender"]
    skills = request.form.getlist("skills")

    return render_template("result.html",name=name,location=location,language=language,
                           comment=comment,gender=gender,skills=skills)
@app.route('/back')
def back():
    return redirect('/')
#run
if __name__ == "__main__":
    app.run(debug=True)