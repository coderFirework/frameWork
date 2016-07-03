from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy();
def create_app():
    app=Flask(__name__)
    from .authority import authorityBp as authority_blueprint
    app.register_blueprint(authority_blueprint)
    from flask_bootstrap import Bootstrap
    bootstrap = Bootstrap(app)
    app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:vgelab010@115.29.110.148:5432/appDB'
    db.init_app(app)
    return app

