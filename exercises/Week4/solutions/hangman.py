import random


class Hangman():
    guess = 10

    def __init__(self):
        with open('sowpods.txt', 'r') as f:
            self.words = [word.strip().lower() for word in f if len(word.strip()) >= 6]
        self.random_word = random.choice(self.words)
        self.found_letters = ['_' for _ in self.random_word]
        self.chosen_letters = []
        self.word_to_list = [letter for letter in self.random_word]

    @classmethod
    def level(cls, level):
        if level == '1':
            cls.guess = 15
        elif level == '2':
            cls.guess = 10
        elif level == '3':
            cls.guess = 5
        return True

    def new_guess(self, letter):
        found_letter = False
        self.chosen_letters.append(letter)

        for i in range(len(self.word_to_list)):
            if self.word_to_list[i] == letter:
                self.found_letters[i] = letter
                found_letter = True


        if not found_letter:
            self.guess -= 1
            return False

        return True

    def guess_full_word(self, word):
        if self.random_word.lower() == word.lower():
            return True
        else:
            self.guess -= 1
            return False

    def found_letters_str(self):
        return ' '.join(self.found_letters)

    def hangman_drawing(self):
        drawing = """
        ===========
            ||     ||
            ||     --
            ||    |oo|
            ||     --
            ||    /||/
            ||     //
            ||    / /
            ||
          ========"""

        if self.guess > 0:
            return drawing[0:int(len(drawing)/self.guess)]
        else:
            return drawing