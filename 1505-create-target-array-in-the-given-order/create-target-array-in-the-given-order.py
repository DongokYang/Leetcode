class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        nl = []
        for i in range(len(nums)):
            nl.insert(index[i],nums[i])
        
        return nl