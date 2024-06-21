class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete(node):
    node.next = node.next.next

def remove(node):
    current = node
    while current and current.next:
        if current.val == current.next.val:
            delete(current)
        else:
            current = current.next
    return node

def printlist(node):
    while node:
        print(node.val, end=' ')
        node = node.next
    print()  # for newline

# Example usage
list = Node(1, Node(1, Node(2)))
list = remove(list)
printlist(list)  # Output: 1 2
