class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        
        zeros_list = [0 for _ in range(num_people)]

        temp = 0
        i = 0
        while candies !=0:
            temp +=1 

            if temp >= candies:
                temp = candies
            
            zeros_list[i] += temp
            candies -= temp
            i += 1
            if i == num_people:
                i =0
        return zeros_list

