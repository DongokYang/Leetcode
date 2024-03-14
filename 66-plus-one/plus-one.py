class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] +=1
        for i in range(len(digits)-1,-1,-1):
            if i==0 and digits[i] == 10:
                digits[i]=0
                digits.insert(0,1)
            elif digits[i] == 10:
                digits[i-1] +=1
                digits[i]=0
        return digits