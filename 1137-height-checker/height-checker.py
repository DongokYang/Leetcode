class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        opt = sorted(heights)
        cnt = 0
        for i in range(len(opt)):
            if opt[i] != heights[i]:
                cnt +=1
    
        return cnt