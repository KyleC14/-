'''
滑动窗口思路
如果遇到新字符，窗口增加字符，更新最大长度
如果遇到已存在字符，对窗口从已存在字符处进行切片，再增加字符，同时不用更新最大长度，因为窗口长度不可能超过上一个窗口长度
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = []
        max_length = 0
        for i in s:
            if i not in res:
                res.append(i)
                max_length = max(len(res), max_length)
            else:
                index = res.index(i)
                res = res[index+1:]
                res.append(i)
        return max_length