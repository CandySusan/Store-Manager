from flask import Flask, jsonify, request, Response
import json
from api_endpoints.products import Product, get_product_inventory, product_inventory
from api_endpoints.sales import Sale, sales_order

app = Flask(__name__)


@app.route('/api/v1/products', methods=["POST"])
def add_product_endpoint():
    request_data = json.loads(request.data)
    product = Product(request_data['product_name'], request_data['product_price'])
    product.add_product()
    return jsonify({"message" : "successfully added product with id"}), 201

# GET all products


@app.route('/api/v1/products/<int:product_id>',methods=["GET"])
def get_product(product_id):
    for product in product_inventory:
        if product.product_id == product_id:
            return jsonify(product.to_json())

    return jsonify({"message": "product not found"}),200

# GET all products


@app.route('/api/v1/products', methods=["GET"])
def get__all_products():
    response_list = []
    for product in product_inventory:
        response_list.append(product.to_json())

    return jsonify({"product_inventory": response_list}),200

# # POST /add_sale_order


@app.route('/api/v1/sales', methods=["POST"])
def add_sale_endpoint():
    data = request.get_json()
    sale = Sale(data['item'], data['price'])
    sale_list = sale.add_sale()
    return jsonify({"sales": sale_list}),201


# GET specific sale
@app.route('/api/v1/sales/<int:sale_id>', methods=["GET"])
def get_sale(sale_id):
    for sale in sales_order:
        if sale["sale_id"] == sale_id:
            return jsonify(sale)
    return jsonify({"message": "Sale order not found"}),200


# GET  all sales
@app.route('/api/v1/sales', methods=['GET'])
def get_all_sales():
    return jsonify({"sale_order": sales_order}),200
