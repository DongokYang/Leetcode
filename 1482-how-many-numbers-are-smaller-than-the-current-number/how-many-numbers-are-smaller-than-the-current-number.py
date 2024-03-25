class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        al = []

        for i in range(len(nums)):
            cnt =0
            for ii in range(len(nums)):
                if nums[i]>nums[ii]:
                    cnt +=1
            al.append(cnt)
        return al