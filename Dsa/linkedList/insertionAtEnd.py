class Node:
    def __init__(self, data):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    ## insert at the end of the linked list
    def insertAtEnd(self, new_data):
        ## creation of new node
        new_node = Node(new_data)
        ## linked list is empty
        if self.head is None:
            self.head = new_node
            return
        
        ## insertion at the end
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node    
         
    
    def printList(self):
        temp = self.head
        while temp:
            print(str(temp.data)+" ", end=" ")    
            temp = temp.next
            
            
## Driver code
llist = LinkedList()
llist.insertAtEnd(12)       
llist.insertAtEnd(9)               
llist.insertAtEnd(4)               
llist.insertAtEnd(8)               
llist.insertAtEnd(18)     
llist.printList()          
        
        