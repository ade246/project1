"""test_vending_machine_.py - simulate a coin operated vending machine
### KHARI WALLACE, 100807131, TPRG 2131 ###


TPRG 2131 Fall 2023 Project 1
November 15, 2023
Khari Wallace <khari.wallace@dcmail.ca>

"""
# test_vending_machine.py



from proj1vending_STUDENT import VendingMachine, WaitingState, AddCoinsState, DeliverProductState, CountChangeState

def test_initial_state():
    vending = VendingMachine()
    vending.add_state(WaitingState())
    vending.add_state(AddCoinsState())
    vending.add_state(DeliverProductState())
    vending.add_state(CountChangeState())
    vending.go_to_state('waiting')
    assert vending.state.name == 'waiting'