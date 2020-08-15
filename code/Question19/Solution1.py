'''
递归做法 参考https://leetcode-cn.com/problems/regular-expression-matching/solution/zheng-ze-biao-da-shi-pi-pei-dong-tai-gui-hua-by-jy/
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #p到结尾时，如果s也到结尾则为true
        if not p:
            return not s
        if len(p) > 1 and p[1] == '*':
            if s and (s[0] == p[0] or p[0] == '.'):
                #这里实际有三种状态(s+1,p+2),(s,p+2),(s+1,p) 但是实际上第一种状态已经包含在第三种状态中
                #对应匹配一次，匹配0次，匹配多次
                return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p)
            return self.isMatch(s, p[2:])

        if s and (s[0] == p[0] or p[0] == '.'):
            return self.isMatch(s[1:], p[1:])
        return False