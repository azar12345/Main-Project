from flask import Flask, render_template,request
from pymongo import MongoClient


app = Flask(__name__)
client = MongoClient('localhost',27017)
db = client.get_database("login")
collection = db.signup
collection1=db.signin


@app.route('/',methods=['POST','GET'])
def reg():
    fname = request.form.get('firstname')
    lname = request.form.get('lastname')
    email = request.form.get('email')
    pw = request.form.get('password')
    repw = request.form.get('repeatpassword')
    collection.insert_one({"firstname": fname, "lastnane": lname, "email": email, "password": pw, "repeatpassword": repw})
    return render_template('signup.html', firstname=fname, lastname=lname, email=email, password=pw, repeatpassword=repw)


@app.route("/signin")
def sinin():

    return render_template('signin.html')


if __name__ == "__main__":
    app.run(debug=True)