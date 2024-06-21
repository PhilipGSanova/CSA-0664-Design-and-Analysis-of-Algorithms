class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def merged(l1,l2):
    if not l1:
        return l2
    if not l2:
        return l1
    if l1.val < l2.val:
        l1.next = merged(l1.next, l2)
        return l1
    else:
        l2.next = merged(l1, l2.next)
        return l2

def printList(node):
    while node:
        print(node.val, end=' ')
        node = node.next

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
mergedlist = merged(list1,list2)
printList(mergedlist)