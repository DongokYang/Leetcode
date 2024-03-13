class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prvs = -101
        rmvlist = []
        for i in nums:
            pointer = i
            print(prvs,pointer)
            if prvs ==pointer:
                rmvlist.append(i)
            prvs = pointer
        for i in rmvlist:
            nums.remove(i)
        return len(nums)