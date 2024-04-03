class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        
        i = 0
        j = len(mat)-1
        ans = 0

        for ii in range(j+1):
            if i!=j:
                ans += mat[ii][i]
                ans += mat[ii][j]
                i+=1
                j -=1
            else:
                ans += mat[ii][i]
                i+=1
                j -=1
        return ans
