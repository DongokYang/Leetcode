class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        cnt = 0
        crntVal =nums[0]


        for i in range(len(nums)):
            if nums[i] == crntVal:
                cnt +=1
            else:
                crntVal = nums[i]
                cnt =1
            if cnt < 3:
                nums[k] = nums[i]
                k +=1

        return k
