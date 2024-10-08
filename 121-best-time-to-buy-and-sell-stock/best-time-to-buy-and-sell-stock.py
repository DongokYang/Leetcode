class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i , j = prices[0] , 0 
        profit = 0

        while j < len(prices):
            if i > prices[j]:
                i = prices[j]

            if prices[j] - i > profit:
                profit = prices[j] - i
            j+=1

        return profit

            