'''
逆序对是归并排序的副产物
https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/jian-dan-yi-dong-gui-bing-pai-xu-python-by-azl3979/
'''
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        #统计逆序对次数
        self.count = 0
        def merge(start,end,mid,temp):
            i,j = start,mid+1
            while i <= mid and j <= end:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    #当左边头数比右边头数大时，存在逆序对，同时包括左边头数到左边序列尾部这么多个逆序对（序列是有序的）
                    #也不会存在重复计数 因为只有两个序列在进行对比时才统计逆序对，当一次归并完成就成为一个序列了
                    self.count += mid-i+1
                    j += 1
            while i <= mid:
                temp.append(nums[i])
                i+=1
            while j <= end:
                temp.append(nums[j])
                j+=1
            for i in range(len(temp)):
                nums[start+i] = temp[i]
            temp.clear()
            return
        #精髓 递归至每个数为一组时开始 归并
        def mergeSort(start,end,temp):
            if start >= end:
                return
            mid = start + (end-start)//2
            mergeSort(start,mid,temp)
            mergeSort(mid+1,end,temp)
            merge(start,end,mid,temp)
            return
        mergeSort(0,len(nums)-1,[])
        return self.count