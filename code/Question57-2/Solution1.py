'''
双指针 滑动窗口
至少需要两个数 所以初始数组为[1,2] 也是头指针和尾指针的起点
如果当前数组之和等于目标，加入结果，如小于目标，尾指针加1，若大于，头指针加1
尾指针界限在 (target+1)//2 例如 9 = 5 + x  x不可能大于5
'''
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        init = [1,2]
        while init[-1] <= (target+1)//2:
            if len(init)*(init[0]+init[-1])/2 == target:
                res.append(list(init))
                init.append(init[-1] + 1)
            elif len(init)*(init[0]+init[-1])/2 < target:
                init.append(init[-1]+1)
            else:
                init = init[1:]
        return res
'''
优化一下空间
'''
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        start,end = 1,2
        while end <= (target+1)//2:
            if (end-start+1)*(start+end)/2 == target:
                res.append(list(range(start,end+1)))
                end += 1
            elif (end-start+1)*(start+end)/2 < target:
                end += 1
            else:
                start += 1
        return res