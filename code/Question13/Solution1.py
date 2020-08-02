'''
遍历所有格子，检查其上一个格子或者左边一个格子是否符合条件，以及当前格子是否符合条件 运用递推的思路
'''


class Solution:
    def __init__(self):
        self.track = set()
    def movingCount(self, m: int, n: int, k: int) -> int:
        def addSum(num):
            re = 0
            if num==0:
                return re
            while num!=0:
                re+= num%10
                num=num//10
            return re
        self.track.add((0,0))
        for i in range(m):
            for j in range(n):
                if ((i-1,j) in self.track or (i,j-1) in self.track) and addSum(i)+addSum(j)<=k:
                    self.track.add((i,j))
        return len(self.track)