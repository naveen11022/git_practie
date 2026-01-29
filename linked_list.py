class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_middle(self):
        pass
    
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next


print("Begin List")
linked_list = LinkedList()
linked_list.insert_at_beginning(5)
linked_list.insert_at_beginning(6)
linked_list.insert_at_beginning(7)
linked_list.print_list()
print("Ending")
linked_list.insert_at_end(8)
linked_list.insert_at_end(9)
linked_list.insert_at_end(10)
linked_list.print_list()
