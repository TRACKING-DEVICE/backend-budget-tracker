from . import db
from datetime import datetime

class Transaction(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    amount=db.Column(db.Float, nullable=False)
    date=db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.String(200))
    category_id=db.Column(db.Integer, db.ForeignKey('category-id'), nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user-id'), nullable=False)

