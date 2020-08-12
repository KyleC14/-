'''
参考leetcode题解 https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/solution/mian-shi-ti-14-ii-jian-sheng-zi-iitan-xin-er-fen-f/
循环求余
'''
class Solution:
    def cuttingRope(self,n: int) -> int:
        #长度小于等于3时直接返回结果
        if n<=3:
            return n-1
        #故意留一位
        a = n//3-1
        #余数
        b = n % 3
        # 取模
        p = 1000000007
        #起始数
        x = 3
        #结果
        rem = 1
        for _ in range(a):
            rem = (rem*x)%p
        if b == 0:
            return (rem*3)%p # = 3^(a+1)%p
        elif b == 1:
            return (rem*4)%p # = 3^a*4%p
        elif b == 2:
            return (rem*3*2)%p # = 3^(a+1)*2%p