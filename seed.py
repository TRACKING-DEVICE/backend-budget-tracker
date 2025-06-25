from app import app, db
from models import User, Transaction, Category
from werkzeug.security import generate_password_hash

def seed_data():
    with app.app_context():
        print("🔄 Resetting database...")
        db.drop_all()
        db.create_all()

        print("👤 Seeding users...")
        user1 = User(username='jesse', password=generate_password_hash('password123'))
        user2 = User(username='tjay', password=generate_password_hash('password321'))
        user3 = User(username='alice', password=generate_password_hash('password123'))
        user4 = User(username='bob', password=generate_password_hash('secure456'))

        db.session.add_all([user1, user2, user3, user4])
        db.session.commit()

        print("📦 Seeding categories...")
        food = Category(name='Food')
        rent = Category(name='Rent')
        salary = Category(name='Salary')
        freelance = Category(name='Freelance')
        transport = Category(name='Transport')

        db.session.add_all([food, rent, salary, freelance, transport])
        db.session.commit()

        print("💰 Seeding transactions...")
        tx1 = Transaction(
            amount=1200.00,
            category="Salary",
            type="income",
            description="Monthly salary",
            user_id=user1.id
        )

        tx2 = Transaction(
            amount=50.00,
            category="Food",
            type="expense",
            description="Lunch at cafe",
            user_id=user1.id
        )

        tx3 = Transaction(
            amount=500.00,
            category="Freelance",
            type="income",
            description="Website project",
            user_id=user2.id
        )

        tx4 = Transaction(
            amount=150.00,
            category="Transport",
            type="expense",
            description="Fuel refill",
            user_id=user2.id
        )

        db.session.add_all([tx1, tx2, tx3, tx4])
        db.session.commit()

        print("✅ Done seeding the database!")

if __name__ == "__main__":
    seed_data()
