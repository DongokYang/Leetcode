class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sascii = [ord(c) for c in s]
        tascii = [ord(c) for c in t]

        diff = sum(tascii) - sum(sascii) 

        return chr(diff)