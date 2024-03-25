class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        
        cnt = 0
        yess = 0

        for i in nums:
            tl = []
            tl.append(i)
            tl.append(i+diff)
            tl.append(i+diff+diff)

            for ii in tl:
                if ii not in nums:
                    yess = 1
            if yess ==0:
                cnt +=1
            else:
                yess=0
        return cnt