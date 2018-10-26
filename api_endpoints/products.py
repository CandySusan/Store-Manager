product_inventory = []


class Product():
    def __init__(self, product_name, product_price):

        self.product_name = product_name
        self.product_price = product_price
        self.product_id = len(product_inventory) + 1
        self.quantity = 10

    def add_product(self, product):
        product_inventory.append(product)

        return product_inventory

    def to_json(self):

        product_json = {
            "product_id": self.product_id,
            "product_name": self.product_name,
            "product_price": self.product_price,
            "quantity": self.quantity

        }

        return product_json


def get_product_inventory():
    return product_inventory


users = []


class Login():
    def __init__(self, username, password):

        self.username = username
        self.password = password

    def add_username(self):
        users.append(self)

        return users

    def to_user_json(self):

        users_json = {
            "username": self.username,
            "password": self.password,
            "logged_in": False
        }

        return users_json


def get_users():
    return users
