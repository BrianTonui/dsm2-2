# utils.py

def get_user_input(prompt):
    return input(prompt)

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")
