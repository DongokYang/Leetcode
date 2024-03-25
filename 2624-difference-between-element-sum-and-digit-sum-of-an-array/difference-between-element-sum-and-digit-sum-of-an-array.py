class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        summ = sum(nums)
        digit_sum = 0
        for i in range(len(nums)):
            digit_sum += sum(int(d) for d in str(nums[i]))

        return summ - digit_sum