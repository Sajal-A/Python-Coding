import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    'A':2,
    'B':4,
    'C':6,
    'D':8
}

symbol_value = {
    'A':5,
    'B':4,
    'C':3,
    'D':2
}

def deposit() -> int:
    while True:
        amount:str = input('What would you like to desposit? $ -> ')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than zero.')
        else:
            print('Please Enter a number.')
    
    return amount

def get_number_of_lines() -> None:
    while True:
        lines = input(f'Enter the number of lines to bet on (1-{MAX_LINES}):')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Enter a valid number of lines!!')

        else:
            print('Please enter a number')
            
    return lines





def main() -> None:
    balance = deposit()
    lines = get_number_of_lines()
    print(balance,lines)
    
if __name__ == '__main__':
    main()