sales_order = []


class Sale():
    def __init__(self, item, price):

        self.item = item
        self.price = price
        self.sale_id = len(sales_order) + 1

    def add_sale(self):
        sales_order.append(self)
        return sales_order

    def to_json(self):

        Sale_json = {
            "sale_id": self.sale_id,
            "item": self.item,
            "price": self.price

        }

        return Sale_json

    def get_sales_order(self):
        return sales_order
