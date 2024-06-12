class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNodes(head):
    if not head:
        return None

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    curr = head

    while curr:
        remove = False
        runner = curr.next

        while runner:
            if runner.val > curr.val:
                prev.next = runner
                curr = runner
                remove = True
            runner = runner.next

        if remove:
            prev.next = curr.next
        else:
            prev = curr

        curr = curr.next

    return dummy.next