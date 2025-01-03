total: int = 0
print('Welcome to Calc+! Add positive number, or insert "0" to exit')
while True:
    user_input : int = int (input('Enter a number :'))

    if user_input < 0:
        print('Please check again do u wanna exit ?')
        continue

    if user_input == 0 :
        print(f'{total}')
        break

    total+= user_input




