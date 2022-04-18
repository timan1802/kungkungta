import pandas as pd

data = pd.read_pickle('./dict_pkl/only_3word.pkl')


def find_word_list(first_word):
    word_list = []
    for word in data:
        if word.startswith(first_word):
            word_list.append(word)
    return word_list


def find_word(first_word, exclude=None):
    if exclude is None:
        exclude = []
    found_word_list = find_word_list(first_word)
    if len(found_word_list) == 0:
        return 'No Such Word'
    complement = list(set(found_word_list).difference(exclude))
    return complement[0]
