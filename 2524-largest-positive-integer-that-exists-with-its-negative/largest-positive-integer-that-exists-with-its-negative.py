class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answerlist=[]
        for i in nums:
            if -i in nums:
                answerlist.append(i)
        for i in range(len(answerlist)):
            answerlist[i] = abs(answerlist[i])
        answerlist.append(-1)
        return max(answerlist)