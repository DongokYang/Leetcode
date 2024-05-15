class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        ans = []
        for i in range(1,area+1):
            if area%i ==0:
                if i >= area/i:
                    return [i,int(area/i)]
        
        return [ans]

