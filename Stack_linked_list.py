from linkedlist import LinkedList

class StackLL:
    def __init__(self) :
        self.stackll = LinkedList()

    
    def push(self,value):
        self.stackll.add_First_Node(value)

    
    def pop(self):
        self.stackll.delete_First()

    
    def isEmpty(self):
        if self.stackll.count_Item() == 0:
            return True
        return False
    

    def size(self):
        return self.stackll.count_Item()
    
    def peek(self):
        return self.stackll.head.value
    
    
    def printstack(self):
        self.stackll.display_List()