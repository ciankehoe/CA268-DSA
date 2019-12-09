class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

# Note, these are methods "A method is a function that is stored as a class attribute"
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next    # remove the item by moving the head pointer
            return item

    def is_empty(self):
        return self.head == None
        
    def __str__(self):
        tmp_str = ""
        ptr = self.head
        while ptr != None:
            tmp_str += ptr.item + " "
            ptr = ptr.next
            
        return tmp_str
        
    def append(self, item, next=None):
        # create a new node
        new_node = Node(item, next)
        
        if self.head is None:
            self.head = new_node
            return
        
        # traverse list until last node
        last = self.head
        while last.next != None:
            last = last.next    # traversing and incrementing through the list
        
        # once the next node is None, we stop traversing the list (we are stopped at the current node being the second last one, before the None node)
        # then we change the 'next' of the last node so that it points to our new_node. We're inserting it between None and the second last node.
        last.next = new_node