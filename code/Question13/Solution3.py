'''
广度优先 BFS
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
        q = Queue()
        q.put((0,0))
        while not q.empty():
            x,y = q.get()
            if x<m and y<n and (x,y) not in self.track and addSum(x)+addSum(y)<=k:
                self.track.add((x,y))
                #本题实际只需检查右、下两个方向
                for ti,tj in [(x+1,y),(x,y+1)]:
                    q.put((ti,tj))
        return len(self.track)