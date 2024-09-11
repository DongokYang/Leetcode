class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        potions.sort()
        ans = [0 for i in range(len(spells))]

        for i in range(len(spells)):
            start = 0
            last = len(potions)

            while start < last:
                mid =(start +last)//2
                if spells[i] * potions[mid] < success:
                    start = mid +1

                elif spells[i] * potions[mid] >= success:
                    last = mid
            
            ans[i] = len(potions)- start

        return ans