from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

# Define metadata with naming convention
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

# Initialize SQLAlchemy with metadata
db = SQLAlchemy(metadata=metadata)
class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'
    serialize_rules = ('-restaurant_pizzas.restaurant',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    address = db.Column(db.String)

    # Relationship with RestaurantPizza model
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='restaurant')

    def __repr__(self):
        return f'<Restaurant {self.id}, {self.name}, {self.address}>'

class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'
    serialize_rules = ('-restaurant_pizzas.pizza',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    ingredients = db.Column(db.String)

    # Relationship with RestaurantPizza model
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='pizza')

    def __repr__(self):
        return f'<Pizza {self.id}, {self.name}, {self.ingredients}>'

class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizzas'
    serialize_rules = ('-restaurant.restaurant_pizzas', '-pizza.restaurant_pizzas',)

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)

    # Foreign keys
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))

    # Relationships
    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')
    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas') 

    def __repr__(self):
        return f'<RestaurantPizza {self.id}, {self.price}>'


