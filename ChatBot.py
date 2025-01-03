import sys
from datetime import datetime



def get_response(text : str)-> str :
    lowered : str = text.lower() # 'Hello' = 'hello'

    if lowered in ['hello','hi','hey']:
        return 'Hey there !'
    elif 'how are you' in lowered:
        return 'I\'m good thanks !'

    elif 'your name' in lowered :
        return 'my name is  Bot :)'

    elif 'time' in lowered :
        current_time : datetime = datetime.now()
        return f'the time is : {current_time :%H: %M}'
    elif lowered in ['bye','see you','goodbye']:
        return 'It was nice talking to you ! Bye !'
    else:
        return  f' Sorry , I dont understand :"{text}" '


while True :
    user_input : str = input('You :')

    if user_input == 'exit' :
        print('Bot : it was nice to chat with you')
        sys.exit()

    bot_response : str = get_response(user_input)
    print(f'Bot:"{bot_response}"')


