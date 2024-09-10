# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        first, end = 1,n

        while first <= end:
            mid = first + (end-first)//2
            res = guess(mid)

            if res == 0:
                return mid
            elif res == 1:
                first = mid +1
            elif res == -1:
                end = mid -1
        
        return -1

        
        
        