class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        
        a = len(grid)
        b = len(grid[0])
        summ = 0
        for i in range(a):
            grid[i] = sorted(grid[i])
                
        for i in range(b):
            temp = 0
            for ii in range(a):
                if grid[ii][i] >temp:
                    temp =grid[ii][i]
            summ += temp
        return summ 
            
            

