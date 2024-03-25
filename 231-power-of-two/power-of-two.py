class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        li = [1]
        cnt = 2
        while li[-1]<n:
            li.append(cnt)
            cnt *= 2
        
        if n in li:
            return True
        else:
            return False