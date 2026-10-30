class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, data):
        self.insertEnd(data)

    def insertFront(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        if self.tail is None:  # liste boştu
            self.tail = newNode

    def insertEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        self.tail.next = newNode
        self.tail = newNode

    def sizeOfList(self):
        if self.head is None:
            return
        size = 0
        temp = self.head
        while temp.next:
            size += 1
            temp = temp.next
            
        return size
    
    def insertSpesificPos(self, data, index):  # index 1'den başlıyor
        size = self.sizeOfList()
        if index < 1 or index > size + 1:
            print("Out of bound !!!")
            return
        if index == 1:
            self.insertFront(data)
            return
        if index == size + 1:
            self.insertEnd(data)
            return
        newNode = Node(data)
        temp = self.head
        for _ in range(index - 2):
            temp = temp.next
        newNode.next = temp.next
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
myList.insertFront(58)
myList.insertFront(61)
myList.insertSpesificPos(0,5)
myList.showList()