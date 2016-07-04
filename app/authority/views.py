from flask import render_template,redirect,url_for

from . import authorityBp
from ..api.AppInfo import APP
#login
@authorityBp.route('/',methods=['GET','POST'])
@authorityBp.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html',title='渔业资源管理系统')
#register
@authorityBp.route('/register',methods=['GET','POST'])
def register():
    return render_template('register.html')
