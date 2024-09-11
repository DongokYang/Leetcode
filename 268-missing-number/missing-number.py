class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = len(nums)
        sm = (s*(s+1))//2


        return sm-sum(nums)