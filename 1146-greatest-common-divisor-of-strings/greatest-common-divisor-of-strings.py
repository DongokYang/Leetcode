class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ans = ""

        start, end = 0,0

        while True:
            if str1[start:end] in str2:
                if len(str1[start:end]) > len(ans):
                    if str1[start:end] * (len(str1)//len(str1[start:end])) == str1 and str1[start:end] * (len(str2)//len(str1[start:end])) == str2:
                        ans = str1[start:end]
            end +=1 
            if end > len(str1):
                start +=1
                end = start +1
            if end == len(str1)+1:
                break
        return ans
