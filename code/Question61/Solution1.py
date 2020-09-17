'''
先进行排序 是整个序列有序
统计有多少个0
遍历数组 抵消0 如果0的数目不够用返回False 如果遇到两个连续相同的数返回False
'''
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        #快排 (手撸快排总是写错 多写写)
        def quicksort(head,end):
            if head>end:
                return
            left,right = head,end
            target = nums[left]
            while head!=end: # while head<end
                while nums[end]>=target and head<end:
                    end-=1
                while nums[head]<=target and head<end:
                    head+=1
                if head<end:
                    nums[head],nums[end] = nums[end],nums[head]
            nums[left],nums[head] = nums[head],nums[left]
            quicksort(left,head-1)
            quicksort(head+1,right)
            return
        #数组排序
        quicksort(0,len(nums)-1)
        #统计有多少个0
        zero_count = nums.count(0)
        for i in range(len(nums)-1):
            if nums[i]!=0:
                gap = nums[i+1]-nums[i]-1
                #如果有两个连续相同的数 直接返回False
                if gap == -1:
                    return False
                zero_count-=gap
                #当0的数量不够用时 直接返回False
                if zero_count<0:
                    return False
        return True