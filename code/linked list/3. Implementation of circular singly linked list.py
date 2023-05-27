class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return self.value


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head   #when this is the only node in our linked list, then it should point to itself to ensure it is circular
        else:
            new_node.next = self.head
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node    #after the while, the current_node holds the last node, now the last node points to the new node we have created
            self.head = new_node

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head  #if there is only one node, then it must be pointing to itself to from a circle
        else:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.head

    def insert_at_position(self, position, value):
        if position == 1:
            self.insert_at_beginning(value)
        elif 1 < position <= len(self)+1:  #here len(self)+1 also valid. say if len = 5 and user tries to insert at 6th position, our logic can add that to, so we can allow that too.
            new_node = Node(value)
            current_node = self.head
            current_position = 1
            while current_position < position-1:
                current_node = current_node.next
                current_position += 1
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            raise Exception("Invalid position")

    def delete_at_beginning(self):
        if self.head is not None:
            if self.head == self.head.next:   #if true, then it implies that there is only one node present in this list. adn obviously i must be pointing to itself.
                self.head = None
            else:
                #to point the tail to new head
                current_node = self.head
                while current_node.next != self.head:
                    current_node = current_node.next
                new_head = self.head.next
                self.head = new_head
                current_node.next = self.head

    def delete_at_end(self):
        if self.head is not None:
            if self.head == self.head.next:  #if only one node exists in this list, then self.head points to itself, so delete it directly.
                self.head = None
            else:
                current_node = self.head
                while current_node.next.next != self.head: #current.next.next = self.head --> last before node, which is then made as the new tail by pointing it to the self.head
                    current_node = current_node.next
                current_node.next = self.head

    def delete_at_position(self, position):
        if self.head is not None:
            if position == 1:
                self.delete_at_beginning()
            elif 1 < position <= len(self): #even if the position = last element, we can use this same logic for that too. if 7 is the position and it is the tail, then 6-->7-->head. we are making 6th node to point to the node which is being pointed by the 7th node at that time which is the head. so it becomes 6-->head. which means now 7 is deleted
                current_node = self.head
                current_position = 1
                while current_position < position-1:
                    current_node = current_node.next
                    current_position += 1
                next_node = current_node.next
                current_node.next = next_node.next
            else:
                raise Exception("Invalid position")

    def empty_this_linked_list(self):
        if self.head is not None:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = None
            self.head = None

    def search(self, search_value):
        if self.head is not None:
            current_node = self.head
            current_position = 1
            while current_node:
                print(f"{current_node.value},{search_value},{current_position}")
                if current_node.value == search_value:
                    return f"{search_value} is at position-{current_position}"
                current_node = current_node.next
                current_position += 1
                if current_node == self.head:
                    # print("inside")
                    break
            return f"{search_value} does not exist in this list!!"
        else:
            return f"Empty List"



    def display(self):
        if self.head is None:
            print("Empty!!")
            return

        current_node = self.head
        while current_node:
            print(current_node.value, end=" --> ")
            current_node = current_node.next
            if current_node == self.head:
                # print("yes!! found cycle",current_node.value)
                print("")
                break #or return

        """my method"""
        # current_node = self.head
        # print(current_node.value, end=" --> ")   #if there is only one node, then it will be the head which points itself. if so, it won't enter into this while loop, it doesn't satisfy the condition.so we are printing the first node's value before the loop.
        # while current_node.next != self.head:
        #     print(current_node.next.value, end=" --> ")  #we are printing the current node's next node's value and after that only we are updating the current node to its next node. if the current node is the last node/tail node, then it won't enter this while loop and so it will not be able to display the last node, so we are printing the current node's next value. if the current node is last before node, then we can print the last node's value
        #     current_node = current_node.next

    def __len__(self):
        count = 0
        if self.head is None:
            pass
        else:
            current_node = self.head
            count = 1
            while current_node.next != self.head:
                current_node = current_node.next
                count += 1
        return count



circular_linked_list = CircularSinglyLinkedList()

circular_linked_list.display()
print("len= ",len(circular_linked_list))


circular_linked_list.insert_at_end(5)

circular_linked_list.display()


circular_linked_list.delete_at_end()
circular_linked_list.display()

circular_linked_list.insert_at_beginning(4)
circular_linked_list.insert_at_end(6)
# circular_linked_list.insert_at_end(7)
#
#
# # circular_linked_list.display()
# circular_linked_list.insert_at_beginning(3)
# circular_linked_list.insert_at_beginning(2)
# circular_linked_list.insert_at_beginning(1)
circular_linked_list.display()


circular_linked_list.delete_at_beginning()
circular_linked_list.display()

circular_linked_list.insert_at_end(10)
circular_linked_list.insert_at_beginning(3)
circular_linked_list.display()
print("len= ",len(circular_linked_list))


circular_linked_list.delete_at_end()
circular_linked_list.display()

print("len= ",len(circular_linked_list))

circular_linked_list.insert_at_position(3,9)
circular_linked_list.display()

circular_linked_list.insert_at_position(4,111)
circular_linked_list.display()


circular_linked_list.insert_at_position(4,444)
circular_linked_list.display()


circular_linked_list.insert_at_position(6,666)
circular_linked_list.display()

circular_linked_list.delete_at_position(1)
circular_linked_list.display()

print(circular_linked_list.search(666))

circular_linked_list.empty_this_linked_list()
circular_linked_list.display()



