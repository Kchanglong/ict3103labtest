from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for

app = Flask(__name__, template_folder='template')

dic = {}


@app.route("/")
def hello_world():
    return str(dic)

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/loginPost",  methods=['POST'])
def logining():
    Username = request.form.get('Username')
    Password = request.form.get('Password')
    if dic.get(Username) is not None:
        if dic[Username] == Password:
            print('login sucess')
    return redirect(url_for('login'))

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/registerPost",  methods=['POST'])
def registering():
    Username = request.form.get('Username')
    Password = request.form.get('Password')
    dic[Username] = Password
    print(Username, Password)
    return redirect(url_for('login'))

if __name__== "__main__": 
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
