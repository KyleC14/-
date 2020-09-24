'''
从右上角或者左下角开始的路径搜索 因为只有这两个角的可选路径方向 其实Solution2那种解法本质是从右上角开始走 
https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/solution/3chong-jie-jue-fang-shi-hou-liang-chong-du-ji-bai-/
这是左下角
'''


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
