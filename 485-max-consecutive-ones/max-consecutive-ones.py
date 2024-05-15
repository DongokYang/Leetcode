class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxnum = 0
        temp = 0
        for i in range(len(nums)):
            if nums[i]==1:
                temp +=1
            else:
                if temp >= maxnum:
                    maxnum = temp
                temp = 0
        if temp >= maxnum:
            maxnum = temp
            temp = 0
        return maxnum