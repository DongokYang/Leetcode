class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        outputcnt = 0
        s = list(s)
        cnt = 0
        for i in s:
            if i =='L':
                cnt +=1
            elif i=='R':
                cnt -=1
            
            if cnt==0:
                outputcnt +=1
        return outputcnt
