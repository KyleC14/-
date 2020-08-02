'''
深度优先 DFS
'''


class Solution:
    def __init__(self):
        self.track = set()
        #本题实际上只需要检查右、下两个方向
        self.option = [
                       [0,1],
                       [1,0],
                       ]
    def movingCount(self, m: int, n: int, k: int) -> int:
        def addSum(num):
            re = 0
            if num==0:
                return 0
            while num!=0:
                re += num%10
                num=num//10
            return re
        def dfs(i,j,k):
            if 0<=i<m and 0<=j<n and (i,j) not in self.track and addSum(i)+addSum(j)<=k:
                self.track.add((i,j))
                for h in range(0,2):
                    ti = i+self.option[h][0]
                    tj = j+self.option[h][1]
                    dfs(ti,tj,k)
            return
        dfs(0,0,k)
        return len(self.track)