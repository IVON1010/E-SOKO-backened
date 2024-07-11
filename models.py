from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

# initialize metadatafrom sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

# initialize metadata
metadata = MetaData()

db = SQLAlchemy(metadata=metadata)  

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    created_at = db.Column(db.TIMESTAMP)

    orders = db.relationship('Order', back_populates='user')
    products = db.relationship('Product', back_populates='user')

    serialize_rules = ('-products.user', '-orders.user',)
    serialize_only = ('id', 'name', 'email', 'password', 'address')

class Product(db.Model, SerializerMixin):
    __tablename__= 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    category = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', back_populates='products')
    cart = db.relationship('Cart', back_populates='products')

    serialize_rules = ('-user.products', 'cart.products',)
    serialize_only = ('id', 'name', 'description', 'price', 'image', 'category')

class Order(db.Model, SerializerMixin):
    __tablename__= 'orders'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', back_populates='orders')
    orderitems = db.relationship('OrderItem', back_populates='order')

    serialize_rules = ('-user.orders',)
    serialize_only = ('id', 'amount', 'status')

class OrderItem(db.Model, SerializerMixin):
    __tablename__= "orderitems"
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    order = db.relationship('Order', back_populates='oderitems')

    serialize_rules = ('-order.orderitems',)
    serialize_only = ('id', 'quantity', 'order', 'product')

class Cart(db.Model, SerializerMixin):
    __tablename__= 'carts'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    products = db.relationship('Product', back_populates='cart')

    serialize_rules = ('-products.cart',)