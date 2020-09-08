'''
直接用二分查找找到目标数，然后双向统计数量
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #二分查找
        def binarySearch(start,end,target):
            #如果这里用!= 在搜索最左边元素时 由于end=mid-1 会出现end<start但是循环不会停止的情况
            while start<=end:
                mid = start + (end - start) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid]>target:
                    end = mid - 1
                else:
                    start = mid + 1
            return None

        count = 0
        if not nums:
            return count
        #二分查找获取目标数字序列 如果为空则代表不存在
        index = binarySearch(0,len(nums)-1,target)
        #如果存在 双向查找 因为如果有重复数不确定左边或者右边有没有同样的数
        if index is not None:
            count += 1
            for i in range(index+1,len(nums)):
                if nums[i] == target:
                    count+=1
                else:break
            for i in range(index-1,-1,-1):
                if nums[i] == target:
                    count+=1
                else:break
        return count
'''
二分法优化
用二分法搜索目标数应该插入的位置，以及 目标数-1 应该插入的位置，二者取差值则是目标数的数量
二分法搜索应该插入目标的位置 数量=right-left
https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/solution/mian-shi-ti-53-i-zai-pai-xu-shu-zu-zhong-cha-zha-5/
'''
class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        #本质是二分查找到目标数插入的位置
        def binarySearchBoundary(target):
            i,j = 0,len(nums)-1
            while i <= j:
                mid = i+(j-i)//2
                if nums[mid] <= target:
                    i = mid + 1
                else:
                    j = mid - 1
            return i
        return binarySearchBoundary(target)-binarySearchBoundary(target-1)