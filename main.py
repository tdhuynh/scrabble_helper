import sys
import argparse


def letter_count(word):
    count = {letter: word.count(letter) for letter in word}
    return count


def word_finder(word, rack):
    rack_count = letter_count(rack)
    word_count = letter_count(word)
    return all([word_count[letter] <= rack_count[letter] for letter in word])


scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}


def scoring(word):
    return sum([scores[letter] for letter in word.lower()])


with open('sowpods.txt') as f:
    word_list = f.read().split('\n')

parser = argparse.ArgumentParser(description="Letter Rack Reader")
parser.add_argument('rack', type=str, help='The letters in your scrabble rack -NO SPACES, all upper or all lower.')
rack = parser.parse_args().rack.upper()

valid_words = [[scoring(word), word] for word in word_list if set(word).issubset(set(rack)) and word_finder(word, rack)]

for score, word in sorted(valid_words, reverse=True):
    print(score, word)
