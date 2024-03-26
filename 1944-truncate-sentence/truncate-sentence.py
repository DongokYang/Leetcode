class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        s = s.split()
        nl=[]

        for i in range(k):
            nl.append(s[i])

        nl = ' '.join(nl)

        return nl