class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        newlist = [1,2,3,5] 
        for i in range(4,n):
            newlist.append((newlist[i-1]*2)-newlist[i-3])
        return newlist[n-1]