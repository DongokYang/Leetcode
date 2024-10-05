class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        for num in nums:
            if num ==val:
                cnt +=1
        
        for i in range(cnt):
            nums.remove(val)

        return len(nums)
        
        
