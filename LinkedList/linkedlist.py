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
            current.next = value
        else:
            self.head = value

    def printll(self):
        current = self.head
        if self.head:
            while current:
                print str(current.value) + "-->",
                current = current.next
        else:
            print "Linkedlist is empty"
        print None

    def insert_at_pos(self, position, value):
        count = 1
        current = self.head
        if position > 1 and self.head:
                while current and count<position:
                    if count == position-1:
                        value.next = current.next
                        current.next = value

                    current = current.next
                    count += 1
        elif position ==1 :
            value.next = self.head
            self.head = value


    def get_position(self, value):
        current = self.head
        counter = 1
        if self.head:
            while current:
                if current.value == value:
                    return counter
                current = current.next
                counter += 1
        return None


    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(100)

ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

ll.printll()

print "*************************************************"
ll.insert_at_pos(2,e4)
ll.printll()

print "*************************************************"
print ll.get_position(100)

ll.delete(2)
print "After applying Dlt Node"
ll.printll()
