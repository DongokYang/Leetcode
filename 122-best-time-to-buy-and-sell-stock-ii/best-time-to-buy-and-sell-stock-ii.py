class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total= 0

        i = 0
        j = 1
        
        while len(prices) > j:
            if prices[j] - prices[i] > 0:
                total += prices[j] - prices[i]
                i = j
                j = i+1   

            elif prices[i] >= prices[j]:
                i = j
                j = i+1    
            else:
                j +=1
                
        return total