class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """

        n = list(str(n))
        for i in range(len(n)):
            n[i] = int(n[i])
            
        return max(n)
        