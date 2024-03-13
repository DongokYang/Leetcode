class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        prvs = -101
        nums = sorted(nums)
        for i in nums:
            pointer = i
            if prvs==pointer:
                return True
            prvs = pointer
        return False
                