class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[-1]
        
        nl = [0 for i in range(len(nums))]
        nl[0] = nums[0]
        nl[1] = nums[1]

        for i in range(2,len(nums)):
            nl[i] = max(nl[i-2]+nums[i],max(nl[:i-1])+nums[i])


        
        return max(nl[-1],nl[-2])