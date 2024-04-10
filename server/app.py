from flask import Flask,request,jsonify
from flask_migrate import Migrate
from models import db,Restaurant,Pizza

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
migrate=Migrate(app,db)
db.init_app(app)
@app.route('/')
def index():
    return "Index for Restaurant/Pizza/Restaurantpizza API"

@app.route('/restaurants')
def restaurant():
    try:
        restaurants = []
        for restaurant in Restaurant.query.all():
            restaurant_dict = restaurant.to_dict()
            restaurants.append(restaurant_dict)
        
        if restaurants:
            return jsonify({'message': 'success', 'data': restaurants}), 200
        else:
            return jsonify({'message': 'No restaurants found'}), 404
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500
@app.route('/restaurants/<int:id>')
def get_restaurant_by_id(id):
    restaurant=Restaurant.query.filter_by(id=id).first()
    restaurant_dict=restaurant.to_dict()
    
    if restaurant is None:
        return jsonify({'message':'The requested restaurant does not exist'}),404
    else:
        return jsonify(restaurant_dict),200

#POST Method to add a new restaurant
@app.route("/restaurants",methods=["POST"])
def create_restaurant():
    new_restaurant=Restaurant (  
    name=request.form.get('name'),
    address=request.form.get("address"),
    )
    db.session.add(new_restaurant)
    db.session.commit()
    
    return jsonify({'message':'New restaurant created','data':new_restaurant.to_dict()})
@app.route('/pizzas',methods=['GET'])
def pizza():
    pass

@app.route('/restaurants/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def get_restaurant(id):
    restaurant = Restaurant.query.filter(Restaurant.id == id).first()

    if  restaurant== None:
        response_body = {
            "message": "This record does not exist in our database. Please try again."
        }

        return jsonify(response_body),404

    else:
        if request.method == 'GET':
            restaurant_dict = restaurant.to_dict()

            return jsonify(restaurant_dict), 200


        elif request.method == 'DELETE':
            db.session.delete(restaurant)
            db.session.commit()

            response_body = {
                "delete_successful": True,
                "message": "Review deleted."
            }

            return jsonify(response_body),200
        
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    try:
        pizzas = Pizza.query.all()
        pizzas_list = [pizza.to_dict() for pizza in pizzas]

        if pizzas_list:
            return jsonify({'message': 'success', 'data': pizzas_list}), 200
        else:
            return jsonify({'message': 'No pizzas found'}), 404
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(port=5555,debug=True)

