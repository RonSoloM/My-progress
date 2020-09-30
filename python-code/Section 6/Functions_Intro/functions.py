def multiply(x, y):
    """
    This function takes two params and multiply them in each other.
    :param x: takes the first `int`
    :param y: takes the secound `int`
    :return: result of param x * param y
    """
    result = x * y
    return result


def is_palindrome(string):
    """
    This function A palindrome is a word, sentence or verse that reads the same forward or backwards
    :param string: Takes and string
    :return: compare if it's equal
    """

    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence):
    """
    This fun
    :param sentence:
    :return:
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)



answer = multiply(18, 3)
print(answer)
