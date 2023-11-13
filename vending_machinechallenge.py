"""vending_machine_.py - simulate a coin operated vending machine
### KHARI WALLACE, 100807131, TPRG 2131 ###
Challenge 1,3,6


Machine has a bulk set of 5 for each item. The quantity reaches zero after 5 purchases. After the 5th purchase is made a
the item colour is faded out and when you try to select the item you will receive a message "(item) is sold out".(challenge 1,3)

The price of the item is shown on the panel beside each selection.(challenge 6)


TPRG 2131 Fall 2023 Project 1
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
ITEM_STOCK = {"surprise": 5, "pop": 5, "chips": 5, "choc": 5, "beer": 5}
COIN_VALUES = {"Nickel": 5, "Dime": 10, "Quarter": 25, "Loonie": 100, "Toonie": 200}

class StateMachine:
    def __init__(self):
        self.coins = 0
        self.stock = ITEM_STOCK.copy()

    def display_money(self, money):
        if money >= 100:
            return f'{money / 100}$'
        else:
            return f'{money}¢'

    def return_money(self):
        change = self.display_money(self.coins)
        if self.coins > 0:
            print(f"Change returned: {change}")
        self.coins = 0
        print("Thank you, come again.")
        return True

    def add_coin(self, coin_value):
        self.coins += coin_value
        print(f"Total inserted: {self.display_money(self.coins)}")

    def select_product(self, product_key, window):
        product_name = next((name for name, key in SELECTION_LIST if key == product_key), None)
        if product_name:
            if self.stock[product_name] == 0:
                print(f"{product_name} is sold out.")
                return
            cost = ITEM_COSTS[product_name]
            if self.coins >= cost:
                self.coins -= cost
                self.stock[product_name] -= 1
                print(f"Dispensed {product_name}. Remaining balance: {self.display_money(self.coins)}")
                if self.stock[product_name] == 0:
                    window[product_key].update(button_color=('white', '#808080'))  # Grey out the button
            else:
                needed = cost - self.coins
                print(f"Not enough money for {product_name}. Need {self.display_money(needed)} more.")

    def update_stock_display(self, window):
        for name, key in SELECTION_LIST:
            if self.stock[name] == 0:
                window[key].update(button_color=('white', '#808080'))  # Grey out the button

    def process_event(self, event, window):
        if event in COIN_VALUES:
            self.add_coin(COIN_VALUES[event])
        elif event in [key for _, key in SELECTION_LIST]:
            self.select_product(event, window)
        elif event == "RETURN":
            return self.return_money()

if __name__ == "__main__":
    machine = StateMachine()

    # Define the GUI layout
    coin_col = [[sg.Text("ENTER COINS")]] + [[sg.Button(item[0], key=item[1], size=(10, 1))] for item in COIN_LIST]
    select_col = [[sg.Text("SELECT ITEM", size=(15, 1)), sg.Text("PRICE", size=(7, 1))]]
    select_col += [
        [sg.Button(name, key=key, size=(15, 1), button_color=('white', '#00FF00')), sg.Text(f'{ITEM_COSTS[name]}¢', size=(7, 1))]
        for name, key in SELECTION_LIST
    ]

    layout = [
        [sg.Column(coin_col, vertical_alignment="TOP"),
         sg.VSeparator(),
         sg.Column(select_col, vertical_alignment="TOP")],
        [sg.Button("RETURN")]
    ]

    window = sg.Window("Vending Machine", layout, size=(600, 400))

    machine.update_stock_display(window)  # Update the stock display initially

    while True:
        event, _ = window.read()
        if event == sg.WIN_CLOSED or machine.process_event(event, window):
            break

        machine.update_stock_display(window)  # Update the stock display after each event

    window.close()
