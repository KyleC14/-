'''
利用快排的思想 不必进行完全排序 而是当基数交换为第k个数时 直接返回
'''
class Solution3:
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
            if i == k:
                return
            elif i<k:
                quicksort(i + 1, right)
            elif i>k:
                quicksort(left, i - 1)
            return
        if not arr or k>len(arr):
            return None
        quicksort(0,len(arr)-1)
        return arr[:k]