"""Function to fetch words."""

import random
from random_word import RandomWords

r = RandomWords()
my_list = r.get_random_words(hasDictionaryDef=True, limit=500, minLength=4, maxLength=20)

WORDLIST = 'wordlist.txt'

with open(WORDLIST, 'w') as f:
    for i in my_list:
        f.write("%s\n" % i)


def get_random_word(min_word_length):
    """Get a random word from the wordlist using no extra memory"""
    num_words_processed = 0
    curr_word = None
    with open(WORDLIST, 'r') as f:
        for word in f:
            if '(' in word or ')' in word:
                continue
            word = word.strip().lower()
            if len(word) < min_word_length:
                continue
            num_words_processed += 1
            if random.randint(1, num_words_processed) == 1:
                curr_word = word
    return curr_word
