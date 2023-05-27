class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return self.value




class SingleLinkedList:
    def __init__(self, head=None):
        self.head = head
        # self.tail = tail

    def insert_at_beginning(self,value):
        new_node = Node(value=value)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self,value):
        new_node = Node(value=value)
        if self.head is None:
            self.head=new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

            # ---- we can also use this, because we have overidded __iter__ method for this class
            # current_node = self.head
            # for node in self:
            #     current_node = node
            # current_node.next = new_node

    def insert_at_position(self,position,value):
        if position == 1:
            self.insert_at_beginning(value)
        elif position == len(self)+1:
            self.insert_at_end(value)
        elif 1 < position <= len(self):  #len(self) means length of this single_linked_list because we have overridden the __len__ method of this class
            new_node = Node(value)
            temp_node = self.head
            current_position = 1
            while current_position < position-1:
                # if temp_node.next is None:
                temp_node = temp_node.next
                current_position+=1

            new_node.next = temp_node.next
            temp_node.next = new_node
        else:
            raise Exception("Invalid Position")

    def delete_at_beginning(self):
        if self.head is not None:
            self.head = self.head.next

    def delete_at_end(self):
        if self.head is not None:
            if self.head.next is None:
                self.head = None
                return
            current_node = self.head
            while current_node.next.next is not None:
                current_node = current_node.next
            current_node.next = None

    def delete_at_position(self,position):
        if position == 1:
            self.delete_at_beginning()
        elif position == len(self):
            self.delete_at_end()
        elif 1 < position <= len(self):
            current_node = self.head
            current_position = 1
            while current_position < position-1:
                current_node = current_node.next
                current_position += 1
            next_node = current_node.next
            current_node.next = next_node.next

        else:
            raise Exception("Invalid Position")

    def empty_this_linked_list(self):
        self.head = None
        #when we make head to none, then there will be no reference to 2nd node, so 3rd node, s0 4th node....so whenever there is 0 reference for a object, then python garbage collection takes place automatically.

    def search(self,search_value):
        if self.head is not None:
            current_node = self.head
            position = 1
            while current_node is not None:
                if current_node.value == search_value:
                    return f"{search_value} is at position {position}"
                current_node = current_node.next
                position += 1
            return f"{search_value} does not exist in this linked list!!"
        else:
            return "Empty Linked List"

    def display(self):
        if self.head is None:
            print("Empty Linked list...")
            return
        current_node = self.head
        while current_node is not None:
            print(current_node.value,end=" --> ")
            current_node = current_node.next
        print("")

    def __len__(self):
        count = 0
        if self.head is not None:
            current_node = self.head
            count=1
            while current_node.next is not None:
                current_node = current_node.next
                count+=1
        return count

    def __iter__(self): #we can iterate the entire class using. for x in linked_list_object:
        node = self.head
        while node is not None:
            yield node #yield is similar to return statement but while using return statement the functions ends with that return statement
            # but yield statement gives the value to the caller,then again comes back and resume where it stopped.
            #if we didn't use yield, then we need to iterate each nodes and store each value in a list or str and then at last after every iteration return the entire list or str.
            # by using yield we save memory, because we don't need to have that list or str to store the entire values, instead we can give the value to the caller in each iteration and continue the iteration as well.
            node = node.next



# head_node = Node(value=1)
# tail_node = Node(value=10)
single_linked_list = SingleLinkedList()

single_linked_list.insert_at_beginning(5)
single_linked_list.delete_at_end()
single_linked_list.display()
single_linked_list.insert_at_beginning(4)
single_linked_list.insert_at_beginning(3)
single_linked_list.insert_at_end(2)
single_linked_list.insert_at_end(1)
single_linked_list.insert_at_beginning(0)
single_linked_list.display()
# ----
single_linked_list.insert_at_position(1,"hello")
single_linked_list.display()

single_linked_list.insert_at_position(7,"7th")

single_linked_list.insert_at_position(8,"8th")
single_linked_list.display()
#-----
single_linked_list.delete_at_beginning()
single_linked_list.display()

single_linked_list.delete_at_end()
single_linked_list.display()

single_linked_list.delete_at_position(4)
single_linked_list.display()

print(single_linked_list.search(4))

single_linked_list.empty_this_linked_list()
single_linked_list.display()





