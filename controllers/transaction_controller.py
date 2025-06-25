from flask import request, jsonify
from models import Transaction, db
from flask_jwt_extended import jwt_required, get_jwt_identity

@jwt_required()
def create_transaction():
    data = request.get_json()
    amount = data.get('amount')
    t_type = data.get('type')  
    category = data.get('category')
    description = data.get('description', '')
    date = data.get('date')

    user_id = get_jwt_identity()

    if not amount or not t_type or not category or not date:
        return jsonify({"error": "All required fields must be filled"}), 400

    transaction = Transaction(
        amount=amount,
        type=t_type,
        category=category,
        description=description,
        date=date,
        user_id=user_id
    )
    db.session.add(transaction)
    db.session.commit()

    return jsonify({"message": "Transaction created"}), 201

@jwt_required()
def get_transactions():
    user_id = get_jwt_identity()
    transactions = Transaction.query.filter_by(user_id=user_id).all()
    result = [{
        "id": t.id,
        "amount": t.amount,
        "type": t.type,
        "category": t.category,
        "description": t.description,
        "date": t.date
    } for t in transactions]
    return jsonify(result), 200

@jwt_required()
def update_transaction(id):
    transaction = Transaction.query.get_or_404(id)
    user_id = get_jwt_identity()

    if transaction.user_id != user_id:
        return jsonify({"error": "Unauthorized"}), 403

    data = request.get_json()
    transaction.amount = data.get('amount', transaction.amount)
    transaction.type = data.get('type', transaction.type)
    transaction.category = data.get('category', transaction.category)
    transaction.description = data.get('description', transaction.description)
    transaction.date = data.get('date', transaction.date)

    db.session.commit()
    return jsonify({"message": "Transaction updated"}), 200

@jwt_required()
def delete_transaction(id):
    transaction = Transaction.query.get_or_404(id)
    user_id = get_jwt_identity()

    if transaction.user_id != user_id:
        return jsonify({"error": "Unauthorized"}), 403

    db.session.delete(transaction)
    db.session.commit()
    return jsonify({"message": "Transaction deleted"}), 200
