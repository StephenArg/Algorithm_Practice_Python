def isMAC48Address(inputString):
    if len(inputString) != 17:
        return False

    group_values = inputString.split("-")

    for value in group_values:
        if len(value) != 2:
            return False
        for char in value:
            if char.isalpha() and (70 < ord(char) or ord(char) < 65):
                return False

    return True

# https://app.codesignal.com/arcade/intro/level-10/HJ2thsvjL25iCvvdm

# A media access control address (MAC address) is a unique identifier assigned to
# network interfaces for communications on the physical network segment.

# The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is six groups
# of two hexadecimal digits (0 to 9 or A to F), separated by hyphens (e.g. 01-23-45-67-89-AB).
# Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.

# For this task I first checked to see through length if the string can even possibly be correct, then I split the
# string into parts pairs of two, separating at '-' junctions. Then I looped through each pair and checked each
# character. If one of the characters was a letter but not A-F based off it's Unicode integer it returns False.
# If every value passes then the function returns True.
