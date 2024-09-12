class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        cnt = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for ii in range(n):
                if grid[i][ii] <0:
                    cnt +=1
        
        return cnt