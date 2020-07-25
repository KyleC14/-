#先从右上角开始，排除列，然后从行开始，排除行，逐步缩小范围，最后目标数会出现在区域右上角

class Solution2:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        # 检查空数组
        rows = len(matrix)
        if rows == 0:
            return False
        columns = len(matrix[0])
        if columns == 0:
            return False
        rows = 0
        columns -= 1
        while rows <len(matrix) and columns >=0:
            if matrix[rows][columns] == target:
                return True
            elif matrix[rows][columns] > target:
                columns -=1
            else:
                rows += 1
        return False