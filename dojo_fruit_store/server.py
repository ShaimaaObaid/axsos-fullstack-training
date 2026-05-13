from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


# GET: عرض صفحة الفاكهة (اختياري)
@app.route('/fruits')
def fruits():
    return render_template("fruits.html")


# POST: معالجة الطلب
@app.route('/checkout', methods=['POST'])
def checkout_post():

    name = request.form.get('name', '')
    student_id = request.form.get('student_id', '')

    strawberry = int(request.form.get('strawberry', 0))
    raspberry = int(request.form.get('raspberry', 0))
    apple = int(request.form.get('apple', 0))

    total = strawberry + raspberry + apple

    # المطلوب بالضبط في assignment
    print(f"Charging {name} for {total} fruits.")

    # نخزن البيانات مؤقتًا عبر query string (حل بسيط للتمرين)
    return redirect(url_for('checkout_get',
                            name=name,
                            student_id=student_id,
                            strawberry=strawberry,
                            raspberry=raspberry,
                            apple=apple,
                            total=total))


# GET: عرض صفحة checkout (هذا المهم)
@app.route('/checkout', methods=['GET'])
def checkout_get():

    name = request.args.get('name', '')
    student_id = request.args.get('student_id', '')

    strawberry = request.args.get('strawberry', 0)
    raspberry = request.args.get('raspberry', 0)
    apple = request.args.get('apple', 0)
    total = request.args.get('total', 0)

    return render_template(
        "checkout.html",
        name=name,
        student_id=student_id,
        strawberry=strawberry,
        raspberry=raspberry,
        apple=apple,
        total=total
    )


if __name__ == "__main__":
    app.run(debug=True)