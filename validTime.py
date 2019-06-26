def validTime(time):
    if len(time) != 5:
        return False
    hours_minutes = time.split(":")
    if int(hours_minutes[0]) > 23 or int(hours_minutes[1]) > 59:
        return False
    else:
        return True


# https://app.codesignal.com/arcade/intro/level-12/ywMyCTspqGXPWRZx5/solutions?solutionId=rMDvjNud7ryYiqqgg

# Check if the given string is a correct time representation of the 24-hour clock.

# Example:

#    For time = "13:58", the output should be
#    validTime(time) = true;
#    For time = "25:51", the output should be
#    validTime(time) = false;
#    For time = "02:76", the output should be
#    validTime(time) = false.

# Checks to see through length if string can possibly be valid, then splits the string by ":" into two positions in an
# array. It then converts the strings to integers and checks to see if their values are within the range of 24 hour time
# If I wasn't sure the string values were numerical, I would convert them within a try/catch block.
