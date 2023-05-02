from flask import Blueprint,render_template
bp=Blueprint('main',__name__,url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello,pybo'

@bp.route('/')
def index():
    return render_template('list.html')