'''
两种双指针方法，第一种比较直观，两个指针相差一步，逐步构建
第二种参考leetcode题解 https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/solution/fan-zhuan-lian-biao-yi-dong-de-shuang-zhi-zhen-jia/
'''

'''
双指针
'''
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or head == None :
            return head
        pre,now = None,head
        while now != None:
            now.next,pre,now = pre,now,now.next
        return pre

'''
另一种双指针 非常不直观 参考 指针的处理顺序很重要 
'''
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or head == None :
            return head
        now = head
        while head.next!=None:
            t = head.next.next
            head.next.next = now
            now = head.next
            #下面这一句也确保now能到去到下一个正确的位置
            head.next = t
        return now