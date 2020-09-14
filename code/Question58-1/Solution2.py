'''
栈 这种方法不用处理首尾和中间多余的字符
'''
class Solution2:
    def reverseWords(self, s: str) -> str:
        res = []
        stackA,stackB = [],[]
        #先把字符全部入栈
        for i in s:
            stackA.append(i)
        while stackA:
            #弹出单词
            while stackA and stackA[-1] != " ":
                cha = stackA.pop()
                stackB.append(cha)
            #单词逆序并且记录
            if stackB:
                stackB.reverse()# stackB = stackB[::-1]
                res.append("".join(stackB))
                stackB.clear() # stackB = []
            #跳过空格
            while stackA and stackA[-1] == " ":
                stackA.pop()
        return " ".join(res)