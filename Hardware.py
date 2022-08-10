class Hardware():
    def __init__(self):
        pass

    def push_snack(self, slot_num, row, col_in_row):
        print("Hardware: Push Snack in slot: "+str(slot_num)+" (" + str(row) + ", " + str(col_in_row) + ") out!")

    def push_card_out(self):
        print("Hardware: Push Card out!")

    def push_change_out(self, ten_cent_count = 0, twenty_cent_count = 0, fifty_cent_count = 0, one_dollar_count = 0, twenty_dollar_count = 0, fifty_dollar_count = 0):
        if ten_cent_count > 0 or twenty_cent_count > 0 or fifty_cent_count > 0 or one_dollar_count > 0 or twenty_dollar_count >0 or fifty_dollar_count>0:
            print("Hardware: Push the following Moneny out:")
        if ten_cent_count > 0:
            print(str(ten_cent_count) + " conis of type 10c")
        if twenty_cent_count > 0:
            print(str(twenty_cent_count) + " coins of type 20c")
        if fifty_cent_count > 0:
            print(str(fifty_cent_count) + " coins of type 50c")
        if one_dollar_count > 0:
            print(str(one_dollar_count) + " coins of type 1$")
        if twenty_dollar_count > 0:
            print(str(twenty_dollar_count) + " notes of type 20$")
        if fifty_dollar_count > 0:
            print(str(fifty_dollar_count) + " notes of type 50$")

    def reject_money(self, money):
        print("Hardware: reject money of type: " + money)

    def check_valid_card_data(self, card_data, price):
        print("Hardware: Check Card Data (" + card_data + ") and balance for " + str(price) + "$")
        return True

    def charge_card(self, price):
        print("Hardware: Charging Card with: " + str(price) + "$")
