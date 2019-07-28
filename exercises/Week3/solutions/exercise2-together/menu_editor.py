from menu_manager import MenuManager


def load_manager():
    new_manager = MenuManager()
    return new_manager

def show_user_menu():
    show_menu = """         MENU
     (a) Add Item
     (b) Delete an Item
     (c) View the Menu
     (x) Exit"""
    print(show_menu)
    choice = input('What is your choice ?')
    return choice

def main():
    manager = load_manager()
    choice = show_user_menu()
    while choice != 'x':
        if choice == 'a':
            item = input('What item do you want to add ?\n')
            price = float(input('What is its price'))
            manager.add_item(item, price)
        if choice == 'b':
            item = input('What do you want to remove ?')
            manager.remove_item(item)
        if choice == 'c':
            print(manager.menu)
        choice = show_user_menu()
    manager.save_to_file()

main()