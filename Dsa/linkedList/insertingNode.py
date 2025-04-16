class Node:
    def __init__(self, data):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
        
    ## insert at the front of the linked list
    def insertAtBeginning(self, new_data):
        ## creation of new node
        new_node = Node(new_data)
        ## insertion at the beginning
        new_node.next = self.head
        self.head = new_node   
    
    def printList(self):
        temp = self.head
        while temp:
            print(str(temp.data)+" ", end=" ")    
            temp = temp.next
            
            
## Driver code
llist = LinkedList()
llist.insertAtBeginning(12)       
llist.insertAtBeginning(9)               
llist.insertAtBeginning(4)               
llist.insertAtBeginning(8)               
llist.insertAtBeginning(18)     
llist.printList()          
        
        