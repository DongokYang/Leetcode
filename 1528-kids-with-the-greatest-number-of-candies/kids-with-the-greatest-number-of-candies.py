class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ansList = []
        maxValue = max(candies)
        for i in candies:
            if i+extraCandies >= maxValue:
                ansList.append(True)
            else:
                ansList.append(False)
        return ansList