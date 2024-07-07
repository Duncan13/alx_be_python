def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            choice1 = input('Item to add: ')
            shopping_list.append(choice1)
            pass
        elif choice == '2':
            # Prompt for and remove an item
            choice2 = input('Item to remove: ')
            if choice2 in shopping_list:
                shopping_list.remove(choice2)
            else:
                print('Item not in the list')
            pass
        elif choice == '3':
            # Display the shopping list
            for i in shopping_list:
                print(i)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

