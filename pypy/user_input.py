import string
import sys

def is_letters_only(text:str) -> None:
    alpha:str = string.ascii_letters+' '
    
    for char in text:
        if char not in alpha:
            raise ValueError('Text can only contain letters from the alphabet!!!')
        
    print(f'"{text}" is letters-only, good job!')
    

def main() -> None:
    while True:
        try:
            user:str = input('Check Text: ')
            if user == 'exit':
                print('Bye! Bye!')
                sys.exit()
            is_letters_only(user)
        except ValueError:
            print('Please only enter English letters....')
        except Exception as e:
            print(f'Encountered an unknown exception: {type(e)} {e}')
            
main()