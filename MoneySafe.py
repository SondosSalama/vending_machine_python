class MoneySafe():
    def __init__(self):
        self.money_type_counts = {50.0: 0, 20.0: 0, 1.0: 0, 0.50: 0, 0.20: 0, 0.10: 0}

    def update_money_amount(self, money_amount):
        self.money_type_counts = money_amount

    def check_if_qty_is_enough(self, money_type, qty_needed):
        if self.money_type_counts[money_type] > 0 and self.money_type_counts[money_type] >= qty_needed:
            self.money_type_counts[money_type] = self.money_type_counts[money_type] - 1
            return True

        return False

    def insert_money_by_name(self, money_name):
        if money_name == "50$":
            self.money_type_counts[50.0] = self.money_type_counts[50.0] + 1
        elif money_name == "20$":
            self.money_type_counts[20.0] = self.money_type_counts[20.0] + 1
        elif money_name == "1$":
            self.money_type_counts[1.0] = self.money_type_counts[1.0] + 1
        elif money_name == "50c":
            self.money_type_counts[0.50] = self.money_type_counts[0.50] + 1
        elif money_name == "20c":
            self.money_type_counts[0.20] = self.money_type_counts[0.20] + 1
        elif money_name == "10c":
            self.money_type_counts[0.10] = self.money_type_counts[0.10] + 1