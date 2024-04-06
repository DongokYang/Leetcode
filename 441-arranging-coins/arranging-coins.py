class Solution:
    def arrangeCoins(self, n: int) -> int:
        cnt = 0
        i = 1
        while n>=i:
            n -= i
            i +=1
            cnt +=1 
        return cnt