class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        RL = 0
        UD = 0
        moves = list(moves)
        for i in moves:
            if i =="R":
                RL +=1
            elif i =="L":
                RL -=1
            elif i =="U":
                UD +=1
            elif i =="D":
                UD -=1

        if RL ==0 and UD ==0:
            return True
        else :
            return False
