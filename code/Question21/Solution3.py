'''
双指针，一头一尾。头指针寻找偶数，尾指针找奇数，二者交换。
'''
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        start,end = 0,len(nums)-1
        while start < end:
            if nums[start] %2 ==0 and nums[end]%2 ==1:
                nums[start],nums[end] = nums[end],nums[start]
                start+=1
                end-=1
            elif nums[start]%2==1 and nums[end]%2==1:
                start+=1
            elif nums[start]%2==0 and nums[end]%2==0:
                end-=1
            else:
                start+=1
                end-=1
        return nums
'''
优化后写法
'''
class Solution2:
    def exchange(self, nums: List[int]) -> List[int]:
        start, end = 0, len(nums) - 1
        while start < end:
            while start<end and  nums[start]%2 == 1:
                start+=1
            while start<end and nums[end]%2 == 0:
                end-=1
            nums[start],nums[end]=nums[end],nums[start]
        return nums