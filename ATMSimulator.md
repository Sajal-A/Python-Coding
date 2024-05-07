Objectives:
    1. Welcome Message
        -->The program starts by greeting the user, setting the stage for the ATM simulation
    2. Initialize Account Balance
        -->The balance variable is set to 1000, representing the user's starting account balance.
    3. Set up and verify PIN:
        -->The user_pin variable holds the correct PIN ('1234')
        -->The user is prompted to enter their PIN
        -->The entered PIN is compared to user_pin
        -->If the pin is incorrect, the program notifies the user and sets atm_on to false to prevent entering the main loop
        -->If the PIN is correct, atm_on is set to True, allowing access too the ATM functionalites
    4. Main ATM operation Loop:
        -->A while loop is used, controlled by the atm_on flag.
        -->Inside the loop, the main menu is displayed with options to check balance, deposit money, withdraw money, or exit.
    5. User choice hnadilng
        --> The user's choice is captured through input.
        --> if-elif-else statements handle the different choices.
    6. Balance Inquiry:
        --> If the user chooses to check the balance, it's displayed using balance variable.
    7. Deposit Money:
        --> The user can deposit money, which is added to balance.
        --> The deposit amount and updated balance are displayed.
    8. Withdraw Money
        --> For withdrawals, the program checks if the balance is sufficient.
        --> If so, the requested amount is substracted from balance, and the withdrawal is confirmed.
        --> If the balance is insufficient, a warning message is shown
    9. Exiting the Program:
        --> The user can choose to exit the ATM
        --> On exiting, a goodbye message is shown, and atm_on is set to False, ending the loop and the program
    10. Invalid choice Handling
        --> If the user enters an option that's not on the menu, the program prompts them to try again
        
