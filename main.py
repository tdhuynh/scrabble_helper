import sys
import argparse

with open('sowpods.txt') as f:
    word_list = f.read().split('\n')

parser = argparse.ArgumentParser(description="Letter Rack Reader")
parser.add_argument('rack', type=str, help='letters in the Scrabble rack')
rack = parser.parse_args().rack.upper()
