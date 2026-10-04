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

    def reverseListWithRecursion(self):

        self.tail = self.head
        self.head = self._reverse(self.head)

    def _reverse(self , data):
        if data is None or data.next is None:
            return data

        rec = self._reverse(data.next)

        data.next.next = data
        data.next = None

        return rec

ourList = LinkedList()
ourList.addNode(5)
ourList.addNode(51)
ourList.addNode(52)
ourList.addNode(35)
ourList.addNode(45)
ourList.addNode(55)

ourList.reverseListWithRecursion()
ourList.print_list()