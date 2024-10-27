class node: 
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        new_node = node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def deleteByValue(self, data):
        if not self.head:
            print("List is empty")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head 
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next
        if current_node.next is None:
            print(f"Node with value '{data}' not found")
        else:
            current_node.next = current_node.next.next
    
    def printList(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def getLength(self):
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count

# Create a linked list and perform operations
linked_list = linkedList()

linked_list.insertAtEnd("Node 1")
linked_list.insertAtEnd("Node 2")
linked_list.insertAtEnd("Node 3")

print("Initial list: ")
linked_list.printList()

linked_list.deleteByValue("Node 2")

print("List after deleting 'Node 2': ")
linked_list.printList()

print("Length of the list: ", linked_list.getLength())
