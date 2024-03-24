class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        answ = [0 for i in range(len(nums))]

        for i in range(len(answ)):
            answ[i] = nums[nums[i]]
        return answ