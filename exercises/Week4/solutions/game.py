from hangman import Hangman
import json

class Player():
    def __init__(self, name, number_of_games=0, score=0):
        self.name = name
        self.number_of_games = number_of_games
        self.score = score

    @classmethod
    def check_if_already_exists(cls, name):
        with open('results.json', 'r') as f:
            json_file = json.load(f)
            for player in json_file['players']:
                if player['name'].lower() == name.lower():
                    return True
        return False

    @classmethod
    def create_new_player(cls, name):
        if cls.check_if_already_exists(name):
            print('user already exists')
            return False
        print('Welcome {} to the best Hangman Game'.format(name))
        return cls(name)

    @classmethod
    def format_player(cls, name, number_of_games=0, score=0):
        return cls(name, number_of_games, score)

    def create_dictionary(self):
        return {
            "name": self.name,
            "number_of_games": self.number_of_games,
            "score": self.score
        }




class Game():
    def __init__(self):
        self.current_player = None
        with open('results.json', 'r') as f:
            self.results = json.load(f)
            self.players = [Player.format_player(player['name'], player['number_of_games'], player['score']) for player in self.results['players']]

    def update_results(self):
        words_picked = self.results['words_picked']
        self.results = {'players': [], 'words_picked':words_picked}
        for player in self.players:
            self.results['players'].append(player.create_dictionary())
        self.save_to_json()

    def save_to_json(self):
        with open('results.json', 'w') as f:
            f.write(json.dumps(self.results, indent=4))

    def select_player(self, name):
        for player in self.players:
            if player.name.lower() == name.lower():
                self.current_player = player
                return True

        print("We did not find any player with that name. Do you want to create one or enter your name again?\n")
        choice = input("\t(1) Create new Player\n\t(2) Enter my name again\n")
        while choice not in ['1', '2']:
            choice = input("Wrong Input!\n\t(1) Create new Player\n\t(2) Enter my name again\n")

        if choice == '1':
            return False
        else:
            self.select_player(input('What is your name ?'))

    @staticmethod
    def create_word():
        return Hangman()

    def play(self):
        self.current_player.number_of_games += 1
        hangman_handler = self.create_word()
        self.results['words_picked'].append(hangman_handler.random_word)
        print(hangman_handler.found_letters_str())
        while hangman_handler.guess > 0:
            choice = input("(1)Guess a letter\n(2)Guess the word\n")
            if choice == '1':
                guess = input("What letter do you want to try\n")

                if len(guess) > 1 and not guess.isdigit():
                    print('please select only one letter\n')
                    continue

                if guess in hangman_handler.chosen_letters:
                    print('you already chose that letter\n')
                    continue

                if hangman_handler.new_guess(guess):
                    print('Good choice !\n')
                    if '_' not in hangman_handler.found_letters:
                        print('you found the word !\n')
                        self.current_player.score += 10
                        break
                else:
                    print('Wrong letter!\n')
                    print(hangman_handler.hangman_drawing())

                print(hangman_handler.found_letters_str())

            elif choice == '2':
                guess = input("What do you think is the word\n")
                if hangman_handler.guess_full_word(guess):
                    print('congrats you found the word !!\n')
                    print(guess.capitalize())
                    self.current_player.score += 10
                    break
                else:
                    print('wrong guess !\n')
                    print(hangman_handler.hangman_drawing())
            else:
                print('Wrong input\n')


        print('the word was {}\n'.format(hangman_handler.random_word))
        self.update_results()
