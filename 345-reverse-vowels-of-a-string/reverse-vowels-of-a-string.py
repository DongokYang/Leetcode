class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        vList = []
        VListReal = []
        s = list(s)
        for i in range(len(s)):
            if s[i] in vowels:
                vList.append(i)
                VListReal.append(s[i])
        vList.reverse()
        for i in range(len(vList)):
            s[vList[i]] =VListReal[i]


        s = "".join(s)
        return s