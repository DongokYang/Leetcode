class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        switch = True
        minlength = min(strs, key=len)
        ans = []

        for i in range(len(minlength)):
            tmp = strs[0][i]
            for ii in range(len(strs)):
                if tmp != strs[ii][i]:
                    switch = False
            
            if switch:
                ans.append(tmp)
            else:
                break
        return "".join(ans)

