from . import db

class Category(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80), nullable=False)
    transactions = db.relationship('Transaction', backref='category', lazy=True)