class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    length = 0
    first = head
    while first:
        length += 1
        first = first.next
    length -= n
    first = dummy
    while length > 0:
        length -= 1
        first = first.next
    first.next = first.next.next
    return dummy.next

def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

n = 2
print("Original Linked List:")
printLinkedList(head)

new_head = removeNthFromEnd(head, n)
print(f"Linked List after removing {n}th node from the end:")
printLinkedList(new_head)