from flask import Blueprint, render_template, request, url_for

from datetime import datetime

from werkzeug.utils import redirect

from .. import db

from pybo.models import Post

from pybo.forms import PostForm

bp = Blueprint('post', __name__, url_prefix='/post')


@bp.route('/list/')
def _list():
    post_list = Post.query.order_by(Post.create_date.desc())
    return render_template('post_list.html', post_list=post_list)


@bp.route('/detail/<int:post_id>/')
def detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post_detail.html', post=post)

@bp.route('/create/', methods=('GET', 'POST'))
def create():
    form = PostForm()
    if request.method == 'POST' and form.validate_on_submit():
        question = Post(subject=form.subject.data, content=form.content.data, create_date=datetime.now())
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.guitar_memes'))
    return render_template('post_form.html', form=form)


