class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        crnt = 0
        zcnt = 0
        maxx = 0
        lstZ = 0
        switch = True
        for i in range(len(nums)):
            if nums[i] ==1:
                crnt +=1
            else:
                if zcnt ==0:         
                    zcnt +=1
                    crnt +=1
                elif zcnt ==1:
                    crnt = i-lstZ
                    zcnt = 1
                lstZ = i
            maxx =max(crnt,maxx)

        maxx-=1   
        return maxx