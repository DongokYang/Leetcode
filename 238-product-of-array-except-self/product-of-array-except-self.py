class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ttl = 1
        zcnt =0
        ans = []

        for i in nums:
            if i==0:
                zcnt +=1

        if zcnt ==1:
            for i in nums:
                if i !=0: 
                    ttl *= i
            for i in nums:
                if i !=0:
                    temp = 0
                else:
                    temp = ttl

                ans.append(temp)

        elif zcnt ==0:
            for i in nums:
                ttl *= i
            for i in nums:               
                temp = ttl//i
                ans.append(temp)
                
        else:
            return [0 for i in range(len(nums))]

        return ans