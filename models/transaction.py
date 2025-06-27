from . import db
from datetime import datetime

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id=db.Column(db.Integer, primary_key=True)
    amount=db.Column(db.Float, nullable=False)
    date=db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.String(200))

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id')) 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    category = db.relationship('Categogy', backref='transactions')
    user = db.relationship('User', backref='transactions')

