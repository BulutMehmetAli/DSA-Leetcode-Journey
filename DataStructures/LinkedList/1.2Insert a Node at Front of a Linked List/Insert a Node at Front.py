class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self , data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        self.tail.next = newNode
        self.tail = newNode

    def insertFront(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        if self.tail is None:  # liste boştu
            self.tail = newNode
    
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
myList.insertFront(58)
myList.showList()