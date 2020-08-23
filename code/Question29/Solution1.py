'''
依靠右，下，左，上的次序依次遍历矩阵
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return matrix
        row_boundary = len(matrix)
        column_boundary = len(matrix[0])
        trace = [[True] * column_boundary for _ in range(row_boundary)]
        option = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        k = 0
        result = []
        i = j = 0
        result.append(matrix[i][j])
        trace[i][j] = False
        while True:
            if 0<=i+option[k][0]<row_boundary and 0<=j+option[k][1]<column_boundary and trace[i+option[k][0]][j+option[k][1]] == True:
                i = i+option[k][0]
                j = j+option[k][1]
                result.append(matrix[i][j])
                trace[i][j] = False
            else:
                if k != 3:
                    k +=1
                else:
                    k = 0
                i = i + option[k][0]
                j = j + option[k][1]
                if i<0 or i>row_boundary-1 or j<0 or j>column_boundary or trace[i][j] == False:
                    break
                result.append(matrix[i][j])
                trace[i][j] = False
        return result