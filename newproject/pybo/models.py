from pybo import db


class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(150),unique=True,nullable=False)
    password=db.Column(db.String(200),nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)




class Reservation(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('user_id',ondelete='CASCADE'))
    reserveuser=db.Column(db.String(150),nullable=False)
    phonenumber = db.Column(db.String(150), unique=True, nullable=False)
    selectcenter = db.Column(db.String(120), nullable=False)
    selectdate = db.Column(db.String(120), unique=True, nullable=False)








