class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = 2
        sm = 0
        cost.insert(0,0)
        cost.append(0)
        lst = [cost[0],cost[1]]
        while n < len(cost):
            lst.append(min(lst[n-1] + cost[n],cost[n]+ lst[n-2]))
            n +=1

        return lst[-1]

