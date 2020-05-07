import random
import re

word_dict = {}
# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    word_base = words.split()
    for index in range(len(word_base)):
        if word_base[index] not in word_dict:
            try:
                word_dict[word_base[index]] = []
                word_dict[word_base[index]].append(word_base[index + 1])
            except IndexError:
                pass
        else:
            try:
                word_dict[word_base[index]].append(word_base[index + 1])
            except IndexError:
                pass


# TODO: analyze which words can follow other words

# TODO: construct 5 random sentences
for i in range(5):
    # generate start words
    while not start_flag:
        start_flag = re.match('^[A-Z"]', start_word)
        index = random.randrange(0, 200)
        start_word = word_dict[index].key
    # generate end words
    while not end_flag:
        end_flag = re.match('[.!?]$', end_word)
        index = random.randrange(0, 200)
        end_word = word_dict[index].key
    # generate our middle words
    word_list = []
    
    num_count = random.randrange(1, 9)
    for i in range(num_count):
        pass
        # start generating random words from available word options
        
    print(start_word, end=" ")
    
    print(end_word, end=" ")
    
