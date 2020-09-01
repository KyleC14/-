'''
大小堆 运用大小顶堆时数组保持有序，长度为奇数时为小顶堆堆顶元素，长度为偶数时为两堆顶和的平均值
https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/solution/mian-shi-ti-41-shu-ju-liu-zhong-de-zhong-wei-shu-y/
'''
import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A =[] #小顶堆 最小在堆顶 存储较大的部分 长度为奇数时小顶堆比大顶堆多一个数
        self.B =[] #大顶堆 最大在堆顶 借由负数实现 存储较小的部分
    def addNum(self, num: int) -> None:
        if len(self.A) != len(self.B):
            heapq.heappush(self.B,-heapq.heappushpop(self.A,num))
        else:
            heapq.heappush(self.A,-heapq.heappushpop(self.B,-num))
    def findMedian(self) -> float:
        if len(self.A) == len(self.B):
            return (self.A[0]-self.B[0])/2.0
        else:
            return self.A[0]