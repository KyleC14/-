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
        self.stack01 = []
        self.stack02 = []

    def appendTail(self, value: int) -> None:
        self.stack01.append(value)

    def deleteHead(self) -> int:
        if len(self.stack02) != 0:
            return self.stack02.pop()
        elif len(self.stack01) != 0:
            while len(self.stack01)!=0:
                self.stack02.append(self.stack01.pop())
            return self.stack02.pop()
        else:
            return -1