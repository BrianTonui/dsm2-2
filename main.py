# main.py

from todo import add_todo, list_todos, complete_todo
from utils import get_user_input, get_int_input

def show_menu():
    print("\nTo-Do List Manager")
    print("1. Add a new to-do")
    print("2. List all to-dos")
    print("3. Complete a to-do")
    print("4. Exit")

def main():
    while True:
        show_menu()
        choice = get_int_input("Choose an option: ")

        if choice == 1:
            task = get_user_input("Enter the to-do task: ")
            add_todo(task)
        elif choice == 2:
            list_todos()
        elif choice == 3:
            list_todos()
            index = get_int_input("Enter the number of the to-do to complete: ")
            complete_todo(index)
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

