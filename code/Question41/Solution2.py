'''
二分查找插入
'''
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data_stack = []
    def binInsert(self,num):
        low,high = 0,len(self.data_stack)-1
        while low!=high:
            mid  = low+(high-low)//2
            if self.data_stack[mid] == num:
                return mid
            elif self.data_stack[mid]>num:
                high = mid #要注意边界
            else:
                low = mid+1 #要注意边界
        return low
    def addNum(self, num: int) -> None:
        if not self.data_stack or num>=self.data_stack[-1]:
            self.data_stack.append(num)
        elif num<=self.data_stack[0]:
            self.data_stack = [num]+self.data_stack
            return
        else:
            #二分查找插入
            index = self.binInsert(num)
            self.data_stack = self.data_stack[:index]+[num]+self.data_stack[index:]
            return
    def findMedian(self) -> float:
        mid = len(self.data_stack)//2
        if len(self.data_stack)%2==1:
            return self.data_stack[mid]
        else:
            return (self.data_stack[mid]+self.data_stack[mid-1])/2.0

'''
二分查找插入的库函数
参考
https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/solution/you-xian-dui-lie-by-z1m/
'''
import bisect
class MedianFinder2:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.store = []

    def addNum(self, num: int) -> None:
        if not self.store:
            self.store.append(num)
        else:
            bisect.insort_left(self.store, num) # 插入

    def findMedian(self) -> float:
        n = len(self.store)
        if n & 1 == 1:  # n是奇数
            return self.store[n // 2]
        else:
            return (self.store[n // 2] + self.store[n // 2 - 1]) / 2