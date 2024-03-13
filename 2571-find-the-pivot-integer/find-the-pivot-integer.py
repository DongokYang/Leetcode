class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        nlist = [i for i in range(1,n+1)]
        for i in range(n):
            if sum(nlist[i-1::]) ==sum(nlist[:i:]):
                return i
        return -1
                