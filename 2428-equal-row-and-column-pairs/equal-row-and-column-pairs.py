class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cnt = 0 

        cGrid = []
        for i in range(len(grid[0])):
            temp = []

            for ii in range(len(grid)):
                temp.append(grid[ii][i])
            
            cGrid.append(temp)

        for i in grid:
            for ii in cGrid:
                if i ==ii:
                    cnt +=1

        return cnt