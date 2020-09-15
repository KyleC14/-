'''
遍历替代
https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/solution/mian-shi-ti-58-ii-zuo-xuan-zhuan-zi-fu-chuan-qie-p/
'''
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = []
        for i in range(n,len(s)):
            res.append(s[i])
        for i in range(n):
            res.append(s[i])
        return ''.join(res)
'''
取余简化代码
'''
class Solution2:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = []
        for i in range(n,n+len(s)):
            res.append(s[i%len(s)])
        return ''.join(res)