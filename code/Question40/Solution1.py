'''
进行排序 取前k个数
'''
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        #快排
        def quicksort(i,j):
            if i>j:
                return
            left,right = i,j
            target = arr[left]
            while i!=j:
                while arr[j]>=target and i<j:
                    j-=1
                while arr[i]<=target and i<j:
                    i+=1
                if i<j:
                    arr[i],arr[j] = arr[j],arr[i]
            arr[left],arr[i] = arr[i],arr[left]
            quicksort(left,i-1)
            quicksort(i+1,right)
            return
        if not arr or k>len(arr):
            return None
        quicksort(0,len(arr)-1)
        return arr[:k]