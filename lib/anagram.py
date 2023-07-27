class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, testing_list):
        anagram_list = []
        sorted_word = sorted([letter for letter in self.word])
        for testing_word in testing_list:
            if sorted([letter for letter in testing_word]) == sorted_word:
                anagram_list.append(testing_word)

        return anagram_list