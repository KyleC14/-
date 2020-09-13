'''
削尖端法
https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/san-chong-fang-fa-cong-jian-dao-fan-zai-dao-jian-b/
如果两个连续的数之和为 target，这两个数相差为 11，也就是说将较大的那个数减一，就是两个相等的数之和为 target - 1。这个数就是 (target - 1)/2，只要保证能整除，就是我们需要的解。
进一步讲，如果三个连续的数和为 target，则将中间那个数减一，最后那个数减二，就是三个相等的数之和为 target - 1 - 2。这个数就是 (target - 1 - 2)/3，只要保证能整除，就是我们需要的解。
'''
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        n = 2
        target -= 1
        while target>0:
            if target%n == 0:
                start = target/n
                res.append(list(range(start,start+n)))
            target -= n
            n += 1
        res = res[::-1]
        return res