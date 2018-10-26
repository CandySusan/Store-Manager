from flask import Flask, jsonify, request, Response
import json
from api_endpoints.products import Product, get_product_inventory, product_inventory, Login
from api_endpoints.sales import Sale, sales_order
from Flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
auth = HTTPBasicAuth()
users = []


@app.route('/')
def store_manager():

    return "Hello, welcome to StoreManager!"


@app.route('/api/v1/users', methods=["POST"])
def add_users():
    data = request.json
    users.append(data)
    return json.dumps({"message": "user added"}), 201


@app.route('/api/v1/users/<int:uid>', methods=["put"])
def update_users(uid):
    data = request.json
    # user = [user for user in users if user["id"] == uid][0]
    user_obj = None
    for user in users:
        if user["uid"] == uid:
            user = user
            index = user_obj.index(user)

            users.insert(index, user.update(**data))
    return json.dumps({"message": "user added"}), 202


@auth.get_password
def get_password(Admin):

    if Admin == "Candy":
        return 1234
    return None


@auth.error_handler
def unauthorized():
    return jsonify({"error": "Unauthorised User!!"}), 401


@app.errorhandler(404)
def not_found(error):
    """ Return an error """
    return jsonify({"error": "Not Found"}), 404
# Add a product


@app.route('/api/v1/products', methods=["POST"])
def add_product_endpoint():
    request_data = json.loads(request.data)
    product = Product(request_data['product_name'],
                      request_data['product_price'])
    product.add_product(product)
    return jsonify({"message": "successfully added product with id"}), 201


# GET specific product by id


@app.route('/api/v1/products/<int:product_id>', methods=["GET"])
def get_product(product_id):
    for product in product_inventory:
        if product.product_id == product_id:
            return jsonify(product.to_json())

    return jsonify({"message": "product not found"}), 200


# GET all products


@app.route('/api/v1/products', methods=["GET"])
# @auth.login_required
def get__all_products():
    response_list = []
    for product in product_inventory:
        response_list.append(product.to_json())

    return jsonify({"product_inventory": response_list}), 200


# POST /add_sale_order


@app.route('/api/v1/sales', methods=["POST"])
def add_sale_endpoint():
    data = json.loads(request.data)
    sale = Sale(data['item'], data['price'], data["quantity"])
    sale.add_sale(sale)
    return jsonify({"message": "Succesfully added sales order"}), 201


# GET specific sale
@app.route('/api/v1/sales/<int:sale_id>', methods=["GET"])
def get_sale(sale_id):
    for sale in sales_order:
        if sale.sale_id == sale_id:
            return jsonify(sale.to_json())

    return jsonify({"message": "Sales order not found"}), 200


# GET  all sales
@app.route('/api/v1/sales', methods=['GET'])
def get_all_sales():
    sales_list = []
    for sale in sales_order:
        sales_list.append(sale.to_json())
    return jsonify({"sales_order": sales_list}), 200


@app.route('/api/v1/login', methods=["POST"])
def login():


    user = json.loads(request.data)
    users = Login(user['username'],
                  user['password'])
    users.add_username()
    return jsonify({"message": "successfully logged in"}), 201
