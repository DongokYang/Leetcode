class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        s = list(s)
        t = list(t)
        ans = 0

        for i in range(len(s)):
            for ii in range(len(s)):
                if s[i] == t[ii]:
                    ans += abs(i-ii)

        return ans
