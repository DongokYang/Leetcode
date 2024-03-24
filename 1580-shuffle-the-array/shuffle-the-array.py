class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        nl = []

        for i in range(len(nums)/2):
            nl.append(nums[i])
            nl.append(nums[i+n])
        return nl