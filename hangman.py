import random


def get_indices(l, w):
    indices = []
    for i in range(len(w)):
        if w[i] == l:
            indices.append(i)
    return indices


print("H A N G M A N")

words = ("python", "java", "kotlin", "javascript")
word = random.choice(words)
word_length = len(word)
hidden_word = ["-"] * word_length
tries = 8

while tries > 0:

    print(tries, "\n", "".join(hidden_word), sep="")
    letter = input("Input a letter: ")
    uncovered_letters = []

    if letter in word:
        if letter in uncovered_letters:
            print("No improvements")
        else:
            uncovered_letters.append(letter)
            for index in get_indices(letter, word):
                hidden_word[index] = letter
            if len(uncovered_letters) == word_length:
                print("You guessed the word!\nYou survived!")
                break
    else:
        print("That letter doesn't appear in the word")
        tries -= 1

if tries == 0:
    print("You lost!")
