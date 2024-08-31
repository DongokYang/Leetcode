class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)

        cnt =0 
        a = 0 
        b = len(nums)-1
        switch = False
        while a < b:
            if nums[a]+nums[b] ==k:
                cnt +=1
                a +=1
                b -=1
            elif nums[a]+nums[b] >k:
                b-=1
            else:
                a+=1
        return cnt
     

