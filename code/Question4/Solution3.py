#路径搜索。应该从右上角或者左下角开始。
#应为左上角的下与右都是递增的，有两条路径。同理右下角，两条路径都是递减的。
#（左下角开始）


class Solution3:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        # 检查空数组
        rows = len(matrix)
        if rows == 0:
            return False
        columns = len(matrix[0])
        if columns == 0:
            return False
        rows_boundary = rows - 1
        columns_boundary = columns - 1
        rows = rows - 1
        columns = 0
        while rows >= 0 and columns <= columns_boundary:
            if matrix[rows][columns] == target:
                return  True
            elif matrix[rows][columns] < target:
                columns += 1
            else:
                rows -= 1
        return False
