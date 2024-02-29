class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        number_list = list(x_str)
        for i in range(len(number_list)//2):
            if number_list[i] != number_list[-i-1]:
                return False
        return True


        