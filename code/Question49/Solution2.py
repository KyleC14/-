'''
一个丑数必然也是由别的丑数乘以2,3,5得到的 还要确保小根堆里没有重复的丑数
利用小根堆 每次弹出最小的丑数 当弹出数等于n时结束
'''
import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        zys = [2,3,5]
        result = []
        heapq.heappush(result,1)
        count = 0
        while result:
            num = heapq.heappop(result)
            count += 1
            if count == n:
                return num
            for i in zys:
                if i*num not in result:
                    heapq.heappush(result,i*num)
        return