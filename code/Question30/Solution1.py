'''
一个常规列表存储元素
一个辅助列表存储最小元素 辅助列表栈顶的元素必为最小元素，每次压栈都要与辅助列表栈顶元素比较 小于等于时入栈
常规弹出元素时如果等于辅助列表的栈顶 则辅助列表也弹出
可参考剑指offer书本或leetcode题解
'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []
        self.minlist = []

    def push(self, x: int) -> None:
        self.list.append(x)
        if not self.minlist() or self.minlist[-1]>=x:
            self.minlist.append(x)

    def pop(self) -> None:
        if self.list.pop() == self.minlist[-1]:
            self.minlist.pop()

    def top(self) -> int:
        return self.list[-1]

    def min(self) -> int:
        return self.minlist[-1]