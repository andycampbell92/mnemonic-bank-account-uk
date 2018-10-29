from nltk.corpus import words
from nltk.corpus import wordnet

# Takes a list of words and returns a list which is a subset of the original
# where any list with matching n letters have been removed. The first occurence
# of the word will remain
def unique_first_n(word_list, n=4):
    word_beginings = []
    unique_n_word_list = []
    for w in word_list:
        if w[:n] not in word_beginings:
            unique_n_word_list.append(w)
            word_beginings.append(w[:n])
    return unique_n_word_list

if __name__ == '__main__':
    # Words of lengthe greater than three
    word_list = list(filter(lambda w: len(w) > 2, words.words()))
    unique_four = unique_first_n(word_list)
    print(len(unique_four))
