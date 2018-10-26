from api_endpoints.products import product_inventory
sales_order = []


class Sale():
    def __init__(self, item, price, quantity):

        self.item = item
        self.price = price
        self.sale_id = len(sales_order) + 1
        self.quantity = quantity

    def add_sale(self, sale):
        sales_order.append(sale)
        for product in product_inventory:
            if product.product_name == sale.item:
                quantity = int(product.quantity)
                quantity -= int(sale.quantity)
                product.quantity = quantity
                break
        return sales_order

    def to_json(self):

        Sale_json = {
            "sale_id": self.sale_id,
            "item": self.item,
            "price": self.price,
            "quantity": self.quantity

        }

        return Sale_json


def get_sales_order():
    return sales_order
