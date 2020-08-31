'''
用堆的思想 python里为最小堆
参考 https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/solution/zui-xiao-de-kge-shu-by-leetcode-solution/
https://blog.csdn.net/u013206202/article/details/78968438?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.edu_weight&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.edu_weight
'''
import heapq
class Solution2:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        #因为python为最小堆 因此需要取负数来控制最小的前k个数
        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in arr[k:]:
            if -hp[0]>i:
                heapq.heappop(hp)
                heapq.heappush(hp,-i)
        result  = [-i for i in hp]
        return result