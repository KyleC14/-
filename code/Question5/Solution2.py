'''
创建一个新列表，遍历原字符串，遇到空格则替换
'''

class Solution:
    def replaceSpace(self, s: str) -> str:
        replace_list = []
        for i in s:
            if i == ' ':
                replace_list.append("%20")
            else:
                replace_list.append(i)
        replace_str = ''.join(replace_list)
        return  replace_str