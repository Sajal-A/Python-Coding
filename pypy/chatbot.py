import sys
from datetime import datetime

def get_response (text:str) -> str:
    lower: str = text.lower()
    
    if lower in ['hello','hi','hey']:
        return 'Hey there!'
    elif 'how are you' in lower:
        return 'I\'m good thanks!'
    elif 'your name' in lower:
        return 'My name is: BOT :)'
    elif 'time' in lower:
        current_time:datetime = datetime.now()
        return f'The time is: {current_time:%H:%M:%S}'
    elif lower in ['bye','see you','goodbye']:
        return 'It was nice talking to you!bye!'
    elif lower in ['thank','thank you']:
        return 'Happy to help you! :)'
    else:
        return f'Sorry, I do not understand: "{text}".'
    
print('Hello, I\'m Bot')
name:str = input('What is your name? -> ')
    
while True:
    user_inputs:str = input(f'{name}: ')
    if user_inputs == 'exit':
        print('Bot: It was nice talking to you!')
        sys.exit()
        
    bot_response: str = get_response(user_inputs)
    print(f'Bot: {bot_response}')
    