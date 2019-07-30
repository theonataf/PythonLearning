class AnagramChecker():
    def __init__(self):
        with open('sowpods.txt', 'r') as f:
            self.words = [word.strip().lower() for word in f]

    def is_valid_word(self, word):
        if word in self.words:
            return True
        else:
            return False

    @staticmethod
    def is_anagram(word1, word2):
        if len(word1) == len(word2):
            if sorted(word1) == sorted(word2):
                return True

        return False

    def get_anagrams(self, word):
        matching_words = [anagram for anagram in self.words if self.is_anagram(word, anagram)]
        return matching_words





