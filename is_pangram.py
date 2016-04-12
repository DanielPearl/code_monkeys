# Determines if a string is a pangram (containing every letter of the alphabet)

sentence = "The quick brown fox jumps over the lazy dog"

def is_letter(letter):
    """
    determines if ascii of char is within given range
    :param letter: string
    :return: boolean
    """
    lowercase = letter.lower()
    ascii_val = ord(lowercase)
    return ascii_val >= 97 and ascii_val <= 122


def is_panagram(sentence):
    """
    Determines if sentence is param
    :param sentence: string
    :return: boolean
    """
    letter_dict = {}
    for i in sentence:
        if is_letter(i) == True:
            letter_dict[i] = 1
    return (len(letter_dict.keys()) >= 26)

print(is_panagram(sentence))
