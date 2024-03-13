class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #Input: nums = [0,1,2,2,3,0,4,2], val = 2
        count=len(nums)
        while val in nums:
            nums.remove(val)
            count -=1
        return count