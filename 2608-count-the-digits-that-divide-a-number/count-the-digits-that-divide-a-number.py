class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        nl = list(map(int,list(str(num))))
        cnt =0

        for i in nl:
            if num%i ==0:
                cnt +=1

        return cnt