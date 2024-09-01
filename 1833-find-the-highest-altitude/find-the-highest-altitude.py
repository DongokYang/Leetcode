class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        crnt = 0
        maxNum = 0


        for i in range(len(gain)):
            crnt += gain[i]
            if crnt > maxNum:
                maxNum = crnt
        return maxNum