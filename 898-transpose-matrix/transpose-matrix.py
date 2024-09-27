class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        nm = [[0 for i in range(len(matrix))]for i in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for ii in range(len(matrix[0])):
                nm[ii][i] = matrix[i][ii]

        return nm        