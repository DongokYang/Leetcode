class Solution:
    def checkRecord(self, s: str) -> bool:
        
        s = list(s)

        acnt = 0
        cc = 0
        for i in s:
            if i =="A":
                acnt +=1
                cc = 0
            elif i =="L":
                cc += 1
                if cc == 3:
                    return False
            else:
                cc =0
        if acnt >=2:
            return False
        else:
            return True