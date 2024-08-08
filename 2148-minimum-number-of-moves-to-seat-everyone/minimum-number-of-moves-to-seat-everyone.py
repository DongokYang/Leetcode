class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)

        rst = 0

        for i in range(len(seats)):
            rst += abs(seats[i] - students[i])
        
        return rst


