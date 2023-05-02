from flask import Blueprint, url_for, render_template, flash, request, session,g

from pybo import db
from pybo.forms import UserReserveForm
from pybo.models import User,Reservation
from pybo.views.auth_views import login_required

bp=Blueprint('list',__name__,url_prefix='/list')


@bp.route('/reserve/',methods=('GET','POST'))
@login_required
def reserve():
    form=UserReserveForm()
    if request.method=='POST' and form.validate_on_submit():
        reserveuser=Reservation.query.filter_by(username=form.username.data).first()
        reserveuser=Reservation(username=form.username.data,phonenumber=form.phonenumber.data,selectcenter=form.selectcenter.data,
                             selectdate=form.selectdate.data)
        db.session.add(reserveuser)
        db.session.commit()
    return render_template('list/reserve.html',form=form)



@bp.route('/spine/')
def spine():
    return render_template('list/spine.html')




@bp.route('/joint/')
def joint():
    return render_template('list/joint.html')


@bp.route('/checkup/')
def checkup():
    return render_template('list/checkup.html')


@bp.route('/hospital/')
def hospital():
    return render_template('list/hospital.html')






