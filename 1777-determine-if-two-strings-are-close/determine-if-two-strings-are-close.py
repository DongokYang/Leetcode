class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        arr = sorted(word1)
        temp = arr[0]

        ans = []
        arr.append(-100000)

        cnt = -1
        for i in range(0,len(arr)):
            cnt +=1
            if arr[i] != temp:
                ans.append(cnt)
                cnt = 0
                temp = arr[i]

        arr = sorted(word2)
        temp = arr[0]
        arr.append(-100000)
        ans2 = []
        cnt = -1

        for i in range(0,len(arr)):
            cnt +=1
            if arr[i] != temp:
                ans2.append(cnt)
                cnt = 0
                temp = arr[i]
        
        cc = [[],[]]

        cc[0].append(set(list(word1)))
        cc[1].append(set(list(word2)))

        if sorted(ans) ==sorted(ans2):
            if cc[0] ==cc[1]:
                return True
       
        return False