class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        new_arr = []
        for i in arr:
            if i not in new_arr:
                new_arr.append(i)
        frequency_arr = [0 for i in range(len(new_arr))]

        for i in range(len(new_arr)):
            for ii in range(len(arr)):
                if new_arr[i] == arr[ii]:
                    frequency_arr[i] +=1

        fnl_list = []
        for i in range(len(new_arr)):
            if frequency_arr[i] ==1:
                fnl_list.append(new_arr[i])
        if k >len(fnl_list):
            return ""
        else:
            return fnl_list[k-1]            
