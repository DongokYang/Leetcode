class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nl = []

        tempsum =0 
        for i in nums:
            tempsum += i
            nl.append(tempsum)
        return nl