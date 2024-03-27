class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        currentnum = 0
        maxnum = 0
        for i in gain:
            currentnum += i
            if currentnum >maxnum:
                maxnum = currentnum
        
        return maxnum