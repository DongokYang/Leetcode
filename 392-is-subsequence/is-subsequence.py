class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)

        a = 0
        b = 0

        if len(s)==0:
            return True
        
        while b < len(t) and a<len(s):
            if s[a] ==t[b]:
                a +=1
                b +=1
            else:
                b +=1

        if a ==len(s):
            return True
        else:
            return False
                    