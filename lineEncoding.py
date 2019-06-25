def lineEncoding(s):
    current = s[0]
    amount = 1
    encoded = ""

    for char in s[1::]:
        if char != current:
            if amount == 1:
                encoded += current
            else:
                encoded += str(amount) + current
            current, amount = char, 1
        else:
            amount += 1

    return encoded + str(amount) + current if amount > 1 else encoded + current


# https://app.codesignal.com/arcade/intro/level-11/o2uq6eTuvk7atGadR

# Given a string, return its encoding defined as follows:

# First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
#  --- for example, "aabbbc" is divided into ["aa", "bbb", "c"].

# Next, each substring with length greater than one is replaced with a
# concatenation of its length and the repeating character
#  --- for example, substring "bbb" is replaced by "3b"

# Finally, all the new strings are concatenated together in the same order and a new string is returned.


# My solution is basically to start the current character at the first position and to move forward with a for loop
# through the string. When the next character is not equivalent to the current, the amount and current character are
# concatenated to the encoded string. However, if the amount was only 1 it will only concatenate char to
# the encoded string.
