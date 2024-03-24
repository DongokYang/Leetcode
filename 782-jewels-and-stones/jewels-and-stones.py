class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewelsli = list(jewels)
        stonesli = list(stones)

        cnt = 0
        for i in stonesli:
            if i in jewelsli:
                cnt+=1
        return cnt