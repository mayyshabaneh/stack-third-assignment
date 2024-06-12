class Node :
    def __init__(self,value) :
        self.value = value
        self.next = None

class StackScratch :
    def __init__(self) :
        self.head = None

    def push(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


    def pop(self):
        if self.head is None :
            print("your stack is empty")
        deleted_node = self.head
        self.head = self.head.next
        return deleted_node.value


    def isEmpty(self):
        if self.head is None :
            return True
        return False


    def size(self):
        count = 0
        currentNode = self.head
        while currentNode.next :
            count +=1
            currentNode = currentNode.next
        return count


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