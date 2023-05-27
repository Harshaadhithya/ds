class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node

    def insert_at_position(self, position, value):
        if position == 1:
            self.insert_at_beginning(value)
        elif position == len(self)+1:
            self.insert_at_end(value)
        elif 1 < position <= len(self):
            new_node = Node(value)
            current_node = self.head
            current_position = 1
            while current_position < position-1:
                current_node = current_node.next
                current_position += 1
            next_node = current_node.next
            new_node.next = current_node.next
            new_node.prev = current_node
            next_node.prev = new_node
            current_node.next = new_node
        else:
            raise Exception("Invalid position!!")

    def delete_at_beginning(self):
        if self.head is not None:
            if self.head.next is None:
                self.head = None
                return
            self.head = self.head.next
            self.head.prev = None
            # old_head = self.head
            # new_head = old_head.next
            # old_head.next = None
            # new_head.prev = None
            # self.head = new_head

    def delete_at_end(self):
        if self.head is not None:
            if self.head.next is None:  #it implies that there is only one element exist in this list
                self.head = None
                return
            current_node = self.head
            while current_node.next.next is not None:
                current_node = current_node.next
            current_node.next = None

    def delete_at_position(self, position):
        if self.head is not None:
            if position == 1:
                self.delete_at_beginning()
            elif position == len(self):
                self.delete_at_end()
            elif 1 < position < len(self):
                current_node = self.head
                current_position = 1
                while current_position < position-1:
                    current_node = current_node.next
                    current_position += 1
                new_next_node = current_node.next.next
                # print("new_next_node",new_next_node)
                current_node.next = new_next_node
                # print("current_node.next",current_node.next)
                new_next_node.prev = current_node
                # print("new_next_node.prev",new_next_node.prev)
            else:
                raise Exception("Inavlid position")

    def search(self, search_value):
        if self.head is not None:
            current_node = self.head
            current_position = 1
            while current_node:
                if search_value == current_node.value:
                    return f"{search_value} is at psoition {current_position}"
                current_node = current_node.next
                current_position += 1
            return f"{search_value} does not exist !!"
        else:
            return "Empty list !!"

    def display(self):
        if self.head is not None:
            current_node = self.head
            while current_node is not None:
                print(current_node.value, end=" --> ")
                current_node = current_node.next
            print("")
        else:
            print("Empty List !!")

    def reverse_display(self):
        if self.head is not None:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            tail = temp
            current_node = tail
            while current_node is not None:
                print(current_node,end=" --> ")
                current_node = current_node.prev
            print()
        else:
            print("Empty list !!")

    def __len__(self):
        count = 0
        if self.head is None:
            return  count
        current_node = self.head
        count = 1
        while current_node.next is not None:
            current_node = current_node.next
            count += 1
        return count


dll = DoublyLinkedList()
dll.insert_at_end(1)
dll.display()
dll.delete_at_end()
dll.display()

# dll.delete_at_beginning()
# dll.display()

dll.insert_at_beginning(0)
dll.display()

dll.insert_at_end(5)
dll.display()

dll.delete_at_beginning()
dll.display()

dll.insert_at_end(6)
dll.insert_at_end(7)
dll.insert_at_beginning(1)
dll.display()

dll.delete_at_end()
dll.display()

print(len(dll))

dll.insert_at_position(3,333)
dll.display()

dll.insert_at_position(5,555)
dll.display()


dll.insert_at_position(1,111)
dll.display()


dll.insert_at_position(2,222)
dll.display()

dll.delete_at_position(4)
dll.display()

dll.delete_at_position(6)
dll.display()

print(dll.search(333))

dll.reverse_display()
dll.delete_at_position(3)
dll.reverse_display()

dll.insert_at_end(99)
dll.reverse_display()

dll.delete_at_position(2)
dll.reverse_display()

dll.delete_at_beginning()
dll.reverse_display()