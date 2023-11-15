# project1
tprg 2131 (project1)

This project simulates a coin-operated vending machine using Python. It includes two main components: vending_machine.py, which is the main application, and test_vending_machine.py, which contains unit tests for the vending machine's functionality.

# vending_machine.py
This script creates a graphical user interface (GUI) for a vending machine. It allows users to insert coins, select products, and receive change. The GUI is built using PySimpleGUI and showcases the interaction of various components in a typical vending machine.

vending machine Features:
Coin insertion with multiple denominations.
Selection of products with dynamic pricing.
Return of change with a simple message.
Display of product names and their prices.
Update of product availability and handling of sold-out scenarios.

# test_vending_machine.py
This script is designed to test the functionality of the VendingMachine class defined in the starter file. The tests ensure that the vending machine behaves as expected under various scenarios, such as adding coins, selecting products with sufficient or insufficient funds, and handling the return of change

test vending machine Features:
test_initial_state(): Verifies the initial state of the vending machine.
test_add_coin(): Tests the addition of coins to the vending machine.
test_product_selection_with_insufficient_funds(): Checks the behavior when selecting a product without enough funds.
test_product_selection_with_sufficient_funds(): Ensures correct product dispensing when sufficient funds are provided.
test_return_change(): Tests the functionality of returning change to the user.


# vending_machine(challenge).py
Challenge 1 & 3: Managing and displaying product stock. Indicating sold-out products both visually (by greying out buttons) and through console messages.
Challenge 6: Displaying the price of each item in the GUI.




# vending_machine-rpi.py
This Vending Machine application is designed to run on a Raspberry Pi with connected hardware components. It simulates a coin-operated vending machine, complete with a graphical user interface (GUI), coin insertion, product selection, and a physical return button connected to the Raspberry Pi's GPIO. The application also controls a servo motor to simulate the action of dispensing a product.


 Utilizes PySimpleGUI for easy-to-use interface.
 Connects to a physical button and a servo motor via GPIO pins on a Raspberry Pi.
 Allows users to insert coins and select products through the GUI.
Physical Return Button is connected hardware button acts as a return mechanism, triggering the dispensing process or returning coins.
