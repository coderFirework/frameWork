from flask import Blueprint
#url_prefix='/auth'
authorityBp = Blueprint('authority',__name__,static_url_path='', template_folder='templates')

from . import views