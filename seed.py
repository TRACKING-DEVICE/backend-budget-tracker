from models import db, User, Category, Transaction
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()

    user1 = User(username='jesse')
    user1.set_password('password123')

    user2 = User(username='tjay')
    user2.set_password('password321')

    user3 = User(username='mark')
    user3.set_password('password456')

    user4 = User(username='daniel')
    user4.set_password('password654')

    db.session.add_all([user1, user2])
    db.session.commit()

    food = Category(name='Food')
    rent = Category('Rent')
    salary = Category('Salary')
    db.session.add_all([food, rent, salary])
    db.session.commit()

    t1 = Transaction(amount=50, description='Groceries', category_id=food.id, user_id=user1.id)
    t2 = Transaction(amount=100, description='Monthly Rent', category_id=rent.id, user_id=user1.id)
    t3 = Transaction(amount=200, description='Monthly Salary', category_id=salary.id, user_id=user1.id)

    db.session.add_all([t1, t2, t3])
    db.session.commit()

    print("The Database has been carefully seeded!")