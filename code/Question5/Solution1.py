'''
如果要求只在原字符串进行修改 （意在降低空间复杂度，虽然在python字符串为不可变对象，即扩充字符串也会建立新的字符串对象）、
先统计空格数，然后拓展字符串，最后在逆序遍历原字符串进行替换

'''

class Solution:
    def replaceSpace(self, s: str) -> str:
        space_counts = 0
        length = len(s)
        #统计字符串中有多少个空格
        for i in s:
            if i == ' ':
                space_counts +=1
        #如果原字符串没有空格，返回原字符串
        if space_counts == 0:
            return s
        #拓展字符串，每一个空格都需要拓展两个空间
        for i in range(0,space_counts):
            s += '  '
        new_length = len(s)
        s = list(s)
        #替换字符串
        j = new_length - 1
        for i in range(length-1,-1,-1):
            if s[i] == ' ':
                s[j] = '0'
                s[j-1] = '2'
                s[j-2] = '%'
                j = j - 3
            else:
                s[j] = s[i]
                j = j - 1
        return ''.join(s)