class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rtype = []
        for i in range(len(nums)):
            for ii in range(i + 1, len(nums)):
                if target == (nums[i] + nums[ii]):
                    rtype.append(i)
                    rtype.append(ii)
        return rtype
