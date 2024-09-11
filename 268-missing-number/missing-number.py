class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = len(nums)
        sm = 0
        for i in range(s+1):
            sm +=i
        return sm-sum(nums)