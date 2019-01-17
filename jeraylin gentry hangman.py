import random
import string
word_list = ["dog", "candy", "edison", "smart", "dumb", "white", "black", "tigers", "field", "person"]
the_word = random.choice(word_list)
word = list(the_word)
print(the_word)
guesses = 8
letter_guessed = []
win = False
alphabet = list(string.ascii_letters)

print(list(string.ascii_letters))

for i in range(len(the_word)):
    if the_word[i] in alphabet:
        word.pop(i)
        word.insert(i, "*")

print(word)
print("".join(word))

letter = input("Guess a letter: ")

