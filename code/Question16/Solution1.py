'''
递归做法 要求x**a 先求x**a//2
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        #递归终止
        if n == 0:
            return 1.0
        elif n<0:
            x = 1 / x
            n = -n
        #result 为 x**n/2
        result = self.myPow(x,n>>1)
        result*=result
        #判断奇偶，奇数二进制最后一位总是为1
        if n&1:
            result*=x
        return result