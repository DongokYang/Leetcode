class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums = sorted(nums)
        i =0
        j = len(nums)-1
        ans = 10000000000000

        while i<j:
            if nums[i] +nums[j] < ans:
                ans = nums[i]+nums[j]
                
            
            i +=1
            j-=1
        return ans/2