'''
参考leetcode题解 https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/solution/mian-shi-ti-14-ii-jian-sheng-zi-iitan-xin-er-fen-f/
快速幂求余
'''
class Solution:
    def cuttingRope(self,n:int)->int:
        if n<=3:
            return n-1
        a = n//3-1
        b = n%3
        x = 3
        p = 1000000007
        rem = 1
        while a>0:
            #当a为奇数的时候
            if a % 2 :
                rem = (rem*x)%p
            x = x**2%p
            a = a//2
        if b == 0:
            return (rem*3)%p
        elif b == 1:
            return (rem*4)%p
        elif b == 2:
            return (rem*6)%p