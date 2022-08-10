from DisplayScreen import DisplayScreen
from Keypad import Keypad
from MoneySlot import MoneySlot
from SnackSlotsDisplay import SnackSlotsDisplay
from Hardware import Hardware

from decimal import Decimal

class VendingMachine():
    def __init__(self):
        self.needed_money = 0
        self.selected_slot = None
        self.is_valid_snack = False

        self.display_screen = DisplayScreen()
        self.keypad = Keypad()
        self.money_slot = MoneySlot()
        self.snack_slots_display = SnackSlotsDisplay()
        self.hardware = Hardware()

        self.keypad.pick_slot_and_dispenses = self.pick_slot_and_dispenses
        self.keypad.get_max_number_of_slots = self.snack_slots_display.get_max_number_of_slots
        self.keypad.display_slot_data = self.display_slot_data
        self.keypad.set_needed_money = self.set_needed_money
        self.keypad.push_money = self.push_money
        self.keypad.display_msg = self.display_screen.display_msg

        self.money_slot.push_card_out = self.hardware.push_card_out
        self.money_slot.push_change_out = self.hardware.push_change_out
        self.money_slot.charge_card = self.hardware.charge_card
        self.money_slot.check_valid_card_data = self.hardware.check_valid_card_data
        self.money_slot.reject_money = self.hardware.reject_money
        self.money_slot.check_if_total_is_enough_and_buy = self.check_if_total_is_enough_and_buy
        self.money_slot.is_item_selected = self.is_item_selected

        self.money_slot.display_msg = self.display_screen.display_msg

        self.snack_slots_display.display_msg = self.display_screen.display_msg
        self.snack_slots_display.push_snack = self.hardware.push_snack

    def is_item_selected(self):
        return self.selected_slot

    def check_if_total_is_enough_and_buy(self):
        charge = False
        if self.money_slot.is_card_in:
            charge = True
        if self.money_slot.total and self.money_slot.total > 0 and self.needed_money and self.needed_money > 0:
            if round(Decimal(self.money_slot.total), 2) >= round(Decimal(self.needed_money), 2):
                charge = True
        if charge:
            is_succeess = self.pick_slot_and_dispenses(self.selected_slot)
            #if is_succeess:
            self.keypad.clear_slot_num()

    def set_needed_money(self, slot_num):
        if not self.is_valid_snack:
            return

        snack_slot = self.snack_slots_display.get_snack_slot_by_num(slot_num)
        self.selected_slot = slot_num
        self.needed_money = snack_slot.get_snack_price()

    def push_money(self):
        if not self.money_slot.is_card_in:
            total_money_inserted = self.money_slot.total
            self.money_slot.calculate_and_push_change(total_money_inserted)
            self.needed_money = 0
            self.selected_slot = None
            self.money_slot.total = 0
            self.is_valid_snack = False
        else:
            self.money_slot.push_card_out()

    def display_slot_data(self, slot_num):
        snack_slot = self.snack_slots_display.get_snack_slot_by_num(slot_num)
        self.is_valid_snack = snack_slot.check_slot_available_and_price()

    def pick_slot_and_dispenses(self, slot_num):
        snack_slot = self.snack_slots_display.get_snack_slot_by_num(slot_num)
        is_succeess = False

        if not self.money_slot.is_card_in:
            total_money_inserted = self.money_slot.total

            returned_money = snack_slot.slot_num_picked(total_money_inserted)
            if returned_money and returned_money > -1:
                is_succeess  = self.money_slot.calculate_and_push_change(returned_money)
            elif returned_money == 0.0:
                is_succeess = True
        else:
            snack_price = snack_slot.get_snack_price()
            is_valid = self.money_slot.check_card_data(snack_price)
            if is_valid:
                snack_slot.slot_num_picked(snack_price)
                is_succeess = True

        if is_succeess:
            self.needed_money = 0
            self.selected_slot = None
            self.money_slot.total = 0
            self.is_valid_snack = False

        return is_succeess

    ## ******************* Action APIs:

    def set_snacks_display(self, rows_num, col_in_row_num):
        self.snack_slots_display.create_rows_and_cols(rows_num, col_in_row_num)

    def fill_snacks(self, snacks):
        self.snack_slots_display.fill_slots_with_snacks(snacks)

    def insert_coins(self, coin):
        self.money_slot.insert_coins(coin)

    def insert_notes(self, notes):
        self.money_slot.insert_notes(notes)

    def insert_card(self, card):
        self.money_slot.insert_card(card)

    def type_number(self, num):
        self.keypad.type_number(num)

    def click_enter(self):
        self.keypad.click_enter()

    def click_cancel(self):
        self.keypad.click_cancel()

    def show_displayed_snacks(self):
        for snack_slot_num in self.snack_slots_display.snack_slots.keys():
            print("Slot: " + str(snack_slot_num))
            self.snack_slots_display.snack_slots[snack_slot_num].print_snack()

    def show_total_money(self):
        print("Total Money: " + str(self.money_slot.total) + "$")

    def set_money_safe(self, money_values):
        self.money_slot.fill_money_safe(money_values)
