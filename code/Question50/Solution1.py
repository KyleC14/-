'''
切片检测当前字符的前后是否存在同样的字符
效率非常低
'''
class Solution:
    def firstUniqChar(self, s: str) -> str:
        s = list(s)
        re = ' '
        for i in range(len(s)):
            if s[i] not in s[:i] and s[i] not in s[i+1:]:
                re = s[i]
                break
        return re