from anagram_checker import AnagramChecker

def create_checker():
    new_checker = AnagramChecker()
    return new_checker

def show_menu():
    menu = "Menu\n\t(1)Check word\n\t(2)Exit"
    choice = input(menu)
    if choice == '1':
        return True
    return False

def main():
    checker = create_checker()
    while show_menu():
        word = input('What is your word ?')
        word = word.strip().lower()
        if checker.is_valid_word(word):
            words = checker.get_anagrams(word)
            print(words)
        else:
            print('not valid word')

main()