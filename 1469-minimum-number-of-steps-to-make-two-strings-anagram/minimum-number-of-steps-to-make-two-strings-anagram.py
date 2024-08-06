class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter

        scounter = Counter(s)
        tcounter = Counter(t)
        cnt = 0
        sset=set(s)
        for i in sset:
            if scounter[i] > tcounter[i]:    
                cnt += scounter[i] - tcounter[i]

        return cnt