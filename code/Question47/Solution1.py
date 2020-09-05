'''
DFS 遍历每一条路径 20/61 leetcode超时
'''
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        self.maxVal = 0
        x_limit = len(grid)
        y_limit = len(grid[0])
        self.count = 0
        def move(x,y):
            if x<x_limit and y<y_limit:
                self.count += grid[x][y]
                if x == x_limit-1 and y == y_limit-1:
                    if self.count > self.maxVal:
                        self.maxVal = self.count
                move(x, y+1)
                move(x+1, y)
                self.count -= grid[x][y]
            return
        move(0, 0)
        return self.maxVal