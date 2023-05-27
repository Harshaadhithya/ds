class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __repr__(self):

        return f"{str(self.prev.value)} <-- {str(self.value)} --> {str(self.next.value)}"


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            #circular linked list, sp the tail must again point to the head so do the follwoing
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            tail_node = current_node
            tail_node.next = new_node
            new_node.prev = tail_node
            self.head = new_node

        print("new-node",new_node)

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.head.next = new_node
            self.head.prev = new_node
            # print(new_node)
        else:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            tail_node = current_node
            tail_node.next = new_node
            new_node.prev = tail_node
            new_node.next = self.head
        print("new node",new_node)

    def delete_at_beginning(self):
        if self.head is not None:
            if self.head.next == self.head:
                self.head =None
                return
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next

            tail_node = current_node
            self.head = self.head.next
            self.head.prev = tail_node
            tail_node.next = self.head

    def delete_at_end(self):
        if self.head is not None:
            if self.head.next == self.head:
                self.head = None
                return
            current_node = self.head
            while current_node.next.next != self.head:
                current_node = current_node.next
            last_before_node = current_node
            last_before_node.next = self.head
            self.head.prev = last_before_node
            print("last node",last_before_node)
            print("head",self.head)


    def display(self):
        if self.head is None:
            print("Empty List !!")
            return
        current_node = self.head
        while current_node:
            print(current_node.value,end=" --> ")
            current_node = current_node.next
            if current_node == self.head:
                break
        print("")


     # ->   1-->2-->3-->4-|
     # |<--   <--    <--

cdll = CircularDoublyLinkedList()
cdll.insert_at_end(3)
cdll.display()

cdll.delete_at_beginning()
cdll.display()

cdll.insert_at_end(4)
cdll.display()

cdll.insert_at_end(5)
cdll.display()

cdll.insert_at_beginning(2)
cdll.display()

cdll.insert_at_beginning(1)
cdll.display()

cdll.delete_at_end()
cdll.display()

cdll.delete_at_beginning()
cdll.display()

cdll.delete_at_end()
cdll.display()
