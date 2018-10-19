product_inventory = []


class Product():
    def __init__(self, item, price):

        self.item = item
        self.price = price

    def add_product(self):
        Product = {
            "product_id": len(product_inventory)+1,
            "item": self.item,
            "price": self.price

        }
        product_inventory.append(Product)
        return product_inventory


def get_product_inventory():
    return product_inventory
