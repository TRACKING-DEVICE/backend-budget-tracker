from flask import Blueprint
from controllers.auth_controller import register, login
from controllers.transaction_controller import create_transaction, get_summary

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
transaction_bp = Blueprint('transaction', __name__, url_prefix='/api')

auth_bp.route('/register', methods=['POST'])(register)
auth_bp.route('/login', methods=['POST'])(login)

transaction_bp.route('/transactions', methods=['POST'])(create_transaction)
transaction_bp.route('/summary', methods=['GET'])(get_summary)
