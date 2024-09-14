class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid[0])-2
        ans = [[]for i in range(n)]

        for i in range(len(grid)-2):
            for ii in range(len(grid)-2):
                a = max(grid[i][ii:ii+3])
                b = max(grid[i+1][ii:ii+3])
                c = max(grid[i+2][ii:ii+3])
                ans[i].append(max(a,b,c))


        
        return ans
        