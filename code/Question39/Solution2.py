'''
进行排序 排序完后的中位数就是结果
leetcode 超时
'''
class Solution3:
    def majorityElement(self, nums: List[int]) -> int:
        #冒泡排序会超时
        def bubbleSort(nums):
            for i in range(len(nums)-1):
                for j in range(len(nums)-i-1):
                    if nums[j]>nums[j+1]:
                        nums[j+1],nums[j] = nums[j],nums[j+1]
            return nums
        #快排也会超时
        def quicksort(i,j):
            if i>j:
                return
            target = nums[i]
            left,right = i,j
            while i!=j:
                while nums[j]>=target and i<j:
                    j -=1
                while nums[i]<=target and i<j:
                    i +=1
                if i<j:
                    nums[j],nums[i]=nums[i],nums[j]
            nums[left],nums[j]= nums[j],nums[left]
            quicksort(left,j-1)
            quicksort(j+1,right)
            return
        if not nums:
            return nums
        # nums = bubbleSort(nums)
        quicksort(0,len(nums)-1)
        mid = len(nums)//2
        return nums[mid]
