from flask import Flask
app = Flask(__name__)
@app.route('/')
def biodata():
    return """
    <h1>Student Biodata</h1>
    <hr>
    <b>Name :</b> Rahul Patil<br><br>
    <b>Roll Number :</b> 101<br><br>
    <b>Class :</b> TYBCA<br><br>
    <b>Department :</b> Computer Science<br><br>
    <b>Email :</b> rahul@gmail.com<br><br>
    <b>Mobile Number :</b> 9876543210<br><br>
    <b>City :</b> Pune
    """
if __name__ == "__main__":
    app.run(debug=True)