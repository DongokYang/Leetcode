class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = list(s.split())
        al = []
        for i in s:
            i = i[::-1]
            al.append(i)
        
        al = " ".join(al)
        return al
