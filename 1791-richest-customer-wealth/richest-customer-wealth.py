class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxnum = 0
        for i in accounts:
            if maxnum < sum(i):
                maxnum = sum(i)
        return maxnum