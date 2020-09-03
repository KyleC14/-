'''
字符串拼接规则
nm>mn 则 n>m (别问怎么证明，问就是不知道) 
https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/solution/mian-shi-ti-45-ba-shu-zu-pai-cheng-zui-xiao-de-s-4/
利用规则进行排序 这里仅列举冒泡和快排
'''
class Solution:
    # 冒泡排序
    def bubbleOrder(self,nums_str):
        for i in range(len(nums_str)):
            for j in range(len(nums_str)-i-1):
                if nums_str[j]+nums_str[j+1]>nums_str[j+1]+nums_str[j]:
                    nums_str[j],nums_str[j+1] = nums_str[j+1],nums_str[j]
        return
    # 快排
    def quicksort(self,nums_str,i,j):
        if i>j:
            return
        left,right = i,j
        target = nums_str[left]
        while i!=j:
            while nums_str[j]+target>=target+nums_str[j] and i<j:
                j-=1
            while nums_str[i]+target<=target+nums_str[i] and i<j:
                i+=1
            if i<j:
                nums_str[i],nums_str[j] = nums_str[j],nums_str[i]
        nums_str[left],nums_str[j] = nums_str[j],nums_str[left]
        self.quicksort(nums_str,left,j-1)
        self.quicksort(nums_str,j+1,right)
        return
    def minNumber(self, nums: List[int]) -> str:
        nums_str = [str(nums) for nums in nums]
        # 冒泡
        # self.bubbleOrder(nums_str)
        # 快排
        self.quicksort(nums_str,0,len(nums_str)-1)
        return ''.join(nums_str)