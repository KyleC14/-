'''
最多O(m+n)次
https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/solution/mian-shi-ti-04-er-wei-shu-zu-zhong-de-cha-zhao-zuo/
'''


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