'''
思路3运用数学原理进行推断得出公式，实际也可通过寻找规律或者贪心思想得出公式。详情见引用的链接思路
数学解法 参考
https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/mian-shi-ti-14-i-jian-sheng-zi-tan-xin-si-xiang-by/
Python 中常见有三种幂计算函数： * 和 pow() 的时间复杂度均为 O(\log a)O(loga) ；
而 math.pow() 始终调用 C 库的 pow() 函数，其执行浮点取幂，时间复杂度为 O(1)。

'''
import math
class Solution3:
    def cuttingRope(self, n: int) -> int:
        #直接包含两种特殊情况
        if n<=3:
            return n-1
        a,b = n//3,n%3
        if b == 0:
            return int(math.pow(3,a))
        elif b == 1:
            return int(math.pow(3,a-1)*4)
        elif b == 2:
            return int(math.pow(3,a)*2)