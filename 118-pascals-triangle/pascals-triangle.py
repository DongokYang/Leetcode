class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        nl = [[] for i in range(0,30)]
        nl[0] = [1]
        nl[1] = [1,1]

        for i in range(2,numRows):
            nl[i].append(1)
            for ii in range(len(nl[i-1])-1):
                nl[i].append(nl[i-1][ii]+nl[i-1][ii+1])
            nl[i].append(1)
        return nl[:numRows:]