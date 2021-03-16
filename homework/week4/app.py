
from flask import Flask, render_template,request,redirect,url_for,session
import os

app = Flask(__name__)

account_data={
    'account':'test',
    'password':'test'
}
app.secret_key = os.urandom(24)


@app.route('/')
def index():
    if 'login_status' in session:
        if session['login_status']:
            return redirect(url_for('success'))
    return render_template('index.html')

@app.route('/member')
def success():
    if 'login_status' not in session or session['login_status']==False:
        return redirect('/')
    return render_template('success.html')

@app.route('/error')
def fail():
    return render_template('fail.html')

@app.route('/signin', methods=['POST'])
def login():
    if request.method=='POST':
        if request.form['account']==account_data['account'] and request.form['password']==account_data['password']:
            print('match')
            session['login_status']=True
            print(session['login_status'])
            return redirect(url_for('success'))
        else:
            print('different')
            return redirect(url_for('fail'))
    

@app.route('/signout')
def signout():
    session['login_status']=False
    print(session['login_status'])
    return redirect(url_for('index'))
    

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)
 