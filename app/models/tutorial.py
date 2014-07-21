# Author: Will Hattingh

import string
from random import randint


def get_random_words():
    """This would be where you normally do module specific code, this is just an example so I'm returning random words"""
    basic_text = "The Quick Brown Fox Jumps Over The Lazy Dog"
    str_to_array = string.split(basic_text, " ")
    num_pieces = len(str_to_array) - 1
    rand_first_word = randint(0, num_pieces)
    rand_second_word = randint(0, num_pieces)

    return str_to_array[rand_first_word] + " " + str_to_array[rand_second_word]
