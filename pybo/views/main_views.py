from flask import Blueprint, render_template, url_for
from pybo.models import User, Order, Post

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

@main_bp.route('/About-us')
def about_us():
    return render_template('About_us.html')

@main_bp.route('/all-proDucts')
def all_products():
    return render_template('all_proDucts.html')

@main_bp.route('/Guitar-memes')
def guitar_memes():
    post_list = Post.query.order_by(Post.create_date.desc())
    return render_template('guitar_memes.html', post_list=post_list)

@main_bp.route('/community')
def community():
    return render_template('community.html')
