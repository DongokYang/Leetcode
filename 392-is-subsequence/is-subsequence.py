class Solution:
    def isSubsequence(self, s: str, t: str) -> bool: 
        s = list(s)
        t = list(t)
        a = 0
        crnt = 0

        if len(s) ==0 :
            return True

        while True:
            if crnt == len(s):
                return True

            if a ==len(t):
                return False

            if s[crnt] == t[a]:
                crnt +=1
                a +=1
            else:
                a +=1
            
    