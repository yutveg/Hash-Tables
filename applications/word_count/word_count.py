import re

def word_count(s):
    word_dict = {}
    regex = re.compile('[^a-zA-Z\']')
    entry = regex.sub(' ', s)
    sanitized_entry = entry.lower()
    print(sanitized_entry)
    if len(s) <= 0:
        return word_dict
    
    list_of_strings = sanitized_entry.split()
    for word in list_of_strings:
        
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    return word_dict



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))