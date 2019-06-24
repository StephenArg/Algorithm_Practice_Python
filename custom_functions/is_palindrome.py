def palindrome(string):
    string = string.lower()
    if string[::-1] == string:
        return True
    else:
        return False

# Simple palindrome checker. Comment out line two for case sensitivity.
