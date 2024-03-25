class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        maxnum = 0

        for i in sentences:
            temp = i.split()
            if len(temp) > maxnum:
                maxnum = len(temp)

        return maxnum