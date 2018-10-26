import unittest

from api_endpoints.app import app

import json


class TestApi(unittest.TestCase):

    def setUp(self):

        self.client = app.test_client()
        self.hostname = "http://localhost:5000/api/v1/"

    def test_invalid_url(self):
        response = self.client.get(self.hostname)
        self.assertEqual(response.status_code, 404)

    def test_get_all_products(self):
        response = self.client.get(self.hostname + 'products')
        self.assertEqual(response.status_code, 200)

    def test_post_a_product(self):
        products = {

            "product_name": "sandals",
            "product_price": 15.99,
            "quantity": 6
        }

        response = self.client.post(
            self.hostname+'products', data=json.dumps(products))

        self.assertEqual(response.status_code, 201)

    def test_get_a_product(self):
        response = self.client.get(self.hostname+'products/1')
        self.assertEqual(response.status_code, 200)

    def test_delete_entry(self):
        delete_list = []
        delete = {

            "product_name": "car",
            "product_price": 600,


        }

        result = self.client.delete(
            '/api/v2/resources/product/', data=json.dumps(delete))

        delete_list.append(delete)
        self.assertEqual(result.status_code, 404)

    def test_unavailable_fetch(self):
        result = self.client.get('/api/v2/resources/products/')
        self.assertEqual(result.status_code, 404)

    def test_post_a_sale(self):
        sales = {

            "item": "boots",
            "price": 15.99,
            "quantity": 2
        }

        response = self.client.post(
            self.hostname+'sales', data=json.dumps(sales))
        self.assertEqual(response.status_code, 201)

    def test_get_all_sales(self):
        response = self.client.get(self.hostname + 'sales')
        self.assertEqual(response.status_code, 200)

    def test_get_a_sale(self):
        response = self.client.get(self.hostname+'sales/1')
        self.assertEqual(response.status_code, 200)

    def test_invalid_update(self):
        product_list = []
        product = {

            "product_name": "hats",
            "product_price": 100.99

        }

        result = self.client.post(
            '/api/v2/resources/product/', data=json.dumps(product))

        product_list.append(product)
        self.assertEqual(result.status_code, 404)

        update = {
            "product_name": "Glasses",
            "product_price": 500.00

        }

        product = [product for product in product_list]
        product[0]['product_name'] = update['product_name']
        dict_name = {'product_name': product[0]['product_name']}
        result = self.client.put(
            '/api/v2/resources/product/2', data=json.dumps(dict_name))
        self.assertEqual(result.status_code, 404)

    def test_user_can_login(self):
        login = {
            "username": "candy",
            "password":  1234
        }

        response = self.client.get(
            self.hostname+'login', data=json.dumps(login))
        self.assertEqual(response.status_code, 405)

    def user_cannot_login(self, username, password):
        pass

    def tearDown(self):
        pass
