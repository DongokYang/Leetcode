class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if len(flowerbed)==1:
                if flowerbed[0]==0 :
                    n-=1
                if n > 0 :
                    return False
                else:
                    return True
            if flowerbed[i] ==0:
                if i ==0:
                    if flowerbed[i+1]==0:
                        n-=1
                        flowerbed[i] =1
                elif i ==len(flowerbed)-1:
                    if flowerbed[i-1] ==0:
                        n-=1
                        flowerbed[i] =1 
                else:
                    if flowerbed[i-1] ==0:
                        if flowerbed[i+1]==0:
                            n-=1
                            flowerbed[i] =1
        if n > 0 :
            return False
        else:
            return True