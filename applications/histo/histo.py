# Implement me.
import re

histogram = {}

def histo(filename):
    file_contents = open(filename, 'r').read()
    word_collection = file_contents.split()
    for word in word_collection:
        regex = re.compile('[^a-zA-Z ]')
        entry = regex.sub('', word)
        sanitized_entry = entry.lower()
        if sanitized_entry not in histogram:
            histogram[sanitized_entry] = 1
        else:
            histogram[sanitized_entry] += 1

def order_histo(word_dict):
    items = list(word_dict.items())
    items.sort(key=lambda e: e[1], reverse=True)
    return items

def print_histo(words):
    for key, value in words:
        print(f"{key} {' ':{10 - len(key) if 10 - len(key) > 0 else 1}}" + '#'*value) 

histo('robin.txt')
word_sorted = order_histo(histogram)
print_histo(word_sorted)