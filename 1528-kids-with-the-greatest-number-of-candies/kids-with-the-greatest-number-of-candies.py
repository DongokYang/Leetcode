class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        maxnum = max(candies)
        al = []
        for i in candies:
            if i+extraCandies >= maxnum:
                al.append(True)
            else:
                al.append(False)
        return al 
