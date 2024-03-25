class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        for i in range(0,len(nums),2):
            temp = nums[i]
            nums[i]=nums[i+1]
            nums[i+1]=temp

        return nums