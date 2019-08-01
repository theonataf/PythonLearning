import json
from hangman import Hangman
from game import Game, Player

class Run():
    def __init__(self):
        self.current_game = Game()

    def main(self):
        print("---------WELCOME TO HANGMAN---------")
        menu = "What do you want to do ?\n\t(1)Create new player\n\t(2)Change current Player\n\t(3)Play Game\n\t(4)See Scores\n\t(5)Exit"
        choice = input(menu)

        while True:
            if choice == '1':
                player = Player.create_new_player(input("What's your name ?\n"))
                while player == False:
                    print("player already exists")
                    player = Player.create_new_player(input("Choose another name:\n"))
                self.current_game.players.append(player)
                self.current_game.current_player = player
                self.current_game.update_results()

            elif choice == '2':
                name = input('What is your name ?\n')
                if not self.current_game.select_player(name):
                    choice = '1'
                    continue

            elif choice == '3':
                if self.current_game.current_player == None:
                    choice = '2'
                    continue

                print("Select Level")
                level = input("\tLevel (1): 15 guesses\n\tLevel (2): 10 guesses\n\tLevel (3): 5 guesses\n")
                while level not in ['1', '2', '3']:
                    level = input("\tLevel (1): 15 guesses\n\tLevel (2): 10 guesses\n\tLevel (3): 5 guesses\n")

                Hangman.level(level)
                self.current_game.play()

            elif choice == '4':
                print(self.current_game.results)

            elif choice == '5':
                break

            else:
                print('Wrong Input')

            choice = input(menu)

run = Run()

run.main()