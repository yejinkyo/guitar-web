from flask import Blueprint, render_template, request
from pybo.models import User, Order

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('main.html')

@main_bp.route('/mypagE')
def mypage():
    user = User.query.first()
    if not user:
        return "User not found", 404  # 사용자 데이터가 없을 때
    orders = Order.query.filter_by(id=user.id).all()
    return render_template('mypagE.html', user=user, orders=orders)

@main_bp.route('/introDuction')
def downloads():
    return render_template('introDuction.html')

@main_bp.route('/All-products')
def all_products():
    return render_template('All_products.html')

@main_bp.route('/Guitar-memes')
def guitar_memes():
    return render_template('Guitar_memes.html')
