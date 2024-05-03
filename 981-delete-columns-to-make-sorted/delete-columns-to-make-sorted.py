class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        count = 0
        for i in range(m):
            temp = 0 
            flag = 0 
            for ii in range(n):
                if temp > ord(strs[ii][i]):
                    flag = 1
                temp = ord(strs[ii][i])
            if flag ==1:
                count +=1

        return count