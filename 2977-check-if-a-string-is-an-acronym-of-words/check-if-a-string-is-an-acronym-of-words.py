class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        
        ans = words[0][0]

        for i in range(1,len(words)):
            ans += words[i][0]

        if ans==s:
            return True
        else:
            return False