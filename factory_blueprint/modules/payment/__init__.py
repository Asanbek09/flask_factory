from flask import Blueprint

payment_bp = Blueprint('payment_bp', __name__,
    template_folder='pages',
    static_folder='resources', static_url_path='static')


import modules.payment.views.payment