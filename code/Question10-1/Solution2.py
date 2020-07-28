'''
标准递归 但leetcode会超时
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
            return self.fib(n-1)+self.fib(n-2) % 1000000007