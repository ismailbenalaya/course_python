import sys

try :
    result : float = 10/0
    print( result)
except Exception as  e :
    print(f'Error : {e}')


try:
    # Code that might cause an error
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    # This will run if there's a ValueError (e.g., entering letters instead of a number)
    print("That's not a valid number!")


while True :
    try:
        user_input : str = input('Enter a number :')
        print(f'10/ {user_input} = {10/float(user_input)}')
    except ZeroDivisionError as e :
        print('You cannot divide by 0')
        sys.exit()

