class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, head = None):
        self.head = head

    def append(self, new_node):
        current = self.head
        if self.head:
            while current.next:
                current = current.next

            current.next = new_node
        else:
            self.head = new_node

    def Printl(self):
        current = self.head
        if self.head:
            while current:
                print str(current.value)+" -->",
                current = current.next
            print "None"
        else:
            print "LinkedList is empty"

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

ll = LinkedList(n1)
ll.append(n2)
ll.append(n3)

ll.Printl()
