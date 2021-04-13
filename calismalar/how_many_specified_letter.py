
def letter_counter(text):
    letters_dict = dict()
    for letter in text:
        counter = text.count(letter)
        letters_dict.update([(letter, counter)])
    return letters_dict
