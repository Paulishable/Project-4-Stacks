"""Class file for stack implementation with a list as the underlying structure"""


class Node:
    """Node class fpr linked list class"""

    def __init__(self, data_for_this_node, next_stuff=None):
        self.data = data_for_this_node
        self.next = next_stuff

    def get_next(self):
        """next node"""
        return self.next

    def set_next(self, next_item):
        """set the next item"""
        self.next = next_item

    def get_data(self):
        """get the data"""
        return self.data

    def set_data(self, data_item):
        """set the data item"""
        self.data = data_item


class Stack:
    """this class  is the implementation of the stack 'last-in, first out' structure"""
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = self.head

    def push(self, item):
        """put an item on the top of the stack"""
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        """pop an item off the top of the stack and remove it"""
        if self.size() == 0:
            raise IndexError("IndexError exception thrown")

        this_node = self.head
        while this_node is not None:
            self.remove()
            return this_node.get_data()
        return ""

    def remove(self):
        """remove a node"""
        this_node = self.head
        prev_node = None

        while this_node:
            if prev_node:
                prev_node.set_next(this_node.next)
            else:
                self.head = this_node.next
            return True  # data removed
            prev_node = this_node
            this_node = this_node.next

    def top(self):
        """return the top node without deleting"""
        if self.size() == 0:
            raise IndexError("IndexError exception thrown")
        this_node = self.head
        while this_node is not None:
            return this_node.get_data()
        return ""

    def size(self):
        """calculate the length of the linked list"""
        count = 0
        current_node = self.head  # Start at head
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

    def clear(self):
        """Remove all nodes in the stack"""
        curr_node = self.head
        while curr_node is not None:
            self.remove()
            curr_node = curr_node.next

    def __str__(self):
        print()
        current_node = self.head  # Start at head
        while current_node is not None:
            print(current_node.get_data().__str__(), end=" ")
            current_node = current_node.next
        else:
            print("Done")
        return "Done"
