class Solution:
    def fib(self, n: int) -> int:
        ff = [0,1]
        for i in range(2,n+1):
            temp = ff[i-1]+ff[i-2]
            ff.append(temp)
        return ff[n]