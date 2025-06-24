from flask import Flask
from config import Config
from models import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from seed import auth_bp, transaction_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

app.register_blueprint(auth_bp)
app.register_blueprint(transaction_bp)

if __name__ == '__main__':
    app.run(debug=True)
