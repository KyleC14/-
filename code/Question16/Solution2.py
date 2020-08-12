'''
非递归
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        #特殊情况
        if x == 0:
            return x
        result = 1
        if n<0:
            x,n = 1/x,-n
        while n:
            #奇偶判断
            if n&1:
                result *= x
            x *= x
            n >>= 1
        return result