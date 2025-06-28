from flask import request, jsonify
from models import db, User
from flask_jwt_extended import create_access_token

def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'message':'User already exists'}), 400

    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message':'User registered successfully'}), 201

def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        token = create_access_token(identity=user.id)
        return jsonify ({'access_token': token})
    return jsonify({'message': 'invalid details'}), 401    
