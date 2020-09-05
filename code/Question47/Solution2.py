'''
动态规划 f(i,j)代表(i,j)最大礼品价值
f(i,j) = max(f(i-1,j),f(i,j-1))+gift(i,j)
'''
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        maxVal = [[0]*len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                up = left = 0
                if i>0:
                    up = maxVal[i-1][j]
                if j>0:
                    left = maxVal[i][j-1]
                maxVal[i][j] = max(up,left)+grid[i][j]
        return maxVal[-1][-1]
'''
动态规划空间优化版
'''
class Solution2:
    def maxValue(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        # 只存储上一行的值
        maxVal = [0]*len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                up = left = 0
                if i>0:
                    up = maxVal[j]
                if j>0:
                    left = maxVal[j-1]
                maxVal[j] = max(up,left)+grid[i][j]
        return maxVal[-1][-1]