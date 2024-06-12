# to create a stack from scratch
# class node had value and next pointer by default
class Node :
    def __init__(self,value) :
        self.value = value
        self.next = None

# create a stack class
class StackScratch :
    def __init__(self) :
        self.head = None

    # when item added to stack new node will intialize and head of the stack will be a new node
    def push(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    #when item removed it removes from the top of stack
    def pop(self):
        if self.head is None :
            print("your stack is empty")
        deleted_node = self.head
        self.head = self.head.next
        return deleted_node.value

    # check if the stack has items or not
    def isEmpty(self):
        if self.head is None :
            return True
        return False

    # count number of nodes in stack
    def size(self):
        count = 0
        currentNode = self.head
        while currentNode.next :
            count +=1
            currentNode = currentNode.next
        return count

    # return the head value of linked list
    def peek(self):
        if self.isEmpty() :
            print("your stack is empty")
        return self.head.value
    

    def printStack(self):
        currentNode = self.head
        while currentNode :
            print(currentNode.value,end="--->")
            currentNode = currentNode.next
        print("None")