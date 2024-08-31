class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAvg = sum(nums[:k])
        crntAvg = maxAvg
        for i in range(k,len(nums)):
            crntAvg += nums[i] - nums[i-k]
            maxAvg = max(crntAvg,maxAvg)
        return maxAvg/k