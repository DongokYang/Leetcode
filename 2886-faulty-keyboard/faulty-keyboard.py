class Solution:
    def finalString(self, s: str) -> str:
        s = list(s)
        al = []
        for i in s:
            if i =='i':
                al = al[::-1]
            else:
                al.append(i)
        
        al = "".join(al)
        return al