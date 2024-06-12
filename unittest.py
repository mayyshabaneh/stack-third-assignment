from Stack_2 import StackScratch
from Stack_linked_list import StackLL
stacksc = StackScratch()
stackll = StackLL()

def push_test():
    stacksc.push(10)
    stacksc.push(20)
    stacksc.push(30)
    stacksc.push(40)
    stacksc.push(40)
    stacksc.push(50)
    stacksc.push(60)
    stacksc.push(70)
    stacksc.push(80)
    stacksc.push(90)
    stacksc.push(100)
    stacksc.printStack()


def pop_test():
    print(f"the poped value is {stacksc.pop()}")
    print(f"the stack after pop is :")
    stacksc.printStack()

def isEmpty_test():
    if stacksc.isEmpty() == True:
        print("your stack is empty")
    else:
        print (f"your stack has {stacksc.size()} nodes")


def peek_test():
    print(f"the value of the top os stack is {stacksc.peek()}")


def pushll_test():
    stackll.push(10)
    stackll.push(20)
    stackll.push(30)
    stackll.push(40)
    stackll.push(50)
    stackll.push(60)
    stackll.push(70)
    stackll.push(80)
    stackll.push(90)
    stackll.push(100)
    stackll.printstack()


def popll_test():
    stackll.pop()
    stackll.printstack()


def isEmptyll_test():
    if stackll.isEmpty() == True:
        print("your stack is empty")
    else:
        print(f"your stack has {stackll.size()} Nodes")


def peekll_test():
    print(f"the value of the top of stack is : {stackll.peek()}")

print("\n\nstack using scratch :")
isEmpty_test()
push_test()
peek_test()
pop_test()
isEmpty_test()
peek_test()

print("\n\nstack using linked list :")
isEmptyll_test()
pushll_test()
peekll_test()
popll_test()
isEmptyll_test()
peekll_test()