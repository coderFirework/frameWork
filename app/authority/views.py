from flask import render_template,redirect,url_for

from . import authorityBp
#登录
@authorityBp.route('/',methods=['GET','POST'])
@authorityBp.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')
#注册
@authorityBp.route('/register',methods=['GET','POST'])
def register():
    return render_template('register.html')
