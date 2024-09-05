class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        temp = arr[0]
        ans = []
        arr.append(-100000)

        cnt = 0
        for i in range(0,len(arr)):
            cnt +=1

            if arr[i] != temp:
                ans.append(cnt)
                cnt = 1
                temp = arr[i]
        
        if len(ans) == len(set(ans)):
            return True
        else:
            return False