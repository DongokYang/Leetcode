class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        count = 0
        for i in range(8):
            for ii in range(8):
                if board[i][ii] =='R':
                    a = i 
                    b = ii

        for i in range(a+1,8):
            if board[i][b] == 'B':
                break
            elif board[i][b] == 'p':
                count +=1
                break
        for i in range(a-1,-1,-1):
            if board[i][b] == 'B':
                break
            elif board[i][b] == 'p':
                count +=1
                break


        for i in range(b+1,8):
            if board[a][i] == 'B':
                break
            elif board[a][i] == 'p':
                count +=1
                break
        for i in range(b-1,-1,-1):
            if board[a][i] == 'B':
                break
            elif board[a][i] == 'p':
                count +=1
                break
        return count
        