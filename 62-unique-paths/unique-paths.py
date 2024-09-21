class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        nl = [[0 for i in range(m)]for ii in range(n)]

        for i in range(n):
            nl[i][0] = 1
            
        for ii in range(m):
            nl[0][ii] = 1

        for i in range(1,n):   
            for ii in range(1,m):
                nl[i][ii] = nl[i-1][ii] + nl[i][ii-1]
        return nl[-1][-1]