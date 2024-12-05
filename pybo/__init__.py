from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    # 블루프린트
    from .views import main_views, auth_views, post_views
    from . import models
    app.register_blueprint(main_views.main_bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(post_views.bp)


    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    return app
