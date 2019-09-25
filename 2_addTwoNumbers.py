# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, x):
#     self.val = x
#     self.next = None

class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    res=ListNode(0)
    now=res
    ln1=l1
    ln2=l2
    exist1=True
    exist2=True
    carry=0
    while exist1 or exist2 or carry!=0:
      temp=0
      if exist1:
        temp+=ln1.val
        if ln1.next:
          ln1=ln1.next
        else:
          exist1=False
      if exist2:
        temp+=ln2.val
        if ln2.next:
          ln2=ln2.next
        else:
          exist2=False
      temp+=carry
      now.next=ListNode(temp%10)
      carry=temp//10
      now=now.next
    return res.next
