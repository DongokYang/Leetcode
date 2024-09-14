class Solution:
    def romanToInt(self, s: str) -> int:
        
        s = list(s)
        roman = {"I": 1,"IV":4,"V": 5, "IX":9,"X": 10,"XL":40,"L": 50,"XC":90,"C": 100,"CD":400,"D": 500,"CM":900,"M": 1000}

        sm = 0

        x = 0
        y = 1

        while y < len(s):
            if s[x]+s[y] in roman:
                sm += roman[s[x]+s[y]]
                x +=2
                y +=2
            else:
                sm += roman[s[x]]
                x +=1
                y +=1
        if x<len(s):
            sm += roman[s[x]]    
        

        return sm






