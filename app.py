from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        name = request.form['name']
        roll_no = request.form['roll_no']

        sub1 = float(request.form['english'])
        sub2 = float(request.form['physics'])
        sub3 = float(request.form['chemistry'])
        sub4 = float(request.form['maths'])
        sub5 = float(request.form['biology'])

        total = sub1 + sub2 + sub3 + sub4 + sub5
        percentage = total / 5

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "Fail"

        result = {
            "name": name,
            "roll_no": roll_no,
            "total": total,
            "percentage": round(percentage, 2),
            "grade": grade
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)