class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        nl = list(ransomNote)
        nlcp =  list(magazine)

        for i in nl:
            if i in nlcp:
                nlcp.remove(i)
            else:
                return False
        
        return True