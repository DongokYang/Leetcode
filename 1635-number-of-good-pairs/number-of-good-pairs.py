class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        for i in range(len(nums)):
            for ii in range(i+1,len(nums)):
                if nums[i]==nums[ii]:
                    cnt +=1
        return cnt
