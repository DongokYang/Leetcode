class Solution:
    def removeStars(self, s: str) -> str:
        s = list(s)
        ans =[]
        for i in range(len(s)):
            if s[i] =='*':
                ans.pop()
            else:
                ans.append(s[i])
        return "".join(ans)