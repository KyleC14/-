'''
暴力循环 超时 414 / 596 
'''
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        #判断一个数是否是丑数
        def isUgly(n):
            while n%2==0:
                n = n//2
            while n%3==0:
                n = n//3
            while n%5==0:
                n = n//5
            return True if n==1 else False
        i = count = 0
        while count<n:
            i += 1
            if isUgly(i):
                count+=1
        return i