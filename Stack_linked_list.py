from linkedlist import LinkedList
# create a class named stacll
class StackLL:
    # when we create any object from this class by defaulf linked list object will create
    def __init__(self) :
        self.stackll = LinkedList()

    # to push items in stack i used to add the node at first of linked list
    def push(self,value):
        self.stackll.add_First_Node(value)

    # to pop any item i used to delete first node
    def pop(self):
        self.stackll.delete_First()

    # check if stack is empty or not
    def isEmpty(self):
        if self.stackll.count_Item() == 0:
            return True
        return False
    
    # return the size / number of nodes in stack
    def size(self):
        return self.stackll.count_Item()
    # to print the value of the top of stack without remove it
    def peek(self):
        return self.stackll.head.value
    

    def printstack(self):
        self.stackll.display_List()