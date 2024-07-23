import os
from datetime import timedelta
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from models import db, User
from resources.product import ProductResource
from resources.order import OrderResource
from resources.cart import CartResource
from resources.user import SignupResource, LoginResource

app = Flask(__name__)
api = Api(app)

migrate = Migrate(app, db)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_ECHO'] = True
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)


cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)

migrate = Migrate(app, db, render_as_batch=True)

bcrypt = Bcrypt(app)

jwt = JWTManager(app)

db.init_app(app)

api.add_resource(ProductResource, '/products', '/products/<int:id>')
api.add_resource(CartResource, '/carts', '/carts/<int:id>')
api.add_resource(OrderResource, '/orders', '/orders/<int:id>')
api.add_resource(SignupResource, '/users', '/signup')
api.add_resource(LoginResource, '/users', '/login')

if __name__ == '__main__':
    app.run(debug=True)


