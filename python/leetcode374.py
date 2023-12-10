
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num):
    pass
class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            pick = (left + right) // 2
            if guess(pick) == -1:
                right = pick - 1
            elif guess(pick) == 1:
                left = pick + 1
            else:
                return pick
        return left