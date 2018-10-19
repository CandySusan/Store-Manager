product_inventory = []


class Product():
    def __init__(self, product_name, product_price):

        self.product_name = product_name
        self.product_price = product_price

    def add_product(self):
        Product = {
            "product_id": len(product_inventory)+1,
            "product_name": self.product_name,
            "product_price": self.product_price

        }
        product_inventory.append(Product)
        return product_inventory


def get_product_inventory():
    return product_inventory
