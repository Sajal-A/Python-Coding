
import sys
class ATM:
    def __init__(self,balance:float) -> None:
        self.balance = balance
        self.atm_pin :str = '1234'
    
    def is_valid(self,atm_pin:str) -> bool:
        if(self.atm_pin == atm_pin):
            return True
        else:
            return False
            
    def display_menu(self)->None:
        print('1. Check current balance')
        print('2. Deposit money')
        print('3. Withdraw Balance')
        print('4. Exit')
        
    def check_balance(self) -> None:
        print(f'Current balance in your card: {str(self.balance)}')

    def deposit_money(self,amount) -> None:
        self.balance += amount
        print('Money deposited Successfully')
        print(f'Current Balance: {self.balance}')
        
    def withdraw_money(self,amount)->None:
        self.balance -= amount 
        print(f'{amount} is withdrawn')
        print(f'Current Balance: {self.balance}')
    

def main() -> None:
    card1:ATM = ATM(1000)
    print('Welcome to the ATM Simulator')
    user_pin:str = input("Enter you ATM Pin: ")
    while True:
        if card1.is_valid(user_pin):
            print('---Welcome User---')
            print('--------Menu------')
            card1.display_menu()
            opt:str = input('Choose any one option: ')
            print('----------------------------------')
            if opt == '1':
                card1.check_balance()
            elif opt == '2':
                amount:int = int(input('Enter you Amount: '))
                card1.deposit_money(amount)
            elif opt == '3':
                amount:int = int(input('Enter you Amount: '))
                card1.withdraw_money(amount)
            else:
                print('Thank you!!!\nPlease Come Again')
                sys.exit()
        else:
            print('Invalid PIN')
            sys.exit()
        

if __name__ == '__main__':
    main()
    