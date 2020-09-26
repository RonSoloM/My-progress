def is_palindrome(string):
    return string[::-1].casefold() == string.casefold()


word = str(input("Please enter a word to check: "))
if is_palindrome(word):
    print(True)
else:
    print(False)