from custom_functions.is_palindrome import palindrome


def buildPalindrome(st):
    index = 1
    final = st
    while not palindrome(final):
        suffix = st[0:index]
        final = st + suffix[::-1]
        index += 1
    return final


print(buildPalindrome("abc"))

# https://app.codesignal.com/arcade/intro/level-10/ppZ9zSufpjyzAsSEx
# Given a string, find the shortest possible string which can be achieved
# by adding characters to the end of initial string to make it a palindrome.

# This was accomplished by setting a while loop that runs a palindrome checking function to return the shortest
# final string when achieved. Each cycle and additional part of the prefix is saved, reversed, and concatenated at the
# end of the string. At some point the shortest possible palindrome will be reached.

