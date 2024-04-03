class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        
        first =0
        second = 1
        third =2

        cnt = 0
        while True:
            if abs(arr[first] -arr[second]) <= a:
                if  abs(arr[second] -arr[third]) <= b:
                    if abs(arr[third] -arr[first]) <= c:
                        cnt +=1 
            third+=1
            if third>len(arr)-1:
                second +=1
                third= second+1
            if second>len(arr)-2:
                first +=1
                second = first+1
                third = second+1
            if first >len(arr)-3:
                break
        return cnt



