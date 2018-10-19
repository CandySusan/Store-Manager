import unittest

from api_endpoints.app import app

import json


class TestApi(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.hostname = "http://localhost:5000/api/v1/"

    def test_get_all_products(self):
        response = self.client.get(self.hostname + 'products')
        self.assertEqual(response.status_code, 200)

    def test_post_a_product(self):
        products = {

            "product_name": "sandals",
            "product_price": 15.99
        }

        response = self.client.post(
            self.hostname+'products', data=json.dumps(products))
        
        self.assertEqual(response.status_code, 201)

    def test_get_a_product(self):
        response = self.client.get(self.hostname+'products/1')
        self.assertEqual(response.status_code, 200)

    def test_post_a_sale(self):
        sales = {

            "item": "boots",
            "price": 15.99
        }

        response = self.client.post(
            self.hostname+'sales', content_type='application/json', data=json.dumps(sales))
        self.assertEqual(response.status_code, 201)

    def test_get_all_sales(self):
        response = self.client.get(self.hostname + 'sales')
        self.assertEqual(response.status_code, 200)

    def test_get_a_sale(self):
        response = self.client.get(self.hostname+'sales/1')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
