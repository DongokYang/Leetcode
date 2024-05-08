class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        temp = arr1.copy()
        na = []
        for i in arr2:
            for ii in arr1:
                if i == ii:
                    na.append(i)
                    temp.remove(i)
        temp = sorted(temp)
        return (na+temp)