class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(1,len(nums)+1):
            a = sum(nums[i:])
            b = sum(nums[:i-1])
            ans.append(abs(a-b))
        return ans