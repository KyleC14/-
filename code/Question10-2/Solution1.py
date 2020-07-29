'''
本质还是斐波那契数列问题
分析青蛙最后一步，只有两种可能：
1. 剩一步台阶
2. 剩两步台阶

剩一步台阶的跳法为f(n-1)
剩两步台阶的跳法为f(n-2)
所以n阶台阶的跳法f(n) = f(n-1)+f(n-2)
这里f(0)=1 f(1)=1

'''

class Solution:
    def numWays(self, n: int) -> int:
        fzero = 1
        fone = 1
        for i in range(n):
            fzero, fone = fone,fone+fzero
        return fzero%1000000007