class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        nl = []
        for i in range(len(points)):
            nl.append(points[i][0])

        nl = sorted(nl)

        mxdf = 0
        for i in range(len(nl)-1):
            if mxdf<nl[i+1]-nl[i]:
                mxdf = nl[i+1]-nl[i]

        return mxdf