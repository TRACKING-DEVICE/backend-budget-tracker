from flask import Blueprint
from flask_jwt_extended import jwt_required
from controllers.auth_controller import register, login
from controllers.transaction_controller import create_transaction, get_summary

auth_bp = Blueprint('auth', __name__)
transaction_bp = Blueprint('transaction', __name__)

auth_bp.route('/register', methods=['POST'])(register)
auth_bp.route('/login', methods=['POST'])(login)

transaction_bp.route('/transactions', methods=['POST'])(jwt_required()(create_transaction))
transaction_bp.route('/summary', methods=['GET'])(jwt_required()(get_summary))
