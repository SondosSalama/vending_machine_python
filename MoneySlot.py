from decimal import Decimal
from MoneySafe import MoneySafe

class MoneySlot():
    def __init__(self):
        self.is_card_in = False
        self.card_data = None
        self.total = 0
        self.money_safe = MoneySafe()

    def fill_money_safe(self, money_amount):
        self.money_safe.update_money_amount(money_amount)

    def insert_coins(self, coin):
        if not self.is_item_selected():
            self.display_msg("Select Item First!")
            self.reject_money(coin)
            return

        accepted_notes = {"10c": 0, "20c": 0, "50c": 0, "1$": 0}

        if coin in accepted_notes:
            accepted_notes[coin] = 1
        else:
            self.display_msg("Not a valid Coin!")
            self.reject_money(coin)
            return

        self.money_safe.insert_money_by_name(coin)

        if self.is_card_in:
            self.display_msg("Can't insert coins with Card in!")
            self.push_change_out(
                ten_cent_count=accepted_notes["10c"], 
                twenty_cent_count=accepted_notes["20c"], 
                fifty_cent_count=accepted_notes["50c"], 
                one_dollar_count=accepted_notes["1$"])
            return

        self.total = self.total + (0.10 * accepted_notes["10c"])
        self.total = self.total + (0.20 * accepted_notes["20c"])
        self.total = self.total + (0.50 * accepted_notes["50c"])
        self.total = self.total + accepted_notes["1$"]

        self.display_msg("Total: " + str(self.total))

        self.check_if_total_is_enough_and_buy()

    def insert_notes(self, note):
        if not self.is_item_selected():
            self.display_msg("Select Item First!")
            self.reject_money(note)
            return

        accepted_notes = {"20$": 0, "50$": 0}
        if note != "20$" and note != "50$":
            self.display_msg("Not a valid Note!")
            self.reject_money(note)
            return 

        accepted_notes[note] = accepted_notes[note] + 1
        self.money_safe.insert_money_by_name(note)

        if self.is_card_in:
            self.display_msg("Can't insert notes money with Card in!")
            self.push_change_out(twenty_dollar_count=accepted_notes["20$"], fifty_dollar_count=accepted_notes["50$"])
            return

        self.total = self.total + (20 * accepted_notes["20$"])
        self.total = self.total + (50 * accepted_notes["50$"])

        self.display_msg("Total: " + str(self.total))

        self.check_if_total_is_enough_and_buy()

    def insert_card(self, card_data):
        if not self.is_item_selected():
            self.display_msg("Select Item First!")
            self.push_card_out()
            return

        self.is_card_in = True
        self.card_data = card_data
        if self.total > 0:
            self.display_msg("Can't insert notes or coins with Card in!")
            self.calculate_and_push_change(self.total)

        self.display_msg("Card Inserted!")

        self.check_if_total_is_enough_and_buy()

    def check_card_data(self, price):
        is_valid = self.check_valid_card_data(self.card_data, price)
        if not is_valid:
            self.display_msg("Invalid Card! Check your balance!")
        else:
            self.charge_card(price)
            self.display_msg("Card charge with: " + str(price) + "$")

        self.push_card_out()
        return is_valid

    def calculate_and_push_change(self, returned_money):
        change_left = returned_money

        currencies_count = {50.0: 0, 20.0: 0, 1.0: 0, 0.50: 0, 0.20: 0, 0.10: 0}

        for curr_amount in currencies_count.keys():

            while round(Decimal(change_left), 2) >= round(Decimal(curr_amount), 2):
                new_count = currencies_count[curr_amount] + 1
                if curr_amount in self.money_safe.money_type_counts and self.money_safe.check_if_qty_is_enough(curr_amount, new_count):
                    currencies_count[curr_amount] = new_count
                    change_left = Decimal(change_left) - Decimal(curr_amount)
                    change_left = round(Decimal(change_left), 2)
                else:
                    break

            if change_left == 0:
                break

        if change_left > 0:
            self.display_msg("Sorry, can't find enough change. Please try with smaller curreny!")
            return False

        self.total = 0

        self.display_msg("Returning Change: " + str(returned_money) + "$")

        self.push_change_out(
            twenty_dollar_count=currencies_count[20.0], 
            fifty_dollar_count=currencies_count[50.0], 
            ten_cent_count=currencies_count[0.10], 
            twenty_cent_count=currencies_count[0.20], 
            fifty_cent_count=currencies_count[0.50], 
            one_dollar_count=currencies_count[1.0])

        return True

    def push_card_out(self):
        pass

    def push_change_out(self, twenty_dollar_count = 0, fifty_dollar_count = 0, ten_cent_count = 0, twenty_cent_count = 0, fifty_cent_count = 0, one_dollar_count = 0):
        pass

    def display_msg(self, msg):
        pass

    def reject_money(self, note):
        pass

    def check_valid_card_data(self, card_data, price):
        pass

    def charge_card(self, price):
        pass

    def is_item_selected(self):
        pass

    def check_if_total_is_enough_and_buy(self):
        pass

