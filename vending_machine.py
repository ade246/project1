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