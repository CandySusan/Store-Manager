product_inventory = []


class Product():
    def __init__(self, product_name, product_price):

        self.product_name = product_name
        self.product_price = product_price
        self.product_id = len(product_inventory) + 1

    def add_product(self):
        product_inventory.append(self)

        return product_inventory
    
    def to_json(self):

        product_json = {
            "product_id": self.product_id,
            "product_name": self.product_name,
            "product_price": self.product_price

        }

        return product_json


def get_product_inventory():
    return product_inventory
