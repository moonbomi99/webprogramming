from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,PasswordField,SelectField,DateField,TimeField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired,Length,EqualTo,Email


class UserCreateForm(FlaskForm):
    username=StringField('사용자 이름',validators=[DataRequired(),Length(min=3,max=25)])
    password1=PasswordField('비밀번호',validators=[DataRequired(),EqualTo('password2','비밀번호가 일치하지 않습니다')])
    password2=PasswordField('비밀번호 확인',validators=[DataRequired()])
    email=EmailField('이메일',[DataRequired(),Email()])


class UserLoginForm(FlaskForm):
    username=StringField('사용자 이름',validators=[DataRequired(),Length(min=3,max=25)])
    password=PasswordField('비밀번호',validators=[DataRequired()])


class UserReserveForm(FlaskForm):
    username=StringField('예약자 이름',validators=[DataRequired(),Length(min=3,max=25)])
    phonenumber=StringField('전화번호',validators=[DataRequired(),Length(min=10,max=13)])
    selectcenter=SelectField('진료 센터',validators=[DataRequired()])
    selectdate=DateField('예약 날짜', validators=[DataRequired()])
    selecttime=TimeField('예약 시간',validators=[DataRequired()])