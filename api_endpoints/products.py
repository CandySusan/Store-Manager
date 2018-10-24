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


class StoreUser:

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Admin(StoreUser):
    def __init__(self, username, password, Admin_username, Admin_password):
        super(Admin, self).__init__(username, password)
        self.Admin_username = Admin_username
        self.Admin_password = Admin_password


class StoreAttendant(StoreUser):
    def __init__(self, username, password, Attendant_username, Attendant_password):
        super(StoreAttendant, self).__init__(
            Attendant_username, Attendant_password)
        self.Attendant_username = Attendant_username
        self.Attendant_password = Attendant_password
