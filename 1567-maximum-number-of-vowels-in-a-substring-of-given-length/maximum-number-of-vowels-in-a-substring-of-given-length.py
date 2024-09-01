class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        s=list(s)
        vList = ['a','e','i','o','u']
        Vcnt = 0
        ans = 0

        for i in range(k):
            if s[i] in vList:
                Vcnt +=1
            ans = max(Vcnt,ans)

        for i in range(k,len(s)):
            if s[i] in vList:
                Vcnt +=1
            if s[i-k] in vList:
                Vcnt -=1
            ans = max(Vcnt,ans)

        return ans

