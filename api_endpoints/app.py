from flask import Flask, jsonify, request, Response
import json
from api_endpoints.products import Product, get_product_inventory, product_inventory
from api_endpoints.sales import Sale, sales_order
app = Flask(__name__)


@app.route('/api/v1/products', methods=["POST"])
def add_product_endpoint():
    request_data = request.get_json()
    product = Product(request_data['item'], request_data['price'])
    product_list = product.add_product()
    return jsonify({"products": product_list})

# GET all products


@app.route('/api/v1/products/<int:product_id>')
def get_product(product_id):
    for product in product_inventory:
        if product["product_id"] == product_id:
            return jsonify(product)

    return jsonify({"message": "product not found"})

# GET all products


@app.route('/api/v1/products', methods=["GET"])
def get__all_products():
    return jsonify({"product_inventory": product_inventory})

# # POST /add_sale_order


@app.route('/api/v1/sales', methods=["POST"])
def add_sale_endpoint():
    request_data = request.get_json()
    sale = Sale(request_data['item'], request_data['price'])
    sale_list = sale.add_sale()
    return jsonify({"sales": sale_list})


# GET specific sale
@app.route('/api/v1/sales/<int:sale_id>', methods=["GET"])
def get_sale(sale_id):
    for sale in sales_order:
        if sale["sale_id"] == sale_id:
            return jsonify(sale)
    return jsonify({"message": "Sale order not found"})


# GET  all sales
@app.route('/api/v1/sales', methods=['GET'])
def get_all_sales():
    return jsonify({"sale_order": sales_order})



