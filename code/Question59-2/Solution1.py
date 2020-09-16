'''
详细解析见
https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/solution/mian-shi-ti-59-ii-dui-lie-de-zui-da-zhi-by-leetcod/
插入操作虽然看起来有循环，做一个插入操作时最多可能会有 n 次出队操作。但要注意，由于每个数字只会出队一次，因此对于所有的 n 个数字的插入过程，对应的所有出队操作也不会大于 n 次。因此将出队的时间均摊到每个插入操作上，时间复杂度为 O(1)。
'''
class MaxQueue:

    def __init__(self):
        #数据队列
        self.data = deque()
        #辅助队列
        self.maxQ = deque()

    def max_value(self) -> int:
        if not self.data:
            return -1
        #辅助队列头部保存着最大值
        return self.maxQ[0]

    def push_back(self, value: int) -> None:
        self.data.append(value)
        #如果当前入队列数比辅助队尾大，弹出辅助队尾 保证辅助队列有序递减
        while self.maxQ and value > self.maxQ[-1]:
            self.maxQ.pop()
        self.maxQ.append(value)
    def pop_front(self) -> int:
        if not self.data:
            return -1
        num = self.data.popleft()
        #如果弹出的数是当前的最大数，则同步弹当前的最大数
        if num == self.maxQ[0]:
            self.maxQ.popleft()
        return num