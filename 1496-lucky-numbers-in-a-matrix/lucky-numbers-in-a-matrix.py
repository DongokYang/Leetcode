class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        rLst = []
        Lst = []

        for i in range(len(matrix)):
            rLst.append(min(matrix[i]))
        for i in range(len(matrix[0])):
            Lst.append(max(transposed[i]))

        nnl = []
        for i in rLst:
            if i in Lst:
                nnl.append(i)
                return nnl