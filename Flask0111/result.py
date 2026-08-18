from flask import Flask
app = Flask(__name__)
@app.route('/')
def result():
    sub1 = 85
    sub2 = 78
    sub3 = 90
    sub4 = 88
    sub5 = 80
    total = sub1 + sub2 + sub3 + sub4 + sub5
    percentage = total / 5
    return f"""
    <h1>Student Result</h1>
    <hr>
    <b>Pytthon :</b> {sub1}<br>
    <b>Java :</b> {sub2}<br>
    <b>Html :</b> {sub3}<br>
    <b>Mad :</b> {sub4}<br>
    <b>Wt :</b> {sub5}<br><br>
    <b>Total marks :</b> {total}<br><br>
    <b>Percentage :</b> {percentage:.2f}%
    """
if __name__ == "__main__":
    app.run(debug=True)