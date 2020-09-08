'''
有序序列就要考虑用二分法
转换成查找第一个值与下标不相同的数
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i,j = 0,len(nums)-1
        while i<=j:
            mid = i+(j-i)//2
            #这里加入mid==0为了考虑数组长度只有1的情况
            if nums[mid]!=mid and (mid == 0 or nums[mid-1] == mid-1) :
                return mid
            elif nums[mid] == mid:
                i = mid+1
            else:
                j = mid-1
        #如果中间没有查找到缺失的数，一定缺失最后一个数
        return i