'''
利用逻辑判断终止递归
https://leetcode-cn.com/problems/qiu-12n-lcof/solution/mian-shi-ti-64-qiu-1-2-nluo-ji-fu-duan-lu-qing-xi-/
'''
class Solution:
    def sumNums(self, n: int) -> int:
        def sumTotal(n):
            n > 1 and sumTotal(n-1)
            self.res += n
            return
        self.res = 0
        sumTotal(n)
        return self.res