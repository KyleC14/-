'''
动态规划：
原理： 以斐波那契数列性质 f(n + 1) = f(n) + f(n - 1)f(n+1)=f(n)+f(n−1) 为转移方程。
'''

class Solution:
    def __init__(self):
        self.fzero = 0
        self.fone = 1
    def fib(self, n: int) -> int:
        if n == 0:
            return self.fzero
        elif n == 1:
            return self.fone
        else:
            a = self.fzero
            b = self.fone
            for i in range(1,n):
                a,b = b,a+b
            return b % 1000000007
        #优化写法
        # a = self.fzero
        # b = self.fone
        # for i in range(n):
        #     a, b = b, a + b
        # return a % 1000000007