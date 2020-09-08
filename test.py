from flask import Flask
from flask import render_template,request,json
app = Flask(__name__)
@app.route("/")
def main():
    return render_template('index.html')
@app.route('/showAboutUs')
def showAboutUs():
    return render_template('aboutUs.html')
@app.route('/showloginpage/')
@app.route('/showNewUserPage/showloginpage/')
def showloginpage():
    return render_template('login.html')
@app.route('/showNewUserPage/')
def showNewUserPage():
    return render_template('newUser.html')
@app.route('/signUp/',methods=['POST'])
def signUp():
    _name = request.form['inputname']
    _phno = request.form['inputphno']
    _email_id = request.form['inputemail_id']
    _password = request.form['inputpassword']
    print(__name__)
    if _name and _email_id and _password and _phno:
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})
@app.route('/showNewUserPage/showloginpage/showStepOne/')
@app.route('/showloginpage/showStepOne/')
def showStepOne():
    return render_template('place.html')
@app.route('/showloginpage/showStepOne/showStepTwo/')
@app.route('/showNewUserPage/showloginpage/showStepOne/showStepTwo/')
def showStepTwo():
    return render_template('language.html')


if __name__ == "__main__":
    app.run()
