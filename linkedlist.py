class Node:
    def __init__(self , value) :
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None


    # display function to print the linked list nodes data
    def display_List(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" ---> ")
            current_node = current_node.next
        print("None")  


    # to add a node at the first of linked list
    def add_First_Node(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


    # to add a node at end of linked list
    def add_Last_Node(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


    # to add a node at a spesific index in linked list
    def insert_At_Index(self, index, value):
        if index == 0:
            self.add_First_Node(value)
        else:
            new_node = Node(value)
            current_node = self.head
            for _ in range(index - 1):
                if current_node is None:
                    return
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
        

    def add_Values(self, value):
        new_node = Node(value)
        current_node = self.head
        if self.head is None or self.head.value >= value:
            new_node.next = self.head
            self.head = new_node
            return
        while current_node.next and current_node.next.value < value:
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node
            



    def delete_First(self):
        if self.head is None:
            print("Your linked list is empty")
            return None
        deleted_node = self.head
        self.head = self.head.next
        return deleted_node


    def delete_Last(self):
        if self.head is None:
            print("Linked list is empty")
            return None
        elif self.head.next is None:
            deleted_node = self.head
            self.head = None
            return deleted_node
        else:
            current_node = self.head
            prev = None
            while current_node.next:
                prev = current_node
                current_node = current_node.next
            prev.next = None
            deleted_node = current_node
            return deleted_node
        

    def delete_At_Index(self, index):
        if index == 0:
            return self.delete_First()
        else:
            current_node = self.head
            for _ in range(index - 1):
                if current_node is None or current_node.next is None:
                    return
                current_node = current_node.next
            deleted_node = current_node.next
            if current_node.next.next:
                current_node.next = current_node.next.next
            else:
                current_node.next = None
            return deleted_node

    

    def count_Item(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count
    

    def remove_duplicates(self):
        if self.head is None:
            return
        current_node = self.head
        while current_node:
            runner = current_node
            while runner.next:
                if runner.next.value == current_node.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current_node = current_node.next


    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def return_Index(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            else:
                index += 1
                current = current.next