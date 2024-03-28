class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings)==1:
            return 1

        nl = [1 for i in range(len(ratings))]
        for i in range(1,len(ratings)-1):
            if ratings[i] > ratings[i-1] and nl[i] <= nl[i-1]:
                nl[i] = nl[i-1] +1
        ratings = ratings[::-1]
        nl = nl[::-1]
        for i in range(1,len(ratings)-1):
            if ratings[i] > ratings[i-1] and nl[i] <= nl[i-1] :
                nl[i] = nl[i-1] +1
        if ratings[0] > ratings[1]:
            nl[0] = nl[1]+1
        if ratings[-1] > ratings[-2]:
            nl[-1] = nl[-2]+1

        return sum(nl)
