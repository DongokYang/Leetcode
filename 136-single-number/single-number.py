class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        newlist = [0 for i in range(60000)]
        for ii in nums:
            newlist[ii+30000] +=1
        for i in range(len(newlist)):
            if newlist[i] == 1:
                return i-30000