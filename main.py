import sys
import argparse

with open('sowpods.txt') as f:
    word_list = f.read().split('\n')

parser = argparse.ArgumentParser(description="Letter Rack Reader")
parser.add_argument('rack', type=str, help='The letters in your scrabble rack -NO SPACES, all upper or all lower.')
rack = parser.parse_args().rack.upper()

rack_list = [x for x in rack]
print(rack_list)

valid = []
for word in word_list:
    for x in word:
        if x not in rack_list:
            continue
        else:
            valid.append(x)
