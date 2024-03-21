class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        nl = [[] for i in range(0,35)]
        nl[0] = [1]
        nl[1] = [1,1]
        for i in range(2,rowIndex+1):
            nl[i].append(1)
            for ii in range(len(nl[i-1])-1):
                nl[i].append(nl[i-1][ii]+nl[i-1][ii+1])
            nl[i].append(1)
        return nl[rowIndex]