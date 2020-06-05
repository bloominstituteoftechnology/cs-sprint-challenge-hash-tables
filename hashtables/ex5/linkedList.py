# class HashTableEntry:
#     """
#     Linked List hash table key/value pair
#     """
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.next = None

#     def __str__(self):
#         return f"{self.key}, {self.value}"

class LinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def traverse_node(self, key):
        # if No head, return None
        # set current to head, work thru while head is not None
        # while head is not None, compare node.key and current.key
        # if it is the same, return the node
        # if not, preceed to traverse
        # if not found, return None,
        if not self.head:
            return None
        current = self.head
        while current:
            if key == current.key:
                return current
            current =  current.next
        return None    

    def insert_head(self, node):
        # if no head, set the node to head
        # if head, traverse_node and update its value
        # set the node.next to head
        # set the head to node
        # increase count

        if not self.head:
            self.head = node
            self.length += 1
        else:
            if self.traverse_node(node.key):
                self.traverse_node(node.key).value = node.value
            else:
                node.next = self.head
                self.head = node
                self.length  += 1

    def delete_node(self, key):
        # if only the head, delete head
        # if more, get prev anc current variable
        # set the pre to head, currrent to head.next
        # while current is not None, 
        # check current.key and node.key is same
        # if those are same, set prev.next to current.next, decrease count and return current, 
        # if not, increase prev & current
        # if no node found, return None
        if not self.head:
            return None
        elif self.head.key == key and not self.head.next:
            self.head = None
        elif self.head.key == key and self.head.next:
            self.head = self.head.next
        else:
            prev = self.head
            current = self.head.next
            while current:
                if current.key == key:
                    prev.next = current.next
                    self.length -= 1
                    return current.value
                else:
                    prev = current
                    current = current.next
            return None

    def print_ll(self):
        if self.length == 0:
            print('no value in this linked list')
        else:
            current = self.head
            
            while current:
          
                print(current.key, current.value)
                current = current.next
        
if __name__ is "__main__":

    my_ll = LinkedList()
    myNode1 = HashTableEntry('one', 1)
    myNode2 = HashTableEntry('two', 2)
    myNode3 = HashTableEntry('three', 3)
    myNode4 = HashTableEntry('four', 4)
    myNode5 = HashTableEntry('Five', 5)
    myNode6 = HashTableEntry('six', 6)
    myNode7 = HashTableEntry('six', 7)

    my_ll.insert_head(myNode1)
    my_ll.insert_head(myNode2)
    my_ll.insert_head(myNode3)
    my_ll.insert_head(myNode4)
    my_ll.insert_head(myNode5)
    my_ll.insert_head(myNode6)
    my_ll.insert_head(myNode7)
    my_ll.delete_node('two')
    my_ll.delete_node('six')
    my_ll.print_ll()