#Yousif Iskander #100851999
from collections import Counter
import string

class WordCounter():
    def __init__(self, input):
        self.__words_dict = input

    def get_words_dict(self):
        wordList = [] #Empty list to add words too
        punctuationTable = str.maketrans('', '', string.punctuation)
        for line in self.__words_dict: #Reads each line in the file
            tempWordList = line.translate(punctuationTable).split() #Used to remove Punctuation
            for word in tempWordList: #Reads each word in the
                wordList.append(word) #Used to add word to the List
        self.__words_dict = wordList #Updates the words to the Variable
        return self.__words_dict

    def top_10_words(self):
        top10 = Counter(self.get_words_dict()).most_common(10) #Used to count the letters and then create a top 10
        #Prints the top 10
        for i in range(10):
            print(f'{i}: {top10[i]}')

def main():
    file = open("text-1.txt", "r")
    Words = WordCounter(file)
    Words.top_10_words()

main()