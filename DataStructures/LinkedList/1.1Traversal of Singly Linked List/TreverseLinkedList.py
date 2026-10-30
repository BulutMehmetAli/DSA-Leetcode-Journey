class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None

    def addNode(self , data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode

    def showList(self):
        if self.head is None:
            print("List has not any node")
            return
        temp = self.head
        while temp:
            print(temp.data , end= " -> ")
            temp = temp.next
        print("None")

myList = LinkedList()

myList.addNode(5)
myList.addNode(51)
myList.addNode(52)
myList.addNode(45)
myList.addNode(55)
myList.addNode(56)
myList.addNode(75)
myList.addNode(35)

myList.showList()