'''
遍历数组，找到第一个符合字符串的元素位置，在该位置使用深度优先方便检索矩阵中是否存在字符串路径
'''

class Solution:
    def __init__(self):
        #依次对应上下左右
        self.option = [[-1,0],
                       [0,1],
                       [1,0],
                       [0,-1]]
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i,j,k):
            tmp = board[i][j]
            if board[i][j] == word[k]:
                k+=1
                board[i][j] = -1
            else:
                return False
            if k == len(word):
                return True
            for h in range(0,4):
                ti = i+self.option[h][0]
                tj = j+self.option[h][1]
                if ti>=0 and  ti<len(board) and tj>=0 and tj <len(board[0]) and board[ti][tj] != -1:
                    if dfs(ti,tj,k):
                        return True
            board[i][j] = tmp
            return False

        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                k = 0
                if board[i][j] == word[0]:
                    if dfs(i,j,k):
                        return True
        return False