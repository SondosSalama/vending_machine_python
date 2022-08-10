from SnackSlot import SnackSlot

class SnackSlotsDisplay():
    def __init__(self, rows_num = None, col_in_row_num = None):
        self.create_rows_and_cols(rows_num, col_in_row_num)

    def create_rows_and_cols(self, rows_num, col_in_row_num):
        self.rows_num = rows_num
        self.col_in_row_num = col_in_row_num

        self.total_num_of_slots = 0
        self.snack_slots = {}

        if self.rows_num and self.col_in_row_num:
            self.total_num_of_slots = self.rows_num * self.col_in_row_num
            self.create_snacks_slots()

    def create_snacks_slots(self):
        row = 0
        col = 0
        for slot_num in range(1, (self.total_num_of_slots + 1)):
            snack_slot = SnackSlot(row, col, slot_num)
            snack_slot.display_msg = self.display_msg
            snack_slot.push_snack = self.push_snack

            self.snack_slots[slot_num] = snack_slot
            col = col + 1
            if col == self.col_in_row_num:
                col = 0
                row = row + 1

    def fill_slots_with_snacks(self, snacks):
        if self.get_max_number_of_slots == 0:
            print("Input Error: Please first define the number of rows and colums in the snack display")

        if len(snacks) > self.get_max_number_of_slots():
            print("Input Error: Number of snacks more than number of availabe slots")

        for snack_slot_num in snacks.keys():
            snack_slot = self.snack_slots[snack_slot_num]
            snack_slot.set_snack(snacks[snack_slot_num])
            self.snack_slots[snack_slot_num] = snack_slot

    def get_snack_slot_by_num(self, slot_num):
        return self.snack_slots[slot_num]

    def get_max_number_of_slots(self):
        return self.total_num_of_slots

    def display_msg(self, msg):
        pass

    def push_snack(self, row, col_in_row):
        pass
    
