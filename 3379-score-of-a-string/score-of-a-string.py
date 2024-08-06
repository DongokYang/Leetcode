class Solution:
    def scoreOfString(self, s: str) -> int:
        nl = []
        for i in s:
            nl.append(ord(i))
        summ = 0
        for i in range(len(nl)-1):
            summ +=abs(nl[i]-nl[i+1])
        return summ