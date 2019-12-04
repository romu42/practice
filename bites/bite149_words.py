# https://codechalleng.es/bites/149/


def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    rough_sort = sorted(words, key=str.lower)
    while (rough_sort[0][0]).isdigit():
        rough_sort.append(rough_sort.pop(0))
    return rough_sort
