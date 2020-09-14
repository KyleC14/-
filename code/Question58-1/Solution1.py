'''
调用库函数
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        # s = s.strip() # 删除首尾空格
        strs = s.split() # 分割字符串 可以不要第一句 split()会把首尾空格去掉 中间的空格无论多少个也会去掉
        strs.reverse() # 翻转单词列表
        return ' '.join(strs) # 拼接为字符串并返回