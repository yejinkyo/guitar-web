from flask import Blueprint, render_template, request
from pybo.models import User

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('main.html')

@main_bp.route('/mypagE')
def mypage():
    user = User.query.first()

    return render_template('mypagE.html')

@main_bp.route('/introDuction')
def downloads():
    return render_template('introDuction.html')

@main_bp.route('/All-products')
def all_products():
    return render_template('All_products.html')

@main_bp.route('/Guitar-memes')
def guitar_memes():
    return render_template('Guitar_memes.html')
