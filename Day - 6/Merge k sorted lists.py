from queue import PriorityQueue

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    class Wrapper:
        def __init__(self, node):
            self.node = node
        
        def __lt__(self, other):
            return self.node.val < other.node.val
    
    pq = PriorityQueue()
    
    for l in lists:
        if l:
            pq.put(Wrapper(l))
    
    dummy = ListNode(0)
    current = dummy
    
    while not pq.empty():
        wrapper = pq.get()
        node = wrapper.node
        current.next = node
        current = current.next
        if node.next:
            pq.put(Wrapper(node.next))
    
    return dummy.next

# Helper function to convert a list of lists into a list of ListNode
def build_linked_lists(arrays):
    lists = []
    for array in arrays:
        head = current = ListNode(0)
        for value in array:
            current.next = ListNode(value)
            current = current.next
        lists.append(head.next)
    return lists

# Helper function to convert a linked list to a Python list
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Example usage:
input_lists = [[1,4,5],[1,3,4],[2,6]]
linked_lists = build_linked_lists(input_lists)
merged_head = mergeKLists(linked_lists)
print(linked_list_to_list(merged_head))  # Output: [1, 1, 2, 3, 4, 4, 5, 6]
