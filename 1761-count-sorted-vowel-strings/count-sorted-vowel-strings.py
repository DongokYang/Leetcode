class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        a, e, i , o ,u = 1,1,1,1,1

        while n> 1 :
            u += sum([a,e,i,o]) 
            o += sum([a,e,i])
            i += sum([a,e])
            e += sum([a])
            n -=1

        
        return a+e+i+o+u