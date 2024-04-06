class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        small = len(s)
        m = len(g)

        if small>=m:
            small = m
        g = sorted(g)
        s = sorted(s)
        cnt = 0
        while len(g)>0 and len(s)>0 :

            if g[0] <= s[0]:
                cnt +=1
                g.pop(0)
                s.pop(0)
            else:
                s.pop(0)

        return cnt
            





