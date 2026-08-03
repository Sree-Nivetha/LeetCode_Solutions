# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lst=[]
        current=head
        while current is not None:
            lst.append(current.val)
            current=current.next

        total=0
        max_total=[]
        for i in range(len(lst)//2):
            total=lst[i]+lst[len(lst)-1-i]
            max_total.append(total)

        return max(max_total)