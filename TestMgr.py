from VendingMachine import VendingMachine
from Snack import Snack
import sys
import filecmp

original_stdout = sys.stdout

def init_vending_machine():

    vending_machine = VendingMachine()
    vending_machine.set_snacks_display(5, 5)
    vending_machine.fill_snacks({
        1:  Snack("s1", 1, 3),    2:  Snack("s2", 2, 2.5),  3: Snack("s3", 2, 1.2),   4: Snack("s4", 4, 3.2),   5: Snack("s5", 5, 4),
        6:  Snack("s6", 3, 3.2),  7:  Snack("s7", 2, 2.3),  8: Snack("s8", 2, 1.7),   9: Snack("s9", 4, 5.1),   10: Snack("s10", 4, 1.5),
        11: Snack("s11", 1, 3.4), 12: Snack("s12", 2, 2.7), 13: Snack("s13", 2, 1.5), 14: Snack("s14", 4, 5.2), 15: Snack("s15", 4, 2.5),
        16: Snack("s16", 4, 3.5), 17: Snack("s17", 2, 2.8), 18: Snack("s18", 2, 1.1), 19: Snack("s19", 4, 5.4), 20: Snack("s20", 4, 3.5),
        21: Snack("s21", 6, 3.6), 22: Snack("s22", 2, 2.0), 23: Snack("s23", 2, 1.3), 24: Snack("s24", 4, 5.5), 25: Snack("s25", 4, 5.5),})

    vending_machine.set_money_safe({50.0: 2, 20.0: 3, 1.0: 100, 0.50: 100, 0.20: 100, 0.10: 100})

    return vending_machine

def doc_case_test():
    with open('running_tests_logs/doc_case_test.log', 'w') as f:
        sys.stdout = f

        vending_machine = init_vending_machine()
        vending_machine.show_displayed_snacks()

        vending_machine.type_number(2)
        vending_machine.click_enter()

        vending_machine.insert_coins("1$")
        vending_machine.insert_coins("1$")
        vending_machine.insert_coins("1$")

    sys.stdout = original_stdout
    result = filecmp.cmp("running_tests_logs/doc_case_test.log", "tests_golden_logs/doc_case_test.log")
    if result: print("doc_case_test PASSED!")
    else: print("doc_case_test FAILED!")

def notes_case_test():
    with open('running_tests_logs/notes_case_test.log', 'w') as f:
        sys.stdout = f

        vending_machine = init_vending_machine()
        vending_machine.show_displayed_snacks()

        vending_machine.type_number(2)
        vending_machine.click_enter()

        vending_machine.insert_notes("20$")

    sys.stdout = original_stdout
    result = filecmp.cmp("running_tests_logs/notes_case_test.log", "tests_golden_logs/notes_case_test.log")
    if result: print("notes_case_test PASSED!")
    else: print("notes_case_test FAILED!")

def card_case_test():
    with open('running_tests_logs/card_case_test.log', 'w') as f:
        sys.stdout = f

        vending_machine = init_vending_machine()
        vending_machine.type_number(2)
        vending_machine.click_enter()

        vending_machine.insert_coins("1$")
        vending_machine.insert_coins("1$")
        vending_machine.insert_card("VISA")

    sys.stdout = original_stdout
    result = filecmp.cmp("running_tests_logs/card_case_test.log", "tests_golden_logs/card_case_test.log")
    if result: print("card_case_test PASSED!")
    else: print("card_case_test FAILED!")

def invalid_slot_num():
    with open('running_tests_logs/invalid_slot_num.log', 'w') as f:
        sys.stdout = f

        vending_machine = init_vending_machine()
        vending_machine.type_number(30)
        vending_machine.click_enter()

    sys.stdout = original_stdout
    result = filecmp.cmp("running_tests_logs/invalid_slot_num.log", "tests_golden_logs/invalid_slot_num.log")
    if result: print("invalid_slot_num PASSED!")
    else: print("invalid_slot_num FAILED!")

def empty_slot_test():
    with open('running_tests_logs/empty_slot_test.log', 'w') as f:
        sys.stdout = f

        vending_machine = init_vending_machine()

        vending_machine.type_number(1)
        vending_machine.click_enter()

        vending_machine.insert_notes("20$")

        vending_machine.type_number(1)
        vending_machine.click_enter()

    sys.stdout = original_stdout
    result = filecmp.cmp("running_tests_logs/empty_slot_test.log", "tests_golden_logs/empty_slot_test.log")
    if result: print("empty_slot_test PASSED!")
    else: print("empty_slot_test FAILED!")

def invalid_coin_and_note_test():
    with open('running_tests_logs/invalid_coin_and_note_test.log', 'w') as f:
        sys.stdout = f

        vending_machine = init_vending_machine()

        vending_machine.type_number(2)
        vending_machine.click_enter()

        vending_machine.insert_notes("30$")
        vending_machine.insert_coins("2$")

        vending_machine.insert_notes("20$")

    sys.stdout = original_stdout
    result = filecmp.cmp("running_tests_logs/invalid_coin_and_note_test.log", "tests_golden_logs/invalid_coin_and_note_test.log")
    if result: print("invalid_coin_and_note_test PASSED!")
    else: print("invalid_coin_and_note_test FAILED!")

def cancel_test():
    with open('running_tests_logs/cancel_test.log', 'w') as f:
        sys.stdout = f

        vending_machine = init_vending_machine()

        vending_machine.type_number(2)
        vending_machine.click_enter()

        vending_machine.insert_coins("50c")
        vending_machine.click_cancel()

        vending_machine.insert_notes("20$")

    sys.stdout = original_stdout
    result = filecmp.cmp("running_tests_logs/cancel_test.log", "tests_golden_logs/cancel_test.log")
    if result: print("cancel_test PASSED!")
    else: print("cancel_test FAILED!")

if __name__ == "__main__":
    doc_case_test()
    notes_case_test()
    card_case_test()
    invalid_slot_num()
    empty_slot_test()
    invalid_coin_and_note_test()
    cancel_test()

    