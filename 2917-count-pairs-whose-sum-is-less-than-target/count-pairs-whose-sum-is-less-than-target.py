class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = left +1
        count = 0
        while len(nums)-1!=left:
            if nums[left] + nums[right] <target:
                count +=1
            right +=1 
            if right== len(nums):
                left +=1
                right = left+1
        return count