class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a = 0
        b = 1
        profit = 0

        while len(prices) > b:
            if prices[b] > prices[a]:
                profit += prices[b] - prices[a]
                a = b
                b = a+1
            else:
                a+=1
                b+=1
        return profit