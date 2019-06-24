def electionsWinners(votes, k):
    total_possible_winners = 0
    current_leading_score = max(votes)
    amount_with_current_leading_score = 0

    for score in votes:
        if score == current_leading_score:
            amount_with_current_leading_score += 1
        if score + k > current_leading_score:
            total_possible_winners += 1

    if amount_with_current_leading_score > 1 and k == 0:
        return 0
    elif amount_with_current_leading_score < 2 and k == 0:
        return 1
    else:
        return total_possible_winners


print(electionsWinners([2,3,5,2], 3))


# https://app.codesignal.com/arcade/intro/level-10/8RiRRM3yvbuAd3MNg

# Given an array of the numbers of votes given to each of the candidates so far, and an integer k equal to the number
# of voters who haven't cast their vote yet, find the number of candidates who still have a chance to win the election.

# The winner of the election must secure strictly more votes than any other candidate. If two or more
# candidates receive the same (maximum) number of votes, assume there is no winner at all.

# The gist of this script is that the max score is accounted for through the use of a built-in python method max(), then
# every score is looped through with the addition of the remaining voter amount. If that sum is greater than the leading
# score then 1 is added to the total_possible_winners integer. The amount of scores that match the max scores value are
# stored, just in case k is equivilent to 0, this way it can return 1 or 0 based on a possible tie for the lead already
# being present or not.
