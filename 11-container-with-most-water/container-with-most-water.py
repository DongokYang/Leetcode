class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        a = 0 
        b = len(height)-1
        while a < b:
            k = min(height[a],height[b])
            if k*(b-a) > ans:
                ans = k*(b-a)

            if height[a] > height[b]:
                b -=1
            else:
                a+=1
                b = len(height)-1

        return ans
            



