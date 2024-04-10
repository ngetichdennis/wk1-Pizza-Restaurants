from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

from faker import Faker
fake = Faker()
with app.app_context():
    #delete all rows in the table
    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()
    # Seed restaurants data
    restaurant1 = Restaurant(name="Dominion Pizza", address="Good Italian, Ngong Road, 5th Avenue")
    restaurant2 = Restaurant(name="Pizza Hut", address="Westgate Mall, Mwanzi Road, Nrb 100")

    db.session.add(restaurant1)
    db.session.add(restaurant2)
    db.session.commit()


    # Seed pizzas data
    pizza1 = Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese")
    pizza2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")

    db.session.add(pizza1)
    db.session.add(pizza2)
    db.session.commit()

    # Seed restaurant_pizzas data
    restaurant_pizza1 = RestaurantPizza(price=10, restaurant_id=1, pizza_id=1)
    restaurant_pizza2 = RestaurantPizza(price=12, restaurant_id=1, pizza_id=2)
    restaurant_pizza3 = RestaurantPizza(price=15, restaurant_id=2, pizza_id=1)

    db.session.add(restaurant_pizza1)
    db.session.add(restaurant_pizza2)
    db.session.add(restaurant_pizza3)
    db.session.commit()


