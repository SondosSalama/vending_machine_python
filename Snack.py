class Snack():
    def __init__(self, name, qty, price):
        self.name = name
        self.qty = qty
        self.price = price

    def check_available(self):
        is_available = True
        if self.qty == 0:
            is_available = False
        return is_available

    def check_money_is_enough(self, money):
        is_enough = True
        returned_money = money - self.price
        if returned_money < 0:
            is_enough = False
        return is_enough, returned_money

    def dispenses(self):
        self.qty = self.qty - 1

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name

    def add_qty(self, additional_qty):
        self.qty = self.qty + additional_qty

    def remove_qty(self, removed_qty):
        self.qty = self.qty - removed_qty