class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        if len(nums)==0:
            if nums[0] ==0:
                return 0

        for i in range(1,len(nums)+1):

            if sum(nums[:i])-nums[i-1] == sum(nums[i:]):
                return i-1
        
        return -1