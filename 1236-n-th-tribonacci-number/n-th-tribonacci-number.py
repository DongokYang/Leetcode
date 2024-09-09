class Solution:
    def tribonacci(self, n: int) -> int:
        nim = [0,1,1,2]

        for i in range(3,n):
            nim.append(nim[-1]+nim[-2]+nim[-3])

        return nim[n]