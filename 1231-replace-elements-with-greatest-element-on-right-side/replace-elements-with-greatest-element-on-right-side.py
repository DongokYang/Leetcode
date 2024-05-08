class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr.reverse()

        na = []
        temp= -1

        na.insert(1,temp)
        for i in range(len(arr)):
            print(temp,arr[i])
            if temp < arr[i]:
                temp = arr[i]
            na.insert(0,temp)
        na.pop(0)
        return na