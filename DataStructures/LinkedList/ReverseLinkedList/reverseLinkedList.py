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
        temp = self.head

        while temp.next:
            temp = temp.next
        
        temp.next = newNode
        self.tail = newNode

    def print_list(self):
        current = self.head
        while current:              
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    
    # def reverseList(self):
    #     prev = None
    #     current = self.head
    #     self.tail = self.head

    #     while current:
    #         next_node = current.next   
    #         current.next = prev        
    #         prev = current             
    #         current = next_node        

    #     self.head = prev

    def reverseList(self):
        current = self.head
        prev = None
        self.tail = self.head

        while current:
            current = current.next
            self.head.next = prev
            prev = self.head
            self.head = current

        self.head = prev     

ourList = LinkedList()
ourList.addNode(5)
ourList.addNode(51)
ourList.addNode(52)
ourList.addNode(35)
ourList.addNode(45)
ourList.addNode(55)

ourList.reverseList()
ourList.print_list()