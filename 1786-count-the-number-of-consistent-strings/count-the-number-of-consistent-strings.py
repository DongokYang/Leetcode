class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_lst= list(allowed)
        cnt = 0
        for i in words:
            i = list(i)
            isallowed = True
            for ii in i:
                if ii not in allowed:
                    isallowed = False
            
            if isallowed:
                cnt +=1
            
        return cnt

