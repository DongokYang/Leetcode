class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        s = list(s)
        nl = [0 for i in range(len(s))]
        for i in range(len(s)):
            nl[indices[i]] = s[i]
        nl = ''.join(nl)
        return nl
