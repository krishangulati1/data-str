class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, head = None):
        self.head = head

    def append(self, value):
        current = self.head

        if self.head:
            while current.next:
                current = current.next
            current.value = value
        else:
            self.head = value


e1 = Node(1)
e2 = Node(2)
e3 = Node(3)

ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)


