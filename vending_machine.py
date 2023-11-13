"""vending_machine_.py - simulate a coin operated vending machine
### KHARI WALLACE, 100807131, TPRG 2131 ###


TPRG 2131 Fall 2022 Project 1
November 15, 2023
Khari Wallace <khari.wallace@dcmail.ca>

"""

import PySimpleGUI as sg
# Define custom font and size
sg.theme('DarkAmber')
font = ('Helvetica', 15)

COIN_LIST = [
    ("5\u00A2", "Nickel"),  # 5 cents
    ("10\u00A2", "Dime"),   # 10 cents
    ("25\u00A2", "Quarter"),# 25 cents
    ("$1", "Loonie"),       # 1 dollar
    ("$2", "Toonie")        # 2 dollars
]

SELECTION_LIST = [
    ("surprise", "A"),  # Example of using single letter keys
    ("pop", "B"),
    ("chips", "C"),
    ("choc", "D"),
    ("beer", "E")
]

ITEM_COSTS = {"surprise": 500, "pop": 100, "chips": 150, "choc": 200, "beer": 300}
COIN_VALUES = {"Nickel": 5, "Dime": 10, "Quarter": 25, "Loonie": 100, "Toonie": 200}

class StateMachine:
    def __init__(self):
        self.coins = 0

    def display_money(self, money):
        if money >= 100:
            return f'{money / 100}$'
        else:
            return f'{money}¢'

    def return_money(self):
        if self.coins > 0:
            change = self.display_money(self.coins)
            print(f"Change returned: {change}")
        print("Thank you, come again.")
        self.coins = 0
        return True  # Indicate that the window should close

    def add_coin(self, coin_value):
        self.coins += coin_value
        print(f"Total inserted: {self.display_money(self.coins)}")

    def select_product(self, product_key):
        product_name = next((name for name, key in SELECTION_LIST if key == product_key), None)
        if product_name:
            cost = ITEM_COSTS[product_name]
            if self.coins >= cost:
                self.coins -= cost
                print(f"Dispensed {product_name}. Remaining balance: {self.display_money(self.coins)}")
            else:
                needed = cost - self.coins
                print(f"Not enough money for {product_name}. Need {self.display_money(needed)} more.")

    def process_event(self, event):
        if event in COIN_VALUES:
            self.add_coin(COIN_VALUES[event])
        elif event in [key for _, key in SELECTION_LIST]:
            self.select_product(event)
        elif event == "RETURN":
            return self.return_money()
    
    