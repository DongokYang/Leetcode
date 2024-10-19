class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack = list(haystack)
        needle = list(needle)

        i = 0

        for i in range(len(haystack)):
            if haystack[i:len(needle) + i] == needle:
                return i

        return -1 
