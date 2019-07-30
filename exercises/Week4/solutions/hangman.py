
class Hangman():
    def __init__(self):
        with open('sowpods.txt', 'r') as f:
            self.words = [word.strip().lower() for word in f if len(word)>=6]
