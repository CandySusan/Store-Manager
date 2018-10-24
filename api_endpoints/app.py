from flask import Flask, jsonify, request, Response
import json
from api_endpoints.products import Product, get_product_inventory, product_inventory
from api_endpoints.sales import Sale, sales_order
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
auth = HTTPBasicAuth()


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


@app.route('/', methods=["GET"])
def home():
    return("Hello there! Welcome to StoreManager")


@app.route('/api/v1/products', methods=["POST"])
def add_product_endpoint():
    request_data = json.loads(request.data)
    product = Product(request_data['product_name'],
                      request_data['product_price'])
    product.add_product()
    return jsonify({"message": "successfully added product with id"}), 201


# GET all products


@app.route('/api/v1/products/<int:product_id>', methods=["GET"])
def get_product(product_id):
    for product in product_inventory:
        if product.product_id == product_id:
            return jsonify(product.to_json())

    return jsonify({"message": "product not found"}), 200


# GET all products


@app.route('/api/v1/products', methods=["GET"])
@auth.login_required
def get__all_products():
    response_list = []
    for product in product_inventory:
        response_list.append(product.to_json())

    return jsonify({"product_inventory": response_list}), 200


# # POST /add_sale_order


@app.route('/api/v1/sales', methods=["POST"])
def add_sale_endpoint():
    data = json.loads(request.data)
    sale = Sale(data['item'], data['price'])
    sale.add_sale()
    return jsonify({"message": "Succesfully added sales order"}), 201


# GET specific sale
@app.route('/api/v1/sales/<int:sale_id>', methods=["GET"])
def get_sale(sale_id):
    sales_list = []
    for sale in sales_order:
        sales_list.append(sale.to_json)
    return jsonify({"sales_order": sales_list}), 200


# GET  all sales
@app.route('/api/v1/sales', methods=['GET'])
def get_all_sales():
    return jsonify({"sale_order": sales_order}), 200
