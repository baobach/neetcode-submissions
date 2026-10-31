class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def get(self, index: int) -> int:
        current = self.head
        for i in range(index):
            if current is None:
                return -1
            current = current.next
        return current.data if current else -1
            

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def insertTail(self, val: int) -> None:
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.size += 1

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for i in range(index):
                prev = current
                current = current.next
            prev.next = current.next
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        ret_list = list()
        current = self.head
        while current:
            ret_list.append(current.data)
            current = current.next
        return ret_list