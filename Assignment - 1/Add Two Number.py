class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            sum_val = carry
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next
            
            carry = sum_val // 10
            current.next = ListNode(sum_val % 10)
            current = current.next
        
        return dummy.next

if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    while result:
        print(result.val, end=" ")
        result = result.next
    print()

    l3 = ListNode(0)
    l4 = ListNode(0)
    result = solution.addTwoNumbers(l3, l4)
    while result:
        print(result.val, end=" ")
        result = result.next
    print()

    l5 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l6 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    result = solution.addTwoNumbers(l5, l6)
    while result:
        print(result.val, end=" ")
        result = result.next
    print()
