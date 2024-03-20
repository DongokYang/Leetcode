class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(s)
        cleaned_string =''.join(char.lower() for char in s if char.isalnum())
        if cleaned_string == cleaned_string[::-1]:
            return True
        else:
            return False