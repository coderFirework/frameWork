from flask import Flask,render_template

def create_app():
    app=Flask(__name__)
    from .authority import authorityBp as authority_blueprint
    app.register_blueprint(authority_blueprint)
    return app

