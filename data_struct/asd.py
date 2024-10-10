class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

# Assuming myNode1 is the head of your linked list
myNode1 = ListNode(10)
myNode1.next = ListNode(20)
myNode1.next.next = ListNode(30)
myNode1.next.next.next = ListNode(40)

myLinkedList = LinkedList()
myLinkedList.head = myNode1

# Insert new node with value 35 after node with value 30
myNewNode = ListNode(35)
Node = myLinkedList.head
search = True

while search and Node is not None:
    if Node.data == 30:
        search = False
    else:
        Node = Node.next

if Node is not None:  # Ensure we found the node with data 30
    NextNode = Node.next
    Node.next = myNewNode
    myNewNode.next = NextNode

print("The elements in the linked list are:")
myLinkedList.printList()
