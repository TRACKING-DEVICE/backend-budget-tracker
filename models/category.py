from . import db

class Category(db.Model):
    __tablename__ = 'categories'
    
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80), nullable=False)
    transactions = db.relationship('Transaction', back_populates='category', lazy=True)