'''
对每个数的每一位统计是否为1 效率低
leetcode超时
'''
class Solution:
    def checkOne(self,num):
        count = 0
        while num:
            mod = num%10
            if mod == 1:
                count+=1
            num = num//10
        return count
        return
    def countDigitOne(self, n: int) -> int:
        count = 0
        for i in range(1,n+1):
            count+=self.checkOne(i)
        return count