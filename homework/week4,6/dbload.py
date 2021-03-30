from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime


if __name__ != '__main__':    
    db = SQLAlchemy()
else:
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:scu02151356@localhost/website'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)

class User(db.Model):
    #read
    id=db.Column(db.BigInteger, primary_key=True,autoincrement=True)
    name=db.Column(db.String(255),nullable=False)
    username=db.Column(db.String(255),nullable=False)
    password=db.Column(db.String(255),nullable=False)
    time=db.Column(db.DateTime,default=datetime.now)

    #create
    def __init__(self,name,username,password):
        self.name=name
        self.username=username
        self.password=password
# User.query.filter_by(username='ply',password='ply').first()



class Message(db.Model):
    id=db.Column(db.BigInteger,nullable=False,primary_key=True,autoincrement=True)
    user_id=db.Column(db.BigInteger,db.ForeignKey('User.id'),nullable=False)
    content=db.Column(db.String(255),nullable=False)
    time=db.Column(db.DateTime,default=datetime.now)

    def __init__(self,user_id,content):
        self.user_id=user_id
        self.content=content

#for u in Message.query.all():
#    print(u.content)