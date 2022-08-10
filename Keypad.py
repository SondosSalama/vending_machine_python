class Keypad():
    def __init__(self):
        self.entered_num = None

    def type_number(self, number_value):
        self.entered_num = 0

        self.entered_num = (self.entered_num * 10) + number_value
        self.display_msg("Slot Number: " + str(self.entered_num))

    def click_enter(self):
        if not self.entered_num or int(self.entered_num) > int(self.get_max_number_of_slots()):
            self.display_msg("Invalid slot number, please enter a new one")
            return

        self.display_slot_data(self.entered_num)
        self.set_needed_money(self.entered_num)

    def click_cancel(self):
        self.display_msg("Cancel select and returning the money!")
        self.clear_slot_num()
        self.push_money()

    def clear_slot_num(self):
        self.entered_num = None

    def pick_slot_and_dispenses(self, slot_num):
        pass

    def display_msg(self, msg):
        pass

    def get_max_number_of_slots(self):
        pass

    def display_slot_data(self, slot_num):
        pass

    def push_money(self):
        pass

    def set_needed_money(self, slot_number):
        pass