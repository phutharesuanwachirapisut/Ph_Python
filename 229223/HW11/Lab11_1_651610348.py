#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# Lab11_1 
# 229223 Sec 002

# "He doesn't want to pay $40,000 for a new car, but his wife doesn't seem to care."
import string

def main():
    assert word_count("He doesn't want to pay $40,000 for a new car, but his wife doesn't seem to care.") == {'new': 1,
'but': 1,
'pay': 1,
'want': 1,
'seem': 1,
'care': 1,
'his': 1,
'40,000': 1,
'wife': 1,
'a': 1,
'for': 1,
'car': 1,
"doesn't": 2,
'to': 2,
'he': 1}


def word_count(text):
    words = text.lower().split()
    words = [word.strip(string.punctuation) for word in words]
    dict_a = {}
    while len(words) > 0:
        
        if words.count(words[0]) > 1:
            dict_a[words[0]] = words.count(words[0])
            words = list(filter(lambda x: x != words[0],words))   
        else:
            dict_a[words[0]] = 1 
            words.remove(words[0])
        # for word in words:
        # word_counts[word] = word_counts.get(word, 0) + 1
    return dict_a

if __name__ == '__main__':
    main()