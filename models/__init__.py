from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .transaction import Transaction
from .category import Category
