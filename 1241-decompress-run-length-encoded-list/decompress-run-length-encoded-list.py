class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nl = []
        for i in range(0,len(nums),2):
            for ii in range(nums[i]):
                nl.append(nums[i+1])
        return nl