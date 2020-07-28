'''
优化递归 不算重复算过的数 leetcode仍然超时
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
            res = [-1 for i in range(n+1)]
            if res[n] == -1:
                res[n] = self.fib(n-1) + self.fib(n-2)
            return res[n] % 1000000007