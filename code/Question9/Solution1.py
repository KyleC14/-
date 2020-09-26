'''
使用两个栈，一个实现进，一个实现出。进的时候使用一个栈，删除队首的时候使用另外一个栈。
另外一个栈的作用是对第一个栈的元素进行逆序。删除的时候只需要弹出第二个栈的元素便实现删除队首的功能。
有三种情况：
1.第二个栈非空，这个时候删除队首直接弹出第二个栈的元素即可
2.第二个栈为空，第一个栈非空，这个时候使用第二个栈对第一个栈的元素进行逆序，然后弹出第二个栈的元素即可
3.两个栈都为空，没有元素，返回-1
'''

class CQueue:

    def __init__(self):
        #数据栈
        self.data = []
        #存储头部元素的辅助栈
        self.helper = []

    def appendTail(self, value: int) -> None:
        self.data.append(value)


    def deleteHead(self) -> int:
        #如果辅助栈非空 直接弹出辅助栈顶元素
        if self.helper:
            return self.helper.pop()
        #如果辅助栈为空 数据栈非空 对数据栈已有元素逆序输出至辅助栈 弹出辅助栈栈顶元素
        elif self.data:
            while self.data:
                self.helper.append(self.data.pop())
            return self.helper.pop()
        else:#两个栈都是空的 不存在元素 返回-1
            return -1