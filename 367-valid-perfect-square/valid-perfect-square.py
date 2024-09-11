class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        first = 0
        last = num

        while first <= last:
            mid = (first+last)//2

            if mid*mid >num:
                last = mid -1
            elif mid*mid <num:
                first = mid +1
            else:
                return True
        return False


