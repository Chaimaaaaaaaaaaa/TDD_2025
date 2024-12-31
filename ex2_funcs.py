class Node: 
    def __init__(self, val):
        self.val = val
        self.next = None

class FIFO:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add(self, item):
        new_node = Node(item)
        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = new_node
    
    def rmv(self):
        if self.head is None:
            print("empty")
        value = self.head.val
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return value   

    def is_empty(self):
        if self.head is None:
            return True
        return False
    
    def len(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
