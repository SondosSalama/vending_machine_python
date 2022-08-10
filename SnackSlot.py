
class SnackSlot():
    def __init__(self, row, col_in_row, slot_num):
        self.row = row
        self.col_in_row = col_in_row
        self.slot_num = slot_num
        self.snack = None

    def set_snack(self, snack):
        self.snack = snack

    def check_slot_available_and_price(self):
        if not self.snack or not self.snack.check_available():
            self.display_msg("Slot " + str(self.slot_num) + " is empty, please chooce a different one!")
            return False

        self.display_msg("The price for " + self.snack.name + " in slot " + str(self.slot_num) + " is " + str(self.get_snack_price()) + "$")
        return True

    def slot_num_picked(self, money_amount):
        if not self.snack or not self.snack.check_available():
            self.display_msg("Slot " + str(self.slot_num) + " is empty, please chooce a different one!")
            return None

        is_enough, returned_money = self.snack.check_money_is_enough(money_amount)
        if not is_enough:
            self.display_msg("The money inserted is not enough, please add " + str(returned_money * -1) + " $")
            return None
        
        self.snack.dispenses()
        self.push_snack(self.slot_num, self.row, self.col_in_row)
        return returned_money

    def get_snack_price(self):
        if self.snack:
            return self.snack.get_price()
        else:
            return -1

    def print_snack(self):
        if self.snack:
            print("{name: "+self.snack.name+", qty: "+str(self.snack.qty)+", price: "+str(self.snack.price)+"}")
        else:
            print("Empty Slot!")

    def display_msg(self, msg):
        pass

    def push_snack(self, slot_num, row, col_in_row):
        pass
