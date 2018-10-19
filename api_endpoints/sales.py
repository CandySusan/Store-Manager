sales_order = []


class Sale():
    def __init__(self, item, price):

        self.item = item
        self.price = price

    def add_sale(self):
        Sales = {
            "sale_id": len(sales_order)+1,
            "item": self.item,
            "price": self.price

        }

        sales_order.append(Sales)
        return sales_order
