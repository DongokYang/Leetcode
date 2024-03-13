class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        current_longest_prefix=""
        for i in range(len(strs[0])):
            testing_prefix=strs[0][0:i+1:]
            for ii in range(len(strs)):
                if testing_prefix!=strs[ii][0:i+1:]:
                    current_longest_prefix = strs[0][0:i:]
                    return current_longest_prefix
                current_longest_prefix = strs[0][0:i+1:]
        return current_longest_prefix
        