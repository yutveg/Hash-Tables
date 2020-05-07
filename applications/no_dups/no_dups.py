def no_dups(s):
    # Implement me.
    word_dict = {}
    sentence = s.split()
    for word in sentence:
        if word in word_dict:
            pass
        else:
            word_dict[word] = 1

    list_string = []
    for key in word_dict:
        list_string.append(key)
    
    final_string = " ".join(list_string)
    return final_string

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))