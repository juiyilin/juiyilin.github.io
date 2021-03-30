from flask import Flask, render_template,request,redirect,url_for,session
import os
from dbload import db,User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:scu02151356@localhost/website'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)

app.secret_key = os.urandom(24)
session={
    'name':None,
    'username':None,
    'password':None,
    'login_status':False
}

@app.route('/')
def index():
    if 'login_status' in session:
        if session['login_status']:
            return redirect(url_for('success'))
    return render_template('index.html')

@app.route('/member')
def success():
    if session['login_status']==False:
        return redirect('/')
  
    return render_template('success.html',name=session['name'])

@app.route('/error/')
def fail():
    error_text=request.args.get('message','')
    print(error_text)
    return render_template('fail.html',error_text=error_text)

@app.route('/signup', methods=['POST'])
def signup():
    if request.method=='POST':
        signup_data={
            'name':request.form['name'],
            'username':request.form['username'],
            'password':request.form['password']
        }
        
        print('signup_username:',signup_data['username'])

        check_username=User.query.filter_by(username=signup_data['username']).first() 
        #註冊失敗
        if check_username!=None:
            print('check_username:',check_username.username)
            if signup_data['username'] == check_username.username:
                return redirect(url_for('fail',message='帳號已經被註冊'))
        
        #註冊成功
        else:
            add_user=User(
                name=signup_data['name'],
                username=signup_data['username'],
                password=signup_data['password']
                )
                                
            db.session.add(add_user)
            db.session.commit()
            print('已新增資料:',signup_data)
            return redirect('/')

@app.route('/signin', methods=['POST'])
def login():
    if request.method=='POST':
        login_data={
            'username':request.form['username'],
            'password':request.form['password']
        }
        check_data=User.query.filter_by(username=login_data['username'],password=login_data['password']).first()
        if check_data!=None:
            print('match')
            print('check_data',check_data)
            session['login_status']=True
            session['username']=login_data['username']
            session['password']=login_data['password']
            session['name']=check_data.name
            print('signin:',session)
        
            return redirect(url_for('success'))
        else:
            print('different')
            print(session)
            return redirect(url_for('fail',message='帳號或密碼輸入錯誤'))
    

@app.route('/signout')
def signout():
    session['name']=None
    session['username']=None
    session['password']=None
    session['login_status']=False
    print('signout:',session)
    return redirect(url_for('index'))
    

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)
    

 