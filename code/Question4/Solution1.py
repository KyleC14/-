#总体是逐行遍历

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        #检查空数组
        rows = len(matrix)
        if rows == 0:
            return False
        columns = len(matrix[0])
        if columns == 0:
            return False
        #查看大致范围
        start = matrix[0][0]
        end = matrix[rows-1][columns-1]
        if target < start or target>end:
            return False
        else:
        #逐行搜寻
            for i in range(0,rows):
                    if target>= matrix[i][0] and target <= matrix[i][columns-1]:
                        for j in range(0,columns):
                            if target == matrix[i][j]:
                                return True
            return False
